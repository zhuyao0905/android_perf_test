import os
from base.config import Config,GetPath
import xlwt
import time

workbook = xlwt.Workbook()
style = xlwt.XFStyle()
path = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

def get_code(a, b):
    # 提取字符串
    p1 = a.split(b)
    if len(p1) > 1:
        p2 = p1[0].split()
        if len(p2) > 1:
            return p2[len(p2)-1]
    return ''

def get_cpu_info():
    '''获取cpu详情，每三秒读取一次cpu值'''
    i = 0
    # 判断应用进程是否存在
    try:
        content = os.popen("adb shell ps| findstr -e " + Config().get_config()['pck_name']).read()
        pid = content.split()[1]
    except IndexError as e:
        print('测试应用的进程不存在,正在开启应用···')
        # 如果不需要自动启动，可以把下面这行命令注释掉
        os.popen('adb shell am start -W ' + Config().get_config()['pck_name']
                 + '/' + Config().get_config()['activity'])
    # 抓取log
    os.popen('adb logcat -c')
    os.popen('adb logcat -v threadtime > ' + GetPath.cpu_info + '\\' + path + '.log')
    # 数据写入Excel
    worksheet = workbook.add_sheet('MySheet2')
    worksheet.write(0, 0, '次数')
    worksheet.write(0, 1, 'Total')
    worksheet.write(0, 2, 'user')
    worksheet.write(0, 3, 'kernel')
    worksheet.write(0, 4, 'iowait')
    worksheet.write(0, 5, 'irq')
    worksheet.write(0, 6, 'softirq')
    rt = runtime * 20
    while i < rt:
        i = i + 1
        j = 0
        worksheet.write(i, 0, i, style)
        process = (os.popen('adb shell dumpsys cpuinfo '+ Config().get_config()['pck_name'])).readlines()
       # print(process)
        output = process[-1]
        if output == '\n':
            output = process[-2]
        print(output)
        Total = output.split()[0]
        user = get_code(output, 'user')
        kernel = get_code(output, 'kernel')
        iowait = get_code(output, 'iowait')
        irq = get_code(output, ' irq')
        softirq = get_code(output, 'softirq')
        print(Total, user, kernel, iowait, irq, softirq)
        time.sleep(3)
        worksheet.write(i, 1, Total)
        worksheet.write(i, 2, user)
        worksheet.write(i, 3, kernel)
        worksheet.write(i, 4, iowait)
        worksheet.write(i, 5, irq)
        worksheet.write(i, 6, softirq)
        time.sleep(3)
        # 数据保存地址，以Excel表格保存
        workbook.save(GetPath.cpu_info + '\\'+  path + '.xls')

if __name__ == "__main__":
    runtime = int(input("请输入测试时间（min）:"))
    get_cpu_info()
