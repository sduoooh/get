import requests
import re
from bs4 import BeautifulSoup as bf
from initial_data import initial_data
from status_raise import StatusError, Status

# 拿问题名字、id，和回答id、内容的，顺便处理了回答的格式

def get_answer_info(url,content):
    base_url, get_way, push_way = initial_data.get_url_list(content)
    response = requests.request("GET", url)

    if bf(response.text, 'html.parser').find_all('title', text="安全验证 - 知乎") != []: 
        raise StatusError(0, '触发反爬了', '触发反爬了')
    if bf(response.text, 'html.parser').find_all('div', class_='ErrorPage') != []: 
        return Status(3, '知识荒原了', '知识荒原了'), '', '', '', ''
    question_info_src = bf(response.text, 'html.parser').find('div', class_='QuestionPage')
    #question_id = question_info_src.find('meta', itemprop='url').get('content').split('/')[-1]
    question_name = question_info_src.find('meta', itemprop='name').get('content')
    base_url = base_url + question_name.replace(' ', '_').replace("\\", '_').replace('/', '_').replace('？','_').replace('?', '_').replace('*', '_').replace(':', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace('\'', '_')
    base_url = base_url + url.split('/')[-1] + '/'
    get_way = get_way + question_name.replace(' ', '_').replace("\\", '_').replace('/', '_').replace('？','_').replace('?', '_').replace('*', '_').replace(':', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace('\'', '_')
    get_way = get_way + url.split('/')[-1] + '/'
    answer = str(question_info_src.find('div', class_="RichContent--unescapable"))
    answer = re.sub(r'(<div class="ContentItem-actions RichContent-actions">.*$)', '</div>', answer, 0,  flags=re.MULTILINE)
    a = bf('<div class="CollectionItem"><div>', 'html.parser')
    inner_tag = a.new_tag('')
    title = a.new_tag('h1')
    title.string = question_name
    inner_tag.append(title)
    inner_tag.append(bf(answer, 'html.parser').select('span[itemprop]')[0])
    b = bf(answer, 'html.parser').select('.ContentItem-time')[0]
    b.find_all('a')[0]['href'] = url
    inner_tag.append(a.new_tag('link', rel="stylesheet", href="../style.css"))
    a.div.contents= inner_tag.contents
    a.div.append(b)
    answer = str(a)

    return Status(0, '一切正常', '一切正常'),answer, question_name, base_url, get_way