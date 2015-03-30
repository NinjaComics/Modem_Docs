CGRAN - A new look
##################

:date: 2015-03-29 20:17
:tags: CGRAN, GNU Radio
:category: /bin
:author: Ravi Sharan
:slug: gr-cgran

Recently I have been working on giving Comprehensive GNU Radio Archive Network 
(CGRAN) a new look. While the `old CGRAN site`_ was built using trac wiki pages,
the new one looks more like a standard website, with nitty-gritty details like 
gnuradio version dependencies, tags associated with each OOT Module, more info
about OOT module developers, etc., all packed in one place. The site's built 
using `pelican`_ static site generator (Hey ! I use pelican for building this blog
as well :D) and uses bootstrap-material-design framework by Fez Vrasta, to style
the site. Design is not just the only attraction to this site - the module page
information is automated and most important of all, the site's tightly copuled 
with `PyBOMBS`_. Read along to know more ! 

Design Idea
===========
  
First off, the site's built with bits and pieces collected from different sources:

* `Bootstrap Material Design framework`_ by Fez Vrasta(with some customization) 
  to style the site.
* `Bootstrap tables plugin`_ by Wenzhixin, to make life with tables easy(OOT Module 
  List).
* `Pelican-md-metayaml`_ plugin to read the YAML metadata and generate Module 
  pages.

Also, while designing the site, I took a bit of linience in borrowing ideas from
two similar websites - `atom.io`_ and `customelements.io`_. The front-page looks 
similar to the `customelements.io`_ with more emphasis on the list of OOT Modules. 
Unlike `customelements.io`_, which is a standalone site for collection of various 
polymer elemets, CGRAN is a part of the GNU Radio family and it was enough that
we display the condensed top-matter, as all the extra information concerning OOT 
Modules is available on GNU Radio wiki. That said, there are relevant links on
the site to connect to the right wiki page :)

Rule Zero : PyBOMBS and CGRAN
=============================

Intelligent CGRAN and integrating it with PyBOMBS has been the top priority ever 
since PyBOMBS task force came into picture. The idea is to automatically generate
a list of OOT modules available as PyBOMBS recipes and display them on CGRAN. 

What does this mean ? 

* The OOT Module developer has to write a PyBOMBS recipe,
* Pull a request for the recipe to be accpeted into PyBOMBS repo, 
* Fill in the details in the Manifest file created by gr-modtool, in the module
  repo,
* Sit back while the CGRAN site collects information about the new module and 
  generate a new page for it. 

Simple isn't it ?

Module Pages and Manifest
=========================

I always liked the `atom.io`_'s way of displaying a detailed information on its 
package/theme on a separate page(that way, the user can stay in a place and get
more info about a project). I created the OOT Module pages in a similar fashion, 
but `atom.io`_ uses the package/theme's README to display information on it's project 
info page. This doesn't fit the CGRAN model, as few already existing OOT Modules
have license embedded into their README file. Not only does the user have to
scroll down to get past the license information, it looks a bit odd on the
individual pages. So what did we do ?
Enter `Manifest.yaml`_ (the format's subject to change) !!! The Manifest.yaml 
provides few mandatory fields to fill in, along with a description field, where
the OOT Module author can write any information regarding the module, which 
he/she thinks will be of best interest to the user.

Now, why is YAML the preferred file format ?

* It is human readable
* Easily readable on github (Assuming the OOT Modules reside on github)
* CGRAN can scrape the necessary information to generate info for Module pages
  in markdown format (remember intelligent CGRAN ?)

Let's talk Logo
===============

Finally, let's talk a bit about the logo. The new CGRAN logo is designed to 
resemble an ecosystem of OOT Modules built around GNU Radio. **Self-interest-alert-**
I am a Dragon Ball fan. That's why there are exactly seven circles,(including 
the GNU Radio circle) in the logo resembling the seven dragon balls spread across 
as a network ;) 

What Next ?
===========
While we have come far from a trac based site to an automated site for CGRAN,
more features (like repo stats, to name one) are to be implemented up the sleeve
without posing any overhead to the OOT Module authors. 

*P.S The current state of CGRAN could not have been achieved, if not for constant
inputs from Nathan West and other PyBOMBS Task Froce members :)*

.. _old CGRAN site: https://web.archive.org/web/20140829151613/https://www.cgran.org/wiki/Projects
.. _pelican: http://blog.getpelican.com/
.. _PyBOMBS: http://gnuradio.org/redmine/projects/pybombs/wiki
.. _Bootstrap Material Design framework: https://github.com/FezVrasta/bootstrap-material-design
.. _Bootstrap tables plugin: http://bootstrap-table.wenzhixin.net.cn/
.. _Pelican-md-metayaml: https://github.com/joachimneu/pelican-md-metayaml
.. _atom.io: https://atom.io/
.. _customelements.io: http://customelements.io/
.. _Manifest.yaml: https://github.com/n-west/manifests
