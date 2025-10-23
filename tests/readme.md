# 🧪 Test Suite (`tests/`)

This folder contains unit tests and integration tests to verify the correctness and reliability of the NSTF/SLEF logic.

## 📝 Folder Purpose

Testing is critical to ensure the deterministic ethical guidance is consistently maintained.
* **Unit Tests:** Verify individual components (e.g., T-Code calculation, Fo/Ma energy balance) work correctly.
* **Integration Tests:** Verify the complete 4-Stage Analysis Pipeline functions as expected.
* **Compliance Tests:** Specific tests to verify adherence to the 15 Immutable Missions.

## ⚠️ Important Rules

* **File Type:** MUST be **`.py`** (Python test scripts, typically using frameworks like `unittest` or `pytest`).
* **Naming Convention:** Test files should ideally start with `test_` (e.g., `test_scenarios.py`).
* **NO Production Code:** Only test files are allowed here. Core logic files belong in **`modules/`**.
