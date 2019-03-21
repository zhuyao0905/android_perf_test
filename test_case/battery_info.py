# coding=utf-8
import time
import os
import re
from base.config import Config

class App:
    def __init__(self, pckName, firstActivity):
        self.pckName = pckName
        self.firstActivity = firstActivity
        print('测试环境准备')

    def start_app(self):
        print('启动待测应用')
        os.popen("adb shell am start " + Config().get_config()['pck_name']
                           + '/' + Config().get_config()['activity'])

    def get_uid(self):
        content = os.popen("adb shell ps| findstr " + Config().get_config()['pck_name']).read()
        UID = content.split()[0].replace('_', '')
        return UID

    def reset_battery(self):
        print('清除手机电量信息')
        os.popen("adb shell dumpsys batterystats --reset")

    def set_usb(self):
        print('开始电量测试，请进行相关操作')
        os.popen("adb shell dumpsys battery unplug")
        os.popen("adb shell dumpsys battery set status 1")

    def rec_usb(self):
        print('测试结束')
        os.popen("adb shell dumpsys batterystats set status 2")
        os.popen("adb shell dumpsys battery reset")

    def get_batteryinfo(self):
        content = os.popen("adb shell dumpsys batterystats|findstr " + self.get_uid()).read()
        a = re.search(r'(Uid.+)\(\s(.+)\).+', content)
        try:
            batteryinfo = a.group(2)
        except AttributeError:
            batteryinfo = "无数据"
            print("无数据")
        return batteryinfo
        print("获取测试数据")

    def stop_app(self):
        print('退出被测应用')
        os.popen("adb shell am force-stop " + self.pckName)


class Go(App):
    def __init__(self, app):
        self.app = app
        self.file = open("d:/BatteryResult.xlsx", "a")

    def run(self):
        time.sleep(2)
        self.app.start_app()
        time.sleep(3)
        self.app.get_uid()
        time.sleep(2)
        self.app.reset_battery()
        time.sleep(2)
        self.app.set_usb()
        time.sleep(60)
        self.app.rec_usb()
        time.sleep(2)
        self.app.get_batteryinfo()
        time.sleep(2)
        self.file.write(self.app.get_batteryinfo() + '\n')
        time.sleep(2)
        self.app.stop_app()
        time.sleep(1)
        self.file.close()


if __name__ == "__main__":
    Go(app).run()