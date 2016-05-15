#!/usr/bin/env python3
import sys, os
import argparse
import pigpio

class IQaudIO:
    def __init__(self):
        self.port = 22
        self.pi = pigpio.pi()
        self.pi.set_mode(self.port, pigpio.OUTPUT)

    def output(self, value):
        self.pi.write(self.port, value)

    def mute(self):
        self.output(0)

    def unmute(self):
        self.output(1)

    def show(self):
        if self.pi.read(self.port):
            print("Pi-DigiAMP+ is in UNMUTE state")
        else:
            print("PI-DigiAMP+ is in MUTE state")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="mute/unmute IQAudIO Pi-DigiAMP+")
    parser.add_argument("--mute", action="store_true", help="mute Pi-DigiAMP")
    parser.add_argument("--unmute", action="store_true", help="unmute Pi-DigiAMP")
    parser.add_argument("--show", action="store_true", help="show status")
    args = parser.parse_args()
    if args.show:
        IQaudIO().show()
        exit()
    if args.unmute:
        IQaudIO().unmute()
        exit()
    if args.mute:
        IQaudIO().mute()
        exit()
    else:
        IQaudIO().show()
        exit()
