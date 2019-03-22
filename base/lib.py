import os
from base.config import Config

def get_code(a, b):
    # 提取字符串
    p1 = a.split(b)
    if len(p1) > 1:
        p2 = p1[1].split()
        if len(p2) > 1:
            return p2[0]
    return ''


def check_adb_connect(self):
    """查看USB连接状态"""
    text = os.popen('adb devices').readlines()
    if 'device' in text[1]:
        print('USB连接正常')
        return True
    else:
        print('USB未连接')
        return False

def get_phone_ip(self):
    # 获取安卓手机的ip地址
    data = os.popen('adb shell netcfg').readlines()
    for i in data:
        if 'wlan0' in i:
            ip = i.split()[2].split('/')[0]
            print(ip)
            return ip

def app_start(self):
    """启动app"""
    os.popen('adb shell am start ' + self.get_app_launch_activity())

