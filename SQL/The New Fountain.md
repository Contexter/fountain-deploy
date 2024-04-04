# The New Fountain v.1

To conceptualize the new Fountain with attributes and types, let's structure it as a set of classes (akin to programming objects). This structure will highlight how various components of the play! system could interact within a microservices architecture, considering the **document**, **core**, and **supplementary** elements.

[![N|Solid](https://coach.benedikt-eickhoff.de/koken/storage/cache/images/000/705/Bild-10,xlarge.1712221972.jpeg)]

#### Document Elements
1. **FormattingRule**
   - Attributes: `ruleId: int`, `name: string`, `description: string`
   - Dependencies: Applied globally or linked to specific `Script` elements for formatting guidance.

2. **TitlePage**
   - Attributes: `title: string`, `author: string`, `revisionDate: date`, `contactInfo: string`
   - Dependencies: Directly associated with a `Script`.

3. **RevisionHistory**
   - Attributes: `revisionId: int`, `scriptId: int`, `date: date`, `description: string`
   - Dependencies: Belongs to `Script`.

4. **Casting**
   - Attributes: `castingId: int`, `scriptId: int`, `characterId: int`, `actorName: string`
   - Dependencies: Links `Character` to specific actors, associated with `Script`.

5. **CharacterRelationship**
   - Attributes: `relationshipId: int`, `character1Id: int`, `character2Id: int`, `description: string`
   - Dependencies: Between `Character` entities, describing their relationships.

#### Core Elements
1. **Script**
   - Attributes: `scriptId: int`, `title: string`, `description: string`, `author: string`
   - Dependencies: Container for `SectionHeading`, `Action`, `Dialogue`, `Character`, etc.

2. **SectionHeading**
   - Attributes: `headingId: int`, `scriptId: int`, `title: string`
   - Dependencies: Part of `Script`, organizes script content.

3. **Action**
   - Attributes: `actionId: int`, `description: string`, `sequence: int`
   - Dependencies: Within `Script` to describe non-dialogue elements.

4. **Character**
   - Attributes: `characterId: int`, `name: string`, `description: string`
   - Dependencies: Participates in `Dialogue`, linked via `Casting` and `CharacterRelationship`.

5. **Dialogue**
   - Attributes: `dialogueId: int`, `characterId: int`, `text: string`, `sequence: int`
   - Dependencies: `Character` to `Scene`; order indicated by `sequence`.

6. **Parenthetical**
   - Attributes: `parentheticalId: int`, `dialogueId: int`, `text: string`
   - Dependencies: Inside `Dialogue` to provide acting guidance.

7. **CrossReference**
   - Attributes: `referenceId: int`, `sourceElementId: int`, `targetElementId: int`, `description: string`
   - Dependencies: Links elements within or across `Script` for reference.

#### Supplementary Elements
1. **Transition**
   - Attributes: `transitionId: int`, `description: string`, `sequence: int`
   - Dependencies: Part of `Script` flow, guiding scene changes.

2. **CenteredText**
   - Attributes: `centeredTextId: int`, `text: string`, `sequence: int`
   - Dependencies: Stylistic element within `Script`.

3. **Note**
   - Attributes: `noteId: int`, `scriptId: int`, `text: string`, `sequence: int`
   - Dependencies: Annotations or reminders within `Script`.

4. **MusicSound**
   - Attributes: `soundId: int`, `description: string`, `sequence: int`
   - Dependencies: Audio cues within `Script`.

This structured approach emphasizes the relationships between elements, with `Script` serving as a central entity around which others are organized. Characters, actions, dialogues, and other elements contribute to the narrative flow, while document elements like `TitlePage` and `RevisionHistory` provide meta-level information and historical tracking. Supplementary elements like `Transition` and `MusicSound` add production and stylistic details.

In a microservices architecture, these elements could be managed by dedicated services (e.g., a Dialogue service, a Character service), with well-defined APIs facilitating interactions between them. This design supports scalability, flexibility, and independent development and deployment of services.
