#!/bin/bash

export CONDA_ACTIVATE=/APSshare/miniconda/x86_64/bin/activate
export CONDA_ENVIRONMENT=bluesky

export IPYTHONDIR=~/.ipython
export IPYTHON_PROFILE=bluesky

export OPTIONS=
export OPTIONS="${OPTIONS} --ipython-dir=${IPYTHONDIR}"
export OPTIONS="${OPTIONS} --profile=${IPYTHON_PROFILE}"
export OPTIONS="${OPTIONS} --IPCompleter.use_jedi=False"

source ${CONDA_ACTIVATE} ${CONDA_ENVIRONMENT}

export LD_LIBRARY_PATH=
ipython  ${OPTIONS} 
