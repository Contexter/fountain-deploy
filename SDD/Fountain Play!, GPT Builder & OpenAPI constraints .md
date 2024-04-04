# GPT Builder & OpenAPI constraints

1. **Use of HTTPS**: All server URLs specified in the `servers` section must use HTTPS to ensure secure communication. This is crucial for protecting data integrity and privacy between the client and server.

2. **OperationId Uniqueness**: Every operation (GET, POST, PUT, DELETE) defined in the paths must have a unique `operationId`. This identifier is used to ensure distinctness across all operations within the API, facilitating code generation, documentation, and client integration.

3. **Detailed Request and Response Bodies**: The request and response bodies need to be thoroughly described in the OpenAPI document. This includes defining the schemas for all resources (like Characters, Scenes, etc.) and specifying the required fields, data types, and any constraints on the data (e.g., string length, numeric range).

4. **Parameters Specification**: All parameters, whether path parameters (e.g., `characterId`) or query parameters, must be explicitly defined. This includes their location (`in: path` or `in: query`), name, required status, and data type.

5. **Error Handling**: The OpenAPI document should specify the possible error responses for each operation. Common HTTP status codes like 400 (Bad Request), 404 (Not Found), and 500 (Internal Server Error) need to be included to help clients handle errors properly.

6. **Security Schemes**: If the API requires authentication or authorization, the security schemes (e.g., API keys, JWT, OAuth2) should be defined in the OpenAPI document. This includes setting up the security scheme and applying it to the entire API or specific operations.

7. **Versioning**: The version of the API should be clearly indicated in the `info` section of the OpenAPI document. This helps in managing changes and ensuring backward compatibility.

By adhering to these constraints, the OpenAPI document ensures that the backend services are well-defined, secure, and easily integrable with frontend applications, other services, and tools like Swagger UI for testing and documentation. This structure supports the principles of a microservices architecture, promoting service isolation, scalability, and flexibility.

## An Example for a `Character` Resource

For each resource, we would typically define API endpoints that allow users to perform CRUD operations. Here's a rough outline of how this might look in an OpenAPI document, which passes the GPT Builder "Linter" and fits into defined constraints:

- **Endpoints**:
  - `GET /characters` - Retrieve all characters.
  - `POST /characters` - Create a new character.
  - `GET /characters/{characterId}` - Retrieve a character by ID.
  - `PUT /characters/{characterId}` - Update a character by ID.
  - `DELETE /characters/{characterId}` - Delete a character by ID.

## an Example in .yaml

```yaml
openapi: 3.0.0
info:
  title: Play Management API
  version: 1.0.0
servers:
  - url: 'https://dummyserver.com/api'
    description: Dummy Server for testing
paths:
  /characters:
    get:
      summary: Get a list of all characters
      operationId: listCharacters
      responses:
        '200':
          description: A list of characters
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Character'
    post:
      summary: Create a new character
      operationId: createCharacter
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Character'
      responses:
        '201':
          description: Created a new character
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Character'
  /characters/{characterId}:
    get:
      summary: Get a character by ID
      operationId: getCharacterById
      parameters:
        - in: path
          name: characterId
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: A single character
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Character'
    put:
      summary: Update a character by ID
      operationId: updateCharacterById
      parameters:
        - in: path
          name: characterId
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Character'
      responses:
        '200':
          description: Updated character
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Character'
    delete:
      summary: Delete a character by ID
      operationId: deleteCharacterById
      parameters:
        - in: path
          name: characterId
          required: true
          schema:
            type: integer
      responses:
        '204':
          description: Deleted character
components:
  schemas:
    Character:
      type: object
      properties:
        id:
          type: integer
        name:
          type: string
        description:
          type: string
        play_id:
          type: integer
      required:
        - name
```



