# /usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
import easygui
from base.config import Config,GetPath

# 执行monkey指令
def start_monkey():
    """获取相关参数，拼接monkey指令，执行指令"""
    # 多个输入框,添加缺省值不需要加default值
    title = "monkey测试"
    filenames = ["包名",'throttle', 'event']
    filevalues = []
    filevalues = easygui.multenterbox("请填写测试参数", title, filenames,
                                      ['com.excelliance.dualaid', '500', '10000'])
    pkg_name = filevalues[0]
    throttle = int(filevalues[1])
    event = int(filevalues[2])
    # log保存地址
    path_log = GetPath.mem_back
    run_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    # 检测usb连接
    if 'device' in os.popen('adb devices').read().split():
        print('设备已连接，开始monkey测试')
        # 把monkey命令分为三个部分
        adb_monkey = 'shell monkey -p %s --throttle %s --ignore-crashes --ignore-timeouts' \
                     ' --ignore-security-exceptions -v %s' % (pkg_name, throttle, event)
        monkey_log = path_log + "\\" + run_time + "monkey.log"
        cmd_monkey = 'adb %s > %s' % (adb_monkey,monkey_log)
        os.popen(cmd_monkey)

        # logcat日志
        logcat_log = path_log + "\\" + run_time + "logcat.log"
        cmd_logcat = "adb logcat -v time > %s" % logcat_log
        os.popen(cmd_logcat)
    else:
        print('请连接设备')



if __name__ == "__main__":
    start_monkey()
    #mem_info.get_mem_info()
