# The New Fountain v2 
###### Class Model Overview
---
## Document Elements
- ### **FormattingRule**
  - **Attributes:**
    - `ruleId: int`
    - `name: string`
    - `description: string`
  - **Dependencies:** Applied globally or linked to specific `Script` elements for formatting guidance.

- ### **RevisionHistory**
  - **Attributes:**
    - `revisionId: int`
    - `scriptId: int`
    - `date: date`
    - `description: string`
  - **Dependencies:** Belongs to `Script`.

- ### **Casting**
  - **Attributes:**
    - `castingId: int`
    - `scriptId: int`
    - `characterId: int`
    - `actorName: string`
  - **Dependencies:** Links `Character` to specific actors, associated with `Script`.

- ### **CharacterRelationship**
  - **Attributes:**
    - `relationshipId: int`
    - `character1Id: int`
    - `character2Id: int`
    - `description: string`
  - **Dependencies:** Between `Character` entities, describing their relationships.

## Core Elements
- ### **Script**
  - **Attributes:**
    - `scriptId: int`
    - `title: string`
    - `description: string`
    - `author: string`
  - **Dependencies:** Container for `SectionHeading`, `Action`, `Dialogue`, `Character`, etc.
  - #### **SectionHeading**
    - **Attributes:**
      - `headingId: int`
      - `scriptId: int`
      - `title: string`
  - #### **Action**
    - **Attributes:**
      - `actionId: int`
      - `description: string`
      - `sequence: int`
  - #### **Dialogue**
    - **Attributes:**
      - `dialogueId: int`
      - `characterId: int`
      - `text: string`
      - `sequence: int`
    - ##### **Parenthetical**
      - **Attributes:**
        - `parentheticalId: int`
        - `dialogueId: int`
        - `text: string`
  - #### **Character**
    - **Attributes:**
      - `characterId: int`
      - `name: string`
      - `description: string`
  - #### **CrossReference**
    - **Attributes:**
      - `referenceId: int`
      - `sourceElementId: int`
      - `targetElementId: int`
      - `description: string`

## Supplementary Elements
- ### **Transition**
  - **Attributes:**
    - `transitionId: int`
    - `description: string`
    - `sequence: int`
  - **Dependencies:** Part of `Script` flow, guiding scene changes.
- ### **CenteredText**
  - **Attributes:**
    - `centeredTextId: int`
    - `text: string`
    - `sequence: int`
  - **Dependencies:** Stylistic element within `Script`.
- ### **Note**
  - **Attributes:**
    - `noteId: int`
    - `scriptId: int`
    - `text: string`
    - `sequence: int`
  - **Dependencies:** Annotations or reminders within `Script`.
- ### **MusicSound**
  - **Attributes:**
    - `soundId: int`
    - `description: string`
    - `sequence: int`
  - **Dependencies:** Audio cues within `Script`.
  
### Class Dependencies ![Class Dependency and Hierarchy](https://coach.benedikt-eickhoff.de/koken/storage/cache/images/000/707/Bild-14,xlarge.1712237762.jpeg)

### Grouped Color Coded

![Class Dependencies with Attributes](https://coach.benedikt-eickhoff.de/koken/storage/cache/images/000/706/Bild-16,xlarge.1712237761.jpeg)

