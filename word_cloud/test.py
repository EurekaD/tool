from wordcloud import WordCloud
import matplotlib.pyplot as plt


# 文本数据
text_data = "这里是你的文本数据，可以是一段文字或从文件中读取的文本。"

# 生成词云对象
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

# 显示词云图
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
