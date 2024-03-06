# What else could we do? Why go there ?

Given the "Fountain Array" and the playground setup we've discussed, there are several engaging ways to "play" with this data and explore the functionalities and relationships within the theatrical script management system. Here are some project ideas and queries you can experiment with to deepen your understanding of database operations and the complex structures of theatrical scripts:

### Project Ideas

1. **Script Analysis Tool**: Develop a tool that analyzes scripts based on various metrics, such as dialogue length, character involvement, and act structure. Use SQL queries to aggregate and analyze data across the `Dialogue`, `Character`, and `Act` tables.

2. **Character Relationship Map**: Create a visualization of character relationships within a script. This could involve querying the `CharacterRelationship` table and using a graph library in your favorite programming language to visually represent these relationships.

3. **Revision History Tracker**: Implement a feature that tracks and displays the revision history of a script. This would involve querying the `RevisionHistory` table and presenting the changes in a user-friendly format, such as a timeline.

4. **Dynamic Script Formatting**: Build a tool that formats scripts dynamically based on the `FormattingRules` table. This tool could output a formatted script document that adheres to specified guidelines, enhancing readability and consistency.

5. **Props and Scene Management**: Create a system for managing props requirements for each scene, leveraging the `Props` and `Scene` tables. This system could help theatrical productions ensure they have all necessary props for each scene, improving logistical planning.

### Example SQL Queries

Here are some example SQL queries corresponding to the project ideas. These queries assume you're working within the playground database and are familiar with basic SQL operations:

1. **Script Analysis Tool**:
   ```sql
   SELECT character.name, COUNT(dialogue.id) AS dialogue_count
   FROM dialogue
   JOIN character ON character.id = dialogue.character_id
   GROUP BY character.name
   ORDER BY dialogue_count DESC;
   ```

2. **Character Relationship Map**:
   ```sql
   SELECT c1.name AS character_one, c2.name AS character_two, relationship.type
   FROM characterrelationship AS relationship
   JOIN character AS c1 ON relationship.character_one_id = c1.id
   JOIN character AS c2 ON relationship.character_two_id = c2.id;
   ```

3. **Revision History Tracker**:
   ```sql
   SELECT script.title, revisionhistory.date, revisionhistory.description
   FROM revisionhistory
   JOIN script ON script.id = revisionhistory.script_id
   ORDER BY revisionhistory.date;
   ```

4. **Dynamic Script Formatting**:
   ```sql
   -- This is more of a procedural operation that would involve querying the `FormattingRules` table and applying the rules to script content dynamically.
   SELECT * FROM formattingrules WHERE script_id = 1;
   ```

5. **Props and Scene Management**:
   ```sql
   SELECT scene.title, array_agg(props.name) AS props_required
   FROM props
   JOIN scene ON scene.id = props.scene_id
   GROUP BY scene.title;
   ```

These projects and queries offer a starting point for exploring the capabilities of the "Fountain" database structure and PostgreSQL. They can be adapted and expanded upon based on your specific interests and the complexity of the scripts you wish to manage.

# BUT !

BUT - let's play full PPN stack ! we're somewhere on the net - not a user on this particular database hosting machine - probably using an iPad or fiddling with Logic and make music with midi 2.0 messaging -  playing with the full PPN (PostgreSQL, PostgREST, Nginx) stack from a remote location, such as an iPad or while working with Logic and MIDI 2.0, requires a slightly different approach. Since you're interested in interacting with the API from a client that isn't directly connected to the database hosting machine, you'll be making HTTP requests to the PostgREST server, which in turn communicates with your PostgreSQL database. Nginx acts as the reverse proxy, providing secure and efficient access to the PostgREST server. Here's how you can explore this setup:

### Step 1: Set Up Remote Access

Ensure your PPN stack is configured to accept connections from the internet:

1. **Nginx**: Configure Nginx to serve as a reverse proxy for PostgREST, including setting up HTTPS with SSL certificates (e.g., using Let's Encrypt) for secure connections.
2. **PostgREST**: Make sure it's configured to point to your PostgreSQL database and is accessible via Nginx.
3. **PostgreSQL**: Configure `pg_hba.conf` and `postgresql.conf` to allow remote connections from your PostgREST service, and ensure your firewall rules permit access on the necessary ports.

### Step 2: Interact with the API

Using an HTTP client application on your iPad or any device, you can make requests to your PostgREST API through the Nginx reverse proxy. Here are examples of actions you might take:

- **Retrieve Data**: Use a GET request to fetch data, such as a list of characters from a specific script.
  ```http
  GET https://yourdomain.com/characters?script_id=eq.1
  ```

- **Insert Data**: Use a POST request to add a new entry, such as a new dialogue line.
  ```http
  POST https://yourdomain.com/dialogue
  Content-Type: application/json

  {
      "script_id": 1,
      "character_id": 2,
      "text": "To be, or not to be, that is the question."
  }
  ```

- **Update Data**: Use a PATCH request to update data, such as modifying a character's description.
  ```http
  PATCH https://yourdomain.com/character?id=eq.2
  Content-Type: application/json

  {
      "description": "The troubled prince of Denmark."
  }
  ```

- **Delete Data**: Use a DELETE request to remove an entry, such as deleting a note.
  ```http
  DELETE https://yourdomain.com/note?id=eq.3
  ```

### Tools and Applications for Remote Access

- **HTTP Client Apps**: On an iPad, you can use apps like Paw (macOS, with iPad via Sidecar), Postman (via its web version), or any other HTTP client that allows you to construct and send HTTP requests.
- **Scripting and Automation**: If you're working with Logic and MIDI 2.0, consider writing scripts (e.g., in Python or JavaScript) that interact with your API to automate tasks or integrate with your music projects. Tools like Node-RED might also be interesting for creating workflows that interact with your API.

### Security Considerations

- Ensure that your Nginx server is properly secured and that HTTPS is enforced.
- Limit access to your API as necessary, using firewalls, VPNs, or IP whitelisting.
- Consider implementing authentication and authorization for your API using JWT tokens or another secure method.

By setting up remote access to your PPN stack, you can interact with your theatrical script management system from anywhere, integrating it with a wide range of applications and workflows.