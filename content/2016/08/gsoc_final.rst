[GSoC] Summary, Final Submission, Future Work
#############################################

:date: 2016-08-22 20:50
:tags: gsoc, final evaluation, coding period
:category: /bin
:author: Ravi Sharan
:slug: gsoc_final_eval

This summer I was very fortunate to work on GNU Radio's installer - Pybombs,
with my mentors Martin Braun and Nathan West, as a part of GSoC '16. I have
worked on several features like developing a PyQt5 based GUI for Pybombs
installer, improve CGRAN website and add some cool features to improve the
overall user experience while using the installer and the CGRAN site. This log
marks the last of the entries under the GSoC tags. Read along to know more
about my contributions during the GSoC program.

PyBOMBS-QTGUI - Design and Development:
=======================================

Developing a GUI frontend for GNU Radio's installer - PyBOMBS was the first
deliverable of my GSoC proposal. One of the prime goals I had in mind while
designing the GUI was to keep it as simple as possible. During the design
phase, I have gone through several existing package managers. PyBOMBS-QtGUI's
design is inspired from two such package manager frontends - Synaptic and Pamac.
While keeping the application's usage as simple as possible, I have added a few
graphics to make it more visually asthetic. A link to few screenshots and a
screencast featuring PyBOMBS-QtGUI can be found at the end of this article.

CGRAN - new look and integration with PyBOMBS:
==============================================

In the final month of the coding period, I have working making CGRAN site look
similar to the new GNU Radio site. Along with the apperance of the front page,
I have added a few features like tag highligting and fixed few minor issues of
the site. The module pages now features a "Install from CGRAN" button to install
individual OOT Modules directly from the CGRAN site. These modules are installed
to the default prefix, if PyBOMBS is already installed on the host PC.

Apart from adding new look to CGRAN, I have also worked on PybombsUrl - a host
side python packag which handles the pybombs URLs and allows to install modules
directly from the CGRAN site.

PybombsUrl works in two modes - Terminal and the GUI mode. If the host side PC
has PybombsGUI installed, a GUI window is presented to the user to install the
desired packages from CGRAN. If the package is unable to detect the presence of
PybombsGUI, it switches back to the terminal mode and the packages are installed
from the default-terminal of the Desktop Environment. A link to few screenshots
of PybombsUrl and CGRAN are provided at the end of this article.

The learning curve:
===================

PyQt5:
++++++

For most part of the coding period, I have learnt a lot on how to develop GUI
applications using the PyQt5 libraries. Although I had no prior experience developing
GUI applications, I have enjoyed every bit of designing and developing the PybombsGUI.
During the process, I have learned a lot on how to sepearate the GUI and code for
smooth user experience and multithreading using the QThread libraries. During the
design phase, I have tried to add a flavor of orange to the wherever necessary, 
to bring the feel and look of GNU Radio project.

PybombsUrl:
+++++++++++

I spent some valuable amount of time researching on how to interface a website
with the client side Desktop environment. To enable the PybombsUrl feature, I
have created a custom protocol/URL handlers and learned a bit more about the
internals of custom protocol/URL handlers. A plus side of all this, I have improved
a lot on my coding skills during the program

Community bonding and help:
+++++++++++++++++++++++++++

While writing the proposal, I have assumed the development of the Qt app to be
on the easy side, but I had a few challenges in understanding the working mechanism
of the Qt libraries during and after the mid-term evaluation period.
During the development phase of the app, I have spent quite some time lurking on
the pyqt and qt irc channels and have pestered the mods with a lot of questions
on the working of Qt apps. Thanks to the PyQt IRC members for the help.


Future Work:
============

Both PybombsGUI and PybombsUrl are now available as pre-developer and alpha
release packages respectively. I am definitely looking forward to add more
features to these projects and see if there can be any improvement to be done
on the CGRAN side. One thing that I am looking forward to improve on the CGRAN
side is to add more documentation to the module pages, to make it a one stop
shop information source on 3rd party OOT Modules. Another feature I am looking
forward to work on is to provide a mirror repository of all the 3rd party OOT
Modules which can serve CGRAN and PyBombs at the same time.

Working with Mentor:
====================

Finally, I am thankful to my mentors Martin Braun and Nathan West, for providing
me an opportunity to contribute to the GNU Radio community as a part of GSoC program.
Martin Braun's weekly calls have really helped me in decision making throughout
the  program. The final section of this log entry holds the links/URls to all my
work during the GSoC program. Finally, I look forward to contribute more to the
community in coming days and fix the above said issues.

For now, pip-pip !

Links and URLs to Repositories, PRs and Screenshots:
====================================================

