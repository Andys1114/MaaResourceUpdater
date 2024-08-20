import requests,json,os,zipfile,shutil
test = 1
find = True

from requests.exceptions import HTTPError, RequestException

def download_file(url):
    # 导入requests模块和os模块
    # 获取文件名
    file_name = os.path.basename(url)
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, file_name)

    try:
        # 下载文件
        response = requests.get(url)
        response.raise_for_status()  # 将引发HTTPError，如果状态不是200

        # 保存文件
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"文件已保存到：{file_path}")
    except HTTPError as http_err:
        # HTTP错误处理
        print(f"HTTP错误：{http_err}")
    except RequestException as req_err:
        # 其他requests相关的错误
        print(f"请求错误：{req_err}")
    except Exception as e:
        # 其他未预料到的错误
        print(f"发生未知错误：{e}")
        
def delete_folder(folder_name):
    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)
def update():
    url = "https://maa.file.andys1114.top/latest.zip"
    print("有新版本，正在下载")
    download_file(url)
    print("文件下载完成")
    print("开始覆盖")
    with zipfile.ZipFile('latest.zip', 'r') as zip_ref:
        zip_ref.extractall()
    print("覆盖完成")
    os.remove("latest.zip")

url = "https://maa.file.andys1114.top/latest.json"
download_file(url)

if not os.path.exists('latest_now.json'):
    print("latest_now.json 文件不存在")
    find = False
else:
    print("找到latest_now.json文件")
    with open('latest.json', 'r') as file:
        data = json.load(file)
    with open('latest_now.json', 'r') as file:
        data_now = json.load(file)
    # 读取version值
    version = data['version']
    version_now = data_now['version']

if find == False:
    update()
    os.rename("latest.json", "latest_now.json")
    with open('latest_now.json', 'r') as file:
        data_now = json.load(file)
    version = data_now['version']
elif find == True and version > version_now:
    update()
    os.remove("latest_now.json")
    os.rename("latest.json", "latest_now.json")
else:
    print("已经是最新版本")

print("The version is:", version)

