import requests
import re
from bs4 import BeautifulSoup as bf
from status_raise import StatusError, Status

class get_set_img(object): 
    is_initial = False
    img_list = []
    img_name_index = 0
    base_url = ''
    get_way = ''

    def __init__(self, content_classed):
        if content_classed.is_classfied:
            get_set_img.base_url, get_set_img.get_way = content_classed.base_url, content_classed.get_way
            get_set_img.is_initial = True
            get_set_img.set_img_list(content_classed.content)
            self.content = get_set_img.change_img_attr(content_classed.content)
        else:
            raise StatusError(404, '传递了未进行前序必要操作的信息', '程序bug')
        

    # 设置<img>的列表
    def set_img_list(res):
        for i in bf(res, 'html.parser').find_all('figure'):
            img_src = get_set_img.get_img_url(i.find('img')['src'])
            print(i.find('img'))
            img_height = i.find('img')['data-rawheight']
            img_width = i.find('img')['data-rawwidth']
            img_aspect_ratio = int(img_width) / int(img_height) 
            img_att = '<img loading="lazy" onerror="this.src=\'' + get_set_img.get_way + img_src + '\';this.onerror=null;" src="' + './' + img_src + '" aspect-ratio ="' + str(img_aspect_ratio) + '">'
            get_set_img.img_list.append(img_att)

    # 下载图片，返回图片的相对路径
    def get_img_url(img_url):
        img_url = img_url.replace('720w.jpg?','1440w.jpg?')

        try:
            with open(get_set_img.base_url +'img/' + str(get_set_img.img_name_index) + '.jpg','wb') as f:
                f.write(requests.get(img_url).content)
                f.close()
        except Exception as e:
            raise StatusError(-3, '文件下载失败', e)
        get_set_img.img_name_index += 1
        return 'img/' + str(get_set_img.img_name_index - 1) + '.jpg'

    # 把懒加载的<figure>替换成<img>
    def change_img_attr(content):
        def replace_img(m):
            return get_set_img.img_list.pop(0)
        content =  re.sub(r"(<figure[^>]*>.*?<\/figure>)", replace_img, (content), 0,  flags=re.MULTILINE)
        return content
    
