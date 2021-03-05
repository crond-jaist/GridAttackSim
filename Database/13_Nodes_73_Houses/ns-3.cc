/* -*- Mode:C++; c-1ile-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/point-to-point-module.h"
#include "ns3/applications-module.h"
#include "ns3/nix-vector-routing-module.h"
#include "ns3/mobility-module.h"
#include "ns3/csma-module.h"
#include "ns3/point-to-point-dumbbell.h"
#include "ns3/bridge-helper.h"
#include "ns3/wifi-module.h"
#include "ns3/netanim-module.h"
#include "ns3/wimax-helper.h"
#include "ns3/lte-helper.h"
#include "ns3/ipv4.h"
#include "ns3/fncs-application.h"
#include "ns3/fncs-application-helper.h"
#include "ns3/fncs-simulator-impl.h"

#include <cstdlib>
#include <vector>
#include <map>
#include <iostream>
#include <stdexcept>

using namespace ns3;
using namespace std;
int data_rate_peer_to_peer;
int delay_peer_to_peer;
int data_rate_cluster; //10000000bps = 10 Mbps
int delay_cluster; //3 MilliSeconds





struct MarketModel{
    string nodeNamePrefixes;
    int numberofnodes;
    int numberofgroups;
    string marketname;
    vector<NodeContainer> csma;
    NodeContainer market;
};

vector<MarketModel*> parseLinkModel(string name) {

    vector<MarketModel*> toReturn;
    ifstream inputFile(name.c_str());
    if(!inputFile.good())
        throw std::invalid_argument("Cannot open file!");

    MarketModel *toAdd;
    while(!inputFile.eof()){
        toAdd=new MarketModel();
        inputFile >> toAdd->numberofnodes
            >> toAdd->marketname
            >> toAdd->nodeNamePrefixes;
        toAdd->numberofgroups = (toAdd->numberofnodes+19)/20;
        if(toAdd->numberofnodes==0) //ifstream zicti
            continue;
        toReturn.push_back(toAdd);
    }
    return toReturn;

}

int main (int argc, char *argv[])
{
    data_rate_peer_to_peer = 40000000;//40000000 bps = 4 Mbps
    delay_peer_to_peer = 3;
    data_rate_cluster = 10000000; //10000000 bps = 10 Mbps
    delay_cluster = 3; //3 MilliSeconds
    // Don't remove
    //Flag

    if(argc < 2){
        cout << "Usage ./first <power grid link model file name>" << endl;
        return 0;
    }
    int totalNumberOfNodes=0;

    /* reads the list of market models from the linkModel file*/

    /* Each market model is defined by its
     * size (Number of HVAC/controllers)
     * Name of Market (MarkNIF)
     * Prefix of Node Names ( Prefix for controller name)
     * the busid of the bus, market is connected to
     */
    /* totalNumberOfNodes is the sum of size of all market model */
    vector<MarketModel *> networks = parseLinkModel(string(argv[1]));

    cout << "Creating " << networks.size() << " networks." << endl;
    for (size_t i=0; i<networks.size(); ++i) {
        cout << "Network " << i << ": "
            << networks[i]->numberofgroups << " groups of "
            << networks[i]->numberofnodes << " nodes total" << endl;
        totalNumberOfNodes += networks[i]->numberofnodes;
        if (networks[i]->numberofgroups > 255) {
            cerr << "too many groups" << endl;
            return EXIT_FAILURE;
        }
    }
    cout << "Total number of nodes is " << totalNumberOfNodes << "." << endl;

    FncsSimulatorImpl *hb=new FncsSimulatorImpl();
    Ptr<FncsSimulatorImpl> hb2(hb);
    hb->Unref();
    Simulator::SetImplementation(hb2);

    LogComponentEnable ("FncsApplication", LOG_LEVEL_INFO);

    Ipv4NixVectorHelper nixRouting;
    Ipv4StaticRoutingHelper staticRouting;
    Ipv4AddressHelper addresses;
    InternetStackHelper ihelper;
    Ipv4ListRoutingHelper list;
    list.Add (staticRouting, 0);
    list.Add (nixRouting, 10);
    ihelper.SetRoutingHelper (list);

    CsmaHelper chelper;

    //ns3::DataRate::DataRate	(	uint64_t 	bps	)	 bps	bit/s value


    //chelper.SetChannelAttribute ("DataRate", DataRateValue (10000000));
    //chelper.SetChannelAttribute ("Delay", TimeValue (MilliSeconds (3)));

    //chelper.SetChannelAttribute ("DataRate", StringValue ("4Mbps"));
    //chelper.SetChannelAttribute ("Delay", StringValue ("1000000ms"));

    chelper.SetChannelAttribute ("DataRate", DataRateValue (data_rate_cluster));
    chelper.SetChannelAttribute ("Delay", TimeValue (MilliSeconds (delay_cluster)));

    ApplicationContainer fncsaps;

    /* Create the various networks. */
    for (size_t netIndex=0; netIndex<networks.size(); ++netIndex)
    {
        /* First step is to create all of the nodes, the basic building
         * block of ns-3. Each network splits the nodes into groups of
         * 20. A 21st node is for the point-to-point connection back to
         * the market. */
        MarketModel *model = networks[netIndex];
        int groups = model->numberofgroups;
        model->csma.resize(groups);
        for (int csmaIndex=0; csmaIndex<groups; ++csmaIndex) {
            model->csma[csmaIndex].Create(21);
        }
        model->market.Create(1);

        ihelper.Install(model->market);

        NetDeviceContainer *csmaDevices = new NetDeviceContainer[groups];

        for(int i=0;i<groups;i++){
            stringstream ip;
            ip << "10." << netIndex << "." << i << ".0";

            csmaDevices[i] = chelper.Install(model->csma[i]);

            ihelper.Install(model->csma[i]);
            addresses.SetBase(ip.str().c_str(),"255.255.255.0");
            addresses.Assign(csmaDevices[i]);
            ip.str(string());
        }

        PointToPointHelper phelper3;
      //phelper3.SetDeviceAttribute ("DataRate", StringValue ("4Mbps"));
      //  phelper3.SetChannelAttribute ("Delay", StringValue ("2ms"));


        phelper3.SetDeviceAttribute ("DataRate", DataRateValue (data_rate_peer_to_peer));
        phelper3.SetChannelAttribute ("Delay", TimeValue (MilliSeconds (delay_peer_to_peer)));

        //connect market nodes to csma nodes.
        for(int i=0;i<groups;i++){
            stringstream ip;
            ip << "11." << netIndex << "." << i << ".0";

            NetDeviceContainer csma1dbell1=phelper3.Install(
                    model->market.Get(0), model->csma[i].Get(0));

            addresses.SetBase(ip.str().c_str(),"255.255.255.0");
            addresses.Assign(csma1dbell1);

            ip.str(string());
        }

        NodeContainer gldnodes;
        for(int i=0;i<groups;i++){
            for (int j=1; j<21; ++j) {
                gldnodes.Add(model->csma[i].Get(j));
            }
        }

        /* the '1' below is the offset where number of nodes begins */
        FncsApplicationHelper help(model->nodeNamePrefixes, 1);
        fncsaps.Add(help.Install(gldnodes));
        fncsaps.Add(help.Install(model->market.Get(0), model->marketname));
    }

    fncsaps.Start (Seconds (0.0));
    fncsaps.Stop (Seconds (259200.0));

    Simulator::Run ();
    Simulator::Destroy ();
}
