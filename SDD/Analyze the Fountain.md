# Analyze the Fountain

Based on the refined extraction from the https://github.com/Contexter/fountain-play/blob/main/SQL/fountain_microservices_bootstrap.sql SQL file, we have identified several resources that would be relevant for an OpenAPI document, representing the database structure designed for managing plays or screenplays. Here are the resources (tables) and their fields:

1. **Playwright**: `Author_ID`, `Name`, `Biography`, `Contact_Information`
2. **Metadata**: `Metadata_ID`, `Creation_Date`, `Last_Modified_Date`, `Version_Number`, `Additional_Information`
3. **Script**: `Script_ID`, `Title`, `Author_ID`, `URL`, `Metadata_ID`
4. **Act**: `Act_ID`, `Script_ID`, `Act_Number`, `Synopsis`, `Notes`
5. **Scene**: `Scene_ID`, `Act_ID`, `Scene_Number`, `Synopsis`, `Notes`
6. **Character**: `Character_ID`, `Script_ID`, `Name`, `Description`
7. **Dialogue**: `Dialogue_ID`, `Scene_ID`, `Character_ID`, `Original_Text`, `Modernized_Text`
8. **Action**: `Action_ID`, `Scene_ID`, `Character_ID`, `Original_Text`, `Modernized_Text`
9. **Transition**: `Transition_ID`, `Scene_ID`, `Transition_Text`
10. **Parenthetical**: `Parenthetical_ID`, `Dialogue_ID`, `Original_Text`, `Modernized_Text`
11. **Note**: `Note_ID`, `Script_ID`, `Type`, `Text`
12. **CenteredText**: `Centered_ID`, `Script_ID`, `Text`
13. **PageBreak**: `Page_Break_ID`, `Script_ID`, `Page_Number`
14. **SectionHeading**: `Section_ID`, `Script_ID`, `Text`
15. **TitlePage**: `Title_Page_ID`, `Script_ID`, `Text`
16. **Casting**: `Casting_ID`, `Character_ID`, `Actor_Characteristics_Choices`
17. **CharacterRelationship**: `Relationship_ID`, `Character1_ID`, `Character2_ID`, `Relationship_Type`
18. **MusicSound**: `Music_Sound_ID`, `Scene_ID`, `Cue`, `Description`
19. **Props**: `Prop_ID`, `Scene_ID`, `Description`
20. **RevisionHistory**: `Revision_ID`, `Script_ID`, `Date`, `Change_Description`, `Editor`
21. **FormattingRules**: `Rule_ID`, `Script_ID`, `Rule_Description`
22. **CrossReferences**: `Cross_Reference_ID`, `Scene_ID`, `Referenced_Scene_ID`, `Description`
23. **ExtendedNotesResearch**: `Research_ID`, `Script_ID`, `Notes`, `Research_Details`
24. **SceneLocation**: `Location_ID`, `Description`, `Historical_Cultural_Significance`

Next steps involve creating the OpenAPI document, which outlines endpoints for accessing these resources. Each resource typically has endpoints for creating, reading (individual and collection), updating, and deleting (CRUD operations). Additionally, relationships between resources (like Script to Acts, Acts to Scenes, etc.) will inform the nested routing structure.

# Grouping Resources to fit into GTP Builder Action contraints 

- **Core Elements**: `Playwright`, `Script`, `Act`, `Scene`, `Character`, `Dialogue`
- **Supplementary Elements**: `Action`, `Transition`, `Parenthetical`, `Note`, `CenteredText`
- **Structural Elements**: `PageBreak`, `SectionHeading`, `TitlePage`
- **Production Elements**: `Casting`, `CharacterRelationship`, `MusicSound`, `Props`
- **Document Elements**: `RevisionHistory`, `FormattingRules`, `CrossReferences`, `ExtendedNotesResearch`, `SceneLocation`
- 

with 
- `MetaData`missing , 
- `Action` being an ambiguous concept, possibly better grouped under the **Core Elements** & 
- `Playwright` becoming a required field of the `Script` resource ... 
- 

# Revised Grouping 

- **Document Elements** : `FormattingRule`, `TitlePage`, `RevisionHistory`, `Casting`, `CharacterRelationship`
- **Core Elements** : `Script`, `SectionHeading`, `Action`, `Character`, `Dialogue`, `Parenthetical` `CrossReference`
- **Supplementary Elements** :  `Transition`, `CenteredText`, `Note`, `MusicSound`

