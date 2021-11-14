import yaml

class read_config():

    def __init__(self):
        with open ('/Users/kelly/PycharmProjects/framework_template/config/test_config.yaml','r') as config:
            self.network = yaml.safe_load(config)

    def getApplicationURL(self):
        return self.network['login_info']['baseURL']

    def getApplication_username(self):
        return self.network['login_info']['username']

    def getApplication_password(self):
        return self.network['login_info']['password']


