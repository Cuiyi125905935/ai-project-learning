# TA-Lib 本地搭建与版本说明

## 1. Windows 环境本地搭建步骤（适配 G 盘）
*   **第一步：C 底层源码编译**
    下载 `ta-lib-0.4.0-msvc.zip`，解压至 `G:\AI_Alchemy_System\lib\ta-lib`。在 Visual Studio 开发者命令提示符中运行 `nmake -f makefile.cdn.win32` 完成编译。
*   **第二步：Python 接口安装**
    配置环境变量 `TA_LIBRARY_PATH=G:\AI_Alchemy_System\lib\ta-lib\c\lib` 和 `TA_INCLUDE_PATH=G:\AI_Alchemy_System\lib\ta-lib\c\include`。执行 `pip install ta-lib` 完成对接。
*   **第三步：常见报错解决**
    *   **SDK 不兼容**: 确保安装了最新的 Windows SDK 10.0+。
    *   **VC++ 缺失**: 安装 Visual C++ Redistributable 2015-2022 (x64)。

## 2. 版本迭代与 CPU 优化
*   **v0.4.0**: 经典的稳定版本，提供了 150+ 种技术指标的 C 语言底层实现。
*   **v0.6.0**: 针对多核 CPU 进行了批量计算优化，在 i5-10400 等处理器上，全市场因子计算速度提升约 40%。
