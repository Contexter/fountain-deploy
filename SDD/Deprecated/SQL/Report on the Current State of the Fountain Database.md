### Report on the Current State of the Fountain Database

#### Introduction
This report provides a detailed analysis of the `fountain` database's current state, focusing on its schema structure and the relational integrity mechanisms in place. The analysis is based on the output of two critical scripts: one detailing the schema, tables, and columns, and the other investigating the presence of foreign key constraints.

#### Database Structure Overview
The `fountain` database is structured into multiple user-defined schemas, each serving distinct facets of the project's data model. Notable schemas include `playwright`, `metadata`, `script`, `act`, `scene`, `character`, `dialogue`, and others. Each schema houses tables tailored to store specific data types, ranging from textual descriptions to integer identifiers.

- **Schemas and Tables**: Each schema is dedicated to a particular aspect of theatrical scripts and their metadata, with tables designed to hold detailed information ranging from playwright details to script metadata, acts, scenes, characters, dialogues, and more.
- **Column Design**: Tables within these schemas follow a consistent design pattern, utilizing integer and text data types for storing identifiers and descriptive information, respectively. This approach facilitates efficient data indexing and flexible information storage.

#### Relational Integrity Analysis
A critical examination of the database's use of foreign key constraints revealed a noteworthy observation: the `fountain` database currently does not employ foreign key constraints to enforce referential integrity at the database level.

- **Lack of Foreign Key Constraints**: The absence of foreign key constraints suggests that referential integrity and relational dependencies between tables are managed outside the database system, likely within the application logic.
- **Implications for Data Integrity**: This design choice places the responsibility for maintaining data consistency and integrity on the application, requiring robust validation and error-handling mechanisms to prevent orphan records and ensure data accuracy.

#### Discussion

##### Data Integrity and Maintenance
Without foreign key constraints, the `fountain` database relies on the application layer to enforce data relationships. While this provides flexibility for bulk operations and schema evolution, it increases the risk of data anomalies such as orphan records. Ensuring data integrity thus becomes a shared responsibility between the application developers and database administrators.

##### Performance Considerations
The absence of foreign key checks might lead to performance improvements for certain operations. However, this benefit comes with the trade-off of potentially compromised data integrity. Proper index management and application-level checks become crucial for maintaining performance and data consistency.

##### Application Design Considerations
The reliance on application logic for enforcing data relationships necessitates a careful design approach, with a significant focus on data validation and error handling. This design paradigm may affect the application's complexity and the developers' workload.

#### Recommendations

1. **Review Data Integrity Mechanisms**: Consider implementing foreign key constraints for critical relational data to leverage the database system's capabilities for maintaining referential integrity automatically.

2. **Enhance Application Logic**: For tables and relationships where foreign keys are not used, ensure robust application-level checks and balances are in place to prevent data inconsistencies.

3. **Monitor Performance and Optimize**: Regularly review the database and application performance, especially for operations that might be affected by the lack of foreign key constraints. Optimize indexes and queries as necessary.

4. **Documentation and Knowledge Sharing**: Maintain comprehensive documentation on the database schema and application logic handling data relationships. Facilitate knowledge sharing among the development team to ensure a common understanding of the database's design and integrity mechanisms.

#### Conclusion
The `fountain` database presents a well-structured and detailed data model for managing theatrical scripts and related metadata. Its design, favoring application-level integrity mechanisms over database-enforced foreign key constraints, offers flexibility and performance benefits but requires careful management to ensure data consistency. Future developments and maintenance efforts should balance these aspects to maintain the integrity and efficiency of the database system.

 ### Birds eye view script

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
### Foreign key Detection
```
SELECT
    tc.table_schema || '.' || tc.table_name AS foreign_table,
    kcu.column_name AS foreign_column,
    ccu.table_schema || '.' || ccu.table_name AS primary_table,
    ccu.column_name AS primary_column
FROM
    information_schema.table_constraints AS tc
    JOIN information_schema.key_column_usage AS kcu
      ON tc.constraint_name = kcu.constraint_name
      AND tc.table_schema = kcu.table_schema
    JOIN information_schema.constraint_column_usage AS ccu
      ON ccu.constraint_name = tc.constraint_name
      AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type = 'FOREIGN KEY'
ORDER BY
    foreign_table,
    foreign_column;
```

