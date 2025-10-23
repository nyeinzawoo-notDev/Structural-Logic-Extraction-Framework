# 📊 Core Data Files (`data/`)

This folder is the central repository for all essential, structured data files used by the NSTF/SLEF core engine.

## 📝 Folder Purpose

Data here is used to directly power the framework's logic. Examples include:
* **Ontologies:** T-Codes, Philosophical Dimensions.
* **Schemas:** Ethical Engine rule structures.
* **Static Reference Data:** Large linguistic datasets.

## ⚠️ Important Rules

* **File Types:** `.json`, `.tsv`, `.csv`, `.yaml` (Structured Data only).
* **NO Source Code:** Python files (`.py`) are strictly prohibited here; they belong in the **`modules/`** folder.
* **Data Integrity:** Changes to these files must follow a strict review process as they directly affect the framework's deterministic ethical guidance.
* **Key Files:**
    * `ultimate_ethical_engine.json` (The Core Schema)
    * `t_codes_ontology.json` (T-Code Definitions)
