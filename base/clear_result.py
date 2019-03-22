import os
import shutil
from base.stop_log import stop_log

'''还未完成'''
def clean_reult(c_dir):
    # 清除测试数据
    BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    path = os.path.exists(BASE_PATH + c_dir)
    shutil.rmtree(path)


if __name__=='__main__':
    stop_log()
    choose = input('请选择清除的文件夹：1.全部;2.cpu_process;3.mem_process;'
                   '4.mem_back;5.mem_info;6.start;7.flow;8.monkey')
    if choose == 1:
        clean_reult('\\result')
    elif choose == 2:
        clean_reult('\\result\\cpu_process')
    elif choose ==3:
        clean_reult('\\result\\mem_process')
    elif choose ==4:
        clean_reult('\\result\\mem_back')
    elif choose ==5:
        clean_reult('\\result\\mem_info')
    elif choose ==6:
        clean_reult('\\result\\start')
    elif choose ==7:
        clean_reult('\\result\\flow')
    else:
        clean_reult('\\result\\monkey')