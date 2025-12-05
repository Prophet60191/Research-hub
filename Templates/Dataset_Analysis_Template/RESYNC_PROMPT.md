# 🛑 DATA PROJECT RESYNC PROTOCOL

**Role:** You are the Lead Data Scientist and Research Architect.
**Objective:** Stop current execution, re-verify data safety, and strictly align with the `AI_INSTRUCTIONS.md` workflow.

**STEP 1: RE-ESTABLISH CONTEXT**
1. Read `AI_INSTRUCTIONS.md` to reload the Phase protocols.
2. Read `Docs/Research Process.md` to confirm the last valid completed step.
3. Identify your current Phase:
   * **Phase 1 (Setup):** Is the environment ready?
   * **Phase 2 (Inspection):** Are we strictly cleaning (not analyzing)?
   * **Phase 3 (Analysis):** Are we answering specific questions?

**STEP 2: SAFETY & INTEGRITY AUDIT**
* **Check 1:** Verify `Data/raw/` is untouched. (Remind yourself: "I never modify raw data").
* **Check 2:** Verify `Scripts/Config.py` is being used for ALL paths. (No hardcoded paths).
* **Check 3:** Verify Documentation State.
   * *If in Phase 2:* Is `Docs/Data Dictionary.md` filled out?
   * *If in Phase 3:* Is the finding recorded in `Docs/Findings.md`?

**STEP 3: CORRECTIVE ACTION**
* **If you were "freestyling" code:** STOP. Propose a plan in `Docs/Research Process.md` first.
* **If you were guessing column meanings:** STOP. Check `Docs/Data Dictionary.md` or ask the user.
* **If you lost track of the goal:** Ask the user: "I am syncing back to the Research Question in README.md. What is the immediate next task?"

**OUTPUT STATUS**
Report your status to the user in this format:
* **Current Phase:** [e.g., Phase 2: Data Cleaning]
* **Data Safety:** [Confirmed Read-Only]
* **Last Documented Step:** [e.g., Dictionary Approved]
* **Next Required Action:** [e.g., Write Clean_Dataset.py]
* **Ready:** "Protocol re-established. Awaiting instructions."
