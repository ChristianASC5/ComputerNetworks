from lib.chapter_2_solver import *
from lib.unit_conversions import bits

transmission_rate = 5 * (10 ** 6)    # 9 megabits/sec
num_links = 3                        # The path includes 3 links
num_routers = 2                      # The path includes 2 routers
link_distance = 1000 * (10 ** 3)     # Each link is 3000 kilometers long
propagation_speed = 1.9 * (10 ** 8)  # 1.8 * 10^8 meters/sec

webpage_size = 13 * (10 ** 3)        # 17 kilobytes
image_count = 11                          # 22 embedded images
image_size = 200 * (10 ** 3)         # 240 kilobytes

max_packet_size = 1 * (10 ** 3)     # 6 kilobytes


# Transmission Delay
t_transmission = transmission_delay(bits(max_packet_size), transmission_rate)

# Propagation Delay
t_propagation = propagation_delay(link_distance, propagation_speed)

# Question 1 - Round Trip Time
rtt = round_trip_time(num_links, t_propagation)
print(f"Answer 1 : {rtt}\n")

# Question 2a - Time for the first packet to arrive at the server
t_server = request_to_server(
    rtt, t_transmission, t_propagation
)
print(f"Answer 2a: {t_server}")

# Question 2b - Time for the first packet to arrive at the first router
t_first_router = request_to_router(t_server, t_transmission, t_propagation)
print(f"Answer 2b: {t_first_router}")

# Question 2c - Time for the first response packet to arrive at the HTTP client
t_response = request_to_response(t_first_router, t_transmission, t_propagation)
print(f"Answer 2c: {t_response}")

# Question 2d - Time for the client to recieve the whole webpage
webpage_packets = webpage_size / max_packet_size

t_webpage = request_to_webpage(t_response, webpage_packets, t_transmission)
print(f"Answer 2d: {t_webpage}")


# Question 3 - Time for the client to receive the first embedded image
image_packets = image_size // max_packet_size

small_packet_size = image_size % max_packet_size
t_small_packet = transmission_delay(small_packet_size, transmission_rate)

t_image = request_to_image(t_webpage, image_packets,
                           rtt, t_transmission, t_small_packet)
print(f"\nAnswer  3: {t_image}")

# Question 4 - Time for the client to receive the full webpage with all images.
t_fullpage = time_fullpage(t_webpage, rtt, image_count,
                           image_packets, t_transmission)
print(f"\nAnswer  4: {t_fullpage}")
