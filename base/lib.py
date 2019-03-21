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

def get_mem():
    mem = os.popen("adb shell dumpsys meminfo " + Config().get_config()['pck_name']).read()
    Total = get_code(mem, "TOTAL:")
    print(Total)

def get_cpu():
    cpu = os.popen("adb shell dumpsys cpuinfo " + Config().get_config()['pck_name']).read()

get_mem()