from chapter_2_solver import round_trip_time, bytes_to_bits

transmission_rate = 9 * (10 ** 6)   # 9 megabits/sec
links = 3                           # The path includes 3 links
routers = 2                         # The path includes 2 routers
link_distance = 3000 * (10 ** 3)    # Each link is 3000 kilometers long
propagation_speed = 1.8 * (10 ** 8)  # 1.8 * 10^8 meters/sec

webpage_size = 17 * (10 ** 3)       # 17 kilobytes
images = 22                         # 22 embedded images
image_size = 240 * (10 ** 3)        # 240 kilobytes

# Question 1 - Round Trip Time
rtt = round_trip_time(links, link_distance, propagation_speed)
print(rtt)
