# Vapor Keys to the Fountain & a System State Router 

In this comprehensive tutorial, we'll guide you through creating a secure and documented web API using Vapor, a popular Swift web framework. This API will include endpoints to check the state of various system services, such as NGINX, PostgreSQL, and your Vapor application itself. For enhanced security, we'll implement API key validation to control access to these endpoints. Additionally, we'll set up OpenAPI documentation to make your API easily understandable and testable. This tutorial is designed with first-time readers in mind, assuming basic familiarity with Vapor and Swift.

### Goal

Our aim is to:

1. Secure our Vapor application's endpoints with API key validation.
2. Enable system state checks within our application.
3. Document our API using OpenAPI specifications.

Let's break down each step:

### Step 1: Configure PostgreSQL for Secure API Access

We start by preparing our PostgreSQL database to store API keys and associate them with specific roles. Run the following script to set up your database:

```bash
#!/bin/bash
# Configure PostgreSQL for Secure Access to PostgREST project.

DATABASE="your_database" # Replace with your actual database name
USERNAME="your_username" # Replace with your PostgreSQL username

# SQL command to create the API keys table with associated roles
SQL_COMMAND="
DO \$\$
BEGIN
    -- Attempt to drop the api_keys table if it already exists
    BEGIN
        DROP TABLE IF EXISTS api_keys;
    EXCEPTION WHEN OTHERS THEN
        RAISE NOTICE 'api_keys table not found, creating new.';
    END;
    -- Create the api_keys table
    CREATE TABLE api_keys (
        id SERIAL PRIMARY KEY,
        key TEXT NOT NULL,
        role_name TEXT NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
    );

    -- Attempt to drop the example_role if it already exists
    BEGIN
        DROP ROLE IF EXISTS example_role;
    EXCEPTION WHEN OTHERS THEN
        RAISE NOTICE 'example_role not found, creating new.';
    END;
    -- Create a new role for demonstration
    CREATE ROLE example_role NOLOGIN;
    
    -- Grant permissions to the example_role on api_keys table (adjust as needed)
    GRANT SELECT ON api_keys TO example_role;
END
\$\$;
"

psql -d "$DATABASE" -U "$USERNAME" -c "$SQL_COMMAND"

echo "PostgreSQL configured."
```

Ensure you replace `your_database` and `your_username` with your actual database name and username.

### Step 2: Implement API Key Validation in Vapor

Next, we implement middleware in Vapor to validate incoming requests based on an API key. Create a file named `APIKeyValidationMiddleware.swift` in `Sources/App/Middleware/` and populate it with:

```swift
// Import Vapor framework
import Vapor

// Define your APIKeyValidationMiddleware here
// This middleware should:
// 1. Check for an API key in the request's headers
// 2. Validate the API key against your database or predefined list
// 3. Allow the request to proceed if the key is valid, otherwise return an unauthorized error
//
// Example:
struct APIKeyValidationMiddleware: Middleware {
    func respond(to request: Request, chainingTo next: Responder) -> EventLoopFuture<Response> {
        guard let apiKey = request.headers.first(name: "API-Key") else {
            return request.eventLoop.future(error: Abort(.unauthorized))
        }
        
        // Add your validation logic here
        
        return next.respond(to: request)
    }
}

// Don't forget to register this middleware in configure.swift
```

Remember to implement the actual validation logic by querying your `api_keys` table to check if the provided API key is valid.

### Step 3: Set Up OpenAPI Support in Vapor

To document your API, run the following script to add OpenAPI support to your Vapor project:

```bash
#!/bin/bash

PROJECT_DIR=$(pwd)
echo "Setting up OpenAPI support in project at $PROJECT_DIR"

# Add VaporToOpenAPI dependency to Package.swift
echo "Adding VaporToOpenAPI dependency to Package.swift..."
sed -i '' '/.package(url: "https://github.com/vapor/vapor.git", from: "4.0.0"),/a\
    .package(url: "https://github.com/dankinsoid/VaporToOpenAPI.git", from: "1.0.0"),
' Package.swift

# Include VaporToOpenAPI in target dependencies
echo "Updating target dependencies to include VaporToOpenAPI..."
sed -i '' '/.product(name: "Vapor", package: "vapor"),/a\
            .product(name: "VaporToOpenAPI", package: "VaporToOpenAPI"),
' Package.swift

# Fetch dependencies and regenerate your project
echo "Fetching dependencies..."
swift package resolve

echo "Regenerating project..."
swift package generate-xcodeproj

# Setting up Swagger UI (Optional)
echo "Setting up Swagger UI (Optional)..."
SWAGGER_UI_DIR="$PROJECT_DIR/Public/SwaggerUI"
if [ ! -d "$SWAGGER_UI_DIR" ]; then
  mkdir -p "$SWAGGER_UI_DIR"
  curl https://codeload.github.com/swagger-api/swagger-ui/tar.gz/v3.25.0 | tar -xz --strip=2 -C "$SWAGGER_UI_DIR" swagger-ui-3.25.0/dist
  echo "Swagger UI setup at $SWAGGER_UI_DIR"
else
  echo "Swagger UI directory already exists."
fi

echo "OpenAPI setup process completed."
```

