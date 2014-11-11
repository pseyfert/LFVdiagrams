#!/usr/bin/env python
#
# \brief        convert small tex snippets w/ feynmap fmfgraph's to pdfs
# \author       Moritz Kiehn <kiehn@physi.uni-heidelberg.de>
# \copyright    Copyright (c) 2014 Moritz Kiehn
# \license      GNU Public License, version 2

from __future__ import print_function, unicode_literals

import io
import os.path
import shutil
import subprocess
import sys
import tempfile

# portable python2 / python3 unicode conversion
if sys.version < '3':
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x


EXIT_FAILURE = 1
TEMPLATE_HEADER = """\\documentclass{minimal}
\\usepackage[utf8]{inputenc}
\\usepackage{feynmp}
\\usepackage{hepnicenames}
\\DeclareGraphicsRule{.1}{mps}{*}{}
\\begin{document}
\\input{"""
TEMPLATE_FOOTER = """}
\\end{document}
"""

def main(input_path, output_path):

    input_name = os.path.splitext(os.path.basename(input_path))[0]
    input_path = os.path.abspath(input_path)
    output_path = os.path.abspath(output_path)

    try:
        tmpdir = tempfile.mkdtemp()
        tmpmp =  os.path.join(tmpdir, input_name + '.mp')
        tmptex = os.path.join(tmpdir, input_name + '-frame.tex')
        tmppdf = os.path.join(tmpdir, input_name + '-frame.pdf')

        with io.open(tmptex, 'wt') as out:
            out.write(TEMPLATE_HEADER)
            out.write(u(input_path))
            out.write(TEMPLATE_FOOTER)

        cmd_pdflatex = ['pdflatex',
                        '-interaction', 'nonstopmode',
                        '-halt-on-error', tmptex]
        cmd_mpost = ['mpost', tmpmp]
        subprocess.check_call(cmd_pdflatex, cwd=tmpdir)
        subprocess.check_call(cmd_mpost, cwd=tmpdir)
        subprocess.check_call(cmd_pdflatex, cwd=tmpdir)
        subprocess.check_call(['pdfcrop', tmppdf, output_path], cwd=tmpdir)

    # always remove the temporary files
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

if __name__ == '__main__':
    main(*sys.argv[1:])
