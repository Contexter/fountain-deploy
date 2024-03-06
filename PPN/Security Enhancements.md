# TRUST ALL - why not ?

The principle of "trust all" in the context of database security and API access represents an extremely permissive approach, essentially allowing any user unrestricted access to the database or API without any form of authentication or authorization. This approach poses significant security risks, including:

1. **Data Breach Risk**: Unrestricted access means any user can read, modify, or delete data, potentially exposing sensitive information or leading to data loss.
2. **Malicious Activity**: Without access controls, malicious users could inject harmful data, execute unauthorized operations, or exploit vulnerabilities within the system.
3. **Compliance Violations**: Many applications need to comply with data protection regulations (like GDPR, HIPAA) that require strict control over who can access and manipulate personal or sensitive data.
4. **System Integrity**: Trusting all users compromises the integrity of your system, as it allows uncontrolled changes that could lead to inconsistencies, errors, or system failures.

### Integrating JWT for Authentication and Authorization

JSON Web Tokens (JWT) provide a secure and scalable way to implement authentication and authorization in your applications, including those using the PostgREST and PostgreSQL stack. JWTs are compact, URL-safe tokens that can be signed (to ensure authenticity) and encrypted (to ensure security). They are designed to carry a payload of claims that can be used to convey the identity of the authenticated user, their roles, and any permissions.

#### How JWT Authentication Works with PostgREST and PostgreSQL:

1. **User Authentication**: Initially, a user authenticates against a trusted identity provider (IdP). Upon successful authentication, the IdP issues a JWT that includes claims about the user's identity and any roles or permissions.

2. **Token Verification**: When a user makes a request to the PostgREST API, the API server verifies the JWT's signature to ensure it was issued by the trusted IdP and hasn't been tampered with.

3. **Role Mapping and Access Control**: PostgREST and PostgreSQL can use the claims within the verified JWT to determine the user's role and enforce access controls based on PostgreSQL's security configurations, such as row-level security policies.

#### Implementing JWT with PostgREST:

1. **JWT Secret Configuration**: Configure PostgREST with the secret key used to sign the JWTs or the public key of the RSA pair if asymmetric keys are used. This allows PostgREST to verify the authenticity of incoming JWTs.

    ```bash
    db-jwt-secret = "your_jwt_secret_here"
    ```

2. **Passing the JWT**: Clients must include the JWT in the `Authorization` header of their HTTP requests to the API.

    ```
    Authorization: Bearer <your.jwt.token>
    ```

3. **Role Claim**: Ensure the JWT includes a role claim that matches the roles defined in your PostgreSQL database. PostgREST uses this claim to set the database session role, which in turn controls access based on the database's permission system.

    ```json
    {
      "role": "user_role",
      "user_id": "123",
      "exp": 1516239022
    }
    ```

4. **Row-Level Security**: In PostgreSQL, define row-level security policies that leverage the user's role or other claims from the JWT to control access to rows in tables.

    ```sql
    CREATE POLICY access_policy ON my_table FOR SELECT
    USING (user_id = current_setting('request.jwt.claim.user_id')::int);
    ```

5. **Refreshing Tokens**: Implement a mechanism to refresh tokens when they expire or when permissions change, ensuring users have continuous access without compromising security.

Using JWT for authentication and authorization with PostgREST and PostgreSQL provides a secure, flexible, and efficient way to control access to your APIs, ensuring that only authenticated and authorized users can perform allowed operations.