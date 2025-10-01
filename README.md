# Prompt Collection

## Overview
This repository is a collection of my personal **Prompt templates** for various AI tasks.

The goal of these templates is to:
- **Increase efficiency**: Quickly reuse optimized prompts and reduce the time spent writing from scratch.
- **Maintain consistency**: Follow a unified standard for prompt creation, making them easier to manage and maintain.
- **Ensure seamless integration**: All templates use **Jinja2** syntax, which can be directly loaded and run with **LangChain** for a smooth workflow.


## Core Tools
To manage and use these prompts more efficiently and securely, I've included the following tools:
- **`prompt_template_loader`**: A LangChain-compatible loader that parses and loads `.j2` prompt templates in a standardized way.
- **`safe_format_message_prompt_template`**: A safe formatting tool that prevents unexpected template formatting errors due to missing or incorrect variable names. It will raise an error if an issue occurs.
- **`base_prompt_template_factory`**: A factory class that encapsulates the logic for loading different types of prompts, simplifying interactions with LangChain.


## Template Categories
All prompt templates are systematically categorized by their primary use for easy navigation and quick access. This list will be updated continuously.
- **Content Understanding**: For extracting, summarizing, and transforming information from text or data.
- **Data Annotation**: Uses large language models (LLMs) or vision-language models (VLMs) as classifiers or annotation tools.
- **Data Processing**: Serves as a component within a data processing pipeline.
- **Knowledge Management**: Integrates with external knowledge bases or information retrieval systems.
- **Software Development**: Assists with code generation, testing, and other daily development tasks.


## My Other Projects
- [**Deep-Learning-Toolkit**](https://github.com/yuliu625/Yu-Deep-Learning-Toolkit): My personal collection of AI Agent tools. The methods for loading and managing prompts in this repository are derived from this project.

