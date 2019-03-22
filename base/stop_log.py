import os

def stop_log():
    # 杀死adb所有进程
    adb_list=[]
    for i in os.popen('tasklist|findstr "adb.exe"').readlines():
        adb_list.append(i.split()[1])
    for log_pid in adb_list:
        print(log_pid)
        os.popen('taskkill /f /pid %s' % log_pid)

stop_log()