import os
import json

from dotenv import load_dotenv

from openai import OpenAI


from pdf_reader import extract_text_from_pdf

from prompt import (
    SYSTEM_PROMPT,
    USER_TEMPLATE
)

from json_parser import (
    parse_json_response
)


# ============================
# 环境配置
# ============================


load_dotenv()


API_KEY = os.getenv(
    "DASHSCOPE_API_KEY"
)


if API_KEY is None:
    raise ValueError(
        "未检测到DASHSCOPE_API_KEY"
    )


# 阿里云百炼兼容OpenAI接口

client = OpenAI(
    api_key=API_KEY,
    base_url=
    "https://dashscope.aliyuncs.com/compatible-mode/v1"
)



# ============================
# 文件路径
# ============================


PDF_PATH = (
    "./input/case.pdf"
)


OUTPUT_PATH = (
    "./output/extracted_case.json"
)



# ============================
# 调用Qwen
# ============================


def call_qwen(case_text):


    user_prompt = USER_TEMPLATE.replace(
    "{case_text}",
    case_text
    )


    response = client.chat.completions.create(

        model="qwen-plus",

        messages=[

            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },

            {
                "role": "user",
                "content": user_prompt
            }

        ],

        temperature=0.1

    )


    result = (
        response
        .choices[0]
        .message
        .content
    )


    return result



# ============================
# 主流程
# ============================


def main():


    print(
        "正在读取PDF..."
    )


    text = extract_text_from_pdf(
        PDF_PATH
    )


    print(
        f"PDF文本长度:{len(text)}"
    )



    print(
        "正在调用Qwen模型..."
    )


    response = call_qwen(
        text
    )


    print(
        "正在解析JSON..."
    )


    json_result = parse_json_response(
        response
    )



    os.makedirs(
        "./output",
        exist_ok=True
    )


    with open(
        OUTPUT_PATH,
        "w",
        encoding="utf-8"
    ) as f:


        json.dump(

            json_result,

            f,

            ensure_ascii=False,

            indent=4

        )



    print(
        "完成!"
    )


    print(
        f"结果保存:{OUTPUT_PATH}"
    )



if __name__ == "__main__":

    main()