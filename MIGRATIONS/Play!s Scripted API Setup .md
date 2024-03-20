# Setup play! 

This guide details setting up a secure API for play!, a custom GPT designed with OpenAI's custom GPT Builder, focusing on PostgREST and JWT authentication. A setup script initially automates your environment's preparation, tailoring PostgREST and Nginx configurations. 

Subsequent steps in the tutorial reveal how to enact JWT authentication, highlighting the generation of a JWT secret, the creation of tokens, and the adjustment of PostgREST for safeguarded endpoint access. Specifically tailored **to ensure that play! is the sole authorized client**, this strategy fortifies the API's security, making data available exclusively to the way play! communicates with you -  and laying the groundwork for a secure and efficient API framework.


```
#!/bin/bash

# Ensure the script exits on any error
set -e

echo "Play!s API Setup"

# Function to validate input
validate_input() {
    if ! [[ "$1" =~ ^[a-zA-Z0-9_]+$ ]]; then
        echo "Invalid input: $1. Only alphanumeric characters and underscores are allowed." >&2
        exit 1
    fi
}

# Collect configuration details with validation
read -p "Enter the database name: " db_name
validate_input "$db_name"

read -p "Enter the database user: " db_user
validate_input "$db_user"

echo "Enter the database password: "
read -s db_pass
echo "Enter your API domain (e.g., api-1.fountain.coach): "
read api_domain

echo "Email address for SSL certificate registration: "
read certbot_email

# Default email if not provided
certbot_email=${certbot_email:-"mail@benedikt-eickhoff.de"}

# Generate a secure JWT secret for PostgREST
jwt_secret=$(openssl rand -base64 32)

# Find an available port for PostgREST
pgrst_port=$(comm -23 <(seq 3000 3100 | sort) <(ss -tan | awk '{print $4}' | cut -d':' -f2 | sort -u) | head -n 1)

# Dropping existing database and user if they exist
echo "Preparing environment..."
sudo -u postgres psql -c "DROP DATABASE IF EXISTS ${db_name};"
sudo -u postgres psql -c "DROP USER IF EXISTS ${db_user};"

# Create the PostgreSQL database and user
echo "Creating database and user..."
sudo -u postgres psql -c "CREATE DATABASE ${db_name};"
sudo -u postgres psql -c "CREATE USER ${db_user} WITH PASSWORD '${db_pass}';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE ${db_name} TO ${db_user};"

# Apply the database schema
echo "Applying database schema..."
sudo -u postgres psql -d "$db_name" < /path/to/your/bootstrap.sql

# Configuring PostgREST
echo "Configuring PostgREST..."
cat << EOF > /etc/postgrest.conf
db-uri = "postgres://${db_user}:${db_pass}@localhost:5432/${db_name}"
db-schema = "public"
db-anon-role = "${db_user}"
jwt-secret = "${jwt_secret}"
server-port = ${pgrst_port}
EOF

# Setting up PostgREST service
echo "Setting up PostgREST service..."
cat << EOF > /etc/systemd/system/postgrest.service
[Unit]
Description=PostgREST Service
After=postgresql.service

[Service]
ExecStart=/usr/local/bin/postgrest /etc/postgrest.conf

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable postgrest
systemctl start postgrest

# Configuring Nginx and setting up SSL
echo "Configuring Nginx and setting up SSL..."
nginx_conf_path="/etc/nginx/sites-available/${api_domain}"
ln -s "${nginx_conf_path}" /etc/nginx/sites-enabled/

cat << EOF > "${nginx_conf_path}"
server {
    listen 80;
    server_name ${api_domain};
    location / {
        proxy_pass http://localhost:${pgrst_port};
    }
}
EOF

nginx -t && systemctl reload nginx

# Using Certbot to obtain and install SSL certificate
certbot --nginx -d "${api_domain}" --non-interactive --agree-tos -m "${certbot_email}" --redirect --force-renewal

echo "Setup complete. Access the API at https://${api_domain}."
echo "Use 'systemctl start|stop|restart postgrest' to manage the PostgREST service."
echo "Use 'systemctl start|stop|restart nginx' for managing the Nginx service."
```
## authentify! & play!

 ![Bearer Authentication ](https://coach.benedikt-eickhoff.de/koken/storage/cache/images/000/703/Bild-6,medium_large.1710915316.jpeg "Bearer Authentication Sequence")

To handle bearer authentication and JWT token creation for use with PostgREST, you need to perform a series of steps to generate a JWT secret, create tokens, and configure your PostgREST instance to recognize and validate these tokens. Below is a detailed tutorial that integrates the necessary manual steps to be accomplished after running the setup script.

### Post-Script Setup Tutorial for Bearer Authentication with PostgREST

After you've successfully run the setup script and your PostgREST service is up and running, you'll need to ensure that the service can authenticate users via JWT tokens. This tutorial outlines how to generate a JWT secret, create tokens, and configure PostgREST to use them.

#### Step 1: Generating a JWT Secret

You've already generated a JWT secret in the script with the following command:

```bash
jwt_secret=$(openssl rand -base64 32)
```

This secret is used by your PostgREST configuration to validate the JWT tokens that are presented by clients. Ensure this secret is kept secure and is not exposed to unauthorized users.

#### Step 2: Creating JWT Tokens

JWT tokens can be generated using various tools or libraries depending on your development environment. For this tutorial, we'll use an online tool for simplicity, but in a production environment, you should use a secure method within your application's backend to generate tokens.

1. Visit a JWT token generation website such as [jwt.io](https://jwt.io).
2. In the "PAYLOAD" section, input the claims required by your application. At a minimum, you'll need to include the `role` claim, which should match the database role you want to authenticate as. For example:

```json
{
  "role": "api_user"
}
```

3. In the "VERIFY SIGNATURE" section, input the JWT secret generated during the setup into the "your-256-bit-secret" field. Ensure the algorithm selected is HS256, which matches the method used to generate the secret.
4. The website will generate a JWT token. This token can be used in the `Authorization` header of your requests to PostgREST.

#### Step 3: Configuring PostgREST to Use the JWT Secret

This step has already been covered by the setup script, which creates a PostgREST configuration file (`/etc/postgrest.conf`) and includes the JWT secret in it:

```conf
jwt-secret = "your_jwt_secret_here"
```

This configuration instructs PostgREST to use the specified secret to validate the JWT tokens presented by clients.

#### Step 4: Making Authenticated Requests to PostgREST

To make an authenticated request to your PostgREST API, include the JWT token in the `Authorization` header as a Bearer token. Here's an example using `curl`:

```bash
curl -X GET \
     -H "Authorization: Bearer <Your-JWT-Token>" \
     https://<Your-API-Domain>/your_endpoint
```

Replace `<Your-JWT-Token>` with the JWT token you generated and `<Your-API-Domain>` with your actual API domain. This request will be authenticated by PostgREST using the JWT token, and the response will depend on the permissions associated with the `role` claimed by the token.

#### Conclusion

By following these steps, you've integrated bearer authentication into your PostgREST setup, allowing you to securely control access to your API. For a production environment, consider implementing a backend service responsible for user authentication and JWT token generation, ensuring secure handling of sensitive information like the JWT secret.

# More on Authentification & Managing Ressources (RBAC)

Implementing Role-Based Access Control (RBAC) in PostgREST, particularly through the use of the `web_anon` role and other role configurations, significantly enhances the security of your API. The `web_anon` role, specifically, plays a crucial role in defining what unauthenticated users can access. By carefully configuring permissions associated with this role, you can ensure that sensitive data remains protected while still allowing necessary public access to your API's endpoints.

Beyond the `web_anon` role, employing a variety of roles aligned with different user permissions allows for fine-grained access control. This means you can specify exactly what actions each role can perform, such as read-only access for some users, while others may insert or update data. By leveraging PostgreSQL's powerful RBAC features in tandem with PostgREST, you create a secure, multi-layered approach to API security.

For instance, creating roles like `api_user` for general authenticated access and more specific roles for administrative tasks ensures that users can only interact with the data they're explicitly permitted to. This not only minimizes the risk of unauthorized data exposure but also adheres to the principle of least privilege, a security best practice.

Furthermore, integrating JWT authentication adds another layer of security. By issuing JWT tokens to users and mapping those tokens to PostgreSQL roles, you establish a secure, stateless method for user authentication and authorization. This method ties the robust security features of PostgreSQL directly to your API's access control, ensuring that each request is authenticated and authorized according to the configured roles and their permissions.

In conclusion, the strategic use of the `web_anon` role, alongside a thoughtful RBAC setup in PostgREST, underpins the security of your API. It ensures that access is tightly controlled based on user roles, significantly mitigating the risk of unauthorized access and data breaches. By carefully planning your RBAC strategy and integrating it with JWT for authentication, you set a solid foundation for a secure, efficient, and scalable API solution.

# A note on GDPR Compliance 

This API setup, incorporating PostgREST and JWT authentication, aligns with GDPR compliance by emphasizing data protection, access control, and the principle of least privilege. GDPR, or the General Data Protection Regulation, sets forth guidelines for the collection, processing, and storage of personal data for individuals within the European Union.

**Data Protection and Encryption:** Through the use of SSL/TLS encryption facilitated by Nginx, this setup ensures that data in transit between the client and server is encrypted, a key requirement for GDPR compliance. This helps protect personal data from interception and unauthorized access.

**Access Control and Authentication:** The implementation of JWT authentication and role-based access control (RBAC) ensures that only authenticated users can access specific data, and only if they have the necessary permissions. The `web_anon` role can be used to tightly control public access, while more privileged roles can be assigned to users who need access to sensitive or personal data. This level of access control is crucial for GDPR, which demands that personal data can only be accessed by individuals with a legitimate reason to do so.

**Principle of Least Privilege:** By configuring specific roles with only the permissions they need to perform their functions, the setup adheres to the principle of least privilege. This reduces the risk of a data breach, as each user or service has only the minimum level of access required. GDPR emphasizes the need for strong access controls and the minimization of data access to what is strictly necessary.

**Data Processing Transparency:** While not directly addressed in the technical setup, GDPR requires transparency in how personal data is processed. Organizations using this API setup must ensure that they have clear policies in place regarding data processing activities and that users are informed about how their data is used. Additionally, mechanisms should be in place to allow users to exercise their GDPR rights, such as data access, rectification, and erasure requests.

To fully comply with GDPR, organizations must also consider data minimization, purpose limitation, data accuracy, and storage limitation principles in their API design and implementation. They should also implement processes for regular security assessments, data protection impact assessments, and ensure that data processors (if any) are compliant with GDPR.

In summary, this API setup provides a strong foundation for GDPR compliance through secure data transmission, robust access control, and adherence to the principle of least privilege. However, technical measures should be complemented with organizational policies, user consent mechanisms, and processes for exercising data subject rights to achieve full compliance.