### Step 4: Create System State Check Endpoints with Authentication

Following the guidance for creating the `SystemStateRouter`, now also include API key validation by using the `APIKeyValidationMiddleware` you've defined. Then, annotate your routes using VaporToOpenAPI for automatic documentation generation.

### Conclusion

By following this tutorial, you've enhanced the security of your Vapor application with API key validation, added system state check functionalities, and set up OpenAPI documentation. This not only secures your application but also makes it easier for developers to understand and interact with your API.

### The SystemStateRouter 

Creating a Vapor router to perform system state checks involves setting up endpoints that, when accessed, will execute system commands to check the status of services like NGINX, postgREST, and PostgreSQL, and even the Vapor application itself. This tutorial assumes you have basic knowledge of Swift and Vapor setup. We'll name this router `SystemStateRouter`.

### Prerequisites

- Vapor 4 installed on your system.
- Basic familiarity with Swift programming.
- Understanding of how to run shell commands in Swift.

### Step 1: Setup a New Vapor Project

If you haven't already, start by creating a new Vapor project:

```bash
vapor new SystemStateChecks
cd SystemStateChecks
```

### Step 2: Define the Router

Create a new Swift file named `SystemStateRouter.swift` in the `Sources/App/Routes` directory. If the directory does not exist, please create it.

```swift
import Vapor

struct SystemStateRouter: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        let systemRoute = routes.grouped("system")
        systemRoute.get("status", use: getStatus)
    }
    
    func getStatus(req: Request) throws -> EventLoopFuture<String> {
        let shellResponse = shell("systemctl", "status", "nginx")
        return req.eventLoop.future(shellResponse)
    }
    
    @discardableResult
    private func shell(_ args: String...) -> String {
        let task = Process()
        let pipe = Pipe()

        task.executableURL = URL(fileURLWithPath: "/usr/bin/env")
        task.arguments = args
        task.standardOutput = pipe
        task.standardError = pipe

        do {
            try task.run()
        } catch {
            return "Error: \(error.localizedDescription)"
        }

        let data = pipe.fileHandleForReading.readDataToEndOfFile()
        let output = String(decoding: data, as: UTF8.self)
        return output
    }
}
```

In this example, `SystemStateRouter` defines a route that responds to GET requests on `/system/status`. The `getStatus` function uses the `shell` method to execute the `systemctl status nginx` command and returns its output. The `shell` method executes shell commands and returns their output as a `String`.

### Step 3: Register the Router

Open `Sources/App/configure.swift` and import the `SystemStateRouter` at the top:

```swift
import Vapor

// Add this line
import SystemStateRouter
```

Then, register the `SystemStateRouter` within the `configure` function:

```swift
public func configure(_ app: Application) throws {
    // Existing configuration
    
    // Register routers
    try routes(app)
    
    let systemStateRouter = SystemStateRouter()
    try app.register(collection: systemStateRouter)
}
```

### Step 4: Expand Functionality

You can expand the `SystemStateRouter` by adding more routes that check the status of other services like postgREST, PostgreSQL, or even the Vapor app itself, similar to the `getStatus` function. You might also need to modify the `shell` method to handle these commands properly.

### Step 5: Running Your Project

Run your project using the Vapor command line tool or your IDE:

```bash
vapor build
vapor run
```

Access the system state check endpoint:

```
http://localhost:8080/system/status
```

This endpoint will now return the status of NGINX as output from the `systemctl status nginx` command.

### Security Note

Exposing system status and executing shell commands through a web API pose security risks. Ensure you implement proper authentication, authorization, and input validation to safeguard your application.

This tutorial provides a basic implementation for checking system status within a Vapor application. Depending on your specific needs, you can customize the router to include additional functionality, such as parsing command outputs more finely or adding endpoints for different system checks.

