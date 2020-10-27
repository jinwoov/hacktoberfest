import time
from datetime import datetime as dt
hosts_path=r"etc/hosts"

redirect = "127.0.0.1"
website_list=["www.facebook.com", " facebook.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16):
        print("Working hours")
        with open(hosts_temp, 'r+') as file:
        	content=file.read()
        	for website in website_list:
        		if website in content:
        			pass
        		else:
        			file.write(redirect+" "+ website+"\n")

            
        
    else:
    	with open(hosts_temp,'r+') as file:
    		content = file.readlines()  # here content becomes a list
    		file.seek(0)
    		for line in content:
    			if not any(website in line for website in website_list):
    				file.write(line)
    		file.truncate()
    	print("Fun Hours woho")
    time.sleep(5)