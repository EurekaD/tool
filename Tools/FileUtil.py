import os
import urllib
from urllib.request import urlretrieve

file_list = []
# 遍历某个文件夹下的所有文件
def gci(filepath):
    # file_list = []
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            file_list.append(fi_d)
    return file_list

# 获取当前文件夹下的所有文件绝对路径
def getAllPaths(filepath):
    file_list = gci(filepath)
    return file_list

# 若字符串超出指定长度则截取
def consistentLineLength(thestr, length):
    if len(thestr) > length:
        thestr = thestr[:length - 1]
    return thestr


# TODO PDF文件下载
def get_file_from_url(fileurl, fileName):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')]
    urllib.request.install_opener(opener)
    os.makedirs('./img1/', exist_ok=True)  # 创建目录存放文件
    urlretrieve(fileurl, './img1/{file}'.format(file=fileName))  # 将什么文件存放到什么位置
