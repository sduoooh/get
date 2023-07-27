import requests
import re
from bs4 import BeautifulSoup as bf
from status_raise import StatusError

class get_set_video(object): 
    is_initial = False
    video_list = []
    video_name_index = 0
    base_url = ''
    get_way = ''

    def __init__(self, content_classed):
        if content_classed.is_classfied:
            get_set_video.base_url, get_set_video.get_way = content_classed.base_url, content_classed.get_way
            get_set_video.is_initial = True
            get_set_video.set_video_list(content_classed.content)
            self.content = get_set_video.change_video_attr(content_classed.content)
        else:
            raise StatusError(404, '传递了未进行前序必要操作的信息', '程序bug')

    # 设置<video>的列表
    def set_video_list(res):
        for i in bf(res, 'html.parser').find_all('a', class_='video-box'):
            video_src = get_set_video.get_video_url(i['data-lens-id'])
            video_att = '<video controls><source type="video/mp4" src="' + './' + video_src + '" ><source type="video/mp4" src=\'' + get_set_video.get_way +  video_src + '\' src="' + './' + video_src + '" ></video>'
            get_set_video.video_list.append(video_att)

    # 下载图片，返回图片的相对路径
    def get_video_url(video_id):
        video_url = 'https://lens.zhihu.com/api/videos/' + video_id
        video_url =  requests.get(video_url).json()['playlist']['hd']['play_url']

        try:
            with open(get_set_video.base_url +'video/' + str(get_set_video.video_name_index) + '.mp4','wb') as f:
                f.write(requests.get(video_url).content)
                f.close()
        except Exception as e:
            raise StatusError(-3, '文件下载失败', e)
        get_set_video.video_name_index += 1
        return 'video/' + str(get_set_video.video_name_index - 1) + '.mp4'

    # 把懒加载的<div>替换成<video>
    def change_video_attr(content):
        def replace_video(m):
            return get_set_video.video_list.pop(0)
        
        content =  re.sub(r"(<a[^>]*class=\"video-box\"[^>]*>(.|[\n])*?</a>)", replace_video, (content), 0,  flags=re.MULTILINE)
        return str(content)
    