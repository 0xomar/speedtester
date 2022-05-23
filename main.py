import math
import speedtest

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

print("Performing download speed test...")
download_speed = wifi.download()


print("Performing upload speed test...")
upload_speed = wifi.upload()

print("Performing ping test...")
ping_result = wifi.results.ping


print(f"\nDownload speed:, {download_speed / 1024 / 1024:.2f} Mbps")


print(f"\nUpload speed:, {upload_speed / 1024 / 1024:.2f} Mbps")


print(f"\nPing result:, {ping_result:.2f} ms")
