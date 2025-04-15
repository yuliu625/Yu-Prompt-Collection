"""
加载.txt格式的prompt template的方法。

可以使用langchain.prompts的load_prompt，这个我方法仅是load_prompt的部分方法，但是需要符合langchain hub对于模板的定义。
"""

from pathlib import Path
# from langchain.prompts import load_prompt


def load_prompt_template(prompt_template_path: str | Path) -> str:
    with open(prompt_template_path, 'r', encoding='utf-8') as f:
        prompt_template = f.read()
    return prompt_template


if __name__ == '__main__':
    eg_prompt_template = load_prompt_template(
        r""
    )

    print(eg_prompt_template)
    print(type(eg_prompt_template))
