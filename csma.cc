#include <fstream>
#include "ns3/netanim-module.h"
#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/internet-module.h"
#include "ns3/csma-module.h"
#include "ns3/applications-module.h"

using namespace ns3;

int main(int argc, char * argv[])
{
    NodeContainer nodes;
    nodes.Create(4);

    InternetStackHelper stack;
    stack.Install(nodes);

    CsmaHelper csma;
    csma.SetDeviceAttribute("Mtu", UintegerValue(1400));
    csma.SetChannelAttribute("DataRate", DataRateValue(DataRate(5000000)));
    csma.SetChannelAttribute("Delay", TimeValue(MilliSeconds(2)));

    NetDeviceContainer devices;
    devices = csma.Install(nodes);

    Ipv4AddressHelper address;
    address.SetBase("10.1.1.0","255.255.255.0");

    Ipv4InterfaceConatiner interfaces = address.Assign(devices);

    UdpEchoServerHelper echoServer(9);

    ApplicationContainer apps = echoServer.Install(nodes.Get(1));
    apps.Start(Seconds(1.0));
    apps.Stop(Seconds(10.0));

    UdpEchoClientHelper echoClient(interfaces.GetAddress(1),9);
    echoClient.SetAttribute("MaxPackets", UintegerValue(1));
    echoClient.SetAttribute("Interval", TimeValue(Seconds(1.0)));
    echoClient.SetAttribute("PacketSize", UintegerValue(1024));

    apps = echoClient.Install(nodes.Get(0));
    apps.Start(Seconds(2.0));
    apps.Stop(Seconds(10.0));

    #if 0
    echoClient.SetFill(apps.Get(0),"Hello World!");
    echoClient.SetFill(apps.Get(0),0xa5,1024);
    unit8_t fill[] = {1,2,3,4,5,6};
    echoClient.SetFill(apps.Get(0),fill,sizeof(fill),1024);
    #endif

    AnimationInterface anim("csma.xml");
    Simulator::Run();
    Simulator::Destroy();

    return 0 ;
}
