import hashlib

import serial

SERIAL_PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600


def generate_hash(data_string):
    return hashlib.sha256(data_string.encode("utf-8")).hexdigest()


def main():
    print(f"[EDR Middleware] Listening on {SERIAL_PORT}...")
    # TODO: Implement physical serial read loop
    # TODO: Integrate cx_Oracle / oracledb driver for database insertion
    print("[EDR Middleware] Awaiting hardware connection...")


if __name__ == "__main__":
    main()
