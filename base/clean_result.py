import os
from base.stop_log import stop_log

'''还未完成'''
def clean_result(c_dir):
    # 清除测试数据
    BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    path = os.path.join(BASE_PATH + c_dir)
    for i in os.listdir(path):
        path_file = os.path.join(path,i)
        print(path_file)
        if os.path.isfile(path_file):
            os.remove(path_file)
            print('文件删除成功！')
        else:
            clean_result(path_file)

if __name__=='__main__':
    stop_log()
    choose = int(input('请选择清除的文件夹：2.cpu_process;3.cpu_info;4.mem_process;'
                   '5.mem_back;6.mem_info;7.start;8.flow;9.monkey'))

    if choose == 2:
        clean_result('\\result\\cpu_process')
    elif choose ==3:
        clean_result('\\result\\cpu_info')
    elif choose == 4:
        clean_result('\\result\\mem_process')
    elif choose ==5:
        clean_result('\\result\\mem_back')
    elif choose ==6:
        clean_result('\\result\\mem_info')
    elif choose ==7:
        clean_result('\\result\\start')
    elif choose ==8:
        clean_result('\\result\\flow')
    elif choose == 9:
        clean_result('\\result\\monkey')