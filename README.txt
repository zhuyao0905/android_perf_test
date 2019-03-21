## 性能测试
* Python3
* 性能统计信息：cpu、mem、battery、flow、start


# 内存测试场景
第一种：多个进程的内存值，mem_processs.py
第二种：主进程的具体内存值，mem_info.py
第三种：back再进的内存值，mem_back.py

# cpu测试场景
第一种：多个进程的cpu值，cpu_processs.py
第二种：主进程的具体CPU值，cpu_info.py

# 启动时间测试场景
冷启动，热启动，暖启动


# monkey测试
* 只需要运行monkey.py,输入测试的参数
* 停止monkey，运行stop_monkey.py


# 只需要修改配置文件config.yaml中的数据即可
---
dev: 721QADRG345FC
pck_name: com.excelliance.dualaid
activity: com.excelliance.kxqp.ui.HelloActivity
# 性能数据保存地址,python目录要用/
mem_info: "D:/perf_test/result/perf_info/mem/"
cpu_info: "D:/perf_test/result/perf_info/cpu/"
start_info: "D:/perf_test/result/perf_info/start/"
flow_info: "D:/perf_test/result/perf_info/flow/"
monkey_info: "D:/perf_test/result/monkey/"
