#!/usr/bin/env python3
import sys, os
import argparse
import RPi.GPIO as GPIO

class IQaudIO:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.port = 22
        GPIO.setup(self.port, GPIO.OUT)

    def output(self, value):
        GPIO.output(self.port, value)

    def mute(self):
        self.output(0)

    def unmute(self):
        self.output(1)

    def __del__(self):
        GPIO.cleanup()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="mute/unmute IQAudIO Pi-DigiAMP+")
    parser.add_argument("--mute", action="store_true", help="umute by default")
    args = parser.parse_args()
    if args.mute:
        IQaudIO().mute()
    else:
        IQaudIO().unmute()
