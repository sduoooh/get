from bs4 import BeautifulSoup as bf
from status_raise import StatusError

def get_all_text(res, base_url):
    content = bf(res.content, 'html.parser').find_all(class_='css-1g0fqss', options="[object Object]")[0]
    show_content = ''
    try:
        with open(base_url + "text.txt",'w' ,encoding='utf-8') as f:
                text = content.get_text()
                show_content = text[0:20]
                f.write(text)
                f.close()
    except Exception as e:
        raise StatusError(-2, '纯文本写入失败', e)
    
    return show_content
        