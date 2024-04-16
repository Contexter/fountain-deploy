# AI Integration - Learn the PPN + jwt-cli to play! 

or , a streamlined approach to leveraging the stack for a project, particularly one involving a custom GPT accessing the `Fountain` backend, focusing on practical steps and considerations for deployment and use.

### Overview

The PPN stack, enhanced with JWT authentication using `jwt-cli`, provides a solid foundation for secure, scalable web applications. PostgreSQL serves as the robust database, PostgREST turns your database into a RESTful API, and NGINX acts as the web server and reverse proxy, ensuring efficient content delivery and request routing. `jwt-cli` adds a layer of security by facilitating JWT token generation and validation, essential for secure communication between the custom GPT client and the Fountain backend.

### Deploying the PPN + jwt-cli Stack

1. **PostgreSQL Setup**
   - Install PostgreSQL on Ubuntu 20.04.
   - Configure your database schemas and permissions according to your application's data model (_`The Fountain`_) and security requirements ( _`Bearer Spec`_).

2. **PostgREST Configuration**
   - Install PostgREST and configure it to connect to your PostgreSQL database. Define your API endpoint configurations, focusing on the routes that the custom GPT will interact with.
   - Ensure PostgREST runs as a service or via a process manager for reliability.

3. **NGINX Integration**
   - Install NGINX and set up reverse proxy configurations to forward requests to PostgREST and any static content or additional services your application requires.
   - Configure SSL with NGINX to secure HTTP traffic using certificates from Let's Encrypt or another certificate authority.

4. **JWT Authentication with jwt-cli**
   - Install `jwt-cli` by downloading the appropriate binary for your system and placing it in a directory included in your system's PATH.
   - Use `jwt-cli` to generate JWT tokens for testing and development. For a production environment, integrate JWT token generation and validation into your application's authentication flow, using `jwt-cli` as a reference or for manual token management tasks. BUT: there will be no "Web Application" or "Production" - everything will stay _`manual`_)

### Security and Maintenance

- **Secure your JWT Secret**: Keep your JWT secret key secure and out of version control. Consider using environment variables or a secret management tool.
- **Database Security**: Regularly update PostgreSQL and monitor for security advisories. Implement database access controls and encrypt sensitive data.
- **API Security**: Use PostgREST's role-based access control to restrict access to your API endpoints. Validate and sanitize all inputs.
- **Regular Updates**: Keep NGINX, PostgREST, PostgreSQL, and `jwt-cli` up to date with the latest versions to ensure you have the latest security patches and features.

### Practical Use

- **For Custom GPT Access**: Implement authentication in your custom GPT application to include a JWT in API requests. Ensure the GPT application checks the validity of the JWT before allowing access to protected Fountain backend resources.
- **Monitoring and Logging**: Utilize NGINX and PostgreSQL logs to monitor access patterns and potential security issues. Consider tools like GoAccess for NGINX log analysis or pgBadger for PostgreSQL.

# Cohesive configuration strategy across components

Each element of the stack relies on configuration files to dictate its behavior, security measures, and how it interacts with other components. Additionally, utilizing JWT tokens for authentication, particularly with the "Bearer" specification in HTTP headers, requires careful setup to ensure secure and functional communication between services.

### Configuration Overview and Default Locations

1. **PostgreSQL**
   - **Config Files**: The main configuration files are `postgresql.conf` for server settings and `pg_hba.conf` for client authentication. Default location: typically in `/etc/postgresql/<version>/main/` or within the data directory (`/var/lib/postgresql/<version>/main/`).
   - **Contribution**: Controls database server behavior, including listening addresses, port, authentication methods, and more. Proper configuration ensures secure and efficient database access and operation.

2. **PostgREST**
   - **Config File**: PostgREST uses a single `.conf` file to define its connection to the PostgreSQL database and other operational parameters. Default setup doesn't have a fixed location; it’s usually placed where it’s convenient for the administrator, and its path is passed when starting PostgREST.
   - **Contribution**: Dictates how PostgREST interfaces with PostgreSQL, including the schema to expose as an API (postgREST <-> postgreSQL `schema` , `View` etc. see postgREST automatic openAPI publishing based on postgrSQL objects) , the database connection details, and JWT secret for authenticating API requests.

3. **NGINX**
   - **Config File**: The main NGINX configuration file is `nginx.conf`, with additional server blocks (virtual hosts) often defined in `/etc/nginx/sites-available/` and enabled through symbolic links in `/etc/nginx/sites-enabled/`.
   - **Contribution**: Configures reverse proxy to PostgREST, static content serving, SSL termination, and request routing. Essential for directing client requests to the correct backend service  and securing communications.

4. **jwt-cli**
   - **Usage**: While `jwt-cli` doesn’t rely on a persistent configuration file, it’s used to generate and validate JWT tokens based on a secret key. It's typically used interactively or scripted into larger workflows.
   - **Contribution**: Generates JWT tokens for testing or administrative purposes. In production, it can help manage tokens for service-to-service authentication scenarios.

### Implementing "Bearer" Authentication with JWT and PostgREST Configuration

To secure the API provided by PostgREST using JWT tokens, you implement "Bearer" token authentication. This process involves generating a secret key, configuring PostgREST to use this key for token verification, and ensuring clients provide a valid JWT in the "Authorization" header of their HTTP requests.

1. **JWT Secret Generation**: Use `jwt-cli` or another secure method to generate a JWT secret key. This key must be known to both the token issuer (possibly another part of your infrastructure) and PostgREST for token verification.

2. **Configure PostgREST for JWT**: In the PostgREST configuration file, specify the JWT secret key using the `jwt-secret` parameter. This enables PostgREST to validate incoming JWTs.

   ```conf
   db-uri = "postgres://user:pass@localhost/dbname"
   db-schema = "public"
   db-anon-role = "web_anon"
   jwt-secret = "your_jwt_secret_here"
   ```

3. **Client JWT Use**: Clients must include the JWT in the "Authorization" header of their requests, prefixed with "Bearer ". For example:

   ```
   Authorization: Bearer <token>
   ```

4. **NGINX Configuration**: Ensure NGINX forwards the Authorization header to PostgREST. In the relevant server block or location block within `nginx.conf` or a site configuration file, add:

   ```nginx
   location /api {
       proxy_pass http://localhost:3000; # Assuming PostgREST listens on port 3000
       proxy_set_header Authorization $http_authorization;
       proxy_pass_request_headers on;
   }
   ```

### System Interconnection and Functioning

The PPN stack, augmented with jwt-cli for JWT management, functions cohesively through these configurations:

- **PostgreSQL** acts as the data store, securely configured to accept connections from PostgREST.
- **PostgREST** transforms the PostgreSQL database into a RESTful API, secured with JWT for authentication, facilitating controlled access to the data.
- **NGINX** serves as the entry point for client requests, routing API calls to PostgREST and serving static content as needed. It also handles SSL termination for secure HTTPS connections, while multiple Vhosts point to multiple openAPI defined endpoints served by postgREST on the same machine.  
- **JWT Tokens** provide a secure method for authenticating API requests, with `jwt-cli` aiding in token generation and management.

By configuring each component to use secure practices, like HTTPS and JWT authentication, and ensuring proper interconnection and data flow between PostgreSQL, PostgREST, and NGINX, you create a secure, efficient, and scalable web application infrastructure.