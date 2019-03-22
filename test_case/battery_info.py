import os
from base.config import Config

# 未完成
class BatteryTest(object):

    # 清空手机耗电记录
    def reset_batteryinfo(self):
        # os.popen('adb shell dumpsys batterystats --enable full-wake-history')
        # time.sleep(1)
        os.popen('adb shell dumpsys batterystats --reset')

    # 检查usb连接状态
    def check_usb_status(self):
        data = os.popen('adb shell dumpsys battery').readlines()
        for i in data:
            if 'USB powered' in i:
                # print(i.split()[bad_path])
                return i.split()[2]

    # 设置usb连接为连接不充电状态
    def set_usb_status(self):
        os.popen('adb shell dumpsys battery set usb 0')
        if self.check_usb_status() != 'false':
            print('设置usb不充电状态失败')

    # 恢复手机默认usb连接状态
    def reset_usb_status(self):
        os.popen('adb shell dumpsys battery reset')
        if self.check_usb_status() != 'true':
            print('恢复usb充电状态失败')

    def get_app_uid(self):
        """根据app包名获取其uid号"""
        content = os.popen('adb shell pm dump ' + Config().get_config()['pck_name'] + ' | findstr "u0a"').read()
        uid = content.split()[-1].replace(':', '')
        print('%s的uid为：%s' % (Config().get_config()['pck_name'], uid))
        return uid

    # 获取设置usb连接状态和恢复usb默认连接状态期间的应用耗电量数据
    def get_batteryinfo(self):
        uid = BatteryTest.get_app_uid()
        content = os.popen('adb shell dumpsys batterystats|findstr "Uid"|findstr ' + uid).readlines()
        # android8.0
        # batteryinfo = (str(re.findall('(?<=[(])[^()]+\.[^()]+(?=[)])', content)).replace('[', '')).replace(']', '')
        for i in content[:int(len(content) / 2)]:
            batteryinfo = i.replace('Uid ' + uid + ': ', '').strip()
            print('消耗电量%0.2f' % float(batteryinfo))
            return round(float(batteryinfo), 2)


if __name__=='__main__':
    battery = BatteryTest()
