import os
import re
import time
import xlwt
from base.config import Config,GetPath

workbook = xlwt.Workbook()
style = xlwt.XFStyle()
path = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

def get_tcp():
    '''测试流量，获取每一秒的流量'''
    # 抓取log
    os.popen('adb logcat -c')
    os.popen('adb logcat -v threadtime > ' + GetPath.flow + '\\' + path + '.log')
    '''判断应用进程是否存在，获取应用pid'''
    try:
        content = os.popen("adb shell ps| findstr -e " + Config().get_config()['pck_name']).read()
        pid = content.split()[1]
    except IndexError as e:
        print('测试应用的进程不存在,正在开启应用···')
        # 如果不需要自动启动，可以把下面这行命令注释掉
        os.popen('adb shell am start -W ' + Config().get_config()['pck_name']
                 + '/' + Config().get_config()['activity'])

    '''数据写入Excel'''
    i = 0
    worksheet = workbook.add_sheet('MySheet')
    worksheet.write(0, 0, '次数')
    worksheet.write(0, 1, '上传流量')
    worksheet.write(0, 2, '下载流量')
    runtime = int(input("请输入测试时间（分钟）:"))
    print('次数', '上行', '下载')
    rt = runtime*60
    while i < rt:
        i = i + 1
        b = os.popen("adb shell cat /proc/" + pid + "/status")
        c = b.read()
        uid = re.search(r'(Uid).\s+(\d{0,5})', c).group(2)
        # 分别获得上行流量和下行流量
        snd = os.popen("adb shell cat /proc/uid_stat/" + uid + "/tcp_snd").read().strip()
        snd_value = int(snd)//1024
        rcv =os.popen("adb shell cat /proc/uid_stat/" + uid + "/tcp_rcv").read().strip()
        rcv_value = int(rcv)//1024
        time.sleep(1)
        print(i, snd_value, rcv_value)
        worksheet.write(i, 0, i,style)
        worksheet.write(i, 1, snd_value )
        worksheet.write(i, 2,rcv_value)
        # 数据保存地址，以Excel表格保存
        workbook.save(GetPath.flow + '\\' + path + '.xls')
    print('测试完毕。')

if __name__ == "__main__":
    get_tcp()

