#!/usr/bin/python

file_list=[
	"prova.html"
	]

apps = [
	["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", 
	 "--headless", 
	 "--enable-crash-reporter"]#,
	#["C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe",
	 #"-headless",
	 #""]
	]

fuzz_output = "fuzz.html"

FuzzFactor = 250
num_tests = 1000

import math
import random
import string
import subprocess
import time
import datetime

for i in range(num_tests):
	file_choice = random.choice(file_list)
	app = random.choice(apps)
	
	buf = bytearray(open(file_choice, 'rb').read())
	
	# start Charlie Miller code
	numwrites = random.randrange(math.ceil((float(len(buf)) / FuzzFactor)))+1
	
	for j in range(numwrites):
		rbyte = random.randrange(256)
		rn = random.randrange(len(buf))
		buf[rn] = rbyte
		print(buf)
	# end Charlie Miller code
	
	open(fuzz_output, 'wb').write(buf)
	
	print('app: ',app,' file: ',file_choice)
	
	t1 = datetime.datetime.now()
	
	process = subprocess.Popen([app[0], app[1], app[2], fuzz_output])
	
	while process.poll() is None:
		time.sleep(1/1000)
	print('crashed: ', process.poll())
	t2 = datetime.datetime.now()
	tD = t2 - t1
	print('Temps: ',tD.microseconds)
	process.terminate()