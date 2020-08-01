#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2020 gr-taller author.
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

from gnuradio import gr, gr_unittest
from gnuradio import blocks
import taller_swig as taller
import pylab as pl
import numpy as np

class qa_freq_monitor(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_t(self):
        fft_size = 1024
        wintype = 0 #Wintype Hamming
        samp_rate = 2e6

        for frequency in np.arange(-1e6, 1e6,  100e3):

            #Blocks
            self.DUT = taller.freq_monitor(fft_size, wintype)
            stim = np.exp(2*1j*np.pi*frequency/samp_rate*np.arange(0,fft_size))


            self.blocks_vector_source_x_0 = blocks.vector_source_c(stim, False, fft_size, [])
    #        self.blocks_vector_sink_x_0 = blocks.vector_sink_c(fft_size, 1024)        

            #Connects
            self.tb.connect((self.blocks_vector_source_x_0, 0), (self.DUT, 0))
            self.tb.run()

            # check data
            spectrum = self.DUT.get_spectrum()

            freq_axis = np.arange(-fft_size/2,fft_size/2)*samp_rate/float(fft_size)
            peak = max(spectrum)
            peak_freq = freq_axis[([i for i, j in enumerate(spectrum) if j == peak])[0]]
            print("Found freq: ", peak_freq)

            self.assertTrue(abs(peak_freq-frequency) < 1000)
            # pl.plot(freq_axis,spectrum)
            # pl.grid()
            # pl.show()

if __name__ == '__main__':
    gr_unittest.run(qa_freq_monitor)
