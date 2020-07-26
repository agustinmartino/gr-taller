/* -*- c++ -*- */

#define TALLER_API

%include "gnuradio.i"           // the common stuff

//load generated python docstrings
%include "taller_swig_doc.i"

%{
#include "taller/deinterleaver.h"
#include "taller/freq_monitor.h"
%}

%include "taller/deinterleaver.h"
GR_SWIG_BLOCK_MAGIC2(taller, deinterleaver);

%include "taller/freq_monitor.h"
GR_SWIG_BLOCK_MAGIC2(taller, freq_monitor);
