import io
import os

import yt_dlp
from bs4 import BeautifulSoup
import requests
from miniIO.local_connection import local_connection


if __name__ == '__main__':
    # Video HTML URL
    video_html_url = "https://tw.news.yahoo.com/7-6%E5%BC%B7%E9%9C%87%E6%92%BC%E6%97%A5%E6%9C%AC-%E5%8F%B0%E7%81%A3%E7%89%B9%E6%90%9C%E9%9A%8A160%E4%BA%BA-4%E9%9A%BB%E6%90%9C%E6%95%91%E7%8A%AC%E6%BA%96%E5%82%99%E5%BE%85%E5%91%BD-234602502.html"
    # Proxy server address and port number (if needed)
    proxy_address = 'https://127.0.0.1'
    proxy_port = '7890'

    # Define yt_dlp configuration options
    ydl_opts = {
        # 'proxy': f'{proxy_address}:{proxy_port}',  # Set proxy
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Set download format to mp4
        'outtmpl': '%(title)s.%(ext)s',  # Set output file name format
    }

    minioClient = local_connection().minioClient
    # 使用 yt_dlp 下载视频
    # 从 YouTube 下载视频并直接上传到 MinIO
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_html_url, download=False)
        video_url = info_dict['formats'][0]['url']
        response = requests.get(video_url)
        video_data = response.content
        video_name = f"{info_dict['title']}.mp4"

        # 将视频数据上传到MinIO
        size = len(video_data)
        minioClient.put_object("test", video_name, io.BytesIO(video_data), size, content_type='audio/mp4')
        print(f"Video uploaded to MinIO: {video_name}")


    # 输出视频信息
    print(info_dict)
