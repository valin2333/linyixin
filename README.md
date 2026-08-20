# linyixin

## 仓库结构

````
```
linyixin/
├── AI_Chat_Records.md
├── README.md
├── TASK1/
│   ├── A case of portal vein recanalization and symptomatic heart failure.pdf #指定PDF原文件
│   ├── extracted_case.json #输出结果文件
│   ├── main.py #源文件代码
│   └── requirements.txt
├── TASK2/
│   ├── 数据分析与建模代码.ipynb
│   ├── heart_failure_clinical_records_dataset.csv #原始数据文件
│   ├── requirements.txt
│   ├── main.tex #LaTeX源文件
│   ├── main.pdf #PDF格式论文
│   ├── ROC_comparison.png #ROC曲线对比图
│   ├── correlation_heatma.png #相关性热力图
│   └── workflow.png #模型工作流程图
└── TASK3/
    ├── 源文件.md
    └── 医疗大模型新人快速上手指南.pdf
```
````



## 任务目录说明



- TASK1/：病例数据提取 
- TASK2/：心衰预测模型
- TASK3/：大模型学习资料与源文件





## 运行方法

1. 进入对应任务目录（`TASK1/` 或 `TASK2/`）
2. 安装依赖：`pip install -r requirements.txt`
3. 运行：
   - 任务一：`python main.py`
   - 任务二：启动 Jupyter Notebook，打开 `数据分析与建模代码.ipynb` 运行
   - 任务三：无需运行代码，直接查看 `医疗大模型新人快速上手指南.pdf`





## 主要提交物位置

### 任务一
- 源代码：`TASK1/main.py`
- 输出结果：`TASK1/extracted_case.json`
- 依赖清单：`TASK1/requirements.txt`
- 病例PDF原文件：`TASK1/A case of portal vein recanalization and symptomatic heart failure.pdf` 

### 任务二

- 分析代码：`TASK2/数据分析与建模代码.ipynb`
- 原始数据：`TASK2/heart_failure_clinical_records_dataset.csv`
- 依赖清单：`TASK2/requirements.txt`
- LaTeX源文件：`TASK2/main.tex`
- 引用的图片：`TASK2/ROC_comparison.png`、`TASK2/correlation_heatma.png`、`TASK2/workflow.png`
- 论文PDF：`TASK2/main.pdf`

### 任务三

- 源文档：`TASK3/源文件.md`
- 导出的PDF：`TASK3/医疗大模型新人快速上手指南.pdf`

## 运行环境

- Python 3.13.5
- Jupyter Notebook
- 详细依赖见各任务目录下的 `requirements.txt`