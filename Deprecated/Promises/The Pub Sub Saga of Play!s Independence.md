# The Pub Sub Saga of Play!s Independence
---
In a microservices architecture where each microservice operates independently with its dedicated schema, managing foreign keys that reference tables across different schemas can be challenging. Typically, in a microservices environment, it's recommended to limit or avoid direct database-level foreign key references between services to maintain service independence and avoid tight coupling. However, if your design requires maintaining relationships similar to foreign keys across different microservices (schemas), consider these approaches:
## Application-Level Enforcement: 
Handle the integrity and consistency of relationships at the application level rather than the database level. This involves implementing checks within your service's logic to ensure that referenced entities exist before creating or updating records.
## Event-Driven Architecture: 
Use an event-driven approach where services listen to events from other services to update their state. For instance, if a primary entity is deleted, an event can be published so that related services can react accordingly, such as deleting or marking related entities as inactive.
## Distributed Transaction Patterns: 
For operations that span multiple services, consider patterns like Saga which ensure data consistency without requiring distributed transactions. Sagas are sequences of local transactions where each service performs its transaction and publishes an event; subsequent transactions are triggered by previous events.
## API Calls for Validation: 
Services can expose APIs to validate the existence of entities. Before performing operations that depend on entities managed by another service, make an API call to ensure the entity exists.
## Replicate Foreign Key Data: 
In some cases, replicating minimal necessary data (like identifiers) can be acceptable to maintain reference integrity. Ensure that this replication is managed carefully to prevent data inconsistency.
## Example:
Assuming you have a playwrights-schema and scripts-schema, instead of creating a direct foreign key from scripts to playwrights, you manage this relationship at the application level or through one of the approaches mentioned above.
## Conclusion:
While foreign keys serve as a foundational element of relational database design by ensuring referential integrity, their direct use in a distributed microservices architecture may introduce challenges. It's essential to balance the need for data integrity with the principles of microservices, such as service autonomy and loose coupling. Therefore, re-evaluating the existing fountain.sql bootstrap script to adapt to these approaches might be necessary, ensuring that each microservice can operate independently while maintaining overall system integrity.