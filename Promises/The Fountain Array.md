# The Fountain Array

The "Fountain" backend, designed to manage and represent the complex structures of theatrical scripts, includes a comprehensive array of tables, each serving a distinct purpose within the ecosystem of script management. Here's a detailed list of 24 key tables within the "Fountain" backend, known as "The Array," highlighting the function and interconnectivity of each:

1. **Playwright**: Stores details about script authors, including names, biographies, and contact information.
2. **Script**: Contains script titles, links (URLs), authorship, and metadata references.
3. **Metadata**: Captures creation dates, modification dates, version numbers, and additional script information.
4. **Act**: Organizes scripts into larger divisions, linking back to the Script table.
5. **Scene**: Breaks down acts into individual scenes, detailing the progression of the narrative.
6. **Character**: Lists characters in scripts, including names and descriptions, linked to specific scripts.
7. **Dialogue**: Stores spoken lines by characters, associated with specific scenes and characters.
8. **Action**: Details non-spoken actions or stage directions, linked to scenes and characters.
9. **Transition**: Manages scene or act transitions within the script, providing pacing and flow.
10. **Parenthetical**: Notes within dialogue blocks, offering additional context or action cues.
11. **Note**: General notes related to scripts, scenes, or characters, for additional information or reminders.
12. **Casting**: Details casting choices for characters, linking actors to roles within scripts.
13. **CharacterRelationship**: Describes relationships between characters, enhancing narrative depth.
14. **MusicSound**: Specifies music and sound effects used within scenes, linked to specific narrative moments.
15. **Props**: Lists physical props required for scenes, ensuring logistical preparation for performances.
16. **RevisionHistory**: Tracks changes to scripts over time, including edits, updates, and version tracking.
17. **FormattingRules**: Defines specific formatting guidelines applied to script texts for consistency.
18. **CenteredText**: Manages text that needs to be centered for stylistic or structural reasons within scripts.
19. **PageBreak**: Controls the pagination of scripts, ensuring clear division and readability.
20. **SectionHeading**: Organizes scripts into sections beyond acts and scenes for additional structure.
21. **TitlePage**: Contains information for the script's title page, including title, author, and copyright.
22. **ExtendedNotesResearch**: Stores extensive notes and research related to scripts for deeper context.
23. **SceneLocation**: Details the setting and location of scenes, providing background and atmosphere.
24. **CrossReferences**: Allows for the referencing of scenes or elements within or across scripts for thematic or narrative linkage.

These 24 tables constitute the foundational structure of the "Fountain" backend, enabling the detailed organization, analysis, and presentation of theatrical scripts. Each table plays a critical role in capturing the multifaceted aspects of scriptwriting and production, from the creative inception of a script to its practical execution on stage.