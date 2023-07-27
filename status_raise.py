class StatusError(Exception):
    def __init__(self, code, tips, response):
        self.code = code
        self.tips = tips
        self.response = response
    def __str__(self):
        return '\n\n\ncode: ' + str(self.code) + '\n\ntips: ' + self.tips + '\n\nresponse: ' + str(self.response) + '\n\n\n'

class Status(object):
    def __init__(self, code, tips, response):
        self.code = code
        self.tips = tips
        self.response = response

    def show_status(self):
        return {'code': self.code, 'tips': self.tips, 'response': self.response}
