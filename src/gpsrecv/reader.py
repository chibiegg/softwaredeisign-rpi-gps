# encoding=utf-8
import serial
import threading
import re
from queue import Queue, Full

RECV_RE = re.compile("^\[(.+):(\d+)\] (.+)$")

class Serial(threading.Thread):

    def __init__(self, port, name="unknown", baudrate=9600, queue=None):
        super(Serial, self).__init__()
        self.serial = serial.Serial(port, baudrate)
        self.daemon = True
        self.name = name
        self.queue = queue

    def run(self):
        index = 0
        while True:
            try:
                line = self.serial.readline().decode("ascii").strip()
            except UnicodeDecodeError:
                continue

            if self.queue:
                try:
                    self.queue.put_nowait({
                                                 "sender":self.name,
                                                 "index":index,
                                                 "data":line
                                                 })
                except Full:
                    pass
            index += 1
