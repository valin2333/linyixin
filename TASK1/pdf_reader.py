import fitz


def extract_text_from_pdf(pdf_path):
    """
    从PDF文件中提取文本

    Args:
        pdf_path: PDF路径

    Returns:
        str: PDF全文文本
    """

    text = ""

    try:
        doc = fitz.open(pdf_path)

        for page in doc:
            text += page.get_text()

        doc.close()

    except Exception as e:
        raise RuntimeError(
            f"PDF读取失败: {e}"
        )

    return text