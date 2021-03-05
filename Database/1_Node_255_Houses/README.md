# FNCS-Tutorial GridLAB-D and ns-3

Step-by-step guide for building and running FNCS, ns-3, and GridLAB-D.

This guide will walk you through installing and running a preliminary
use case: running a single instance of GridLAB-D and realistically
delaying and routing messages through ns-3.

## Table of Contents
- [Hardware Requirements](#hardware-requirements)
- [Software and Dependencies](#software-and-dependencies)
  - [ZeroMQ Installation](#zeromq-installation)
  - [CZMQ Installation](#czmq-installation)
  - [FNCS Installation](#fncs-installation)
  - [Xerces-C++ Installation](#xerces-c-installation)
  - [GridLAB-D Installation](#gridlab-d-installation)
  - [ns-3 Installation](#ns-3-installation)
- [Important Environment Variables](#important-environment-variables)
- [Model Description](#model-description)
- [Running the Co-Simulation](#running-the-co-simulation)

## Hardware Requirements
[back to contents](#table-of-contents)

This software was developed and tested exclusively using the Linux
operating system.  Our developers have used RedHat EL5 as well as Ubuntu
12.04.5 LTS (precise), both of which were 64-bit systems. This software
has not been built or tested on Windows. Although all of the software
packages and their dependencies are known to have Windows installers, we
have not yet developed any way to patch those official distributions
with FNCS enhancements.

## Software and Dependencies
[back to contents](#table-of-contents)

This portion of the tutorial will walk you through installing all
prerequisite software. The following software will be covered,
indicating the primary software installed and the list of dependencies:

You will need to install git in order to clone (checkout) all of our
FNCS and related software packages.

- FNCS
  - ZeroMQ (3.2.x)
  - CZMQ (3.0.x)
- GridLAB-D (ticket 797)
  - Xerces (3.1.1)
  - autoconf (2.63 or better)
  - automake (1.11 or better)
  - libtool (2.2.6b or better)
  - FNCS
- ns-3 (our version based on 3.26)
  - Python (for the waf installer)
  - FNCS

It will be assumed that you will be installing all software into
$HOME/FNCS-install. Doing so will greatly simplify the steps of this
tutorial since we can set $LD_LIBRARY_PATH and $PATH accordingly, as
well as any other needed installation paths while building many of the
involved software packages. In fact, now would be a good time to set a
shortcut environment variable, like so:

```
export FNCS_INSTALL="$HOME/FNCS-install"
```

NOTE: You could, in theory, change this to point to wherever you wish to
install FNCS and all related software packages.

It is also assumed that you are using a Bourne shell; all of the
step-by-step instructions (like the one above) that appear in this
tutorial  will assume a Bourne shell. If you are using a C shell, we
hope you can adapt the steps as needed, mostly in how environment
variables are set.

## ZeroMQ Installation
[back to contents](#table-of-contents)

http://zeromq.org/

The ZeroMQ library is the only library that our FNCS library depends on.
We have extensively tested our software using version 3.2.x, however
later versions may also work but have not yet been tested.

Get the ZeroMQ software and install it using the following steps:

```
# we are doing everything from your $HOME directory
cd $HOME

# download zeromq
wget http://download.zeromq.org/zeromq-3.2.4.tar.gz
# if you do not have wget, use
# curl -O http://download.zeromq.org/zeromq-3.2.4.tar.gz

# unpack zeromq, change to its directory
tar -xzf zeromq-3.2.4.tar.gz
cd zeromq-3.2.4

# configure, make, and make install
./configure --prefix=$FNCS_INSTALL
make
make install
```

Congratulations, you have now installed ZeroMQ.

### CZMQ Installation
[back to contents](#table-of-contents)

http://czmq.zeromq.org/

Installing CZMQ is like any other software using configure and make.
The main challenge is specifying the installation location (--prefix)
for CZMQ as well as the location where ZeroMQ was installed.  If you
installed ZeroMQ as written above, the following will work for you.

```
# we are doing everything from your $HOME directory
cd $HOME

# download czmq
wget http://download.zeromq.org/czmq-3.0.0-rc1.tar.gz
# if you do not have wget, use
# curl -O http://download.zeromq.org/czmq-3.0.0-rc1.tar.gz

# unpack czmq, change to its directory
tar -xzf czmq-3.0.0-rc1.tar.gz
cd czmq-3.0.0

# configure, make, and make install
./configure --prefix=$HOME/FNCS_install --with-libzmq=$HOME/FNCS_install
make
make install
```

Congratulations, you have now installed CZMQ.

## FNCS Installation
[back to contents](#table-of-contents)

https://github.com/FNCS/fncs

The FNCS software will build and install the FNCS library, the various
FNCS header files, as well as the broker application. The FNCS broker
represents the central server that all other simulator clients will
connect to in order to synchronize in time and exchange messages with
other simulators. The FNCS library and header represent the needed API
for communicating with the broker using the sync and messaging function
calls.

Get the FNCS software and install it using the following steps:

```
# we are doing everything from your $HOME directory
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

Congratulations, you have now installed FNCS.

## Xerces-C++ Installation
[back to contents](#table-of-contents)

http://xerces.apache.org/xerces-c/

```
# we are doing everything from your $HOME directory
cd $HOME

# download Xerces-C++ 3.1.1 source code
wget http://apache.mirrors.pair.com//xerces/c/3/sources/xerces-c-3.1.1.tar.gz
# if you do not have wget, use
# curl -O http://apache.mirrors.pair.com//xerces/c/3/sources/xerces-c-3.1.1.tar.gz

# unpack xerces, change to its directory
tar -xzf xerces-c-3.1.1.tar.gz
cd xerces-c-3.1.1

# configure, make, and make install
./configure --prefix=$FNCS_INSTALL
make
make install
```

Congratulations, you have now installed Xerces-C++ and are ready to
install GridLAB-D.

## GridLAB-D Installation
[back to contents](#table-of-contents)

http://www.gridlabd.org/

GridLAB-D is a power distribution system simulator and analysis tool.
Please see its website for complete details.

Currently the only version of GridLAB-D that will compile with FNCS is the develop branch of GridLAB-D on github. https://github.com/gridlab-d/gridlab-d.git.

Get our version of the GridLAB-D software and install it using the
following steps:

```
# we are doing everything from your $HOME directory
cd $HOME

# download our FNCS-capable version of GridLAB-D
git clone https://github.com/gridlab-d/gridlab-d

# change to FNCS-gridlab-d directory
cd gridlab-d

# checkout the develop branch
git checkout -b develop origin/develop

# run to autotools to generate the configure script and Makefile.in
# templates
# minimum required versions:
# autoconf 2.63
# automake 1.11
# libtool 2.2.6b
autoreconf -fi

# configure, make, and make install
./configure --prefix=$FNCS_INSTALL --with-xerces=$FNCS_INSTALL --with-fncs=$FNCS_INSTALL --enable-silent-rules 'CFLAGS=-g -O0 -w' 'CXXFLAGS=-g -O0 -w' 'LDFLAGS=-g -O0 -w'
make
make install
```

Congratulations, you have now installed GridLAB-D ticket 797.

## ns-3 Installation
[back to contents](#table-of-contents)

http://www.nsnam.org/

ns-3 is a discrete-event network simulator for Internet systems. Please
see their website for complete details.

We added a FNCS "application" as a patch to ns-3.26. Our application
receives FNCS messages from GridLAB-D and injects them into the network,
and once through the network (if not dropped), sends the FNCS message on
to its intended recipient.

Get our version of the ns-3 software and install it using the following
steps:

```
# we are doing everything from your $HOME directory
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

# insatll
./waf install
```

Congratulations, you have now installed ns-3, at least, our version
of it.

## Important Environment Variables
[back to contents](#table-of-contents)

Now that all of the FNCS and related software is installed, now would be
a great time to set some important environment variables. If you have
been following the steps exactly, then you can copy-and-paste the
following into a handy shell script that you can source before running
the co-simulation. If you are reading this file from the github sources,
you will find the file [here](https://github.com/FNCS/FNCS-Tutorial/blob/master/demo-gld-ns3/env.sh).

Here is what the file recently looked like, but please refer to the
original file as linked above.

```Bash
#!/bin/sh

export FNCS_INSTALL="$HOME/FNCS-install"

# update LD_LIBRARY_PATH
if test "x$LD_LIBRARY_PATH" = x
then
    export LD_LIBRARY_PATH="$FNCS_INSTALL/lib"
else
    export LD_LIBRARY_PATH="$FNCS_INSTALL/lib:$LD_LIBRARY_PATH"
fi

# update PATH
if test "x$PATH" = x
then
    export PATH="$FNCS_INSTALL/bin"
else
    export PATH="$FNCS_INSTALL/bin:$PATH"
fi
```

## Model Description
[back to contents](#table-of-contents)

In this current directory you will find many files, the vast majority of
them are input files for GridLAB-D.

- Tutorial files
    - env.sh -- source this file to set up your environment variables
    - README.md -- this file
- GridLAB-D files
    - appliance_schedules.glm
    - ColumbusWeather2009_2a.csv
    - fncs_GLD_300node_Feeder_1.glm
    - phase_A.player
    - phase_B.player
    - phase_C.player
    - tzinfo.txt
    - unitfile.txt
    - water_and_setpoint_schedule_v3.glm
    - configgld.json -- FNCS config file for ns-3
- ns-3 files
    - compile-ns3.sh -- our helper script for compiling ns-3 model
    - firstN.cc -- the ns-3 model source file
	- LinkModelGLDNS3.txt

### GridLAB-D Model
Our GridLAB-D model consists of 300 houses. Some of the houses
participate in a transactive market where they send their
(price,quantity) bids to an auction house. The bids are collected,
sorted, and from them a price signal is broadcast back out to the
participating homes. The bids as well as the price signal are
communicated through the ns-3 model to realistically delay the messages.

To get GridLAB-D to work with FNCS, we needed to modify how it processes
time. For details, see the core/exec.c and core/main.c files in our
custom distribution of GridLAB-D. In order for houses to communicate
with the auction, we created a new GridLAB-D module called "comm", the
source code for which can be found in the communications directory can
in our custom GridLAB-D distribution. Within the comm module we created
the "market network interface" as well as the "controller network
interface" classes which create, send, and receive FNCS Messages between
them.

Figuring out how to control time within GridLAB-D was challenging,
however the exchange of messages between entities within GridLAB-D is
really no more complicated than our first simple "power+power" demo in
these tutorial pages.

### ns-3 Model
Our ns-3 model [firstN.cc](https://github.com/FNCS/FNCS-Tutorial/blob/master/demo-gld-ns3/firstN.cc) creates 250 nodes within the
network in groups of 20. We use the CSMA model of ns-3 in order to set a
"DataRate" as well as a "Delay". ns-3 is its own feature-rich network
modeling simulator, so our simple model should not be considered the
only solution. We give each node an IP address and later map the IP
addresses to names given to each house from the GridLAB-D model. The
GridLAB-D house names follow a regular pattern which we exploit when
naming the nodes in our ns-3 network -- we only need to know the number
of houses in the GridLAB-D model and the name prefix for the houses. The
single input file [LinkModelGLDNS3.txt](https://github.com/FNCS/FNCS-Tutorial/blob/master/demo-gld-ns3/LinkModelGLDNS3.txt) provides
this information to our ns-3 model.

To get ns-3 to work with FNCS, we created a new ns-3 FNCS "application".
Applications are associated with individual nodes. Each node holds a
list of references to its applications. In other words, a node in ns-3
on its own doesn't do anything, rather it must have one or more
applications running on the node. Our FNCS application listens for
FNCS
messages. Upon receiving a FNCS message, a FNCS application running at a
node injects the message into the simulated network at its node. The
ns-3 model routes the message appropriately, realistically delaying its
transmission, and then the FNCS application instance running on the
destination node in the network reads the message once it arrives and
sends it back to the FNCS broker so it can be sent back to the
destination simulator.

It may sound complicated, but it's really not so different from our
simple network simulator from the second tutorial.

## Running the Co-Simulation
[back to contents](#table-of-contents)

The rest of this tutorial assumes that you have installed FNCS and our
versions of GridLAB-D and ns-3 i.e. all of the software mentioned above.

We will use the current directory of the tutorial as the working
directory for our co-simulation.  Each simulator software package will
generate output files, as usual, to the current working directory. In
addition, we have may have added own diagnostic output to standard
output (the terminal). The simulators are designed to locate files from
the working directory, for example, as inputs.

If you have sourced the env.sh file and installed the softare as we
had indicated, you should be ready to compile the ns-3 model and run the
demo. Start by compiling the ns-3 model.

```bash
./compile-ns3.sh firstN.cc
```

If we didn't already have a handy script for you this time around to run
the demo, instead you would need to manually open up three terminal
windows, one for running the fncs_broker, one for GridLAB-D, and the last
for ns-3. If you're wanting to run the demo that way, do the following
steps.

In the first window, from this tutorial directory, run GridLAB-D and
specify the demo GLM model file.

```bash
gridlabd ./F1_250_house.glm
```

In the second window, from this tutorial directory, run the compiled
ns-3 model and specify its model file.

```bash
./firstN LinkModelGLDNS3.txt
```

In the third window, from this tutorial directory, run fncs_broker. The
command-line argument '2' indicates that two simulators will be
connecting to the broker.
```bash
fncs_broker 2
```

As mentioned above, we have a useful script for running all of the
simulators and the broker in separate windows. This assumes you have
followed the installation process exactly as documented. No need to
source the env.sh file because it is embedded into the run.sh
script. The run.sh script will set up your environment for you and then
run 'xterm' once for each of the simulators and the broker. xterm
instances should start appearing on your desktop. If you only see a
subset of the xterm windows, chances are they are overlapping so you
will need to drag them around your desktop to reveal hidden ones.

In either the terminals you manually created or in the ones created for
you by the run.sh script, you should start seeing (in addition to the
usual output from any of the simulators like GridLAB-D) our diagnostic
messages coming from each simulator (note that fncs_broker is silent).

Once one of the simulators reaches the end of their simulated time, or
if you manually terminate any of them using Ctrl+C, all of the
simulators should stop. If you have used the run.sh script, this should
also automatically close the xterm sessions.

What you do with the output from this co-simulation is really up to you,
the modeler. You could experiment by setting longer delays to our ns-3
model, or better yet create your own ns-3 model that is more
complicated or uses a different network protocol. You could use a
GridLAB-D model that has more houses or has greater market penetration.
