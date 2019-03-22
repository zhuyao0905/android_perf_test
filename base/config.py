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

def check_dir(c_dir):
    # 检测测试数据目录是否存在
    BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    if not os.path.exists(BASE_PATH + c_dir):
        os.makedirs(BASE_PATH + c_dir)

class GetPath:
    # 读取测试数据地址
    BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    check_dir('\\result\\cpu_info')
    check_dir('\\result\\cpu_process')
    check_dir('\\result\\mem_process')
    check_dir('\\result\\mem_back')
    check_dir('\\result\\mem_info')
    check_dir('\\result\\start')
    check_dir('\\result\\flow')
    check_dir('\\result\\monkey')
    flow = os.path.join(BASE_PATH, 'result', 'flow')
    mem_info = os.path.join(BASE_PATH, 'result', 'mem_info')
    mem_process = os.path.join(BASE_PATH, 'result', 'mem_process')
    mem_back = os.path.join(BASE_PATH, 'result', 'mem_back')
    cpu_process = os.path.join(BASE_PATH, 'result', 'cpu_process')
    cpu_info = os.path.join(BASE_PATH, 'result', 'cpu_info')
    start = os.path.join(BASE_PATH, 'result', 'start')
    monkey = os.path.join(BASE_PATH, 'result', 'monkey')

