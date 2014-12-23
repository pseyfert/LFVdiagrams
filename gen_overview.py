#!/usr/bin/env python
#
# \brief        build html with overview of contents of pdf_files
# \author       Paul Seyfert <pseyfert@physi.uni-heidelberg.de>
# \copyright    Copyright (c) 2014 Paul Seyfert
# \license      GNU Public License, version 2

from __future__ import print_function, unicode_literals

import re, os, io

TEMPLATE_HEADER = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="chrome=1">
    <title>LFVdiagrams: Output diagrams</title>
    <link rel="stylesheet" href="stylesheets/styles.css">
    <link rel="stylesheet" href="stylesheets/pygment_trac.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
    <script src="javascripts/respond.js"></script>
    <!--[if lt IE 9]>
      <script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
    <!--[if lt IE 8]>
    <link rel="stylesheet" href="stylesheets/ie.css">
    <![endif]-->
    <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">

  </head>
  <body>
      <div id="header">
        <nav>
          <li class="fork"><a href="https://github.com/pseyfert/LFVdiagrams">View On GitHub</a></li>
          <li class="downloads"><a href="https://github.com/pseyfert/LFVdiagrams/zipball/master">project-ZIP</a></li>
          <li class="downloads"><a href="https://github.com/pseyfert/LFVdiagrams/tarball/master">project-TAR</a></li>
          <li class="downloads"><a href="https://pseyfert.github.io/LFVdiagrams/LFVdiagrams.tar.gz">diagrams-TAR</a></li>
          <li class="downloads"><a href="https://pseyfert.github.io/LFVdiagrams/LFVdiagrams.zip">diagrams-ZIP</a></li>
          <li class="title">DOWNLOADS</li>
        </nav>
      </div><!-- end header -->

    <div class="wrapper">

      <section>
        <div id="title">
          <h1><a href="index.html">LFVdiagrams</a></h1>
          <p></p>
          <hr>
          <span class="credits left">Project maintained by <a href="https://github.com/pseyfert">pseyfert</a></span>
          <span class="credits right">Hosted on GitHub Pages &mdash; Theme by <a href="https://twitter.com/michigangraham">mattgraham</a></span>
        </div>

        <h1>
<a id="outputdiagrams" class="anchor" href="#outputdiagrams" aria-hidden="true"><span class="octicon octicon-link"></span></a>Output diagrams</h1>

<p>All output files can be downloaded in a single <a href="https://pseyfert.github.io/LFVdiagrams/tarball/">tar-file</a> or <a href="https://pseyfert.github.io/LFVdiagrams/zipball/">zip-file</a> or as individual files below.</p>
<table class="reference" style='table-layout:fixed; font-size:100%' width=675><col width=100><col width=400><col width=200>
"""
TEMPLATE_FOOTER="""</table>
<h2>
<a id="license" class="anchor" href="#license" aria-hidden="true"><span class="octicon octicon-link"></span></a>License</h2>

<p>The diagrams are licensed under the
<a href="https://creativecommons.org/licenses/by-sa/3.0">Creative Commons Attribution-ShareAlike 3.0</a> license.</p>

      </section>

    </div>
    <!--[if !IE]><script>fixScale(document);</script><![endif]-->
    
  </body>
</html>
<table class="reference" style='table-layout:fixed; font-size:100%' width=675><col width=100><col width=400><col width=200>
"""

def compile_entry(name):
  retval = "<tr><td><img src=\"white_png_files/"
  retval += name
  retval += ".png\" /></td>"
  retval += "<td><nav><li class=\"downloads\"><a class=\"download\" href=\"pdf_files/" + name + ".pdf\">PDF</a></li>"
  retval += "<li class=\"downloads\"><a class=\"download\" href=\"png_files/" + name + ".png\">PNG (transparent)</a></li>"
  retval += "<li class=\"downloads\"><a class=\"download\" href=\"white_png_files/" + name + ".png\">PNG (white)</a></li>"
  retval += "</nav></td></tr>\n"
  return retval
  

with io.open('outputs.html', 'wt') as out:
  out.write(TEMPLATE_HEADER)
  import tarfile
  with tarfile.open("LFVdiagrams.tar.gz", "w:gz") as tar:
    for name in os.listdir('pdf_files'):
      tar.add('pdf_files/'+name)
    for name in os.listdir('png_files'):
      tar.add('png_files/'+name)
    for name in os.listdir('white_png_files'):
      tar.add('white_png_files/'+name)
  import zipfile
  with zipfile.ZipFile("LFVdiagrams.zip", "w") as archive:
    for name in os.listdir('pdf_files'):
      archive.write('pdf_files/'+name)
    for name in os.listdir('png_files'):
      archive.write('png_files/'+name)
    for name in os.listdir('white_png_files'):
      archive.write('white_png_files/'+name)
  for f in os.listdir('pdf_files'):
    basename = os.path.splitext(f)[0]
    out.write(compile_entry(basename))
  out.write(TEMPLATE_FOOTER)
