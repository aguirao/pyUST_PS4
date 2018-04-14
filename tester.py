#!/usr/bin/python

file_list=[
	"c:\\usr\\dev\\pyWorkspace\\pyUST_PS4\\f1.html",
	"c:\\usr\\dev\\pyWorkspace\\pyUST_PS4\\f2.html"
	]

apps = [
	"C:\\PROGRA~2\\Google\\Chrome\\Application\\chrome.exe --headless --enable-crash-reporter"#,
	#"C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe -headless"
	]

temp_file_name = "c:\\usr\\dev\\pyWorkspace\\pyUST_PS4\\temp.html"

fuzz_factor = 250
num_tests = 10000

import math
import random
import string
import subprocess
import time
import datetime
import shlex

errors = 0

t0 = datetime.datetime.now()

for i in range(num_tests):
	chosen_file_name = random.choice(file_list)
	selected_app = random.choice(apps)
	
	buf = bytearray(open(chosen_file_name, 'rb').read())
	
	# start Charlie Miller code: 
	# * https://youtu.be/Xnwodi2CBws 
	# * https://youtu.be/lK5fgCvS2N4
	numwrites = random.randrange(math.ceil((float(len(buf)) / fuzz_factor)))+1
	
	for j in range(numwrites):
		rbyte = random.randrange(256)
		rn = random.randrange(len(buf))
		buf[rn] = rbyte
	# end Charlie Miller code
	
	open(temp_file_name, 'wb').write(buf)
	
	t1 = datetime.datetime.now()
	
	process = subprocess.Popen(selected_app+" "+temp_file_name)
	
	while process.poll() is None:
		time.sleep(1/1000)
	t2 = datetime.datetime.now()
	tD = t2 - t1
	return_status = process.poll()
	total_seconds = round(tD.total_seconds(),3)
	if (return_status != 0 or total_seconds > 10):
		errors = errors + 1
		buf = bytearray(open(chosen_file_name, 'rb').read())
		error_file_name = chosen_file_name+"."+str(return_status)+"."+str(round(total_seconds))+"s.html"
		open(error_file_name, 'wb').write(buf)
		print('Crashed: '+str(return_status)+'. Temps: '+str(total_seconds)+'s '+error_file_name)
	t = datetime.datetime.now()
	print("Iteracions: "+str(i)+"; errors: "+str(errors)+"; temps: "+str(round((t-t0).total_seconds()/60))+"min");
	process.terminate()