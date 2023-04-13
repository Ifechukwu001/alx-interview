#!/usr/bin/python3
"""Read stdin and compute metrics.

"""
import sys
import re
import signal


breakout = False
iteration = 0
total_size = 0
status_codes = {}
sample = r'\d+\.\d+\.\d+\.\d+ - \[\d{4}-\d{2}-\d{2} (?:\d{2}:){2}\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (?P<code>\d{3}) (?P<size>\d+)'


def sigint_handler(signum, frame):
    """SIGINT handler

    Args:
        signum: Signal number.
        frame: ?
    """
    global breakout
    print_details()
    breakout = True

signal.signal(signal.SIGINT, sigint_handler)


def print_details():
    """Prints the needed details on screen

    """
    print("File size: {}".format(total_size))
    for key in sorted(status_codes.keys()):
        print("{}: {}".format(key, status_codes[key]))



for line in sys.stdin:
    data = re.fullmatch(sample, line.rstrip())
    if data:
        data = data.groupdict()
        total_size += int(data.get("size"))
        num = status_codes.get(data.get("code"))
        if num:
            status_codes[data.get("code")] = num + 1
        else:
            status_codes[data.get("code")] = 1
    iteration += 1
    if iteration and iteration % 10 == 0:
        print_details()
    if breakout:
        print_details()
