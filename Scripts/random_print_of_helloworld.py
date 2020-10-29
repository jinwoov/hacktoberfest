# Aim: print each letter of 'hello world' in order and in random points in time
# How: printing letter based on whether the ascii code of each letter appears in the milliseconds of the current time

# get the characters of the phrase in ascii code and put them in a list
helloworld = 'hello world'
in_ascii = []
for i in helloworld: in_ascii.append(ord(i))
#print(in_ascii)
#[104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100]

import datetime
import time

# from now + 1 minute
endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
for i in in_ascii:
    while True:
        milliseconds = time.time()*1000.0
        milliseconds_str = str(milliseconds)
        if str(i) in milliseconds_str: 
            print(chr(i) ) # print the character of the ascii code
            break # if letter printed, succceded, break 
