from status_raise import StatusError

def save_html(base_url,content_ed):
        try:
            with open(base_url +'index.html','w',encoding='utf-8') as f:
                f.write(content_ed.content)
                f.close()
        except Exception as e:
            raise StatusError(-2, 'html保存失败', '文件创建失败')
        return base_url +'index.html'
