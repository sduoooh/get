from bs4 import BeautifulSoup as bf

def return_needs(res):
    img_need = False
    video_need = False


    res = bf(res, 'html.parser')
    img_need = res.find_all('figure') != []
    video_need = res.find_all('a', class_='video-box') != []
    return img_need, video_need
    