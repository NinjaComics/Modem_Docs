[GSoC] Week One - Pybombs Frontend & Design Idea
################################################

:date: 2016-05-29 14:45
:tags: gsoc, weekly progress, coding period
:category: /bin
:author: Ravi Sharan
:slug: gsoc_week_one

One week into `GSoC`_ coding period and I have been working on finalizing the
GUI design for `Pybombs`_. While I was writing the proposal for GSoC, I had in 
mind a design similar to the `Synaptic`_ package manager. Synaptic is one of 
the popular GUI front-ends for the apt tool and anyone coming from the Debian and 
Ubuntu world will more than agree to it. 

Another graphical package manager that picqued my interest is `Pamac`_, a GTK3 
based GUI frontend for pacman(The package manager for Arch Linux) and ships with
the Antergos distro. Both Pamac and Synaptic have a table view which lists out 
the packages available, followed by a brief description and other information 
like version number etc., in the subsequent columns.  

The Pybombs1 appstore had a grid view displaying the OOT Modules with an icon for
each module. Although the UI looked simple, with the lack of proper branding of OOT
Modules, only one thumbnail picture appeared for most of the OOT Modules. The reason
behind choosing the tableview approach mentioned above is to keep the UI simple and 
clean, while providing a bit more information on the OOT Modules like the version 
number, repository URL, etc., that are available from the recipe files.

Progress and Update for next Week
=================================

Currently, all the design and development is being done on Antergos distro and
I am using PyQt5 as the GUI toolkit along with Qt Designer to design most of the UI. 
Although most of the design is complete, I am still working on polishing certain areas 
of the design. In the next week, I intend to bind the existsing pybombs API with the UI and 
come up with a minimalistic frontend for Pybombs. I will post my progress and design files
on the mailing list during next week to get feedback on the design before proceeding with 
any changes to the original pybombs repo.  

Pip Pip !

.. _GSoC: https://summerofcode.withgoogle.com/
.. _Pybombs: https://github.com/gnuradio/pybombs
.. _Synaptic: http://www.nongnu.org/synaptic/
.. _Pamac: https://github.com/manjaro/pamac  
