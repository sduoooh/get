import os
from status_raise import StatusError
from initial_data import initial_data

def git(content):
    base_url, get_way, push_way = initial_data.get_url_list(content)
    if push_way == None:
        print('未配置git命令')
        return
    print('正在上传到github...')
    os.chdir(base_url)
    os.system('git init')
    os.system('git add -A')
    os.system('git commit -m "update"')
    os.system('git config http.sslVerify "false"')
    os.system(push_way)
    print('上传成功')

def trans_pull(local_way, pull_way):
    if local_way == None:
        raise StatusError(1, '未配置git命令', '配置文件错误')
    print('正在从远程仓库拉取...')
    print ('cd ' + local_way )
    os.chdir(local_way)
    os.system('git config http.sslVerify "false"')
    print(pull_way)
    os.system(pull_way)
    print('拉取成功')

def trans_push(local_way, push_way):
    if local_way == None:
        raise StatusError(1, '未配置git命令', '配置文件错误')
    print('正在往远程仓库推送...')
    os.chdir(local_way)
    os.system('git add -A')
    os.system('git commit -m "already"')
    os.system(push_way)
    print('推送成功')

def proxy_start():
    os.system("start C:/Users/1/Desktop/工具/fastgithub_win-x64/fastgithub.exe")
    return

def proxy_stop():
    os.system('runas /user:administrator "taskkill /f /t /im fastgithub.exe"')
    return