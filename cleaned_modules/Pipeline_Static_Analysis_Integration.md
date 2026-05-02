# Pipeline 工程治理与静态分析集成方案

## 1. 核心目标
将 **SonarLint**（编码规范）与 **Clang Static Analyzer**（逻辑漏洞检测）深度集成到 `ai-project-learning` 的 Pipeline 自动化链路中，实现“生成即审计，审计即修复”的闭环。

## 2. 集成架构设计
*   **触发机制**：在代码生成脚本（如 `generate_dependency_map.py`）执行完毕后，自动调用静态分析引擎。
*   **分析规则**：
    *   **SonarLint**: 重点检查 Python 代码的可读性、复杂度及潜在的类型错误。
    *   **Clang Static Analyzer**: 针对底层 C/C++ 扩展（如 TA-Lib 接口）进行内存泄漏和空指针检测。
*   **自动修复**：引入 `ruff` 或 `autopep8` 作为第一道防线，自动修正格式问题；对于逻辑漏洞，生成修复建议并阻断提交。

## 3. 实施步骤
1.  **配置化**：在 `pipeline/` 目录下创建 `sonar-project.properties` 和 `clang_scan_config.json`。
2.  **流水线嵌入**：修改 `volume_price_time_pipeline.py`，在 `run_batch_scan` 前增加 `static_analysis_gate()` 环节。
3.  **报告输出**：将分析结果以 HTML/JSON 格式存入 `pipeline_output/quality_report/`。

## 4. 预期效果
*   **零低级错误**：杜绝变量未定义、类型不匹配等基础 Bug。
*   **逻辑健壮性**：提前发现除零错误、索引越界等隐藏风险。
*   **代码标准化**：确保所有生成的模块符合工业级代码规范，便于后续的自我迭代与维护。

---
**结论**：通过此集成，我们的 Pipeline 将从单纯的“计算工具”进化为具备**自我质检能力的智能工厂**。
