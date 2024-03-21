# Normalization ?

_Database_ normalization is a systematic approach of organizing the fields and tables of a relational database to minimize redundancy and dependency. This process involves dividing large tables into smaller, more manageable ones and defining relationships between them to increase the coherence and integrity of data. The primary aim of normalization is to reduce and even eliminate data anomalies, improve data integrity, and enhance the efficiency of database operations.

Normalization is typically performed in several stages, called "normal forms," each addressing a specific type of problem. The most commonly used normal forms are:

1. **First Normal Form (1NF):** Ensures that the values in each column of a table are atomic, meaning that they are indivisible. This eliminates repeating groups, ensuring that there is a primary key and that the table structure is flat.

2. **Second Normal Form (2NF):** Achieved by taking data that is already in 1NF and removing partial dependencies; that is, making sure that all non-key attributes are fully functional dependent on the primary key.

3. **Third Normal Form (3NF):** In addition to meeting all the requirements of 2NF, a table is in 3NF if it has no transitive dependencies. This means that non-key attributes do not depend on other non-key attributes.

4. **Boyce-Codd Normal Form (BCNF):** Sometimes considered a stricter version of 3NF, a table is in BCNF if, for every one of its dependencies, the left side of the dependency is a candidate key. This form deals with certain types of anomaly not covered by 3NF.

There are further normal forms (4NF and 5NF, also known as the Project-Join Normal Form), which deal with more complex types of redundancy and dependency issues, but these first three (along with BCNF) are foundational and the most frequently implemented in practical database design.

By adhering to normalization principles, databases can reduce storage costs, avoid data inconsistencies, and ensure a scalable and flexible structure that supports efficient queries, updates, and integrity of the data. However, over-normalization can lead to excessive table joins, which might degrade performance. Therefore, balancing normalization with the practicalities of application use is essential.

# Normalize! Character play!
##### unnormal initial ALTER Statements  

---
```
-- Create Plays Table
CREATE TABLE plays (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) DEFAULT 'William Shakespeare'
);
-- Create Acts Table
CREATE TABLE acts (
    id SERIAL PRIMARY KEY,
    play_id INTEGER REFERENCES plays(id),
    number INTEGER NOT NULL,
    title VARCHAR(255),
    UNIQUE(play_id, number)
);
-- Create Scenes Table
CREATE TABLE scenes (
    id SERIAL PRIMARY KEY,
    act_id INTEGER REFERENCES acts(id),
    number INTEGER NOT NULL,
    title VARCHAR(255),
    location VARCHAR(255),
    UNIQUE(act_id, number)
);
-- Create Dialogues Table
CREATE TABLE dialogues (
    id SERIAL PRIMARY KEY,
    scene_id INTEGER REFERENCES scenes(id),
    character_name VARCHAR(255) NOT NULL,
    original_text TEXT NOT NULL,
    modern_text TEXT,
    sequence INTEGER NOT NULL,
    UNIQUE(scene_id, sequence)
);
-- Index for efficient query performance
CREATE INDEX idx_play ON acts(play_id);
CREATE INDEX idx_act ON scenes(act_id);
CREATE INDEX idx_scene ON dialogues(scene_id
);
-- Characters Table
CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    play_id INTEGER REFERENCES plays(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    CONSTRAINT character_name_unique UNIQUE (play_id, name)
);
-- Modify Dialogues Table to include character_id
ALTER TABLE dialogues ADD COLUMN character_id INTEGER;
ALTER TABLE dialogues ADD CONSTRAINT fk_character FOREIGN KEY (character_id) REFERENCES characters(id);
ALTER TABLE dialogues DROP COLUMN character_name;
```

# Rewriting is Normalization

Rewriting the SQL script to initially create all tables and include the modifications previously done through `ALTER` statements into the initial `CREATE TABLE` commands, along with comprehensive comments, results in the following:

```sql
-- Create Plays Table
-- Stores information about each play, including title and author. Default author is William Shakespeare.
CREATE TABLE plays (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) DEFAULT 'William Shakespeare'
);

-- Create Characters Table
-- Contains details about characters in the plays, linked to the plays table.
CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    play_id INTEGER REFERENCES plays(id),
    name VARCHAR(255) NOT NULL,
    description TEXT,
    CONSTRAINT character_name_unique UNIQUE (play_id, name)
);

-- Create Acts Table
-- Organizes plays into acts, ensuring each act is uniquely numbered within a play.
CREATE TABLE acts (
    id SERIAL PRIMARY KEY,
    play_id INTEGER REFERENCES plays(id),
    number INTEGER NOT NULL,
    title VARCHAR(255),
    UNIQUE(play_id, number)
);

-- Create Scenes Table
-- Breaks down acts into scenes with unique numbering within each act and includes scene locations.
CREATE TABLE scenes (
    id SERIAL PRIMARY KEY,
    act_id INTEGER REFERENCES acts(id),
    number INTEGER NOT NULL,
    title VARCHAR(255),
    location VARCHAR(255),
    UNIQUE(act_id, number)
);

-- Create Dialogues Table
-- Stores dialogues within scenes, linking to characters by ID instead of name for better normalization.
-- Each dialogue entry includes original and modern text versions, uniquely sequenced within each scene.
CREATE TABLE dialogues (
    id SERIAL PRIMARY KEY,
    scene_id INTEGER REFERENCES scenes(id),
    character_id INTEGER REFERENCES characters(id), -- Links to characters table
    original_text TEXT NOT NULL,
    modern_text TEXT,
    sequence INTEGER NOT NULL,
    UNIQUE(scene_id, sequence)
);

-- Indexes for efficient query performance on foreign keys
CREATE INDEX idx_play ON acts(play_id);
CREATE INDEX idx_act ON scenes(act_id);
CREATE INDEX idx_scene ON dialogues(scene_id);
```

This script integrates the modifications into the initial creation of the `dialogues` table, by including the `character_id` from the start and omitting the `character_name` column, which was dropped in the original script through an `ALTER` operation. By doing this, the structure becomes more normalized from the outset, with a clear relational path from dialogues to characters, then to plays, thereby enhancing data integrity and query efficiency. The inclusion of comments explains the purpose of each table and key relationships within the database schema.

Here is a comparison table in Markdown format that outlines the key differences between the original SQL script and the new, revised script:


| Feature/Change                 | Original Script                                                                                                          | New, Revised Script                                                                                                       |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Characters Table Creation**  | Not present in the initial creation. Characters table was assumed to be existing or not mentioned in the provided script. | Included at the start, before dialogues, to ensure the character_id column in the dialogues table has a valid reference. |
| **Dialogues Table Character Reference** | Included a character_name VARCHAR(255) NOT NULL, then altered to add character_id and drop character_name.               | Directly creates the dialogues table with a character_id INTEGER REFERENCES characters(id), omitting character_name.      |
| **Normalization**              | Altered the dialogues table to improve normalization by adding a character reference.                                     | Begins with a normalized approach by directly referencing characters in the dialogues table, avoiding later alterations.  |
| **Indexes Creation**           | Created after tables creation.                                                                                           | No change in index creation; both scripts include this step after tables creation for query optimization.                 |
| **Comments**                   | Comments are minimal or focused on changes like table modifications through ALTER statements.                            | Comprehensive comments explaining the purpose and relationships of each table, enhancing readability and maintenance.     |

This comparison highlights the key structural and organizational improvements in the new, revised script, aiming for clarity, normalization, and efficiency from the outset.

This table offers a clear visualization of the differences between the original and revised scripts, emphasizing the shift towards a more normalized and clearly commented initial setup in the revised version.