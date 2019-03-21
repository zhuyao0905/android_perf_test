import re
import time
import easygui
from base.config import Config
import xlwt
import os

workbook = xlwt.Workbook()
style = xlwt.XFStyle()
path = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

def get_start_time(type):
    '''根据type的数值，选择进行back，home和冷启动的循环操作'''
    i = 0
    worksheet = workbook.add_sheet('MySheet3')
    worksheet.write(0, 0,'次数')
    worksheet.write(0, 1,'TotalTime')
    worksheet.write(0, 2,'ThisTime')
    worksheet.write(0, 3,'WaitTime')
    while i < runtime:
        '''获取启动时间'''
        time.sleep(2)
        i = i + 1
        worksheet.write(i, 0, i, style)
        content = os.popen('adb shell am start -W ' + Config().get_config()['pck_name']
                           + '/' + Config().get_config()['activity']).read()
        TotalTime = re.search(r'(TotalTime:)\s(\d+)', content).group(2)
        print('TotalTime:' + TotalTime)
        ThisTime = re.search(r'(ThisTime:)\s(\d+)', content).group(2)
        print('ThisTime:'+ThisTime)
        WaitTime = re.search(r'(WaitTime:)\s(\d+)', content).group(2)
        print('WaitTime:'+WaitTime)
        worksheet.write(i, 1, TotalTime)
        worksheet.write(i, 2, ThisTime)
        worksheet.write(i, 3, WaitTime)
        time.sleep(3)
        os.popen('adb shell input keyevent '+ type)
        if type == "0":
           os.popen('adb shell am force-stop ' + Config().get_config()['pck_name'])
        workbook.save( Config().get_config()['start_info'] + path + '.xlsx')


if __name__ == "__main__":
    type = input("输入要测项前面数字：4.back 3.home 0.冷启动")
    runtime = int(input('请输入需要循环的次数:'))
    if type == "4":
        get_start_time(type)
    elif type == "3":
        get_start_time(type)
    elif type == "0":
        get_start_time(type)
