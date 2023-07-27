import requests

# 这俩是用来拿问题下其他回答的
def get_answers_respones(question_id):
    global next_page_url
    global is_end

    url = 'https://www.zhihu.com/api/v4/questions/'+ question_id +'/feeds?include=%2Ccontent&limit=40'
    response = requests.request("GET", url).json()
    next_page_url = response['paging']['next']
    is_end = response['paging']['is_end']
    return response

def get_answers_content(frist_response ,answer_id):
    global next_page_url
    global is_end
    for i in frist_response['data']:
        if str(i['target']['id']) == answer_id:
            return i['target']['content']
        else :
            next_page_url = frist_response['paging']['next']
            is_end = frist_response['paging']['is_end']
            continue
    while not is_end:
        response = requests.request("GET", next_page_url).json()
        for i in response['data']:
            if str(i['target']['id']) == answer_id:
                return i['target']['content']
            else :
                next_page_url = response['paging']['next']
                is_end = response['paging']['is_end']
                continue
    return None