#!/bin/sh

# use a fresh custom loader path
unset LD_LIBRARY_PATH

# shortcut
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

export FNCS_LOG_STDOUT=no
export FNCS_LOG_FILE=yes

# run ns3 in separate window
xterm -e ./run_ns-3 LinkModelGLDNS3.txt &

# run gld in separate window
xterm -e gridlabd run_GridLab-D.glm &

# run fncs_broker in separate window
xterm -e fncs_broker 2 &

echo "running"
