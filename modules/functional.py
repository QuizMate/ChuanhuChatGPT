import json
import os


tutor_prompt_data = ""

file = os.path.join(os.path.dirname(__file__), '../configs', 'ai_tutor.json')
with open(file, 'r') as file:
    tutor_prompt_data = json.load(file)

def get_core_functions():

    return {
    "生成内容摘要": {
        'Prefix':  r"请帮我生成文件摘要",
        "Content": "",
        "Base": True
    },
    "翻译文本": {
        'Prefix':  r"请帮我翻译文件中的内容",
        "Content": "",
        "Base": True
    },
    "解析习题": {
        'Prefix':  r"请帮我解析文件中习题",
        "Content": "",
        "Base": True
    },
    "获取答案和解题步骤": {
        'Prefix':  r"请作为大学教授, 帮我获取答案和解题步骤",
        "Content": "",
        "Medium": True
    },
    "查看相关知识点": {
        'Prefix':  r"请作为大学教授, 帮我推荐相关知识点",
        "Content": "",
        "Medium": True
    },
    "查找相似题目": {
        'Prefix':  r"请作为大学教授, 帮我理解这个题目的内容",
        "Content": "",
        "Medium": True
    },
    "开始学习": {
        'Prefix': str(tutor_prompt_data),
        "Content": "",
        "Deep": True
    },
    "请继续": {
        'Prefix':  r"/continue",
        "Content": "",
        "Deep": True
    },
    "请用中文回复": {
        'Prefix':  r"/language 中文",
        "Content": "",
        "Deep": True
    },
    "出题测试": {
        'Prefix':  r"/test",
        "Content": "",
        "Deep": True
    },
}
