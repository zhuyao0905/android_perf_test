import os
import re
import xlwt
import time
import datetime
from base.config import Config,GetPath

workbook = xlwt.Workbook()
style = xlwt.XFStyle()
style.num_format_str = 'h:mm:ss'
path = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

def get_cpu():
    j = 1
    i = 1
    processSum = 0
    processList = []
    worksheet = workbook.add_sheet('MySheet3')
    worksheet.write(0, 0, '时间')
    # 抓取log
    os.popen('adb logcat -c')
    os.popen('adb logcat -v threadtime > ' + GetPath.cpu_process + '\\'+  path + '.log')
    contents = os.popen("adb shell ps| findstr " + Config().get_config()['pck_name']).readlines()
    rt = runtime * 20
    while i < rt:
        j = 0
        worksheet.write(i, 0, datetime.datetime.now(), style)
        while j < len(contents):
            if contents[j] == '\n':
                j = j + 1
            else:
                ''''遍历应用所有的进程和pid'''
                pid = contents[j].split()[1]
                #proc = contents[j].split()[8]
                try:
                    proc = re.search('(com.+)\n', contents[j]).group(1)
                except AttributeError:
                    continue
                '''遍历所有进程的CPU'''
                b = os.popen('adb shell dumpsys cpuinfo |findstr ' + pid)
                c = b.read()
                d = re.search(r'([0-9]{0,1}[0-9]{0,1}[.][1-9]{0,1}\%|[0-9]{0,1}[0-9]{0,1}\%)\s\d{0,5}.', c)
                try:
                    cpu = d.group(1)
                except AttributeError:
                    cpu = None
                    pass
                print(proc + '的CPU：' + str(cpu))
                j = j + 1
                name = str(pid) + proc
                if name not in processList:
                    processSum = processSum + 1
                    worksheet.write(0, processSum, name)
                    processList.append(name)
                processIndex = processList.index(name)
                if processIndex != -1:
                    worksheet.write(i, processIndex + 1,cpu)
            workbook.save(GetPath.cpu_process+ '\\'+  path + '.xls')
        i = i + 1
        time.sleep(3)
    print('测试完毕。')

if __name__ == "__main__":
    runtime = int(input("请输入测试时间（分钟）:"))
    get_cpu()