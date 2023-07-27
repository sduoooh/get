from pathlib import Path
from status_raise import StatusError,Status

def create_dir(img_need, comment_need, video_need, base_url, stop = False):
    if img_need:
        img_dir = Path(base_url + 'img')
    if video_need:
        video_dir = Path(base_url + 'video')
    if comment_need:
        text_dir = Path(base_url + 'text')
        comment_dir = Path(base_url + 'text/' + 'comment')
        child_comment_dir = Path(base_url + 'text/' + 'child_comment')
    try :
        Path(base_url).mkdir()
        if img_need:
            img_dir.mkdir()
        if video_need:
            video_dir.mkdir()
        if comment_need:
            text_dir.mkdir()
            comment_dir.mkdir()
            child_comment_dir.mkdir()
        return Status(0, '目录创建成功', '目录创建成功')
    except FileExistsError:
        if stop:
            return Status(2, base_url.split('/')[-2] + '已存在', FileExistsError)
        else :
            raise StatusError(-2, '目录创建失败，该目录已存在', FileExistsError)
    