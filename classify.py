from initial_data import initial_data
from query_all_needs import return_needs
from status_raise import StatusError


class Classifier(object):
    is_classfied = False
    is_pri = False
    def __init__(self, labels):
        if not initial_data.is_initial:
            raise StatusError(404, '传递未进行必需的前序操作的信息','')
        self.labels = labels
        self.is_pri = classify(self.labels)
        self.is_classfied = True
        self.base_url, self.get_way, self.push_way = initial_data.get_url_list(self)

    def set_content(self, content, base_url, get_way):
        self.content = content
        self.base_url = base_url
        self.get_way = get_way
        self.img_need,self.video_need = return_needs(self.content)
        pass




def classify(labels):
    if '私人' in labels:
        return True
    else :
        return False
    