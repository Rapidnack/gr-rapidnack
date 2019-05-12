#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2019 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import socket
import threading
import time

class CSRP(gr.basic_block):
    """
    docstring for block CSRP
    """
    def __init__(self, address,port,rate,gain,frequency):
        gr.basic_block.__init__(self,
            name="CSRP",
            in_sig=[],
            out_sig=[])
        self._address = address
        self._port = port
        self._rate = rate
        self._gain = gain
        self._frequency = frequency

        print('connecting to %s:%d' % (self._address, 28888))
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self._address, 28888))
        response = self.client.recv(256).strip()
        print(response)
        if response != 'DEVICE -': return

        self.client.send('DEVICE 0\n')
        response = self.client.recv(256).strip()
        print(response)
        if response == 'DEVICE -': return
        if response.startswith('DEVICE ') == False: return

        myaddress = self.client.getsockname()[0]
        self.client.send('DEST %s:%d\n' % (myaddress, self._port))
        response = self.client.recv(256).strip()
        print(response)
        if response.startswith('DEST OK') == False: return

        self.client.send('HEADER OFF\n')
        response = self.client.recv(256).strip()
        print(response)
        if response.startswith('HEADER OK') == False: return

        self.client.send('RATE %d\n' % self._rate)
        response = self.client.recv(256).strip()
        print(response)
        if response.startswith('RATE OK') == False: return

        if self.send_gain() == False: return

        if self.send_frequency() == False: return

        self.client.send('GO\n')
        response = self.client.recv(256).strip()
        print(response)

        self.keepalive_thread = keepalive_thread(self.client, 1)
        self.keepalive_thread.start()

    def send_gain(self):
        self.client.send('GAIN %f\n' % self._gain)
        response = self.client.recv(256).strip()
        print(response)
        if response.startswith('GAIN OK') == False: return False
        return True

    def send_frequency(self):
        self.client.send('FREQ %f\n' % self._frequency)
        response = self.client.recv(256).strip()
        print(response)
        if response.startswith('FREQ OK') == False and\
           response.startswith('FREQ HIGH') == False and\
           response.startswith('FREQ LOW') == False: return
        return True

    def gain(self):
        return self._gain

    def set_gain(self, gain):
        self._gain = gain
        self.send_gain()

    def frequency(self):
        return self._frequency

    def set_frequency(self, frequency):
        self._frequency = frequency
        self.send_frequency()

class keepalive_thread(threading.Thread):

    def __init__(self, client, interval, **kwds):
        threading.Thread.__init__(self, **kwds)
        self.setDaemon(1)
        self.client = client
        self.interval = interval

    def start(self):
        self.active = True
        threading.Thread.start(self)

    def stop(self):
        self.active = False

    def run(self):
        while self.active:
            time.sleep(self.interval)
            self.client.send('\n')
