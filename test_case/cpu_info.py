import os
from base.config import Config,GetPath
import xlwt
import time

workbook = xlwt.Workbook()
style = xlwt.XFStyle()
path = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

def get_cpu_info():
    '''获取内存详情，每三秒读取一次内存值'''
    i = 0
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
        worksheet.write(i, 0, i, style)
        process = (os.popen('adb shell dumpsys cpuinfo '+ Config().get_config()['pck_name'])).readlines()
        output = process[-1]
        print(output)
        Total = output.split()[0]
        user = output.split()[2]
        kernel = output.split()[5]
        iowait = output.split()[8]
        irq = output.split()[11]
        softirq = output.split()[14]
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
