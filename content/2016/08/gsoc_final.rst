[GSoC] Summary, Final Submission, Future Work
#############################################

:date: 2016-08-22 20:50
:tags: gsoc, final evaluation, coding period
:category: /bin
:author: Ravi Sharan
:slug: gsoc_final_eval

|

.. image:: http://ninjacomics.github.io/radioblogr/images/gsoc_banner.png

|

This summer I was very fortunate to work on GNU Radio's installer - Pybombs,
with my mentors Martin Braun and Nathan West, as a part of GSoC '16. I have
worked on several features like developing a PyQt5 based GUI for Pybombs
installer, improve CGRAN website and add some cool features to improve the
overall user experience while using the installer and the CGRAN site. This log
marks the last of the entries under the GSoC tags. Read along to know more
about my contributions during the GSoC program.

PyBOMBS-QTGUI - Design and Development:
=======================================

|

.. image:: http://ninjacomics.github.io/radioblogr/images/pybombsgui.png

|


Developing a GUI frontend for GNU Radio's installer - Pybombs was the first
deliverable of my GSoC proposal. One of the prime goals I had in mind while
designing the GUI was to keep it as simple as possible. During the design
phase, I have inspected several existing package manager GUIs. PyBOMBS-QtGUI's
design is inspired from two such package manager frontends - Synaptic and Pamac.
While keeping the application's usage as simple as possible, I have added a few
graphics to make it more visually asthetic. Few key features of Pybombs-QtGUI:

- Recipes are loaded from the active prefix.
- Separate Prefix manager and Recipe manager dialogs.
- A dialog to add new recipe to the active prefix.
- The application consumes a few KBs of memory when installed.

A link to few screenshots and a screencast featuring PyBOMBS-QtGUI can be found
in the futher sections of this article.

CGRAN - new look and integration with PyBOMBS:
==============================================

|

.. image:: http://ninjacomics.github.io/radioblogr/images/new_cgran.png

|

In the final month of the coding period, I have worked on making CGRAN site look
similar to the new GNU Radio site. Along with the apperance of the front page,
I have added a few features like tag highligting and fixed few minor issues of
the site. The module pages now features a "Install from CGRAN" button to install
individual OOT Modules directly from the CGRAN site. These modules are installed
to the default prefix, if Pybombs is already installed on the host PC.

Apart from adding new look to CGRAN, I have also worked on PybombsUrl - a host
side python package which handles the Pybombs' URLs and allows to install modules
directly from the CGRAN site.

PybombsUrl works in two modes - Terminal and the GUI mode. If the host side PC
has PybombsGUI installed, a GUI window is presented to the user to install the
desired packages from CGRAN. If the package is unable to detect the presence of
PybombsGUI, it switches back to the terminal mode and the packages are installed
from the default-terminal of the Desktop Environment. Few key features of this
deliverable are:

- CGRAN site is designed to blend in with the new `gnuradio`_ site
- OOT Modules can be installed from the CGRAN website using PybombsUrl
- Pybombsurl uses a custom protocol to handle the install from CGRAN feature
- On the client side, the pybombsurl python package handles the pybombs' URLs
- Packages can either be installed from GUI or from terminal, depending upon
  the availability of the GUI package

A link to few screenshots of PybombsUrl and CGRAN are provided in the next
section of this article.

Links and URLs to Repositories, PRs and Screenshots:
====================================================

PybombsGUI and PybombsUrl Gitlab Repos:
+++++++++++++++++++++++++++++++++++++++

- `PybombsGUI Gitlab Repository`_
- `PybombsUrl Gitlab Repository`_

List of commits and Pull requests:
++++++++++++++++++++++++++++++++++

- `List of commits for PybombsGUI`_  Complete commit history of the package
- `List of commits for PybombsUrl`_  Complete commit history of the package
- `Pull request 1 to Pybombs`_ This PR addresses the `issue #348`_
- `Pull request 2 to Pybombs`_ This PR includes fix to `issue #363`_ and `issue #369`_. Along with that recipe files are added for PybombsUrl and PybombsGUI
- `Pull request to gr-recipes`_ Adds documentation to reflect in PybombsGUI
- `Pull request to gr-etcetera`_ Adds documentation to reflect in PybombsGUI
- `Pull request to cgran.org`_ Reflects new design changes, custom protocol handler for pybombs' URLs along with few fixes.

