# Prompt Collection

## 概述
这是一个专门收集和整理我在各种 AI 任务中积累的 Prompt 模板 仓库。
这些模板旨在:
- 提升效率: 快速复用经过优化的 Prompt，减少从零开始编写的时间。
- 统一标准: 采用一致的编写规范，让 Prompt 更易于管理和维护。
- 无缝集成: 所有模板均使用 Jinja2 语法，可直接通过 LangChain 加载和运行，实现流畅的工作流。


## 核心工具
为了让 Prompt 的管理和使用更加高效和安全，我提供了以下工具：
- **`prompt_template_loader`**: 一个 LangChain 兼容的加载器，能规范地解析和加载 `.j2` 格式的 Prompt 模板。
- **`safe_format_message_prompt_template`**: 一个安全格式化工具，可以避免因缺少变量或变量名错误导致的模板格式化意外。发生错误时，它会报错！
- **`base_prompt_template_factory`**: 一个工厂类，用于封装不同类型的 Prompt 加载逻辑，简化 LangChain 的交互过程。


## 模板分类
所有 Prompt 模板都已按其主要用途进行系统分类，方便快速查找和使用。此列表会持续更新。
- **内容理解 (Content Understanding)**: 用于从文本或数据中提取、总结和转换信息。
- **数据标注 (Data Annotation)**: 将大型语言模型或视觉语言模型作为分类器或标注工具。
- **数据处理 (Data Processing)**: 作为数据处理流水线的一个组成部分。
- **知识管理 (Knowledge Management)**: 与外部知识库或信息检索系统结合使用。
- **软件开发 (Software Development)**: 辅助代码生成、测试和日常开发任务。


## 我的其他项目
- [**Deep-Learning-Toolkit**](https://github.com/yuliu625/Yu-Deep-Learning-Toolkit): 我个人开发的 AI Agent 工具集。这个项目中加载和管理 Prompt 的方法就源自于此。

