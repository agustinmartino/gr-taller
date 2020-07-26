#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: amartino
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from gnuradio import blocks
import pmt
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import video_sdl
import taller
from gnuradio import qtgui

class test_deinterleave(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "test_deinterleave")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 132000
        self.orden = orden = [171,  68,   4,  74,  41,   7, 110, 117, 174, 102, 158,  17,  59, 141, 159, 112,  46, 129, 182, 131,  50, 101,  64, 138, 170,  77, 125, 181,  92,  27,  65,  86,   8,  73, 123, 144, 198,  87,  20, 62, 108,  28,  94, 151,  13, 113, 165, 127,  39,  89,  11, 152, 120, 186,  56, 109, 164, 114,  53, 155, 107,  99, 154, 169, 153, 40,  79, 128,  32,  29,  47, 193,  81, 195,  97,  93, 140,  23, 35,  33,  98, 132,  54, 142, 126,  66, 191, 134, 133,  42,  76, 161,  61, 177,  71,  19,  36, 162,  58, 175,  45, 147,  48, 146, 80, 160,  44,  60,  12,  96, 196,  49, 116,   3, 183, 187,  88, 10,  16, 115, 197,  26,  57,  25, 143, 122, 137, 199,   9,  38, 24, 173, 105,  31,  18,  91, 172, 121, 111, 104, 192,   2, 180, 119,70,  67, 176, 148,  82,  84, 136, 130, 179,  69,   0,  75, 168,  63,  37,  43,   6,  21, 163, 100,  55,  22,  78,  83, 194, 157, 178, 103,  52,  95, 139, 166, 184,  90,  72,  30, 156,  85, 167,  34,   5, 189,1,  14, 106, 124, 145, 185, 188, 150,  51, 149, 135, 118, 190,  15]

        ##################################################
        # Blocks
        ##################################################
        self.video_sdl_sink_0 = video_sdl.sink_s(0, 200, 172, 0, 200, 172)
        self.taller_deinterleaver_0 = taller.deinterleaver(orden)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_short*1, len(orden))
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, len(orden))
        self.blocks_float_to_short_0 = blocks.float_to_short(len(orden), 1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/home/amartino/GNU_RADIO/Taller_GNU_Radio/grabacion.dat', False, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(len(orden))



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_short_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_float_to_short_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.taller_deinterleaver_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.video_sdl_sink_0, 0))
        self.connect((self.taller_deinterleaver_0, 0), (self.blocks_complex_to_float_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "test_deinterleave")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)

    def get_orden(self):
        return self.orden

    def set_orden(self, orden):
        self.orden = orden



def main(top_block_cls=test_deinterleave, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
