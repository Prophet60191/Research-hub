# Research Hub: User Guide

**Welcome.** This guide is split into two phases:
1.  **Setup:** Do this only once to install the Hub.
2.  **Generator:** Do this every time you start a new project.

---

## 🛑 PHASE 1: ONE-TIME SETUP
*Perform this step only once on your computer.*

1.  Create a folder named `Research_Workspace` in your Documents.
2.  Open your AI Editor (Windsurf/Cursor) and **Open Folder** -> `Research_Workspace`.
3.  Paste the **INSTALLER PROMPT** below:

### 🛠️ The Installer Prompt
```text
**Role:** System Administrator
**Task:** Install the Research Hub repository.

1.  Check if a folder named "Research Hub" exists in this directory.
2.  If NO, run: `git clone https://github.com/Prophet60191/Research-hub "Research Hub"`
3.  If YES, stop and say: "Research Hub is already installed."
4.  Once the folder `Research Hub` exists, list its contents to confirm installation.
```

🚀 PHASE 2: START A NEW PROJECT
Use this prompt every time you want to begin a new research assignment.
Open your Research_Workspace in your AI Editor.
Paste the GENERATOR PROMPT below:
🏗️ The Generator Prompt

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
2.  **Switch Persona:** Adopt the specific role defined in that file (e.g., Lead Data Scientist or Intelligence Analyst).
3.  **Execute:** Begin Phase 1 of the instructions found in that file.

Tips for Success
Always keep your Research_Workspace as the root folder in your editor.
Never modify the files inside Research Hub directly. If you want to change a template, make a copy first.
