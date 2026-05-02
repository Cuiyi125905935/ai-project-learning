# AI Alchemy Agent Skills & Tools Installation Guide

## 1. MCP Server Configuration
To enable the "Intercept-Fix-Generate" workflow, ensure the following MCP servers are active in your IDE:
- **ai-alchemy-governance**: Handles real-time code validation (SonarLint/Clang-Tidy).
- **github**: For repository interaction and dependency review.

## 2. Required Plugins/Skills
Install the following skills to empower the agent with project-specific memory and tool scheduling:

### A. RepoGPT (Project Memory)
- **Function**: Indexes `LightGBM`, `Backtrader`, and `HQChart` logic into vector embeddings.
- **Config**: `.comate/repogpt.config.json`
- **Trigger**: Automatically activates when generating strategy code to retrieve verified patterns.

### B. CodeGuru (Error Loop Learning)
- **Function**: Monitors compilation/runtime errors and logs them to `docs/error_cases.json`.
- **Integration**: Linked with GitHub Actions for automated error case updates.

### C. LangChain Agent Scheduler (Tool Autonomy)
- **Function**: Registers `akshare` (data), `Optuna` (tuning), and `Backtrader` (backtesting) as callable tools.
- **Config**: `.comate/agent_scheduler.md`
- **Goal**: Achieve autonomous "Data -> Train -> Backtest" loops with Sharpe Ratio > 1.5 targets.

## 3. Verification Steps
1. Run `python .comate/ai_alchemy_mcp_server.py` to test local governance.
2. Check `.github/workflows/code_quality.yml` for CI/CD integration.
3. Generate a sample strategy to verify RepoGPT retrieval and Self-Review execution.
