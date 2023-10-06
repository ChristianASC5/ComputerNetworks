def transmission_delay(packet_size, link_speed):
    """
    Calculate transmission delay of a network device.

    Parameters:
    - packet_size: Size of a single packet in bits to be transmitted.
    - link_speed: The rate at which a network device can transmit data in bits per second.

    Returns:
    - The calculated transmission delay.
    """

    return packet_size / link_speed


def propagation_delay(distance, propagation_speed):
    """
    Calculate propagation delay of physical network link.

    Parameters:
    - distance: Distance of the physical link.
    - propagation_speed: Propagation speed at which data travels over the physical link.

    Returns:
    - The calculated propagation delay.
    """

    return distance / propagation_speed


def round_trip_time(links, t_p):
    """
    Calculate round trip time to establish a TCP connection between a client and server. 
    This calculation assumes TCP connection requests/responses are small enough for their transmission delay to be ignored.

    Parameters:
    - links: Number of physical links between a client and server that data needs to travel over.
    - t_p: Propagation delay for data to travel over a single physical link.

    Returns:
    - Total time to send a TCP request and recieve a TCP response.
    """

    return (links * 2) * t_p


def request_to_server(rtt, t_t, t_p):
    """
    Calculate the time for the first packet of a HTTP request to travel from a HTTP client to a HTTP server.

    Parameters:
    - rtt: Total round trip time to send a TCP request and recieve a TCP response.
    - t_t: The transmission delay of a network device.
    - t_p: Propagation delay for data to travel over a single physical link.

    Returns:
    - Time for the first packet of a HTTP request to travel from a HTTP client to a HTTP server.
    """

    return rtt + (rtt / 2) + t_t + t_p


def request_to_router(req_server_time, t_t, t_p):
    """
    Calculate the time for the first packet of a HTTP request to travel from a HTTP client to the first router on the connection path.

    Parameters:
    - req_server_time: Time for the first packet of a HTTP request to travel from a HTTP client to a HTTP server.
    - t_t: The transmission delay of a network device.
    - t_p: Propagation delay for data to travel over a single physical link.

    Returns:
    - Time for the first packet of a HTTP request to travel from a HTTP client to the first router on the connection path.
    """

    return req_server_time + t_t + t_p


def request_to_response(req_to_router, t_t, t_p):
    """
    Calculate the time elapsed from the HTTP request being transmitted to HTTP client receiving the first response packet.

    Parameters:
    - req_to_router: Time for the first packet of a HTTP request to travel from a HTTP client to the first router on the connect path.
    - t_t: The transmission delay of a network device.
    - t_p: Propagation delay for data to travel over a single physical link.

    Returns:
    - Time elapsed from the HTTP request being transmitted to HTTP client receiving the first response packet.
    """

    return req_to_router + t_t + t_p


def request_to_webpage(req_to_resp, packet_count, t_t):
    """
    Calculate the time elapsed from the HTTP request being transmitted to HTTP client receiving the whole webpage.

    Parameters:
    - req_to_resp: Time elapsed from the HTTP request being transmitted to HTTP client receiving the first response packet.
    - packet_count: Number of packets to be recieved by the HTTP client.
    - t_t: The transmission delay of a network device.

    Returns:
    - Time elapsed from the HTTP request being transmitted to HTTP client receiving the whole webpage.
    """

    return req_to_resp + (packet_count-1) * t_t


def request_to_image(time_webpage, packet_count, rtt, t_t, small_packet_delay):
    """
    Calculate the time elapsed from the HTTP request being transmitted to HTTP client receiving the first image.

    Parameters:
    - time_webpage: Time elapsed from the HTTP request being transmitted to HTTP client receiving the whole webpage.
    - packet_count: Number of image packets to be received by the HTTP client.
    - rtt: Time to send a TCP request and recieve a TCP response.
    - t_t: The transmission delay of a network device.
    - small_packet_delay: Transmission delay of a packet that isn't the maximum packet size.

    Returns:
    - Time elapsed from the HTTP request being transmitted to HTTP client receiving the first image.
    """

    return time_webpage + (2 * rtt) + ((2 + packet_count) * t_t) + small_packet_delay


def time_fullpage(time_webpage, img_count, packet_count, rtt, t_t, small_packet_delay, multiple_connections=False, persistant=False):
    """
    Calculate the time elapsed from the HTTP request being transmitted to HTTP client receiving the full webpage with all images.

    Parameters:
    - time_webpage: Time elapsed from the HTTP request being transmitted to HTTP client receiving the whole webpage.
    - img_count: Number of images.
    - packet_count: Number of image packets to be received by the HTTP client.
    - rtt: Time to send a TCP request and recieve a TCP response.
    - t_t: The transmission delay of a network device.
    - small_packet_delay: Transmission delay of a packet that isn't the maximum packet size.
    - multiple_connections: Indicates whether or not multiple TCP connections are in use.
    - persistant: Indicates whether or not HTTP is persistant.

    Returns:
    - time elapsed from the HTTP request being transmitted to HTTP client receiving the full webpage with all images.
    """

    if multiple_connections:
        result_time = time_webpage + rtt + \
            ((2 + packet_count) * t_t) + ((img_count - 1)
                                          * t_t * packet_count) + small_packet_delay

        if persistant:
            return result_time

        return result_time + rtt
    else:
        return time_webpage + (img_count * rtt) + ((2 + packet_count) * t_t) * img_count + small_packet_delay
