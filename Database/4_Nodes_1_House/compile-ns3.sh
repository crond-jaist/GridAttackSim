#!/bin/bash

g++ \
-g \
-o run_ns-3 \
run_ns-3.cc \
-I$FNCS_INSTALL/include \
-I$FNCS_INSTALL/include/fncs \
-I$FNCS_INSTALL/include/ns3.26 \
-L$FNCS_INSTALL/lib \
-lns3.26-applications-debug \
-lns3.26-fncs-debug \
-lns3.26-nix-vector-routing-debug \
-lns3.26-internet-debug \
-lns3.26-bridge-debug \
-lns3.26-csma-debug \
-lns3.26-point-to-point-debug \
-lns3.26-mpi-debug \
-lns3.26-stats-debug \
-lns3.26-network-debug \
-lns3.26-core-debug \
-lfncs \
-lczmq \
-lzmq

#g++ \
#-g \
#-o firstN \
#firstN.cc \
#-I$FNCS_INSTALL/include/fncs \
#-I$FNCS_INSTALL/include/ns3.19 \
#-L$FNCS_INSTALL/lib \
#-lns3.19-fncs-debug \
#-lfncs \
#-lzmq \
#-lns3.19-point-to-point-debug \
#-lns3.19-applications-debug \
#-lns3.19-nix-vector-routing-debug \
#-lns3.19-csma-debug \
#-lns3.19-point-to-point-layout-debug \
#-lns3.19-wifi-debug \
#-lns3.19-netanim-debug \
#-lns3.19-wimax-debug \
#-lns3.19-core-debug
