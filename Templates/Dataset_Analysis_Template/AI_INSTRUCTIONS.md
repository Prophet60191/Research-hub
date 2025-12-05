# AI INSTRUCTIONS: Dataset Analysis Project Setup

**Purpose:** Complete instructions for AI assistants to help users set up professional dataset analysis research projects.

**Your Role:** Create complete research project structure with all necessary documentation, scripts, and quality controls. Follow these instructions systematically.

---

## TABLE OF CONTENTS

1. [Overview](#overview)
2. [Project Standards](#project-standards)
3. [Directory Structure](#directory-structure)
4. [Documentation Files](#documentation-files)
5. [Script Templates](#script-templates)
6. [Data Organization](#data-organization)
7. [Quality Control](#quality-control)
8. [Workflow](#workflow)
9. [User Interaction Guidelines](#user-interaction-guidelines)

---

## OVERVIEW

### What You're Building

A professional research project with:
- Organized directory structure
- Complete documentation
- Reproducible analysis scripts
- Quality control measures
- Audit trail
- Professional standards

### Standards to Maintain

- **Reproducibility:** Anyone can replicate results
- **Transparency:** All decisions documented
- **Rigor:** Professional academic/legal standards
- **Organization:** Self-documenting structure
- **Accessibility:** Clear for non-experts

---

## PROJECT STANDARDS

### Core Principles

1. **Separation of Concerns**
   - Raw data ≠ processed data ≠ analysis ≠ outputs
   - Each stage has its own directory
   - No mixing of stages

2. **Documentation First**
   - Document as you go, not later
   - Every decision explained and justified
   - Complete audit trail

3. **Never Modify Raw Data**
   - Raw data is read-only
   - All transformations via scripts
   - Original files preserved exactly as received

4. **Reproducibility**
   - All analysis scripted (no manual steps)
   - All paths in Config.py
   - Clear instructions for replication

5. **Professional Quality**
   - Assume work will be audited
   - Suitable for publication
   - Traceable sources
   - Quality verified

---

## DIRECTORY STRUCTURE

### Standard Structure

Create this exact structure for every project:

```
[Project_Name]/
│
├── README.md                           # Project overview
├── Requirements.txt                    # Dependencies
│
├── Docs/                               # ALL documentation
│   ├── Data Source.md                  # Data provenance
│   ├── Data Cleaning.md                # Cleaning methodology
│   ├── Data Quality.md                 # Limitations
│   ├── Data Dictionary.md              # Field definitions
│   ├── Methodology.md                  # Analysis methods
│   ├── Findings.md                     # Results
│   ├── Research Process.md             # Decision log
│   ├── Scripts.md                      # Script documentation
│   └── How to Use This Repository.md   # User guide
│
├── Data/
│   ├── raw/                            # Original, untouched
│   ├── processed/                      # Cleaned data
│   └── reference/                      # Supporting materials
│
├── Scripts/
│   ├── Config.py                       # Paths/settings
│   ├── Clean Dataset.py                # Data cleaning
│   └── Analysis/                       # Analysis scripts
│       └── [analysis_name].py
│
├── Outputs/
│   ├── tables/                         # CSV/Excel results
│   └── figures/                        # Visualizations
│
└── Database/                           # Optional SQLite
    ├── create_database.py
    └── [project].db
```

### Directory Creation Command

**Mac/Linux:**
```bash
mkdir -p "[Project_Name]/Docs"
mkdir -p "[Project_Name]/Data/raw"
mkdir -p "[Project_Name]/Data/processed"
mkdir -p "[Project_Name]/Data/reference"
mkdir -p "[Project_Name]/Scripts/Analysis"
mkdir -p "[Project_Name]/Outputs/tables"
mkdir -p "[Project_Name]/Outputs/figures"
mkdir -p "[Project_Name]/Database"
```

**Windows:**
```cmd
mkdir "[Project_Name]\Docs"
mkdir "[Project_Name]\Data\raw"
mkdir "[Project_Name]\Data\processed"
mkdir "[Project_Name]\Data\reference"
mkdir "[Project_Name]\Scripts\Analysis"
mkdir "[Project_Name]\Outputs\tables"
mkdir "[Project_Name]\Outputs\figures"
mkdir "[Project_Name]\Database"
```

---

## DOCUMENTATION FILES

### 1. README.md (Essential)

**Purpose:** First file anyone reads; 2-minute project overview

**Required Sections:**
- Title and 1-sentence description
- Quick Start (3-5 steps to use project)
- Data Source (where data came from)
- Key Findings (3-5 bullet points)
- Documentation links
- Citation format

**Template:** See `README_TEMPLATE.md`

### 2. Data Source.md (Essential)

**Purpose:** Document data provenance for transparency

**Required Content:**
- Primary source (organization, URL, date obtained)
- Legal basis (FOIL, public records, etc.)
- Source credibility (why trustworthy)
- Date range covered
- Known issues
- Proper citation format

**Template:** See `Docs_Templates/Data_Source_TEMPLATE.md`

### 3. Data Cleaning.md (Essential)

**Purpose:** Document every transformation for reproducibility

**Required Content:**
- Original data state (format, records, issues)
- Each cleaning step (why, how, result)
- Final data state
- Excluded data (what and why)
- Link to cleaning scripts

**Template:** See `Docs_Templates/Data_Cleaning_TEMPLATE.md`

### 4. Data Dictionary.md (Essential)

**Purpose:** Define every field in the dataset

**Required Content:**
- Field name
- Data type
- Description
- Possible values (if categorical)
- Missing data handling
- Transformations applied

**Template:** See `Docs_Templates/Data_Dictionary_TEMPLATE.md`

### 5. Findings.md (Essential)

**Purpose:** Document all results in organized sections

**Required Structure:**
- Numbered sections for each analysis
- Statistics in tables
- Key metrics highlighted
- Interpretations provided
- Confidence levels stated

**Template:** See `Docs_Templates/Findings_TEMPLATE.md`

### 6. Research Process.md (Essential)

**Purpose:** Chronicle every decision (audit trail)

**Required Content:**
- Timeline of decisions
- Rationale for each choice
- Results of each step
- Dead ends (what didn't work)
- Future research ideas

**Template:** See `Docs_Templates/Research_Process_TEMPLATE.md`

### 7. Data Quality.md (Essential)

**Purpose:** Document limitations honestly

**Required Content:**
- Known limitations
- Missing data issues
- Measurement problems
- Sampling concerns
- Interpretation caveats

**Template:** See `Docs_Templates/Data_Quality_TEMPLATE.md`

### 8. Methodology.md (Recommended)

**Purpose:** Explain statistical/analytical methods

**Template:** See `Docs_Templates/Methodology_TEMPLATE.md`

### 9. Scripts.md (Recommended)

**Purpose:** Document what each script does

**Template:** See `Docs_Templates/Scripts_TEMPLATE.md`

---

## SCRIPT TEMPLATES

### Config.py (Essential)

**Purpose:** Store ALL paths and settings in ONE place

**Required Content:**
- Project root path
- All directory paths
- All file paths
- Analysis parameters
- Display settings

**Why:** Change one setting, updates entire project

**Template:** See `Scripts_Templates/Config_TEMPLATE.py`

### Clean Dataset.py (Essential)

**Purpose:** Reproducible data cleaning pipeline

**Required Structure:**
- Imports and configuration
- Load data function
- Cleaning functions (one per step)
- Validation functions
- Export function
- Main execution

**Template:** See `Scripts_Templates/Clean_Dataset_TEMPLATE.py`

### Analysis Script Template (Standard)

**Required Structure:**
```python
"""
Script: [Name]
Purpose: [What it does]
Inputs: [Files needed]
Outputs: [Files created]
"""

# Imports
from Config import *

# Load data
def load_data():
    pass

# Analysis function
def analyze():
    pass

# Export results
def export_results():
    pass

# Main
if __name__ == "__main__":
    data = load_data()
    results = analyze(data)
    export_results(results)
```

**Template:** See `Scripts_Templates/Analysis_TEMPLATE.py`

---

## DATA ORGANIZATION

### Three-Stage Data Flow

#### Stage 1: Raw Data (NEVER MODIFY)

**Location:** `Data/raw/`

**Rules:**
- ✅ Store original files exactly as received
- ✅ Keep original filenames
- ✅ Write-protect if possible
- ❌ NEVER edit
- ❌ NEVER rename
- ❌ NEVER delete

**Why:** Proves no source manipulation

#### Stage 2: Processed Data

**Location:** `Data/processed/`

**Rules:**
- ✅ Created by scripts only
- ✅ Reproducible from raw
- ✅ Standardized formats
- ✅ Missing data handled
- ❌ No manual edits

**Why:** Analysis-ready, reproducible

#### Stage 3: Reference Materials

**Location:** `Data/reference/`

**Purpose:** Supporting documents
- Codebooks
- Regulations
- Background materials
- Related datasets

### File Naming Convention

**Format:** `source_description_status_YYYY-MM-DD.ext`

**Examples:**
- `DCJS_Decertifications_Raw_2024-11-01.csv`
- `NYCLU_Misconduct_Cleaned_2024-11-15.csv`

**Rules:**
- Lowercase
- Underscores (not spaces)
- Dates in YYYY-MM-DD format
- Descriptive
- Include status

---

## QUALITY CONTROL

### Validation Requirements

**Every Script Must:**
- Print progress messages
- Validate input data
- Check for missing values
- Verify transformations
- Report summary statistics
- Log errors

**Every Analysis Must:**
- State confidence level
- Report sample sizes
- Note limitations
- Document assumptions
- Provide uncertainty estimates

### Documentation Requirements

**Every Document Must:**
- Have date created/updated
- Be organized with sections
- Use proper formatting
- Include sources
- Be kept current

### Code Requirements

**Every Script Must:**
- Have docstring
- Use Config.py for paths
- Include error handling
- Use meaningful names
- Have comments for complex logic
- Be testable

---

## WORKFLOW

### Step-by-Step Process

### Phase 1: Project Setup (The Interview & Configuration)

**Trigger:** You have just been initialized in the new project folder.

**Step 1: The Intake & Data Ingestion**
Do not touch any files yet. You must secure the raw data before proceeding.

1.  **Project Name:** "What shall we call this project? (I will rename the root folder if needed)."
2.  **The Data Question:** Ask clearly:
    > "To begin, I need your raw data file saved safely in the `Data/raw/` folder.
    > Option A: Drag and drop the file into `Data/raw/` yourself.
    > Option B: Paste the full file path here, and I will copy it for you."
    
**Step 2: Physical Verification (The Gatekeeper)**
1.  **Check `Data/raw/`:** List the contents of this directory.
    * *If empty:* Ask the user again. Do NOT create a dummy file.
    * *If multiple files:* Ask the user which one is the primary dataset.
2.  **Handle "Option B" (Copying):**
    * If the user provided a path (e.g., `/Users/Jose/Downloads/data.csv`), use the terminal to copy it:
        `cp "/Users/Jose/Downloads/data.csv" "Data/raw/data.csv"` 
3.  **Lock it down:**
    * Once the file is confirmed in `Data/raw/`, tell the user: "✅ Data secured. I will treat this file as Read-Only."
    * **Action:** Update `Scripts/Config.py` immediately with the exact filename found in `Data/raw/`.

**Step 3: Documentation Initialization**
Update the existing template files with the User's answers:
1.  **Update `README.md`:**
    * Change Title to [Project Name].
    * Update "Research Question" section.
    * Update "Data Source" summary.
2.  **Update `Docs/Data Source.md`:**
    * Fill in the "Filename" and "Date Received".
    * Ask the user: "Where did this data come from? (e.g., FOIL request, Download URL, Internal Database)."
    * Record their answer in the provenance section.

**Step 4: Environment Configuration**
1.  Read `Requirements.txt`.
2.  Ask the user: "I see standard dependencies (pandas, numpy). Do you want me to install these now?"
    * *Action:* If yes, run `pip install -r Requirements.txt` (if you have terminal access).
3.  Update `Scripts/Config.py`:
    * Set the `RAW_DATA_FILE` variable to match the specific filename provided in Step 1.

**Checkpoint:**
Only proceed to Phase 2 (Data Inspection) when:
* [ ] Data file is safely in `Data/raw/`.
* [ ] `README.md` is customized.
* [ ] `Data Source.md` has provenance info.
* [ ] User confirms they are ready to inspect the data.

### Phase 2: Data Inspection & Cleaning

**Objective:** Understand the raw data deeply and create a reproducible cleaning pipeline.

**Step 1: The "Health Check" (Read-Only Inspection)**
1.  **Load Data:** Use `Config.RAW_DATA_PATH` to load the file (do NOT hardcode paths).
2.  **Inspect:** Run `.info()`, `.head()`, and `.describe()` in a temporary scratchpad or terminal.
3.  **Diagnose:**
    * **Missing Values:** What percentage is missing per column?
    * **Data Types:** Are dates stored as objects? Are numbers stored as strings (e.g., "$1,000")?
    * **Duplicates:** Are there identical rows?
    * **Ambiguity:** Are column names clear (e.g., "Q1_Res" vs "Response_Date")?

**Step 2: Build the Dictionary (The "Truth" Source)**
1.  Open `Docs/Data Dictionary.md`.
2.  **Populate:** List every column found in the raw data.
3.  **Define:** Fill in "Data Type" and "Sample Values" based on your inspection.
4.  **Infer & Ask:**
    * Fill in obvious descriptions.
    * **CRITICAL:** If a column is ambiguous (e.g., "Code_99"), **STOP** and ask the user what it means.

**Step 3: Define the Cleaning Strategy (The Plan)**
1.  Open `Docs/Data Cleaning.md`.
2.  **Write the Plan:** Document exactly what needs to happen *in plain English* before writing code.
    * *Bad:* "Run cleaning script."
    * *Good:* "1. Drop rows where 'ID' is null. 2. Convert 'Date' to datetime. 3. Fill missing 'Age' with median."
3.  **Approval:** Present this plan to the user: "Here is my strategy to clean the data. Do you approve?"

**Step 4: Execute Cleaning (The Code)**
1.  **Code:** Once approved, write the logic into `Scripts/Clean_Dataset.py`.
2.  **Constraint:** Use modular functions (e.g., `def standardize_dates(df):`).
3.  **Run:** Execute the script.
4.  **Verify:** Check that `Data/processed/cleaned_data.csv` exists and is readable.

**Checkpoint:**
Only proceed to Phase 3 (Analysis) when:
* [ ] `Data Dictionary.md` is complete and defines all variables.
* [ ] `Data Cleaning.md` documents the logic used.
* [ ] `Clean_Dataset.py` runs successfully.
* [ ] Processed data is saved.

### Phase 3: Analysis & Reporting

**Objective:** Answer the Research Question using the clean data.

**Step 1: The Analysis Plan**
1.  **Review:** Read the "Research Question" in `README.md`.
2.  **Propose:** Suggest 2-3 specific analyses to answer it.
    * *Example:* "To answer 'Is policy X effective?', I will: 1) Calculate descriptive stats of X, 2) Run a time-series analysis before/after the policy date."
3.  **Confirm:** Ask the user: "Shall I proceed with these analyses?"

**Step 2: Modular Scripting**
1.  **Create Script:** Create a NEW script in `Scripts/Analysis/` for each distinct task.
    * *Naming Convention:* `01_Descriptive_Stats.py`, `02_Hypothesis_Test.py`.
2.  **Constraint:**
    * Import `Config` to access `CLEAN_DATA_PATH`.
    * Save all charts to `Outputs/figures/`.
    * Save all summary tables to `Outputs/tables/`.
3.  **Run:** Execute the script and verify outputs.

**Step 3: Documentation (The Findings)**
1.  Open `Docs/Findings.md`.
2.  **Record:** Create a new section for the analysis.
3.  **Summarize:**
    * **The Fact:** "Average cost increased by 15% (Table 1)."
    * **The Chart:** "See Figure 1 for trendline."
    * **The Meaning:** "This suggests the policy change increased costs."

**Step 4: Methodology Check**
1.  Open `Docs/Methodology.md`.
2.  **Define:** If you calculated a metric (e.g., "Recidivism Rate"), write the exact formula used so others can replicate it.

**Checkpoint:**
Only proceed to Finalization when:
* [ ] Scripts in `Scripts/Analysis/` run without errors.
* [ ] Tables and Figures exist in `Outputs/`.
* [ ] `Findings.md` summarizes the results in plain English.
* [ ] User is satisfied with the answers.

#### Phase 4: Finalization (Week 3)

13. **Complete Documentation**
    - Fill all remaining sections
    - Update README
    - Create How to Use guide

14. **Quality Check**
    - Review checklist
    - Verify reproducibility
    - Test all scripts

15. **Finalize**
    - Archive project
    - Create backup
    - Prepare for sharing

---

## USER INTERACTION GUIDELINES

### For AI Assistants

#### Communication Style

**Do:**
- Ask clarifying questions
- Explain what you're doing
- Provide options when uncertain
- Document decisions
- Request validation after major steps

**Don't:**
- Assume user intent
- Skip documentation
- Make unsupported claims
- Proceed without confirmation on major decisions

#### When to Ask for Input

**Always Ask:**
- Project name and research question
- Data source and permissions
- Analysis priorities
- Interpretation of ambiguous findings
- Major methodological decisions

**Can Proceed Without Asking:**
- Standard directory setup
- Template creation
- Documentation formatting
- Code structure
- File organization

#### Error Handling

**When Errors Occur:**
1. Explain what went wrong
2. Explain why it matters
3. Provide options to fix
4. Document in Research Process.md
5. Proceed after user confirms

#### Progress Updates

**Provide Updates:**
- After completing each major section
- When starting new phase
- When encountering issues
- At natural checkpoints

**Update Format:**
```
✅ Completed: [What was done]
📊 Status: [Current state]
⏳ Next: [What's coming]
❓ Need: [Any user input required]
```

---

## CHECKLIST FOR COMPLETION

### Project Setup Checklist

- [ ] Directory structure created
- [ ] README.md complete
- [ ] Requirements.txt created
- [ ] Config.py configured
- [ ] All doc templates created

### Data Preparation Checklist

- [ ] Raw data in `Data/raw/`
- [ ] Data Source.md complete
- [ ] Data Dictionary.md complete
- [ ] Data Quality.md complete
- [ ] Data Cleaning.md complete
- [ ] Clean Dataset.py functional
- [ ] Processed data validated

### Analysis Checklist

- [ ] Analysis scripts created
- [ ] Scripts.md documented
- [ ] Methodology.md complete
- [ ] All analyses run successfully
- [ ] Findings.md populated
- [ ] Outputs generated

### Finalization Checklist

- [ ] Research Process.md current
- [ ] How to Use guide complete
- [ ] All scripts reproduce results
- [ ] All documentation complete
- [ ] No placeholder text
- [ ] All links functional
- [ ] Quality standards met

---

## EXAMPLE PROJECT

See `Examples/` folder for complete working example following all standards.

---

## TEMPLATE FILES

All templates are in:
- `README_TEMPLATE.md`
- `Docs_Templates/` directory
- `Scripts_Templates/` directory

Replace `[PLACEHOLDER]` text with project-specific content.

---

## GETTING STARTED

**Your Workflow:**
1. Read this file completely
2. Confirm you understand the standards
3. Ask user for basic project information
4. Create directory structure
5. Generate documentation from templates
6. Guide user through each phase
7. Maintain quality standards throughout

---

## VERSION INFORMATION

**Template Version:** 1.0  
**Created:** November 30, 2024  
**Based On:** NYCLU DOCCS Misconduct Dataset Project  
**Standards:** Academic/Legal Research Quality  

**Tested With:**
- Cascade (Windsurf)
- Claude Code (Cursor)
- GPT-4 with Code Interpreter

**Compatible With:** Any AI assistant with file management capabilities

---

**END OF AI INSTRUCTIONS**

*These instructions encode 7+ hours of professional research methodology, distilled into a reusable framework. Follow them to produce publication-quality research projects.*