PybombsGUI and PybombsUrl PyPI packges:
+++++++++++++++++++++++++++++++++++++++

Both PybombsGUI and PybombsUrl are available on PyPI as pre-developer release
packages and they can be found at:

- `PybombsGUI PyPI package`_
- `PybombsUrl PyPI package`_

Screenshots and screencast of a working PybombsGUI:
+++++++++++++++++++++++++++++++++++++++++++++++++++

- `PybombsGUI screencast`_
- `PybombsGUI screenshots`_

The Learning Curve:
===================

PyQt5:
++++++

For most part of the coding period, I have learnt a lot on how to develop GUI
applications using the PyQt5 libraries. Although I had no prior experience
developin GUI applications, I have enjoyed every bit of designing and developing
the PybombsGUI. During the process, I have learned a lot on how to sepearate the
GUI and code for smooth user experience and multithreading using the QThread
libraries. During the design phase, I have tried to add a flavor of orange to
the application wherever necessary, to bring the feel and look of GNU Radio project.

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
on the working of Qt apps. Thanks to the PyQt IRC members for the help. Along
with the communication on IRC, I have interacted with few GNU Radio community
members on the mailing list to update the progress during the coding period.

Future Work:
============

Both PybombsGUI and PybombsUrl are now available as pre-developer and alpha
release packages respectively. I am definitely looking forward to add more
features to these projects and see if there can be any improvement to be done
on the CGRAN side. Even after GSoC, I plan on supporting the CGRAN and Pybombs' 
tools. Few areas I am looking forward to work on before the release of the
packages are:

- [CGRAN] Add more documentation to the module pages, to make it a one stop shop
  information source on 3rd party OOT Modules.
- [Pybombs and CGRAN] Provide a mirror repository of all the 3rd party OOT Modules which can serve
  CGRAN and PyBombs at the same time.
- [Pybombs] Proper handling of QThread functionality in the Pybombsgui.
- [Pybombs] A more realistic progress bar implementation in the Pybombsgui.

I am looking forward to address all these issues in the coming 1-2 weeks and
release both PybombsGUI and PybombsUrl as stable packages.

Acknowledgements and Working with Mentor:
=========================================

Finally, I am thankful to my mentors Martin Braun and Nathan West, for providing
me an opportunity to contribute to the GNU Radio community as a part of GSoC program.
Martin Braun's weekly calls have really helped me in decision making throughout
the  program. I look forward to contribute more to the GNU Radio community in coming days.

For now, pip-pip ! Here's a `random xkcd cartoon strip`_ :)

.. _PybombsGUI Gitlab Repository: https://gitlab.com/NinjaComics/pybombs-qtgui
.. _PybombsUrl Gitlab Repository: https://gitlab.com/NinjaComics/pybombsurl
.. _List of commits for PybombsGUI: https://gitlab.com/NinjaComics/pybombs-qtgui/commits/master
.. _List of commits for PybombsUrl: https://gitlab.com/NinjaComics/pybombsurl/commits/master
.. _Pull request 1 to Pybombs: https://github.com/gnuradio/pybombs/pull/356/commits
.. _Pull request 2 to Pybombs: https://github.com/gnuradio/pybombs/pull/367/commits
.. _Pull request to gr-recipes: https://github.com/gnuradio/gr-recipes/pull/42/commits
.. _Pull request to gr-etcetera: https://github.com/gnuradio/gr-etcetera/pull/14/commits
.. _Pull request to cgran.org: https://github.com/n-west/cgran.org/pull/2/commits
.. _PybombsGUI PyPI package: https://pypi.python.org/pypi/PyBOMBS-QtGUI/
.. _PybombsUrl PyPI package: https://pypi.python.org/pypi/PybombsUrl/
.. _issue #348: https://github.com/gnuradio/pybombs/issues/348
.. _issue #369: https://github.com/gnuradio/pybombs/issues/369
.. _issue #363: https://github.com/gnuradio/pybombs/issues/363
.. _random xkcd cartoon strip: https://c.xkcd.com/random/comic/
.. _PybombsGUI screencast: https://youtu.be/LJ_610wAsLk
.. _PybombsGUI screenshots: https://drive.google.com/drive/folders/0By6XhrfIWygqaU05ajVGVzREMU0?usp=sharing
.. _gnuradio: gnuradio.org
