import os
import yaml

class Config:
    # 读取配置文件
    def get_config(self):
        BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        CONFIG_FILE = os.path.join(BASE_PATH, 'base', 'config.yaml')
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'rb') as f:
                 # load后是个字典
                data = yaml.load(f)
               # print(data)
                return data
        else:
            raise FileNotFoundError('文件不存在！')

co = Config()
co.get_config()
