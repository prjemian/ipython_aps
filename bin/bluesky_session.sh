#!/bin/bash

export IPYTHON_DIR=~/.ipython

source /APSshare/anaconda3/x86_64/bin/activate
conda activate bluesky
export LD_LIBRARY_PATH=
ipython --profile=bluesky --ipython-dir=$IPYTHON_DIR --IPCompleter.use_jedi=False

