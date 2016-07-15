[GSoC] Pybombs GUI - Weekly Update
##################################

:date: 2016-07-15 20:50
:tags: gsoc, weekly progress, coding period
:category: /bin
:author: Ravi Sharan
:slug: gsoc_weekly_report

This week I worked on refining the UI and getting things ready for the release.
One more thing I have worked on this week is separating the GUI and the time
consuming features that power up the GUI, like generating data and installing
packages etc., using Qt framework's QThread functionality. The app now doesn't
lose focus while installing/updating/removing packages or generating data or
while adding recipes from a remote URL. Read along to know more bombs, pybombs !

To SUDO or to pkexec:
=====================

`pybombs-cli`_ uses sudo for authentication, like I mentioned in my previous week's
update. The advantage of sudo or the sudo based GUI frontends is that one doesn't
have to authenticate for a certain time period (that's 5 minutes to be precise).
Disadvantage is that these sudo based GUI frontends may or may not be available on
all distros and we might have to add another dependency just for granting elevated
privileges.
Another alternative is to use `pkexec`_, an authentication mechanism based on polkit.
The good part about pkexec is, it is available on all distros by default and uses
an authentication agent that is native to the distro - meaning no dependencies.
But, like I mentioned in this `issue`_, depending on the policies available,
and given the fact that pybombs packs different native package managers, one
might have to authenticate for elevated privileges every time a different package
manager requests for elevated privileges, while performing tasks with pybombs.
This can be overcome by using policies for different package managers while using
pybombs in GUI mode and using using sudo as the authentication agent while running
pybombs in cli mode.

Collecting and displaying logs:
===============================

Providing information on what went wrong(or right), while performing a task
using GUI makes it more easy to use. The pybombs-cli uses python's logging module
to display information on what's happening while pybombs is running. The idea is
to route this information to the GUI while performing the install/update/remove
tasks or while creating a prefix for example.

Release and Moving onto next deliverable:
=========================================

Finally, I am looking forward to release a usable GUI frontend for pybombs,
by mid next week. I am testing the GUI on different distros and so far I like how
the GUI looks all nice on Fedora 23 and 24. The app inherits the GTK style so well
on Fedora. The progress can be tracked at `gitlab`_ repo.
Apart from working on pybombs-gui, I have also started working
a bit on the CGRAN site, which happens to be my next deliverable. For now,
Pip pip ! If you followed this post till here, enjoy this random `xkcd comic strip` !


.. _pybombs-cli: https://github.com/gnuradio/pybombs
.. _gitlab: https://www.gitlab.com/NinjaComics/pybombs-qtgui
.. _random xkcd comic: https://c.xkcd.com/random/comic/
.. _pkexec: https://www.freedesktop.org/software/polkit/docs/0.105/pkexec.1.html
.. _issue: https://github.com/gnuradio/pybombs/issues/369
