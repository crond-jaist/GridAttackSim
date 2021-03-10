
# GridAttackSim: Smart Grid Attack Simulation Framework

GridAttackSim is a framework that makes it possible to simulate
various cyber-attacks on the smart grid infrastructure and visualize
their consequences. GridAttackSim uses a co-simulation approach, and
it is based on a combination of [GridLAB-D](https://www.gridlabd.org),
[ns-3](https://www.nsnam.org), and
[FNCS](https://github.com/FNCS). The framework is extensible by end
users, and the current release includes five smart grid topologies,
two smart grid applications (demand response and dynamic pricing), and
an attack library with four types of attacks (channel jamming,
malicious code, injection attacks, and message replay). GridAttackSim
is being developed by the Cyber Range Organization and Design
([CROND](https://www.jaist.ac.jp/misc/crond/index-en.html))
NEC-endowed chair at the Japan Advanced Institute of Science and
Technology ([JAIST](https://www.jaist.ac.jp/english/)) in Ishikawa,
Japan.

GridAttackSim is intended as a tool that helps researchers investigate
smart grid security issues and develop technologies for improving
smart grid security. An overview of how GridAttackSim can be used to
visualize the consequences of a smart grid cyber-attack is shown
below.

![GridAttackSim Use](Figures/use_overview.png?raw=true "Overview of the GridAttackSim use")

The architecture of GridAttackSim comprises six main modules, as
illustrated below:
* **Preprocessing Module**: Prepare the files needed to run the
  GridLAB-D simulation and to configure the FNCS broker
* **Attack Pattern Library**: Store information about the attack type,
  target and schedule that will be used for the cyber-attack
  simulation
* **Model Manager**: Core component of GridAttackSim that coordinates
  the entire smart grid attack simulation framework
* **Ns-3**: Discrete-event network simulator
* **GridLAB-D**: Power distribution system simulation and analysis tool
* **FNCS Broker**: Component of the FNCS co-simulation framework that
  mediates the communication between ns-3 and GridLAB-D

![GridAttackSim Architecture](Figures/framework_architecture.png?raw=true "Architecture of the GridAttackSim framework")

GridAttackSim can be extended, and end users can add new smart grid
topologies or new types of attacks. Please consult the [Developer
Guide](/developer_guide.md) for more information on how to extend the
framework.


## Installation

GridAttackSim was developed and tested exclusively using the Ubuntu
16.04 LTS operating system; either a physical host or a virtual
machine installation can be used. Other Linux OSes may work, but have
not been tested, nor has this software been tested on Windows.

To run GridAttackSim, you have to first install and configure the
three external components, FNCS, ns-3, and GridLAB-D. For details,
please consult our [Installation Guide](/installation_guide.md).

Once the external components are installed, use the
[releases](https://github.com/crond-jaist/GridAttackSim/releases) page
to download the latest version of GridAttackSim, and extract the
source code archive into a directory of your choice.


## Quick Start

1. Use a terminal window to navigate to the GridAttackSim directory

2. Start the GridAttackSim GUI

   ```$ python3 GridAttackSim.py```

   ![GridAttackSim GUI](Figures/gui_screenshot.png?raw=true "GridAttackSim GUI")

3. Once the GUI is displayed, as shown above, follow the next steps to
   configure and run a simulation:
   1. Select the simulation parameters: Smart Grid Model, Application,
      Attack Category, Attack Type
   2. Click on the "Run Simulation" button to start the simulation
   3. When the simulation process finishes, click on "Load Results" to
      display the output files
   4. Select the output files of interest, then click on "Show Charts" to
      visualize the results


## References

For a research background regarding GridAttackSim, please refer to the
following papers:
1. T. D. Le, A. Anwar, S. W. Loke, R. Beuran, Y. Tan, "GridAttackSim:
   Cyber Attack Simulation Framework for Smart Grids", MDPI
   Electronics, Special Issue on Applications of IoT for Microgrids,
   vol. 9, no. 8, August
   2020, 1218. [https://doi.org/10.3390/electronics9081218]
2. T. D. Le, A. Anwar, R. Beuran, S. W. Loke, "Smart Grid
   Co-Simulation Tools: Review and Cybersecurity Case Study", 7th
   International Conference on Smart Grid (icSmartGrid 2019),
   Newcastle, Australia, December 9-11, 2019,
   pp. 39-45. [https://ieeexplore.ieee.org/abstract/document/8990712]

For a list of contributors to this project, check the file
CONTRIBUTORS included with the source code.
