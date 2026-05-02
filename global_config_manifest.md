# AI Alchemy Agent Global Configuration Manifest

**Version**: 2.0  
**Scope**: Agent-Wide (Cross-Project)  
**Last Updated**: 2026-05-02

---

## 1. Dependency Governance (`dependency_fix_rules.json`)
- **Global Scope**: Automatically scans project root for `requirements.txt`, `setup.py`, or `pyproject.toml`.
- **Adaptation Logic**: Classifies packages into "Critical Business", "General Tools", and "Optional Plugins" based on import frequency and core logic relevance.
- **Validation**: Run `pip check` in any new project; the agent will now prioritize fixes for core modules without manual input.

## 2. Memory Adaptation Engine (`logic_adaptation_rules.json`)
- **Global Scope**: Applies to all historical logic retrieval from `agent_memory`.
- **3D Scenario Recognition**: Identifies context via:
  - **Data Frequency**: 1min, Daily, Weekly, Tick.
  - **Market Type**: A-Share, US Stock, Crypto, Forex.
  - **Indicator Type**: Volume, Price, Momentum, Volatility.
- **Validation**: When reusing code, verify that parameters (e.g., `find_peaks_distance`) are automatically scaled by the adaptation factors defined in the engine.

## 3. Universal Error Avoidance (`error_avoidance_rules.json`)
- **Global Scope**: Pre-loaded at the start of every task execution across all projects.
- **Cross-Project Learning**: Errors recorded in one project are immediately available as avoidance rules for all future tasks.
- **Validation**: Attempt to generate code with a known error pattern (e.g., 79-char line length); the agent should proactively correct it to the global standard (88 chars).

## 4. Unified Toolchain Standard (`unified_tool_config.toml`)
- **Global Scope**: Serves as the default configuration for `flake8`, `black`, and `ruff` in all new environments.
- **Mandatory Rules**: 
  - Line Length: 88 characters.
  - Indentation: 4 spaces.
  - Error Priority: Aligned across all three tools.
- **Validation**: Run quality checks in a new project; all tools must report zero conflicts regarding formatting standards.

## 5. Universal Boundary Testing (`extreme_test_cases.py`)
- **Global Scope**: Template for generating robustness tests in Quantitative, ML, and Data Analysis projects.
- **Multi-Dimensional Adaptation**:
  - **Quant**: Limit-up boards, suspensions, zero-volume gaps.
  - **ML**: Extreme overfitting, adversarial samples, missing features.
  - **Data**: Null values, outliers, type mismatches.
- **Validation**: Execute the template with different `project_type` arguments; ensure appropriate boundary scenarios are generated for each domain.

---

## Conclusion
This manifest confirms the transition from project-specific configurations to a **Global Agent Framework**. These files are now stored in the repository's central configuration directories and will be automatically referenced by the AI Alchemy Agent for all future development tasks.
