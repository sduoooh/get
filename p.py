import requests
from bs4 import BeautifulSoup as bf
from initial_data import initial_data
from status_raise import StatusError, Status

# 返回： 1. 状态，状态[0] 为0 则正常；其后为需求。
def get_p_info(p_url,content):
    base_url, get_way, push_way = initial_data.get_url_list(content)
    res = requests.get(p_url).text

    if bf(res, 'html.parser').find_all('title', text="安全验证 - 知乎") != []:
        raise StatusError(0, '触发反爬了', '触发反爬了')
    
    p_name = bf(res, 'html.parser').select('.Post-Title')[0].text
    base_url = base_url + p_name.replace(' ', '_').replace("\\", '_').replace('？','_').replace('/', '_').replace('?', '_').replace('*', '_').replace(':', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace('\'', '_')+ p_url.split('/')[-1] + '/'
    get_way = get_way + p_name.replace(' ', '_').replace("\\", '_').replace('？','_').replace('/', '_').replace('?', '_').replace('*', '_').replace(':', '_').replace('"', '_').replace('<', '_').replace('>', '_').replace('|', '_').replace('\'', '_') + p_url.split('/')[-1]+ '/'
    a = bf('')
    new_tag = bf('<div class="CollectionItem"><div>', 'html.parser').div
    title = a.new_tag('h1')
    title.string = p_name
    address = a.new_tag('a')
    address['href'] = p_url
    new_tag.append(title)
    new_tag.append(bf(res, 'html.parser').select('div[options]')[0])
    print(bf(res, 'html.parser').select('.ContentItem-time')[0].contents)
    address.contents = [bf(res, 'html.parser').select('.ContentItem-time')[0].contents[0]]
    ip = a.new_tag('span')
    ip_contents = bf(res, 'html.parser').select('.ContentItem-time')[0].contents
    if len(ip_contents) == 3:
        ip.contents = [bf(res, 'html.parser').select('.ContentItem-time')[0].contents[2]]
    new_end = bf('<div class="ContentItem-time" role="button" tabindex="0">'+ str(address) + str(ip) +'</div>', 'html.parser')
    new_tag.append(a.new_tag('link', rel="stylesheet", href="../style.css"))
    new_tag.append(new_end)
    p = str(new_tag)
    
    return Status(0, '一切正常', '一切正常'),p, p_name, base_url, get_way
