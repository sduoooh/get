import json
from do_git import trans_pull, trans_push, git
from execute import execute
from initial_data import initial_data 
from status_raise import StatusError

def run_from_trans_station(is_pri):
    trans_loacal_way, trans_pull_way, trans_push_way = initial_data.get_trans(is_pri)
    data = ''
    try:
            trans_pull(trans_loacal_way, trans_pull_way)  
            with open(trans_loacal_way + '/collection.json','r',encoding="utf-8") as f:
                data = json.load(f)
                f.close()
            with open(trans_loacal_way + '/collection.json','w',encoding="utf-8") as f:
                new_file = {
                     "url": []       
                }
                json.dump(new_file,f,ensure_ascii=False)
                f.close()
    except Exception as e:
            raise StatusError(-3, '获取远端url失败', e)
    print(data['url'])
    content = ''
    for i in data['url']:
        answer_url = ''
        p_url = ''

        url = i
        if url.split('/')[-2] == 'answer':
            answer_url = url
        elif url.split('/')[-2] == 'p':
            p_url = url

        comment_need = False
        label = []
        status, file_url,content = execute(p_url ,answer_url, label, comment_need,stop=True)
        if status.code == 2:
            print('\n\n\n', status.tips + '\n\n\n')
            continue
        elif status.code == 3:
            print('\n\n\n', status.tips + '\n\n\n')
            continue
    git(content)
    input('\n完成，即将清空序列......\n')
    trans_push(trans_loacal_way, trans_push_way)
