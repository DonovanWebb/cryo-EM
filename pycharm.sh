#!/bin/bash

module load python/2.7
export PYTHONPATH="${PYTHONPATH}:/dls_sw/apps/EM/ccpem/ccpem-20190529/lib/python2.7/site-packages/"
export PYTHONPATH="${PYTHONPATH}:/dls_sw/apps/EM/ccpem/ccpem-20190529/lib/py2/"
export PYTHONPATH="${PYTHONPATH}:/dls_sw/apps/EM/ccpem/ccpem-20190529/lib/py2/site-packages"
export PYTHONPATH="${PYTHONPATH}:/dls_sw/apps/EM/ccpem/ccpem-20190529/lib/py2/ccpem/src"
export PYTHONPATH="${PYTHONPATH}:/dls_sw/apps/EM/ccpem/ccpem-20190529/lib/py2/ccpem/src/ccpem_core/"
module load pycharm
pycharm
