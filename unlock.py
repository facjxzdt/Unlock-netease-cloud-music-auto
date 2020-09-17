# -- coding: utf-8 --
import git,requests,os,zipfile
if not os.path.exists('./node'):
    os.mkdir('./node')
def unzip_file(zip_src, dst_dir):
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, 'r')
        for file in fz.namelist():
            fz.extract(file, dst_dir)
print('正在下载文件')
if os.path.exists('./netmusic'):
    print('文件已存在')
else:
    clone_repo = git.Repo.clone_from('https://github.com/meng-chuan/Unlock-netease-cloud-music', './netmusic')
if os.path.exists('./node/node-v14.10.0-win-x64'):
    print('文件已存在')
else:
    url = 'https://cdn.npm.taobao.org/dist/node/v14.10.0/node-v14.10.0-win-x64.zip'
    r = requests.get(url)
    with open("node.zip", "wb") as code:
        code.write(r.content)
    print('下载完成')
    print('开始解压')
    unzip_file('./node.zip','./node')
    print('解压完成')
    print('开始清理')
if os.path.exists('./node.zip'):
    os.remove('node.zip')
print('清理完成')
print('网易云反代已搭建完成，请勿关闭此窗口，网易云中代理设置为本机ip，端口为52000')
os.system('powershell ./node/node-v14.10.0-win-x64/node.exe ./netmusic/app.js -p 52000 -f 59.111.181.38')
