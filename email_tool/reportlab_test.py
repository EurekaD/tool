from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
# 调用模板，创建指定名称的PDF文档
doc = SimpleDocTemplate("Hello.pdf")


style = ParagraphStyle()

# 初始化内容
story =[]

# 将段落添加到内容中
story.append(Paragraph("在阵阵的轰鸣中，随着剧烈的震动，呼的一声，从贵阳飞往三亚的航班，把我从地面拽入了天空，瞬间我飘飘然起来，像孙悟空师兄三人上天入云，像神仙们那般腾云驾雾，遨游仙界。",style))
# 将内容输出到PDF中
doc.build(story)
