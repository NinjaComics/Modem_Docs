[GSoC] Week Two & Three - Experimental PyBOMBS GUI
##################################################

:date: 2016-06-12 09:51
:tags: gsoc, weekly progress, coding period
:category: /bin
:author: Ravi Sharan
:slug: gsoc_week2_3

In my last `update`_ , I had discussed the motivation behind designing the
GUI frontend for the new `Pybombs`_. In this week's update, I present an almost 
finished GUI for the pybombs (it still lacks an interface to the Pybombs API).  
The gui features a wizard, where it prompts for the user to fill in/choose the
prefix and the contents in the main window are displayed according to the chosen
prefix. The OOT Modules are listed out in the main window along with some more
information like the category, a one line description of the package and the
remote repository. There's a Module info dialog from which one can query the module
information and it's dependencies. Like I mentioned in my previous update, I have
borrowed the design idea from `Synaptic`_ and `Pamac`_ package managers, with some 
addition of graphics to make it look a bit more orangy.

What's left ? 
=============

By mid-term evaluatation period, I am looking forward to completely interface the 
GUI with the Pybombs API and polish the graphics a bit more. Also, during the 
interaction sessions with my mentor, Martin Braun, we have decided to make 
the GUI frontend installable from within pybombs, which will look something like:


::

    pybombs install <pybombs-gui-frontend>    

That makes it a small update for this week and here's a small `screencast`_ I have made,
on how the GUI will look like. 

Pip-pip !

.. _Pybombs: https://github.com/gnuradio/pybombs
.. _Synaptic: http://www.nongnu.org/synaptic/
.. _Pamac: https://github.com/manjaro/pamac
.. _update: http://ninjacomics.github.io/radioblogr/2016/05/gsoc_week_one.html 
.. _screencast: https://www.youtube.com/watch?v=VVN534cHtm4 
