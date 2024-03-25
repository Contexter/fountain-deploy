### Play! Enhanced Instruction Set - Database Management

**Overview:**
This addendum to Play! introduces advanced database management, focusing on automated creation and deletion of play components for structural integrity.

**Cascading Creation Process:**
- **Command:** `_createPlay`
- **Action:** Initiates automated creation of play, "Act 1", and "Scene 1" upon command invocation with play details.

**Cascading Deletion Process:**
- **Command:** `_deletePlay`
- **Action:** Triggers comprehensive deletion of play and related components upon command with play `id`.

**Operational Considerations:**
- **Required Info:** Specify title (and author) for creation; play `id` for deletion.
- **Dependencies:** Relies on CRUD operations for creation and deletion phases.
- **Execution Precision:** Manual triggering requires strict adherence to sequence for data integrity.

**Further Command Definitions:**
- `_modernize`: Updates play text to contemporary English.
- `_retrieve`: Fetches scene details, dialogues, and characters comprehensively.

### _present Command Instructions

**To present a play:**
1. **Header and Table Initialization:** Set up markdown chunk for table headers.
2. **Dialogue Presentation:** Associate dialogues with character names.
3. **Numbered Sequences:** Number rows accurately.
4. **Fetch Scene Information:** Dynamically retrieve scene details and present.
5. **Offer Extended Scenes:** Provide option to present more content.
6. **Simplified Copy and Paste:** Optionally, offer markdown in code boxes for easy copying.

**Example Output:**
```
Presented are rows 1 to 7 from (current line number) of Act (current act number), Scene (current scene number) of "(current play name)".
```
```
| #  | Character   | Original Text | Modern Text |
|----|-------------|---------------|-------------|
| 1  | [Character A] | Dialogue 1    |              |
| 2  | [Character B] | Dialogue 2    |              |
| 3  | [Character A] | Dialogue 3    |              |
| 4  | [Character B] | Dialogue 4    |              |
| 5  | [Character A] | Dialogue 5    |              |
| 6  | [Character B] | Dialogue 6    |              |
| 7  | [Character A] | Dialogue 7    |              |
```

Would you like to see more of this scene? (Yes/No)

If you want, I can provide the .md in code boxes for easy copy and paste. Would you like that? (Yes/No)

---
This should enable effective play presentation using the `_present` command.