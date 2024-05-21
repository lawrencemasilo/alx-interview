#!/usr/bin/python3
"""
log parsing algorithm
"""
import sys
import re
import signal


total_file_size = 0
status_code_count = {
        200: 0,
        301: 0,
        400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def print_statistics():
    """
    printing the status codes
    """
    print("File size:", total_file_size)
    for status_code in sorted(status_code_count.keys()):
        if status_code_count[status_code] > 0:
            print(f"{status_code}: {status_code_count[status_code]}")


def signal_handler(sig, frame):
    """
    handles the signals
    """
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line_number, line in enumerate(sys.stdin, start=1):
    line = line.strip()

    string = re.compile(
        r"""^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
            \s+-\s+\[([^]]+)\]
            \s+"GET\s+/projects/260\s+HTTP/1\.1"
            \s+(\d{3})
            \s+(\d+)$""",
        re.VERBOSE
    )
    match = string.match(line)
    if not match:
        continue

    ip_address, date, status_code_str, file_size_str = match.groups()
    status_code = int(status_code_str)
    file_size = int(file_size_str)

    total_file_size += file_size
    if status_code in status_code_count:
        status_code_count[status_code] += 1

    if line_number % 10 == 0:
        print_statistics()

print_statistics()
