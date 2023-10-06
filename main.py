from lib.chapter_2_solver import *
from lib.unit_conversions import bits

transmission_rate = 5 * (10 ** 6)    # 9 megabits/sec
links = 3                            # The path includes 3 links
routers = 2                          # The path includes 2 routers
link_distance = 1000 * (10 ** 3)     # Each link is 3000 kilometers long
propagation_speed = 1.9 * (10 ** 8)  # 1.8 * 10^8 meters/sec

webpage_size = 17 * (10 ** 3)        # 17 kilobytes
images = 22                          # 22 embedded images
image_size = 240 * (10 ** 3)         # 240 kilobytes

max_packet_size = 1 * (10 ** 3)     # 6 kilobytes


# Transmission Delay
t_t = transmission_delay(bits(max_packet_size), transmission_rate)

# Propagation Delay
t_p = propagation_delay(link_distance, propagation_speed)

# Question 1 - Round Trip Time
rtt = round_trip_time(links, t_p)
print(f"Answer 1 : {rtt}")

# Question 2a - Time for the first packet to arrive at the server
req_to_server = request_to_server(
    rtt, t_t, t_p
)
print(f"Answer 2a: {req_to_server}")

# Question 2b - Time for the first packet to arrive at the first router
req_to_router = request_to_router(req_to_server, t_t, t_p)
print(f"Answer 2b: {req_to_router}")

# Question 2c - Time for the first response packet to arrive at the HTTP client
req_to_response = request_to_response(req_to_router, t_t, t_p)
print(f"Answer 2c: {req_to_router}")
