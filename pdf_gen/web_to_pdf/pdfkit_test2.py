import pdfkit

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': 'UTF-8',
    'no-outline': None,
    "enable-local-file-access": ""
}

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PDF with Images</title>
</head>
<body>
    <h1>Hello, PDF with Images!</h1>
    <p>This is a sample HTML with images:</p>
    <p><a><img src='file:///C:/Users/RZ/OneDrive/PycharmProjects/workspace/web_to_pdf/local_image_2.png'></a></p>
</body>
</html>
"""

def html_to_pdf(html, to_file):
    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdfkit.from_string(html, to_file, configuration=config, options=options)

# 替换为你想要保存的PDF文件路径
pdf_file_path = 'output.pdf'

html_to_pdf(html, pdf_file_path)
print(f'PDF generated: {pdf_file_path}')
