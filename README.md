LFVdiagrams
===========

These are some Feynman diagrams which may be usefull when discussing the
charged lepton flavour violating process τ→μμμ. To allow users to modifiy them
or extend them, the code is provided and users are invited to describe e.g.
µ→eee.

origin
======

The diagrams are partially self drawn, following the feynmp/feynmf
documentation, partially they are modified versions of diagrams provided within
FDL (see LICENSE.md).

usage
=====

``` cd code ```
``` source build.sh ```

requirements
============

It should be rather obvious that mpost and pdflatex are required. On top of
that I'm using the hepnicenames package for the labels. By modifying the tex
files, this dependency can be removed. Further depencencies certainly exist.

TODO
====

 - The build process takes place in /tmp/ which should better be an mktemp -d
   directory.

 - An annoyance is that the fmffile name, specified within the tex file, has to
   coincide with the tex filename.
