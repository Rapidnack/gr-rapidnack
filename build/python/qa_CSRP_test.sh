#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/zaurus/gnuradio/gr-rapidnack/python
export PATH=/home/zaurus/gnuradio/gr-rapidnack/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/zaurus/gnuradio/gr-rapidnack/build/swig:$PYTHONPATH
/usr/bin/python2 /home/zaurus/gnuradio/gr-rapidnack/python/qa_CSRP.py 
