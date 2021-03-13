#!/usr/bin/env python3
import logging


def fib(n):
    current = 0
    forward = 1
    for __ in range(n):
        forward, current = current, forward + current
    return current


def main():
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    logging.info("Enter the order of required Fibonacci number (up to 300000):")
    while 1:
        n = int(input())
        if n <= 300000:
            logging.info(fib(int(n)))
            break
        logging.info("Too huge, try again")


if __name__ == '__main__':
    try:
        main()
    except (OverflowError, EOFError, KeyboardInterrupt, ValueError):
        logging.info("\nTerminating program due to critical input error.")
