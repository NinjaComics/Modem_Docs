[GSoC] Pybombs GUI - Condensed progress for past four weeks
###########################################################

:date: 2016-07-08 18:51
:tags: gsoc, weekly progress, coding period
:category: /bin
:author: Ravi Sharan
:slug: gsoc_condensed_report

I am updating this blog almost after a month. This is a condensed report on my
GSoC progress so far. The progress has been really slow but on the brighter side,
I have made a good amount of changes to the design.

The gui displays the application, baseline and prefix specific/sdk packages
in two separate pages. Apart from displaying the list of packages, there is a
recipe manager and a prefix manager to handle the prefixes and recipes in a proper
way. Read along for more information on the design.

Prefix Manager:
===============

Prefix management in the pybombs-gui is split into two parts. One is the prefix
config dialog and the other is a prefix chooser. The prefix config dialog works
like the :code:`pybombs prefix init` command. Bonus, you can even add a virtualenv
to the prefix by just ticking a checkbox, while creating it - just like
`pybombs-cli`_.

The prefix chooser does what it says - choose a prefix from the list of available
prefixes and load the respective recipes. The idea here is to present the
user with those packages that are specific to the prefix, rather than displaying
recipes from all the recipe repositories. Currently, the tableview is posing a bit
of a problem by not refreshing the content after choosing a prefix. Fixing this is
the top priority now.

Recipe Manager:
===============

The recipe manager dialog displays a list of recipe aliases, the source and the
directory in which those recipes reside. By default, pybombs ships with basic
recipes required to run it in a minimal mode. One can add the other recipes
similar to the :code:`pybombs recipes add <recipe-alias> <recipe-repo uri>` command.
Again, functionality is similar to what you see with the pybombs-cli.

When pybombs-gui is launched, it checks for the existing prefixes and if it
doesn't find any suitable prefix or recipes to load, the prefix config dialog
followed by a recipe manager dialog are presented to the user and the main window
is displayed only when the user has created a prefix and added the recipes. If
the default prefix is present, the main window loads those recipes specific to
that prefix.

Main Window:
============

The main window displays the prefix specific recipes, baseline packages and the
sdk packages (if any) separately as stated above. A package can be selected by
right clicking the row it is present and based on the package's status(install/
update/remove), a context menu is provided to the user to choose from. Apart
from the status of the package, the module info also can be viewed on a per
package basis. One thing that I am not really sure about adding to this context menu
is the package flags - forcebuild from source and forcedinstall flags. Just a small
addition - Can be done !
Once the user is happy with the selected packages, applying changes will automatically
take care of installing, updating and removing the packages in a sequential manner
(can turn out to be a time consuming process).

Apart from the abovementioned dialogs, there is a running config dialog which displays
the current local and global config. And there's also a new recipe dialog which helps
to create a recipe from within pybombs.

What's left ?
=============

There are serious to less serious issues I am currently dealing with and hoping 
to complete the deliverable as soon as possible. Here are a list of problems I am
currently working on to finish this deliverable:

- The app throws a lot of stdout, stderr and other pybombs' specific log messages.
  One solution can be to redirect this output to a textedit for better logs.
- Use an intelligent way to cater the elevated privileges issue. Solution is to
  use polkit to present the authentication system whenever pybombs' gui requires
  elevated privileges. I am still learning on how to use it and a help in any form
  in this direction is much welcome (Actually I will be more happy to have someone
  help me fixing this).
- Refresh the table content once the changes are applied to the packages. Currently,
  the app doesn't refresh the table content in the main window until and unless it
  gets the focus back or sometimes restart. Serious issue, but can be fixed with little
  effort.


Apart from working on the GUI, I am alos working on fixing the pybomb's backend a bit.
Finally the repository is hosted at `gitlab`_ as mentioned in my previous update.
Also, I am recording some `screencasts`_ to mark the progress (explaining GUI is
tough.Duh). Also, I will be updating the progress on blog every Friday, hereafter.
For now, Pip-pip !

.. _pybombs-cli: https://github.com/gnuradio/pybombs
.. _screencasts: https://www.youtube.com/watch?v=tN0KIX0YE4w
.. _gitlab: https://www.gitlab.com/NinjaComics/pybombs-qtgui
