from pathlib import Path
from PIL import Image
from bs4 import BeautifulSoup as bf

from status_raise import StatusError

from run_from_trans_station import run_from_trans_station
from initial_data import initial_data
from execute import execute
from do_git import git, proxy_start, proxy_stop


def collect():
    answer_url = ''
    p_url = ''

    url = input('请输入链接：')
    if url.split('/')[-2] == 'answer':
        answer_url = url
    elif url.split('/')[-2] == 'p':
        p_url = url

    comment_need = input('是否需要附上评论：')
    if comment_need == 'y' or comment_need == 'Y' or comment_need == 'yes' or comment_need == 'Yes' or comment_need == 'YES':
        comment_need = False
        print('暂不支持附上评论哦')
    else:
        comment_need = False
    label = []
    status ,file_url,content = execute(p_url ,answer_url, label, comment_need)
    print('\n\n\n点击这里访问：\n\n\n', file_url)
    git(content)

if __name__ == '__main__':
    try:
        initial_data.initial()
    except StatusError:
        print('\n\n\n初始化失败')
        print('请先在同目录下正确配置data.json文件')
        print('格式如下：\n\n')
        print('{')
        print('    "pri_base_url": "x:/xx/xx",  -----(OPTIONAL)')
        print('    "pri_push_way": "git push xxx xxx",  -----(OPTIONAL)')
        print('    "pri_get_way": "https://raw.githubusercontent.com/your_user_name/file/main/" -----(OPTIONAL)' )  
        print('    "pub_base_url": "x:/xx/xx",')
        print('    "pub_push_way": "git push xxx xxx", ')
        print('    "pub_get_way": "https://raw.githubusercontent.com/your_user_name/file/main/" -----(Your picturebed address)' )  
        print('}\n\n')
        input('按任意键退出')
    print('\n\n\n选择：\n')
    print('1. 从单个知乎链接获取;\n')
    print('2. 从中转站批量获取.\n\n\n')
    choice = input('请输入：')
    proxy_start()
    if choice == '1':
        collect()
    elif choice == '2':
        print('\n\n\n选择：\n')
        print('1. pri;\n')
        print('2. pub.\n\n\n')
        choice = input('请输入： ')
        if choice == 'pri':
            run_from_trans_station(True)
        elif choice == 'pub':
            run_from_trans_station(False)
        else :
            raise StatusError(2, '未正确输入信息', '用户输入不在预期内')
    else :
        raise StatusError(2, '未正确输入信息', '用户输入不在预期内')
    proxy_stop()

    

