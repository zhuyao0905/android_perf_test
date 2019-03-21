# /usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import time
from base.config import Config,GetPath
import xlwt

workbook = xlwt.Workbook()
style = xlwt.XFStyle()
path = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

def get_code(a, b):
    # 提取字符串
    p1 = a.split(b)
    if len(p1) > 1:
        p2 = p1[1].split(" +")
        if len(p2) > 1:
            return p2[0]
    return ''

def get_mem_info():
    '''获取内存详情，每三秒读取一次内存值'''
    i = 0
    # 抓取log
    os.popen('adb logcat -c')
    os.popen('adb logcat -v threadtime > ' + GetPath.mem_info + '\\'+ path + '.log')
    # 数据写入Excel
    worksheet = workbook.add_sheet('MySheet4')
    worksheet.write(0, 0, '次数')
    worksheet.write(0, 1, 'Total')
    worksheet.write(0, 2, 'Java Heap')
    worksheet.write(0, 3, 'Native Heap')
    worksheet.write(0, 4, 'Stack')
    worksheet.write(0, 5, 'Graphics')
    worksheet.write(0, 6, 'Prinvate Other')
    worksheet.write(0, 7, 'System')
    worksheet.write(0, 8, 'TOTAL SWAP PSS')
    rt = runtime * 20
    while i < rt:
        i = i + 1
        worksheet.write(i, 0, i, style)
        out = os.popen("adb shell dumpsys meminfo " + Config().get_config()['pck_name']).read()
        print(out)
        # 读取内存数值
        JavaHeap = get_code(out, 'Java Heap:')
        NativeHeap = get_code(out, "Native Heap:")
        Stack = get_code(out, "Stack:")
        Graphics = get_code(out, "Graphics:")
        PrinvateOther = get_code(out, "Private Other:")
        System = get_code(out, "System:")
        Total = get_code(out, "TOTAL:")
        TotalSwapPss = get_code(out, "TOTAL SWAP PSS:")
        print('TOTAL:' + Total)
        print('Java Heap:' + JavaHeap)
        print("Native Heap:"+ NativeHeap)
        print("Stack:"+ Stack)
        print("Graphics:" + Graphics)
        print("Private Other:" + PrinvateOther)
        print("System:" + System)
        print("TOTAL SWAP PSS:" + TotalSwapPss)
        worksheet.write(i,1,Total)
        worksheet.write(i,2,JavaHeap)
        worksheet.write(i,3,NativeHeap)
        worksheet.write(i,4,Stack)
        worksheet.write(i,5,Graphics)
        worksheet.write(i,6,PrinvateOther)
        worksheet.write(i,7,System)
        worksheet.write(i,8, TotalSwapPss)
        time.sleep(3)

        # 数据保存地址，以Excel表格保存
        workbook.save(GetPath.mem_info + '\\' + path +'.xls')

if __name__ == "__main__":
    runtime = int(input("请输入测试时间（min）:"))
    get_mem_info()
