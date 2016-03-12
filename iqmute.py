#!/usr/bin/env python3
import sys, os
import argparse
import RPi.GPIO as GPIO

class IQaudIO:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.port = 22
        GPIO.setup(self.port, GPIO.OUT)

    def output(self, value):
        GPIO.output(self.port, value)

    def mute(self):
        self.output(0)

    def unmute(self):
        self.output(1)

    def show(self):
        if GPIO.input(self.port):
            print("Pi-DigiAMP+ is in UNMUTE state")
        else:
            print("PI-DigiAMP+ is in MUTE state")

    def __del__(self):
        GPIO.cleanup()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="mute/unmute IQAudIO Pi-DigiAMP+")
    parser.add_argument("--mute", action="store_true", help="unmute by default")
    parser.add_argument("--show", action="store_true", help="show status")
    args = parser.parse_args()
    if args.show:
        IQaudIO().show()
        exit()
    if args.mute:
        IQaudIO().mute()
        exit()
    else:
        IQaudIO().unmute()
        exit()
