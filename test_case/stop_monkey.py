import os

def stop_monkey():
    '''查找monkey的pid并杀死进程'''
    monkey_process = os.popen('adb shell ps |findstr monkey').readlines()
    # shell        21210 19696 3700220  83372 futex_wait_queue_me 79c7c27530 S com.android.commands.monkey
    for monkey_pid in monkey_process:
        if 'monkey' in monkey_pid:
            os.popen('adb shell kill %s' % monkey_pid.split()[1])
            print('monkey已停止')
        else:
            print('当前没有monkey进程')

if __name__ == "__main__":
    stop_monkey()

