
# Installation Guide

GridAttackSim was developed and tested exclusively using the Ubuntu
16.04 LTS operating system; either a physical host or a virtual
machine installation can be used. Other Linux OSes may work, but have
not been tested, nor has this software been tested on Windows.

To run GridAttackSim, you have to first install and configure the
three external components it uses: FNCS, ns-3, and GridLAB-D. To do
this, please follow the official [FNCS
tutorial](https://github.com/FNCS/FNCS-Tutorial/tree/master/demo-gld-ns3). In
case you encounter any difficulties, see the notes below about the
installation process.


## Set up environment variables

In order to configure FNCS, you _must_ set up the related environment
variables, for example by adding the code shown next to the file
`~/.bashrc`:

```shell
export FNCS_INSTALL="$HOME/FNCS-install"
# update LD_LIBRARY_PATH
if test "x$LD_LIBRARY_PATH" = x
then
    export LD_LIBRARY_PATH="$FNCS_INSTALL/lib:$FNCS_INSTALL/lib/gridlabd"
else
    export LD_LIBRARY_PATH="$FNCS_INSTALL/lib:$FNCS_INSTALL/lib/gridlabd:$LD_LIBRARY_PATH"
fi
# update PATH
if test "x$PATH" = x
then
    export PATH="$FNCS_INSTALL/bin:$FNCS_INSTALL/share/gridlabd"
else
    export PATH="$FNCS_INSTALL/bin:$FNCS_INSTALL/share/gridlabd:$PATH"
fi
export GLPATH="$FNCS_INSTALL/share/gridlabd:$FNCS_INSTALL/lib/gridlabd"
```


## Install required packages and dependencies

```shell
sudo apt install automake libtool autoconf libczmq-dev libxerces-c-dev
```


## Download, build and install FCNS

```shell
# change to the $HOME directory
cd $HOME
# download FNCS
git clone https://github.com/FNCS/fncs
# change to FNCS directory
cd FNCS
# configure, make, and make install
./configure --prefix=$FNCS_INSTALL --with-zmq=$FNCS_INSTALL
make
make install
```


## Download, build and install ns-3

```shell
# change to the $HOME directory
cd $HOME
# download our FNCS version of ns-3
git clone https://github.com/FNCS/ns-3.26
# change to ns-3.26 directory
cd ns-3.26
# the ns-3 install typically uses the compiler flag for
# warnings-as-errors which often broke our ability to build and install
# it, so we recommend the following configure of ns-3
CFLAGS="-g -O2" CXXFLAGS="-g -O2" ./waf configure --prefix=$FNCS_INSTALL --with-fncs=$FNCS_INSTALL --with-zmq=$FNCS_INSTALL --disable-python
# 'make'
./waf build
# install
./waf install
```


## Download, build and install GridLAB-D

```shell
# change to the $HOME directory
cd $HOME
# download our FNCS-capable version of GridLAB-D
git clone https://github.com/gridlab-d/gridlab-d
# change to the FNCS-gridlab-d directory
cd gridlab-d
# checkout the develop branch
git checkout -b develop origin/develop
# generate the configure script and Makefile.in templates
# minimum required versions:
# autoconf 2.63
# automake 1.11
# libtool 2.2.6b
autoreconf -fi
# configure, make, and make install
./configure --prefix=$FNCS_INSTALL --with-xerces=$FNCS_INSTALL --with- fncs=$FNCS_INSTALL --enable-silent-rules 'CFLAGS=-g -O0 -w' 'CXXFLAGS=-g -O0 -w' 'LDFLAGS=-g -O0 -w'
make
make install
```

**NOTE**: At this stage we suggest you restart the operating system to
make sure that all the changes are taken into account.


## Fix issue with GridLAB-D

We have encountered an issue when compiling GridLAB-D. To solve it you
need to edit the file `climate/climate.cpp` in the GridLAB-D
distribution, and change the math library as shown below:

_ORIGINAL CODE:_
```
#include <math.h>
```

_NEW CODE:_
```
#include <cmath>
```


## Run co-simulation experiment

In order to run a co-simulation using FNCS, you can use the `run.sh`
file included in the [source
code](https://github.com/FNCS/FNCS-Tutorial/tree/master/demo-gld-ns3)
of the FNCS tutorial.


## Reset installation

If you encounter an error while installing any of the above tools, you
can use the following command to reset the installation, then try again:

```
Make
```
