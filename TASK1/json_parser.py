import json
import re


def parse_json_response(response_text):

    """
    将模型输出转换为JSON

    """

    try:

        return json.loads(response_text)


    except json.JSONDecodeError:


        # 防止模型返回markdown代码块

        cleaned = re.sub(
            r"```json",
            "",
            response_text
        )

        cleaned = re.sub(
            r"```",
            "",
            cleaned
        )


        return json.loads(
            cleaned.strip()
        )