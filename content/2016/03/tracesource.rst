Custom tracesource to get CQI info in ns-3 apps
###############################################

:date: 2016-03-10 13:37
:tags: ns3, Tracing
:category: /bin
:author: Ravi Sharan
:slug: Tracing

I am updating something on this blog exactly after a year - minus 19 days plus 
a leap day. In this post, I will walkthrough the steps required to add a tracesource 
and a corresponding tracesink in ns-3 applications to acquire the downlink Channel 
Quality Indicator (CQI) information sent by each UE attached to the respective 
eNB in the network. 

A bit about CQI in lte - the eNB receives information from the UE
in the form of CQI (ranging from 0 to 15), according to the perceived downlink 
channel at the UE. The higher the CQI, the better the channel is. Thus, based on 
the CQI received from the UE, appropriate modulation & coding scheme (MCS) is used 
to serve the UE better. The CQI reporting modes can either be periodic or aperiodic 
in time and wideband or subband in frequency, based on the eNB implementation.
Further information on CQI reporting can be found elsewhere on the internet. 
For now, let's get to the main part of this log.

Custom tracesource and Callback for CQI
=======================================

Add the following piece(s) of code in the respective files in your ns-3 source
tree:

In ``lte-enb-phy.cc``:

Adding a TraceSource


.. code-block:: C++

   .AddTraceSource ("ReportCqiValues",
                    "DL transmission PHY layer CQI statistics.",
                    MakeTraceSourceAccessor (&LteEnbPhy::m_reportCqiTrace),
                    "ns3::LteEnbPhy::ReportCqiTracedCallback")

In ``lte-enb-phy.h``:

Adding a TracedCallback declaration


.. code-block:: C++
   
   TracedCallback<uint16_t, uint16_t, std::vector <uint8_t> > m_reportCqiTrace;


The typedef for the callback function signature


.. code-block:: C++

   typedef void (* ReportCqiTracedCallback)
       (uint16_t cellId, uint16_t rnti, std::vector <uint8_t>);

What did we do in the previous section ?
========================================

In the above section, the ``AddTraceSource`` provides hooks to the ns-3 application 
using the Config system, the ``TracedCallback< >`` contains trace information about the
CQI and the typedef void ``(* ReportCqiTraceCallBack)`` provides a callback 
mechanism to the tracesource we just created.

In ns-3, the CQI values from each UE, packed in the form of control messages 
appear at three levels in the ns-3's lte stack - PHY, MAC and the Scheduler. We
catch the CQI values at the lowest level of the stack and route it to our application.
Specifically, we are piping the information held in the ``CqiListElements_s`` struct
that is later passed onto the MAC and to the Scheduler layer for further decision making.

The further process of connecting a tracesink to the source, in the application,
is left to the reader. In essence, the tracing mechanism in ns-3 provides a neat
solution to pipe the information that the stack uses during the simulation, without 
disrupting the actual simulation.  

Pip-Pip !
