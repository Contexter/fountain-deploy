-- Fountain Database Bootstrap for Microservices Architecture

/* 
Reason for change:
Moving from a monolithic structure with tight coupling via foreign keys to a microservices architecture.
This shift enhances scalability, flexibility, and service isolation, allowing each part of the play or screenplay
to be managed by dedicated microservices. Using SERIAL PRIMARY KEY in each table ensures uniqueness and independence,
aligning with the principles of microservices by eliminating direct dependencies between tables.
*/

-- Playwright Table
CREATE TABLE Playwright (
    Author_ID SERIAL PRIMARY KEY,
    Name TEXT NOT NULL,
    Biography TEXT,
    Contact_Information TEXT
);

-- Metadata Table
CREATE TABLE Metadata (
    Metadata_ID SERIAL PRIMARY KEY,
    Creation_Date DATE,
    Last_Modified_Date DATE,
    Version_Number INTEGER,
    Additional_Information TEXT
);

-- Script Table
CREATE TABLE Script (
    Script_ID SERIAL PRIMARY KEY,
    Title TEXT NOT NULL,
    Author_ID INTEGER,
    URL TEXT,
    Metadata_ID INTEGER
);

-- Act Table
CREATE TABLE Act (
    Act_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Act_Number INTEGER NOT NULL,
    Synopsis TEXT,
    Notes TEXT
);

-- Scene Table
CREATE TABLE Scene (
    Scene_ID SERIAL PRIMARY KEY,
    Act_ID INTEGER,
    Scene_Number INTEGER NOT NULL,
    Synopsis TEXT,
    Notes TEXT
);

-- Character Table
CREATE TABLE Character (
    Character_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Name TEXT NOT NULL,
    Description TEXT
);

-- Dialogue Table
CREATE TABLE Dialogue (
    Dialogue_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER,
    Character_ID INTEGER,
    Original_Text TEXT,
    Modernized_Text TEXT
);

-- Action Table
CREATE TABLE Action (
    Action_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER,
    Character_ID INTEGER,
    Original_Text TEXT,
    Modernized_Text TEXT
);

-- Transition Table
CREATE TABLE Transition (
    Transition_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER,
    Transition_Text TEXT
);

-- Parenthetical Table
CREATE TABLE Parenthetical (
    Parenthetical_ID SERIAL PRIMARY KEY,
    Dialogue_ID INTEGER,
    Original_Text TEXT,
    Modernized_Text TEXT
);

-- Note Table
CREATE TABLE Note (
    Note_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Type TEXT,
    Text TEXT
);

-- CenteredText Table
CREATE TABLE CenteredText (
    Centered_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Text TEXT
);

-- PageBreak Table
CREATE TABLE PageBreak (
    Page_Break_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Page_Number INTEGER
);

-- SectionHeading Table
CREATE TABLE SectionHeading (
    Section_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Text TEXT
);

-- TitlePage Table
CREATE TABLE TitlePage (
    Title_Page_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Text TEXT
);

-- Casting Table
CREATE TABLE Casting (
    Casting_ID SERIAL PRIMARY KEY,
    Character_ID INTEGER,
    Actor_Characteristics_Choices TEXT
);

-- CharacterRelationship Table
CREATE TABLE CharacterRelationship (
    Relationship_ID SERIAL PRIMARY KEY,
    Character1_ID INTEGER,
    Character2_ID INTEGER,
    Relationship_Type TEXT
);

-- MusicSound Table
CREATE TABLE MusicSound (
    Music_Sound_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER,
    Cue TEXT,
    Description TEXT
);

-- Props Table
CREATE TABLE Props (
    Prop_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER,
    Description TEXT
);

-- RevisionHistory Table
CREATE TABLE RevisionHistory (
    Revision_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Date DATE,
    Change_Description TEXT,
    Editor TEXT
);

-- FormattingRules Table
CREATE TABLE FormattingRules (
    Rule_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Rule_Description TEXT
);

-- CrossReferences Table
CREATE TABLE CrossReferences (
    Cross_Reference_ID SERIAL PRIMARY KEY,
    Scene_ID INTEGER,
    Referenced_Scene_ID INTEGER,
    Description TEXT
);

-- ExtendedNotesResearch Table
CREATE TABLE ExtendedNotesResearch (
    Research_ID SERIAL PRIMARY KEY,
    Script_ID INTEGER,
    Notes TEXT,
    Research_Details TEXT
);

-- SceneLocation Table
CREATE TABLE SceneLocation (
    Location_ID SERIAL PRIMARY KEY,
    Description TEXT NOT NULL,
    Historical_Cultural_Significance TEXT
);

/*
Each table is designed as a microservice, capable of operating independently. This architecture choice promises enhanced scalability, resilience, and flexibility in managing and evolving the fountain backend. By employing SERIAL PRIMARY KEYS, each entity within the ecosystem maintains its uniqueness and integrity, facilitating seamless interactions within and across services without the need for direct database relationships.
*/
