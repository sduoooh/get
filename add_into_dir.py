import json
from status_raise import StatusError

def add_into_dir(base_url, url, name,show_content):
    try:    
            data = ''
            index = 0
            file_name = ''
            with open(base_url + 'dir.json','r',encoding="utf-8") as f:
                data = json.load(f)
                f.close()
            with open(base_url + 'dir.json','w',encoding="utf-8") as f:
                new_file = {
                      'index': len(data['dir']),
                      'file_name' : name.replace(' ', '_').replace("\\", '_').replace('/', '_').replace('？','_').replace('?', '_').replace('*', '_').replace(':', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace('\'', '_') + url.split('/')[-1],
                      'show_name': name,
                      'show_content':  show_content + '......'        
                }
                index = new_file['index']
                file_name = new_file['file_name']
                data['dir'].append(new_file)
                json.dump(data,f,ensure_ascii=False)
                f.close()
            with open(base_url + 'map.json','r',encoding="utf-8") as f:
                data = json.load(f)
                f.close()
            with open(base_url + 'map.json','w',encoding="utf-8") as f:
                data['map'][file_name] = index
                json.dump(data,f,ensure_ascii=False)
                f.close()
    except Exception as e:
            raise StatusError(-3, '文件下载失败', e)