import json
from status_raise import StatusError, Status

class initial_data(object):
    is_initial = False
    __pri = []
    __pub = []

    def initial():
        try : 
            with open('./data.json') as f:
                data = json.load(f)
                f.close()
                initial_data.__pub = [data['pub_base_url'], data['pub_get_way'], data['pub_push_way'], data['pub_trans_local_way'], data['pub_trans_pull_way'], data['pub_trans_push_way']]
                initial_data.__pri = [data['pri_base_url'], data['pri_get_way'], data['pri_push_way'], data['pri_trans_local_way'], data['pri_trans_pull_way'], data['pri_trans_push_way']]     
        except Exception as e:
            if initial_data.__pub == []:
                raise StatusError(1, 'data.json文件未正确配置，缺少必要的公开/默认路径 pub 设置。', '配置文件错误')
            elif initial_data.__pri == []:
                initial_data.is_initial = True
                return Status(1, 'data.json文件正确配置，但缺少可选的私人路径 pri 设置。', '配置文件不完整')
            
            raise StatusError(-1, 'data.json文件读取出错。\n' + str(e.args), '未知系统错误')

        initial_data.is_initial = True
        return Status(0,'data.json文件读取成功，数据完整。', '配置文件完整读取')
    
    def get_url_list(classed_obj):
        if classed_obj.is_pri:
            if initial_data.__pri != []:
                return initial_data.__pri[0:3]
            else: 
                raise StatusError(1, '未提供对应功能所需信息，请检查data.json文件是否正确进行私人路径 pri 设置。', '配置文件错误')
        else :
            return initial_data.__pub[0:3]
        
    def get_trans(is_pri):
        if is_pri:
            if initial_data.__pri != []:
                return initial_data.__pri[3], initial_data.__pri[4], initial_data.__pri[5]
            else: 
                raise StatusError(1, '未提供对应功能所需信息，请检查data.json文件是否正确进行私人路径 pri 设置。', '配置文件错误')
        else:
            return initial_data.__pub[3], initial_data.__pub[4], initial_data.__pub[5]
        
    