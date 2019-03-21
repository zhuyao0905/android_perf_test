import os
import re
import xlwt
import time
from base.config import Config

workbook = xlwt.Workbook()
style = xlwt.XFStyle()
path = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

def get_mem():
    '''查询多个进程的内存值'''
    j = 1
    i = 1
    processSum=0
    processList=[]
    worksheet = workbook.add_sheet('MySheet2')
    worksheet.write(0, 0, '次数')
    rt = runtime * 20
    while i < rt:
        '''每三秒获取一次内存值'''
        #print(contents)
        j = 0
        worksheet.write(i, 0, i, style)
        contents = os.popen("adb shell ps| findstr " + Config().get_config()['pck_name']).readlines()
        while j < len(contents):
            if contents[j] == '\n':
                j = j + 1
            else:
                ''''遍历应用所有的进程和pid'''
                pid = contents[j].split()[1]
                #proc =contents[j].split()[8]
                try:
                    proc = re.search('(com.+)\n', contents[j]).group(1)
                except AttributeError:
                    continue
                '''Get all processes's memV'''
                b = os.popen('adb shell dumpsys meminfo ' + pid)
                c = b.read()
                d = re.search(r'(TOTAL)\s*(\d{0,8})', c)
                try:
                    mem = round(int(d.group(2)) / 1024, 2)
                except AttributeError:
                    mem = 0
                    pass
                print(proc + 'memValue：' + str(mem))
                j = j + 1
                name = str(pid)+proc
                if name not in processList:
                    processSum = processSum+1
                    worksheet.write(0, processSum, name)
                    processList.append(name)
                processIndex = processList.index(name)
                if processIndex != -1:
                   worksheet.write(i, processIndex+1, mem)
            workbook.save(Config().get_config()['mem_process']+ path + '.xlsx')
        i = i + 1
        time.sleep(3)
    print('The test is finished!')

if __name__ == "__main__":
    os.popen('adb logcat -c')
    os.popen('adb logcat -v threadtime >' + Config().get_config()['mem_process'] + path + '.log')
    runtime = int(input("Please enter the test time（min）:"))
    get_mem()
