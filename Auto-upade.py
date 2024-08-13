import requests,json,os,zipfile,wget

url_json = "https://maa.file.andys1114.top/latest.json"
url_file = "https://maa.file.andys1114.top/latest.zip"
wget.download(url)

with open("latest.json", "wb") as f: f.write(response.content)

# 打开并读取文件内容
with open('latest.json', 'r') as file:
    data = json.load(file)
with open('latest_now.json', 'r') as file:
    data_now = json.load(file)
# 读取version值
version = data['version']
version_now = data_now['version']

if version > version_now:
    print("有新版本，正在下载")
    response = requests.get(url)
    with open("latest.zip", "wb") as f:
        f.write(response.content)
    print("文件下载完成")
    print("开始覆盖")
    with zipfile.ZipFile('latest.zip', 'r') as zip_ref:
        zip_ref.extractall()
    print("覆盖完成")
    os.remove("latest_now.json")
    os.rename("latest.json", "latest_now.json")

print("The version is:", version)

print("文件下载完成")

