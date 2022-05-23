#import math
import speedtest
from contextlib import redirect_stdout
from time import time, sleep
from datetime import datetime

#a function to convert bits per second to mega bits per second
#def bytes_to_mb(size_in_bytes):
#    i = int(math.floor(math.log(size_in_bytes,1024)))
#    power = math.pow(1024, i)
#    size = round(size_in_bytes / power, 2)
#    return f"{size} Mbps"


wifi = speedtest.Speedtest() # object that can be used for testing download and upload
print("Loading server list...")
wifi.get_servers() # get list of servers to test from 
print("Choosing best server...")
best_server = wifi.get_best_server() # get best server
print(f"Found the best sever at: {best_server['host']} located in {best_server['country']}")

print("\nPerforming download speed test...")
download_speed = wifi.download() # a function to get the download speed


print("Performing upload speed test...")
upload_speed = wifi.upload() # a function to get the upload speed

print("Performing ping test...")
ping_result = wifi.results.ping # to get the ping results 


# datetime object containing current date and time
dt_now = datetime.now()  # using now function to get date and time now
dt_string = dt_now.strftime("%d/%m/%Y %H:%M:%S") # for formatting date and time 

print(f"\nDate and Time now: {dt_string}") # printing Current Date and Time

print(f"\nDownload speed: {download_speed / 1024 / 1024:.2f} Mbps") # divid result by 1024 twice to get mega bit per second


print(f"\nUpload speed: {upload_speed / 1024 / 1024:.2f} Mbps") # divid result by 1024 twice to get mega bit per second


print(f"\nPing result: {ping_result:.2f} ms") # have the .2 floor to ONLY two decimals at the .


while True:
    sleep(60 - time() % 60) #  sleep(60 - time() % 60)
    with open('out.txt', 'a') as f:
        upload_speed = wifi.upload() # a function to get the upload speed
        download_speed = wifi.download() # a function to get the download speed
        dt_now = datetime.now()  # using now function to get date and time now
        dt_string = dt_now.strftime("%d/%m/%Y %H:%M:%S") # for formatting date and time
        with redirect_stdout(f):
	        print(f"\nDate and Time: {dt_string} | Download speed: {download_speed / 1024 / 1024:.2f} Mbps | Upload speed: {upload_speed / 1024 / 1024:.2f} Mbps") # divid result by 1024 twice to get mega bit per second
