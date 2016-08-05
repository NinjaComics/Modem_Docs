[GSoC] Weekly Update
####################

:date: 2016-08-05 20:50
:tags: gsoc, weekly progress, coding period
:category: /bin
:author: Ravi Sharan
:slug: gsoc_cgran_progress

This log is a condensed report about my GSoC progress for the past two weeks.
Quick update is, pybombs-gui is now on PyPi as a pre-release package. On the
other hand, I am working on the "Install from CGRAN", which is a part of my
proposal. Read along for more updates.

Pybombs on PyPi and CGRAN Fixes
===============================

As mentioned above, I have pushed the pybombs-gui package as a pre-release package
on PyPi. I am looking forward to release the GUI at the end of my GSoC, along
with few bug fixes to the Pybombs-cli. There are a few things left before I can
push the code for a full release. The idea is to make pybombs-gui installable
from pybombs-cli. The recipe takes care of the PyQt5 dependencies and the
gui-package is installable using Pip. Also I am working on a new icon for the
gui - expect for more orange flavor. Maybe ?

On the CGRAN part, I am working on an idea similar to AptUrl, to install/prompt
for package installation, from the CGRAN website. If the site is accessed on a
Linux distro with Gnome or KDE, the default terminal emulator is invoked and
pybombs will try to install package from website in the default prefix. If pybombs
is not installed, the user is displayed an "Unable to install message" (obviously).

GSoC is about to end in another 15-18 days time and I am planning to finish off
the tasks as quickly as possible. Hopefully, by the end of the GSoC period, we
will have a new pybombs-gui and new features for CGRAN website. That makes it
a short update. For now, pip-pip !
