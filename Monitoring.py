import psutil
import time
import datetime


while True:
	cpu_pre = psutil.cpu_percent()
	cpu_cores = psutil.cpu_count(logical=True)
	cpu_freq = psutil.cpu_freq().current
	sys_load = psutil.getloadavg()
	ram = psutil.virtual_memory().percent
	mem_pre_used = psutil.disk_usage('/').percent
	up_time_sec = datetime.datetime.now() - datetime.datetime.fromtimestamp(psutil.boot_time())
	up_time = str(up_time_sec).split('.')[0]
	b_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
	print(f'CPU%: {cpu_pre}, Cores: {cpu_cores}, Freq: {cpu_freq}, sys load: {sys_load}')
	print(f'mem: {ram}%, disk% used: {mem_pre_used}%, BOOT TIME: {b_time}, Up_time: {up_time}')
	time.sleep(1)
