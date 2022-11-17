from selenium import webdriver
import psutil
import time
import numpy


game_url = int(input("digite 1 para godot, digite 2 para unity "))
url = ""
if game_url == 1: 
	url = "https://srpantoja.itch.io/mortos-vivos-quixada-godot"
if game_url == 2:
	url = "https://srpantoja.itch.io/mortos-vivos-quixada-unity"

print(url)
browser = webdriver.Firefox()
browser.get(url)

manager = True
cpu_arr = []
ram_arr = []
while manager:
	cpu_arr.append(psutil.cpu_percent())
	ram_arr.append(psutil.virtual_memory().percent)
	print(f"\rCPU usage: " + str(psutil.cpu_percent())+"%           ", end="")
	print(f"RAM usage: " + str(psutil.virtual_memory().percent)+"% ", end="\r")
	time.sleep(0.5)
	try:
		if len(browser.current_url) > 0:
			continue
	except:
		manager = False


cpu_min = 10000
cpu_max = 0
ram_min = 10000
ram_max = 0
sum_cpu = 0
sum_ram = 0

for cpu in cpu_arr:
	if(cpu >= cpu_max):
		cpu_max = cpu
	if(cpu <= cpu_min):
		cpu_min = cpu
	sum_cpu = cpu + sum_cpu
		
for ram in ram_arr:
	if(ram >= ram_max):
		ram_max = ram
	if(ram <= ram_min):
		ram_min = ram
	sum_ram = ram + sum_ram
	

media_cpu = sum_cpu/len(cpu_arr)
media_ram = sum_ram/len(ram_arr)

print("media cpu: " + str(media_cpu) + " menor valor cpu: " + str(cpu_min) + " maior valor cpu: " + str(cpu_max))
print("media ram: " + str(media_ram) + " menor valor ram: " + str(ram_min) + " maior valor ram: " + str(ram_max))


