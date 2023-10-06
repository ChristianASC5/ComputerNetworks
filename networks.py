from custom_exceptions import InsufficientDevicesException
from typing import List, Dict


def transmission_delay(packet_size: int, link_speed: int):
    return packet_size / link_speed


def propagation_delay(distance: int, propagation_speed: int):
    return distance / propagation_speed


def round_trip_time(devices: List[Dict['str', 'int']], links: List[Dict['str', 'int']]) -> int:
    if (devices < 2):
        raise InsufficientDevicesException("At least two devices are required.")
    
    client = devices[0]

    intermediary_devices = devices[1:-1]

    server = devices[-1]


    pass
