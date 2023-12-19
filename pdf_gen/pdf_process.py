import PyPDF2


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        # 创建 PdfReader 对象
        pdf_reader = PyPDF2.PdfReader(file)

        # 获取 PDF 文件的总页数
        total_pages = pdf_reader.numPages
        print(f"总页数: {total_pages}\n")

        # 逐页读取并打印文本内容
        for page_num in range(total_pages):
            # 获取指定页码的页面对象
            page = pdf_reader.getPage(page_num)

            # 提取文本内容并打印
            text = page.extractText()
            print(f"第 {page_num + 1} 页:\n{text}\n{'=' * 30}\n")


if __name__ == "__main__":
    # 替换为你的 PDF 文件路径
    pdf_file_path = r"C:\Users\RZ\OneDrive\桌面\台湾各地关于教育程度和年龄的人口数据表\宜兰县人口结构.pdf"
    read_pdf(pdf_file_path)
