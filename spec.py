import psutil

# Get CPU information
cpu_count = psutil.cpu_count()
cpu_freq = psutil.cpu_freq().current
cpu_percent = psutil.cpu_percent()

# Get memory information
total_memory = psutil.virtual_memory().total
available_memory = psutil.virtual_memory().available
used_memory = psutil.virtual_memory().used
memory_percent = psutil.virtual_memory().percent

# Get disk information
disk_usage = psutil.disk_usage('/')
total_disk_space = disk_usage.total
used_disk_space = disk_usage.used
free_disk_space = disk_usage.free
disk_percent = disk_usage.percent

# Print out system information
print(f"CPU count: {cpu_count}")
print(f"CPU frequency: {cpu_freq} MHz")
print(f"CPU usage: {cpu_percent}%")
print(f"Total memory: {total_memory} bytes")
print(f"Available memory: {available_memory} bytes")
print(f"Used memory: {used_memory} bytes")
print(f"Memory usage: {memory_percent}%")
print(f"Total disk space: {total_disk_space} bytes")
print(f"Used disk space: {used_disk_space} bytes")
print(f"Free disk space: {free_disk_space} bytes")
print(f"Disk usage: {disk_percent}%")
