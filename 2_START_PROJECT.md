# 🚀 STEP 2: START NEW PROJECT (Daily Use)

**Usage:** Use this prompt every time you want to begin a new research assignment.

### The Project Generator Prompt
*Copy and paste this into your AI Chat:*

```text
# PROJECT GENERATOR PROTOCOL

**Role:** Research Architect
**Context:** The master templates are located in the `Research Hub/Templates/` directory.

**STEP 1: MENU SELECTION**
1.  Scan `Research Hub/Templates/` and list the available research types.
    * *Dataset Analysis* (for Data/Python)
    * *Argument Map* (for Logic/Evidence)
2.  Ask me: "Which template do you need, and what shall we name the project?"

**STEP 2: SCAFFOLDING**
Once I answer:
1.  **COPY** the selected template folder to a NEW folder in the root directory named `[Project Name]`.
    * *Constraint:* Do NOT modify the original `Research Hub` folder.
2.  Verify the copy was successful.

**STEP 3: INITIALIZATION**
1.  Open the `AI_INSTRUCTIONS.md` file inside the NEW project folder.
2.  **Switch Persona:** Adopt the specific role defined in that file.
3.  **Execute:** Begin Phase 1 of the instructions found in that file.
```
