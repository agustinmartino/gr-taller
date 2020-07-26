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

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "freq_monitor_impl.h"

namespace gr {
  namespace taller {

    freq_monitor::sptr
    freq_monitor::make(int fft_size, int wintype)
    {
      return gnuradio::get_initial_sptr
        (new freq_monitor_impl(fft_size, wintype));
    }


    /*
     * The private constructor
     */
    freq_monitor_impl::freq_monitor_impl(int fft_size, int wintype)
      : gr::sync_block("freq_monitor",
              gr::io_signature::make(1, 1, fft_size*sizeof(gr_complex)),
              gr::io_signature::make(0, 0, 0))
    {
      d_fftsize = fft_size;
      d_wintype = (filter::firdes::win_type) wintype;
      d_fft = new fft::fft_complex(d_fftsize, true);
      buildwindow();
    }

    /*
     * Our virtual destructor.
     */
    freq_monitor_impl::~freq_monitor_impl()
    {
      delete d_fft;      
    }

    int
    freq_monitor_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *in = (const gr_complex *) input_items[0];

      // Do <+signal processing+>

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

    void freq_monitor_impl::buildwindow()
    {
      d_window.clear();
      if (d_wintype != filter::firdes::WIN_NONE) {
        d_window = filter::firdes::window(d_wintype, d_fftsize, 6.76);
      }
    }    

    void freq_monitor_impl::psd(float* psd_out, const gr_complex* data_in, int size)
    {
      if (!d_window.empty()) {
        volk_32fc_32f_multiply_32fc(d_fft->get_inbuf(), data_in, &d_window.front(), size);
      } else {
        memcpy(d_fft->get_inbuf(), data_in, sizeof(gr_complex) * size);
      }

      d_fft->execute(); // compute the fft

      volk_32fc_s32f_x2_power_spectral_density_32f(
        psd_out, d_fft->get_outbuf(), size, 1.0, size);

      //d_fft_shift.shift(psd_out, size);
    }        

  } /* namespace taller */
} /* namespace gr */

