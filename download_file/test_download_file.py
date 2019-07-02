import requests
import re
import urlparse
import urllib
import os


def list_file(url):
    file_list = []
    url_html = requests.get(url)
    pattern = re.compile('<a href=.*?\..*?>(.*?)</a>')
    name_list = re.findall(pattern, url_html.text)
    for item in name_list:
        path = urlparse.urljoin(url, item)
        file_list.append(path)
    return file_list, name_list


def download_file(file_list=None, dest_path=None, name_list=None, file_num=None):
    if file_num:
        file_num = file_num
    else:
        file_num = 5000

    if dest_path:
        dest_path = dest_path
    else:
        dest_path = "/home/joy/gcsd_download/"

    for i in range(file_num):
        dest_name = os.path.join(dest_path, name_list[i])
        try:
            urllib.urlretrieve(file_list[i], dest_name)
            print("downloading file " + file_list[i])
        except Exception as e:
            print("download file failed" + e.message)


def main():
    file_list, name_list = list_file("http://10.103.64.129/gcsd_file/")
    download_file(file_list=file_list, name_list=name_list, file_num=10)


if __name__ == "__main__":
    main()
