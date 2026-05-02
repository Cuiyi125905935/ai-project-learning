# LangChain Agent Tool Scheduler Configuration

## 1. Registered Tools
- **Data Fetcher**: `akshare`/`tushare` wrappers for real-time market data.
- **Model Trainer**: `LightGBM` + `Optuna` hyperparameter optimization pipeline.
- **Backtest Engine**: `Backtrader` strategy execution with Sharpe/Drawdown metrics.

## 2. Trigger Rules
- **Post-Generation**: After generating a strategy, auto-trigger `Data Fetcher` (3 years history).
- **Pre-Merge**: Auto-trigger `Backtest Engine`; block merge if `Sharpe Ratio < 1.5`.
- **Error Handling**: If training fails, consult `docs/error_cases.json` before retrying.

## 3. Agent Workflow
1. **Retrieve**: Check Repo Memory for similar strategies.
2. **Generate**: Create code using Copilot Skills.
3. **Review**: Run Self-Review (No look-ahead bias, feature screening).
4. **Execute**: Call Backtest Tool.
5. **Learn**: Log results/errors to Error Case Library.
