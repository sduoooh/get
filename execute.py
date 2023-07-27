from pathlib import Path
from PIL import Image
from bs4 import BeautifulSoup as bf

from status_raise import StatusError,Status

from initial_data import initial_data
from answer import get_answer_info
from p import get_p_info
from dir import create_dir
from classify import Classifier
from img import get_set_img
from video import get_set_video
from save_html import save_html
from get_text import get_all_text
from add_into_dir import add_into_dir

def execute(p_url, answer_url, label,comment_need = False, stop = False):
    label= []
    url = ''
    content = Classifier(label)
    if p_url == '':
        url = answer_url
        status, got_content, name, base_url, get_way = get_answer_info(answer_url,content)
    else:
        url = p_url
        status ,got_content, name, base_url, get_way = get_p_info(p_url,content)
    if status.code == 3:
        if stop:
            return status, '',content
        else :
            raise StatusError(3, '知识荒原了', '知识荒原了')
    content.set_content(got_content, base_url, get_way)
    img_need, video_need = content.img_need, content.video_need
    dir_status = create_dir(img_need,comment_need,video_need,base_url, stop)
    if dir_status.code == 2:
        return dir_status, '',content
    if img_need:
        content.content = get_set_img(content).content
    if video_need:
        content.content = get_set_video(content).content
    show_content =  get_all_text(content,base_url)
    add_into_dir(initial_data.get_url_list(content)[0],url,name,show_content)
    file = 'file://' + save_html(base_url, content)
    return Status(0, '一切正常', '一切正常'),file,content