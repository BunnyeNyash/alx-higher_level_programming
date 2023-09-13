#!/usr/bin/python3
import sys

status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
        }
total_size = 0
line_count = 0

def print_statistics():
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_codes.keys())
    for code in sorted_codes:
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) > 2:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
            except ValueError:
                pass

        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print_statistics()
    raise
