import base64
import os
import time
from urllib.parse import unquote

import requests
import zipfile


def printBanner():
    print(r'''
    ________         .__.__         ________                        .__     ___________           .__   
    \______ \ _____  |__|  | ___.__.\______ \   ____   _____ _____  |__| ___\__    ___/___   ____ |  |  
     |    |  \\__  \ |  |  |<   |  | |    |  \ /  _ \ /     \\__  \ |  |/    \|    | /  _ \ /  _ \|  |  
     |    `   \/ __ \|  |  |_\___  | |    `   (  <_> )  Y Y  \/ __ \|  |   |  \    |(  <_> |  <_> )  |__
    /_______  (____  /__|____/ ____|/_______  /\____/|__|_|  (____  /__|___|  /____| \____/ \____/|____/
            \/     \/        \/             \/             \/     \/        \/                          
        ''')


def get_file_name(url, headers):
    filename = ''
    if 'Content-Disposition' in headers and headers['Content-Disposition']:
        disposition_split = headers['Content-Disposition'].split(';')
        if len(disposition_split) > 1:
            if disposition_split[1].strip().lower().startswith('filename='):
                file_name = disposition_split[1].split('=')
                if len(file_name) > 1:
                    filename = unquote(file_name[1])
    if not filename and os.path.basename(url):
        filename = os.path.basename(url).split("?")[0]
    if not filename:
        return time.time()
    return filename


if __name__ == '__main__':
    # 打印banner
    printBanner()
    # 获取指定格式的今日日期并通过base64编码，用于拼接下载URL
    date_str = time.strftime('%Y-%m-%d', time.localtime())
    date_str_base64 = str(base64.standard_b64encode(bytes(date_str)), encoding='utf-8')
    # 拼接新注册域名数据下载URL
    url = 'https://whoisds.com//whois-database/newly-registered-domains/' + date_str_base64 + '/nrd'
    # request 方式下载文件
    res = requests.get(url)
    # 指定下载的文件名
    zip_file = get_file_name(url, res.headers)
    file_to_extract = "domain-names.txt"
    # 下载的文件落盘
    with open(zip_file, "wb") as zip:
        zip.write(res.content)
    # ZIP文件解压
    try:
        with zipfile.ZipFile(zip_file) as z:
            with open(file_to_extract, 'wb') as f:
                f.write(z.read(file_to_extract))
    except:
        print("fail")
