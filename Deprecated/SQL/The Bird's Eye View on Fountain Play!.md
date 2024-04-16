# The Bird's Eye View on Fountain play!
This script is designed to provide a comprehensive overview of the database's structure by iterating through all schemas, tables within those schemas, and columns within those tables, excluding system schemas to focus on user-defined content. Here's an in-depth commentary on its flow and function:

### Script Overview:
The script uses a PL/pgSQL anonymous block (`DO $$ ... $$;`) to execute a series of nested loops that traverse through the database's hierarchy from schemas to tables to columns. It dynamically fetches and displays information about each level of the database structure.

### Declaration Section:
- **`schema_rec RECORD;`**: Declares a variable to temporarily hold records from the `information_schema.schemata` table, representing each schema in the database.
- **`tbl RECORD;`**: Declares a variable to temporarily hold records from the `information_schema.tables` table, representing each table within a schema.
- **`col RECORD;`**: Declares a variable to temporarily hold records from the `information_schema.columns` table, representing each column within a table.

### Operational Flow:

1. **Schema-Level Loop**:
    - The outermost loop iterates over all user-defined schemas by querying the `information_schema.schemata` table, excluding the system schemas (`public`, `information_schema`, `pg_catalog`) to focus on the schemas created by the user or application.
    - For each schema, it uses `RAISE NOTICE` to output the schema's name, utilizing the `schema_rec.schema_name` field from the loop's current record.

2. **Table-Level Loop**:
    - Within each schema iteration, a nested loop queries the `information_schema.tables` table to retrieve all tables belonging to the current schema (`schema_rec.schema_name`).
    - Tables are ordered by their name to ensure a consistent and readable output.
    - For each table, it outputs the table's name with indentation for readability and hierarchical understanding.

3. **Column-Level Loop**:
    - The innermost loop fetches all columns for the current table by querying the `information_schema.columns` table, filtering by the current schema and table name.
    - Columns are ordered by their `ordinal_position` to respect the defined order within the table.
    - For each column, it outputs the column name and data type, providing detailed insight into the table's structure and the nature of the data it holds.

### Purpose and Use Case:
This script is particularly useful for database administrators, developers, or data analysts who need to quickly understand the structure of an unfamiliar database or verify the schema after migrations or major changes. It provides a bird's eye view of the database's organization, facilitating tasks such as schema reviews, documentation, or planning data models and relationships.

By outputting the structure in a hierarchical, indented format, the script makes it easy to visualize the relationships between schemas, tables, and columns, aiding in the comprehension and analysis of the database's design.

```sql
DO $$
DECLARE
    schema_rec RECORD;
    tbl RECORD;
    col RECORD;
BEGIN
    FOR schema_rec IN SELECT schema_name FROM information_schema.schemata WHERE schema_name NOT IN ('public', 'information_schema', 'pg_catalog') LOOP
        RAISE NOTICE 'Schema: %', schema_rec.schema_name;
        FOR tbl IN SELECT table_name FROM information_schema.tables WHERE table_schema = schema_rec.schema_name ORDER BY table_name LOOP
            RAISE NOTICE '    Table: %', tbl.table_name;
            FOR col IN SELECT column_name, data_type FROM information_schema.columns WHERE table_schema = schema_rec.schema_name AND table_name = tbl.table_name ORDER BY ordinal_position LOOP
                RAISE NOTICE '        Column: %, Type: %', col.column_name, col.data_type;
            END LOOP;
        END LOOP;
    END LOOP;
END $$;
```

