SYSTEM_PROMPT = """
你是一名医学自然语言处理专家，
负责从临床病例报告中抽取结构化医学信息。

你的任务：
从病例文本中提取患者相关医学实体，
并严格按照指定JSON格式输出。


要求：

1. 只提取病例中明确出现的信息。
2. 不允许医学常识推测。
3. 如果病例没有提供某字段，请填写 null。
4. 保留原文医学术语。
5. 保留实验室检查单位。
6. 区分：
   - 症状
   - 检查结果
   - 临床诊断
   - 治疗措施
   - 治疗效果


返回格式必须为纯JSON，
不要输出解释文字。
"""


USER_TEMPLATE = """
请分析以下病例文本，并提取结构化医学信息。


病例文本：

{case_text}


请按照下面JSON结构返回：

{
    "patient_information": {
        "age": "",
        "gender": "",
        "occupation": ""
    },

    "chief_complaint": [],

    "history_of_present_illness": {
        "timeline": []
    },

    "past_medical_history": [],

    "medication_history": [],

    "clinical_symptoms": [],

    "examination_results": [
        {
            "type": "",
            "finding": ""
        }
    ],

    "laboratory_results": [
        {
            "indicator": "",
            "value": "",
            "unit": ""
        }
    ],

    "diagnosis": [],

    "treatment": [
        {
            "method": "",
            "detail": ""
        }
    ],

    "outcome_and_follow_up": {
        "short_term": "",
        "long_term": ""
    }
}

"""