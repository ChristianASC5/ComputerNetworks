from typing import List, Dict


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
    - Total time for the first packet of a HTTP request to travel from a HTTP client to a HTTP server.
    """

    return rtt + (rtt / 2) + t_t + t_p


def request_to_router(req_server_time, t_t, t_p):
    """
    Calculate the time for the first packet of a HTTP request to travel from a HTTP client to the first router on the connection path.

    Parameters:
    - req_server_time: Total time for the first packet of a HTTP request to travel from a HTTP client to a HTTP server.
    - t_t: The transmission delay of a network device.
    - t_p: Propagation delay for data to travel over a single physical link.

    Returns:
    - Total time for the first packet of a HTTP request to travel from a HTTP client to the first router on the connection path.
    """

    return req_server_time + t_t + t_p


def request_to_response(req_to_router, t_t, t_p):
    """
    Calculate the time elapsed from the HTTP request being transmitted to HTTP client receiving the first response packet.

    Parameters:
    - req_to_router: Total time for the first packet of a HTTP request to travel from a HTTP client to the first router on the connect path.
    - t_t: The transmission delay of a network device.
    - t_p: Propagation delay for data to travel over a single physical link.

    Returns:
    - Total time elapsed from the HTTP request being transmitted to HTTP client receiving the first response packet.
    """

    return req_to_router + t_t + t_p
