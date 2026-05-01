import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os

# 定义模块及其依赖关系（基于已学的16个项目）
modules = {
    "TA-Lib": {"inputs": ["Price", "Volume"], "outputs": ["MACD", "RSI", "OBV"], "deps": []},
    "pmdarima": {"inputs": ["Price_Series"], "outputs": ["Time_Cycle"], "deps": []},
    "HQChart": {"inputs": ["Price_Series", "Time_Cycle"], "outputs": ["Gann_Price_Point"], "deps": ["pmdarima"]},
    "technical-analysis": {"inputs": ["High", "Low", "Time_Cycle", "Gann_Price_Point"], "outputs": ["Resonance_Score"], "deps": ["pmdarima", "HQChart"]},
    "Stock-Pattern-Analyzer": {"inputs": ["Volume", "Time_Cycle", "Gann_Price_Point", "Resonance_Score"], "outputs": ["Quad_Match_Score"], "deps": ["TA-Lib", "pmdarima", "HQChart", "technical-analysis"]},
    "LightGBM": {"inputs": ["TA-Lib_Features"], "outputs": ["Selection_Probability"], "deps": ["TA-Lib"]},
    "FinRL": {"inputs": ["Market_Data"], "outputs": ["Multi_Factor_Features"], "deps": ["TA-Lib"]},
    "Backtrader": {"inputs": ["K_Line_Data"], "outputs": ["Period_Environment"], "deps": ["TA-Lib"]},
    "TFT": {"inputs": ["Static_Features", "Dynamic_Features"], "outputs": ["High_Low_Prediction"], "deps": ["TA-Lib", "pmdarima"]}
}

# 1. 生成 CSV 关系表
rows = []
for name, info in modules.items():
    for dep in info['deps']:
        rows.append({"Source": dep, "Target": name, "Input_Type": ", ".join(info['inputs']), "Output_Type": ", ".join(info['outputs'])})

df = pd.DataFrame(rows)
df.to_csv("dependency_map/module_relations.csv", index=False)

# 2. 生成 NetworkX 图谱
G = nx.DiGraph()
for row in rows:
    G.add_edge(row['Source'], row['Target'])

plt.figure(figsize=(15, 10))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=8, font_weight="bold", arrowsize=20)
plt.title("AI Alchemy System Module Dependency Graph")
plt.savefig("dependency_map/dependency_graph.png", dpi=300, bbox_inches='tight')

# 3. 冗余检测（示例：检测功能重叠）
redundant = []
if "TA-Lib" in modules and "technical-analysis" in modules:
    redundant.append("Potential Overlap: TA-Lib and technical-analysis both handle price levels/retracements.")

with open("dependency_map/redundant_modules.txt", "w") as f:
    for r in redundant:
        f.write(r + "\n")

print("Dependency map generation completed successfully.")
