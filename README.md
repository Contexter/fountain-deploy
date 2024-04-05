![](https://coach.benedikt-eickhoff.de/koken/storage/cache/images/000/708/Bild-17,xlarge.1712241062.jpeg)

### Class Model Overview
---

#### Core Elements

- **Script**
  - Attributes:
    - scriptId: int
    - title: string
    - description: string
    - author: string
    - sequence: int
  - Dependencies: Container for SectionHeading, Action, SpokenWord, Character, Transition, Note, MusicSound. Acts as a repository for formatting rules applicable to these elements.

- **SectionHeading**
  - Attributes:
    - headingId: int
    - scriptId: int
    - title: string
    - sequence: int

- **Action**
  - Attributes:
    - actionId: int
    - description: string
    - sequence: int

- **SpokenWord**
  - Attributes:
    - dialogueId: int
    - text: string
    - sequence: int

- **Character**
  - Attributes:
    - characterId: int
    - name: string
    - description: string
    - sequence: int

#### Supplementary Elements

- **CrossReference**
  - Attributes:
    - referenceId: int
    - sourceElementId: int
    - targetType: string (can be one, all, or a specific named entity type)
    - targetId: int (optional, used when targetType is a specific named entity)
    - description: string
  - Dependencies: Allows any entity (SectionHeading, Action, SpokenWord, Character, Transition, Note, MusicSound, Script) to be cross-referenced to one, all, or named entities, including RevisionHistory, enhancing narrative and structural complexity.

- **Transition**
  - Attributes:
    - transitionId: int
    - description: string
    - sequence: int

- **Note**
  - Attributes:
    - noteId: int
    - scriptId: int
    - text: string
    - sequence: int

- **MusicSound**
  - Attributes:
    - soundId: int
    - description: string
    - sequence: int

#### Revision History

- **RevisionHistory**
  - Attributes:
    - revisionId: int
    - scriptId: int
    - date: date
    - description: string
  - Dependencies: Belongs to Script. Now, it can also be targeted by CrossReferences, providing a link between revisions and other script elements.

This revised dependency list incorporates the new connection between "CrossReference" and "RevisionHistory," further enhancing the model's capacity for detailed, interconnected script management and documentation.
