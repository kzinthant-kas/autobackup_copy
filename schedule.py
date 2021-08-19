import time
import subprocess

seconds_to_wait = 60

while(True):
  subprocess.call(['sh', './copy.sh'])
  time.sleep(60)


    
  
