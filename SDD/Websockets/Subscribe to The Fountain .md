### Subscribe to The Fountain

The following specification defines a complete structure for WebSocket interaction across various components of a play script, including characters, spoken words, actions, section headings, the script, transitions, music/sound, and notes. It allows for real-time communication with a server handling "The Fountain." Each **get** operation represents a subscription to a WebSocket stream for a particular aspect of the play.


```
openapi: 3.0.1
info:
  title: The Fountain WebSocket API
  description: WebSocket API to interact with different aspects of the play script for "The Fountain."
  version: "1.0.0"

servers:
  - url: https://fountain.coach
    description: Root HTTPS server for The Fountain
  - url: wss://fountain.coach
    description: Root WebSocket server for The Fountain

paths:
  /characters:
    get:
      summary: Subscribe to Character WebSocket
      operationId: subscribeCharacters
      tags:
        - Characters
      responses:
        '200':
          description: Connection established to Character WebSocket
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CharacterEvent'

  /spoken-word:
    get:
      summary: Subscribe to Spoken Word WebSocket
      operationId: subscribeSpokenWord
      tags:
        - Spoken Word
      responses:
        '200':
          description: Connection established to Spoken Word WebSocket
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SpokenWordEvent'

  /action:
    get:
      summary: Subscribe to Action WebSocket
      operationId: subscribeAction
      tags:
        - Action
      responses:
        '200':
          description: Connection established to Action WebSocket
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionEvent'

  /section-heading:
    get:
      summary: Subscribe to Section Heading WebSocket
      operationId: subscribeSectionHeading
      tags:
        - Section Heading
      responses:
        '200':
          description: Connection established to Section Heading WebSocket
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SectionHeadingEvent'

  /script:
    get:
      summary: Subscribe to Script WebSocket
      operationId: subscribeScript
      tags:
        - Script
      responses:
        '200':
          description: Connection established to Script WebSocket
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ScriptEvent'

  /transition:
    get:
      summary: Subscribe to Transition WebSocket
      operationId: subscribeTransition
      tags:
        - Transition
      responses:
        '200':
          description: Connection established to Transition WebSocket
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TransitionEvent'

  /music-sound:
    get:
      summary: Subscribe to Music and Sound WebSocket
      operationId: subscribeMusicSound
      tags:
        - Music Sound
      responses:
        '200':
          description: Connection established to Music and Sound WebSocket
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MusicSoundEvent'

  /note:
    get:
      summary: Subscribe to Note WebSocket
      operationId: subscribeNote
      tags:
        - Note
      responses:
        '200':
          description: Connection established to Note WebSocket
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NoteEvent'

components:
  schemas:
    CharacterEvent:
      type: object
      properties:
        characterId:
          type: string
          description: Unique identifier for the character
        name:
          type: string
          description: Name of the character
        dialogue:
          type: string
          description: Dialogue spoken by the character
        action:
          type: string
          description: Action performed by the character

    SpokenWordEvent:
      type: object
      properties:
        text:
          type: string
          description: The spoken word text content

    ActionEvent:
      type: object
      properties:
        description:
          type: string
          description: Description of the action within the script

    SectionHeadingEvent:
      type: object
      properties:
        heading:
          type: string
          description: Text of the section heading

    ScriptEvent:
      type: object
      properties:
        content:
          type: string
          description: The script content or update

    TransitionEvent:
      type: object
      properties:
        transitionType:
          type: string
          description: Description of the transition (e.g., cut to, fade in)

    MusicSoundEvent:
      type: object
      properties:
        music:
          type: string
          description: Music description or content
        sound:
          type: string
          description: Sound effect description or content

    NoteEvent:
      type: object
      properties:
        content:
          type: string
          description: The content of the note

