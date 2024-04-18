# CRUD Operation Sequence for a Play

To accurately reflect the enforced sequence of CRUD operations for a play, with the clarification that the creation of more than one scene is optional and based on user request, the description is adjusted as follows:

## Create Sequence

1. **Create Play**: Initially, a play must be created. Without the play, no further components—acts, scenes, characters, or dialogues—can exist, as they all require a play for their association.
2. **Create Characters**: Immediately after establishing the play, characters must be created. Since characters may appear across various acts and scenes, establishing them at this early stage ensures they are ready to be associated with any dialogues that are later developed.
3. **Create Act**: Following the play's creation, an act must be created. Each act serves as a subdivision of the play and must be directly linked to the play upon its creation.
4. **Create Scene**: After creating an act, a single scene must then be created within that act. While the creation of one scene is mandatory, the creation of additional scenes is optional and contingent upon the user's requirements. Each scene created must have a specific act it is associated with, thereby linking it back to the parent play.
5. **Create Dialogue**: The final mandatory step in the creation process involves establishing dialogues within the scene(s) and associating them with characters. The existence of both a scene and characters is a prerequisite for any dialogue to be created.

## Update Sequence

1. **Update Play**: Updates to the play must precede updates to any associated acts, scenes, characters, or dialogues, as changes may impact how these entities are managed or displayed.
2. **Update Characters**: Following updates to the play, characters must be updated next, as changes could affect their representation across various dialogues, scenes, and acts.
3. **Update Act**: Acts within the play must be updated after characters. This may involve changing titles, descriptions, or the sequence of acts within the play.
4. **Update Scene**: Updates to scenes must occur after acts have been updated. Changes can affect their sequence within an act or other specific details.
5. **Update Dialogue**: Dialogues represent the most granular level of the structure and thus must be updated last. Since dialogues are contained within scenes and associated with characters, updates here have the least impact on the overall structure.

## Delete Sequence (Cascading Delete)

1. **Delete Dialogue**: The deletion process begins with dialogues. Dialogues must be deleted first to avoid leaving orphan dialogues without an associated scene.
2. **Delete Scene**: After all relevant dialogues have been deleted, the scene (or scenes, if more than one was created) must then be removed. This step ensures no scenes are left without a parent act.
3. **Delete Act**: Following the deletion of all scenes within an act, the act itself must be removed. This ensures no acts are left without a parent structure.
4. **Delete Characters**: Characters must be deleted after ensuring they are not tied to any remaining scenes or acts. This step might be complex given characters’ potential span across the play.
5. **Delete Play**: The final action in the sequence is to delete the play. Once all acts, scenes, dialogues, and characters have been removed, the play itself must be deleted to prevent orphan entities from remaining.

This enforced sequence, with the clarification regarding scene creation, maintains the hierarchical integrity and relational dependencies within a play's structure throughout the CRUD operations.
