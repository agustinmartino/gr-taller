/* -*- c++ -*- */
/*
 * Copyright 2020 gr-taller author.
 *
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_TALLER_FREQ_MONITOR_IMPL_H
#define INCLUDED_TALLER_FREQ_MONITOR_IMPL_H

#include <taller/freq_monitor.h>

#include <gnuradio/fft/fft.h>
#include <gnuradio/filter/firdes.h>
#include <volk/volk.h>

namespace gr {
  namespace taller {

    class freq_monitor_impl : public freq_monitor
    {
     private:
      int d_fftsize;
      fft::fft_complex* d_fft;
      filter::firdes::win_type d_wintype;
      std::vector<float> d_window;

      void buildwindow();
      void psd(float* psd_out, const gr_complex* data_in, int size);
      
     public:
      freq_monitor_impl(int fft_size, int wintype);
      ~freq_monitor_impl();

      // Where all the action really happens
      int work(
              int noutput_items,
              gr_vector_const_void_star &input_items,
              gr_vector_void_star &output_items
      );
    };

  } // namespace taller
} // namespace gr

#endif /* INCLUDED_TALLER_FREQ_MONITOR_IMPL_H */

