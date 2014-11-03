#!/usr/bin/env python
#
# \brief        convert small tex snippets w/ feynmap fmfgraph's to pdfs
# \author       Moritz Kiehn <kiehn@physi.uni-heidelberg.de>
# \copyright    Copyright (c) 2014 Moritz Kiehn
# \license      GNU Public License Version 2

from __future__ import print_function, unicode_literals

import io
import os.path
import shutil
import subprocess
import sys
import tempfile


EXIT_FAILURE = 1
TEMPLATE_HEADER = """\\documentclass{minimal}
\\usepackage[utf8]{inputenc}
\\usepackage{feynmp-auto}
\\usepackage{hepnicenames}
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
        tmptex = os.path.join(tmpdir, input_name + '-frame.tex')
        tmppdf = os.path.join(tmpdir, input_name + '-frame.pdf')

        with io.open(tmptex, 'wt') as out:
            out.write(TEMPLATE_HEADER)
            out.write(input_path)
            out.write(TEMPLATE_FOOTER)

        cmd_pdflatex = ['pdflatex',
                        '-interaction', 'nonstopmode',
                        '-halt-on-error', tmptex]
        args = {'cwd': tmpdir, 'universal_newlines': True}
        subprocess.check_call(cmd_pdflatex, **args)
        subprocess.check_call(cmd_pdflatex, **args)
        subprocess.check_call(['pdfcrop', tmppdf, output_path], **args)

    # always remove the temporary files
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)

if __name__ == '__main__':
    main(*sys.argv[1:])
