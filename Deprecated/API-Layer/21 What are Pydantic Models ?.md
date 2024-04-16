Pydantic is a data validation and settings management library for Python. It uses Python type annotations to validate data and automatically convert it to the desired data types. This makes it a powerful tool for data parsing, validation, and modeling, particularly in applications where strict data integrity is necessary.

Pydantic models are essentially Python classes that define the structure of your data. These models include fields with type annotations, and Pydantic ensures that any data assigned to these fields matches the specified types. If the data does not conform, Pydantic raises a validation error.

Here’s a basic example of a Pydantic model:

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: float

# When you create an instance of the User model, Pydantic will validate the data:
user = User(id=123, name="John Doe", age=30.5)

# If you try to create a user with invalid data types, a validation error is raised:
# user = User(id="123", name="John Doe", age="30.5")  # This will raise an error
```

Key features of Pydantic models include:

- **Data validation:** Automatically performs data type validation and conversion. It can also handle more complex validation rules.
- **ORM mode:** Allows models to work with ORM objects by converting them into Pydantic models for data validation and serialization.
- **Settings management:** Pydantic can be used to manage application settings, loading from environment variables and ensuring that all settings conform to a specified schema.
- **JSON serialization:** Pydantic models can be easily converted to and from JSON, making them highly useful in web development, especially with FastAPI.

Overall, Pydantic models provide a robust way to ensure that your data structures are consistent, validated, and easily serialized/deserialized, which is particularly useful in web APIs, data processing, and configuration management scenarios.

# How does FTAB support Pydantic Models ?

FTAB is designed to scaffold a Python web application project using SQLAlchemy for database models and Pydantic for data validation and schema definition. It automates several steps in setting up a new resource (like a new entity or model in your application) by generating boilerplate code for models, schemas, CRUD operations, and API routes. Here's how it supports Pydantic models and integrates them into the overall application structure:

1. **Pydantic Schema Generation:**
   - The script generates Pydantic schemas based on user-provided field definitions. These schemas are created in the `SCHEMAS_DIR` directory. Pydantic schemas are used for data validation and serialization/deserialization of request and response payloads in the API layer. The schema files include base schemas, create schemas (for creating new instances of the resource), and in-database schemas (representing the database model plus any additional computed fields).

2. **Data Validation and Conversion:**
   - Pydantic uses the type annotations in the schema definitions to validate and convert incoming JSON payloads into Python objects. This ensures that the data received by the API endpoints meets the expected structure and types before any processing or database operations are performed.

3. **ORM Mode Configuration:**
   - In the generated Pydantic schemas, the script includes a configuration class with `orm_mode` set to `True`. This allows Pydantic models to work with ORM objects, making it easier to return SQLAlchemy model instances directly from your endpoints. Pydantic will understand how to read data from these instances (not just dictionaries), which simplifies the integration between the database layer and the API layer.

4. **CRUD Operations:**
   - The script also scaffolds CRUD (Create, Read, Update, Delete) operations in the `SERVICES_DIR` directory. While these operations are primarily focused on SQLAlchemy models for database interactions, they interact closely with Pydantic schemas for data validation and conversion when creating new instances or processing incoming data.

5. **API Routes:**
   - Finally, API endpoint routes are set up to use the Pydantic schemas for validating request payloads and serializing response payloads. This integration ensures that all data entering and leaving the application via the API is validated against the Pydantic models, providing a layer of data integrity and error handling.

In summary, this script supports Pydantic models by generating schema files based on user input, configuring them for integration with SQLAlchemy models, and setting up API endpoints to utilize these schemas for robust data validation and serialization/deserialization. This structure is commonly used in modern Python web applications, especially those built with FastAPI, to ensure type safety, data validation, and easy integration between the database layer and the API layer.