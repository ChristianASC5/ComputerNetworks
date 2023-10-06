from custom_exceptions import InsufficientValueException
from typing import List, Dict


def bytes_to_bits(bytes: int) -> int:
    """
    Converts bytes to bits.

    Parameters:
    - bytes (int): The number of bytes to be converted.

    Returns:
    - The value after unit conversion.
    """
    return bytes * 8


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


def round_trip_time(links, distance, propagation_speed):
    """
    Calculate round trip time to establish a TCP connection between a client and server. 
    This calculation assumes TCP connection requests/responses are small enough for their transmission delay to be ignored.

    Parameters:
    - links: Number of physical links between a client and server that data needs to travel over.
    - distance: Length of each physical link.
    - propagation_speed: Propagation delay for data to travel over a single physical link.

    Returns:
    - Total time to send a TCP request and recieve a TCP response.
    """

    return (links * 2) * propagation_delay(distance, propagation_speed)
