#!/usr/bin/env python3

stop_split = "0,"
while(i < len(s) and i+1 < len(s)):
    if(ord(s[i]) > ord(s[i+1])):
        stop_split = stop_split + str(i+1)
        if(i != (len(s)-1)):
            stop_split = stop_split + ","
    i=i+1
stop_split = stop_split + str(len(s))
i=1
start = 0
length = 0
split = stop_split.split(",")
while(i < len(split)):
    if((int(split[i]) - int(split[i-1])) > length):
        start = int(split[i-1])
        length = int(split[i]) - int(split[i-1])
    i=i+1

print(f"Longest substring in alphabetical order is: {s[start:start+length]}")
