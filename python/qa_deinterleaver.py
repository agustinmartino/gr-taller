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

class qa_deinterleaver(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_001_t(self):
        # set up fg
        self.orden = orden = [171,  68,   4,  74,  41,   7, 110, 117, 174, 102, 158,  17,  59, 141, 159, 112,  46, 129, 182, 131,  50, 101,  64, 138, 170,  77, 125, 181,  92,  27,  65,  86,   8,  73, 123, 144, 198,  87,  20, 62, 108,  28,  94, 151,  13, 113, 165, 127,  39,  89,  11, 152, 120, 186,  56, 109, 164, 114,  53, 155, 107,  99, 154, 169, 153, 40,  79, 128,  32,  29,  47, 193,  81, 195,  97,  93, 140,  23, 35,  33,  98, 132,  54, 142, 126,  66, 191, 134, 133,  42,  76, 161,  61, 177,  71,  19,  36, 162,  58, 175,  45, 147,  48, 146, 80, 160,  44,  60,  12,  96, 196,  49, 116,   3, 183, 187,  88, 10,  16, 115, 197,  26,  57,  25, 143, 122, 137, 199,   9,  38, 24, 173, 105,  31,  18,  91, 172, 121, 111, 104, 192,   2, 180, 119,70,  67, 176, 148,  82,  84, 136, 130, 179,  69,   0,  75, 168,  63,  37,  43,   6,  21, 163, 100,  55,  22,  78,  83, 194, 157, 178, 103,  52,  95, 139, 166, 184,  90,  72,  30, 156,  85, 167,  34,   5, 189,1,  14, 106, 124, 145, 185, 188, 150,  51, 149, 135, 118, 190,  15]

        #Blocks
        self.taller_deinterleaver_0 = taller.deinterleaver(orden)
        self.blocks_vector_source_x_0 = blocks.vector_source_c(range(200), False, 200, [])
        self.blocks_vector_sink_x_0 = blocks.vector_sink_c(200, 1024)        

        #Connects
        self.tb.connect((self.blocks_vector_source_x_0, 0), (self.taller_deinterleaver_0, 0))
        self.tb.connect((self.taller_deinterleaver_0, 0), (self.blocks_vector_sink_x_0, 0))
        
        self.tb.run()

        my_data = self.blocks_vector_sink_x_0.data()
        for kk in range(len(self.orden)):
            #print(kk, " ", my_data[kk])
            self.assertEqual(my_data[self.orden[kk]],kk)
                




if __name__ == '__main__':
    gr_unittest.run(qa_deinterleaver)
