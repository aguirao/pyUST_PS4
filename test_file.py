#!/usr/bin/python

chosen_file_name="c:\\usr\\dev\\pyWorkspace\\pyUST_PS4\\f2.html.slow.0.t0023s.it0012.html"

selected_app = "C:\\PROGRA~2\\Google\\Chrome\\Application\\chrome.exe --headless --enable-crash-reporter"

import math
import random
import string
import subprocess
import time
import datetime

t1 = datetime.datetime.now()
process = subprocess.Popen(selected_app+" "+chosen_file_name)
while process.poll() is None:
	time.sleep(1/1000)		
t2 = datetime.datetime.now()
	
total_seconds = round((t2-t1).total_seconds(),3)
return_status = process.poll()
	
print("Temps: "+str(total_seconds)+"s; Return: "+str(return_status));
	
process.terminate()