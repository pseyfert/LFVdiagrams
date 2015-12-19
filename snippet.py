# \brief        helper script to interface convert_feynmp with ipynb frontend
# \author       Paul Seyfert <pseyfert@mib.infn.it>
# \copyright    Copyright (c) 2015 Paul Seyfert
# \license      GNU Affero General Public License

from convert_feynmp import TEMPLATE_HEADER, TEMPLATE_FOOTER, u

import io
import os.path
import shutil
import subprocess
import tempfile
import re

MYWD = None

def process(diagram):
    global MYWD
    diagram = re.sub('\\\\','\\\\\\\\',diagram)
    try:
        if MYWD is None:
            MYWD = tempfile.mkdtemp()
        elif not os.path.isdir(MYWD):
            os.mkdir(MYDIR)

        tmpmp =  os.path.join(MYWD, 'dummy.mp')
        tmptex = os.path.join(MYWD, 'dummy-frame.tex')
        tmppdf = os.path.join(MYWD, 'dummy-frame.pdf')
        endpdf = os.path.join(MYWD, 'dummy.pdf')
        endpng = os.path.join(MYWD, 'dummy.png')

        with io.open(tmptex, 'wt',encoding="utf-8") as out:
            out.write(TEMPLATE_HEADER)
            out.write(u("dummy}\n"))
            out.write(u(diagram))
            out.write(u("{"))
            out.write(TEMPLATE_FOOTER)

        cmd_pdflatex = ['pdflatex',
                        '-interaction', 'nonstopmode',
                        '-halt-on-error', tmptex]
        cmd_mpost = ['mpost', tmpmp]
        subprocess.check_call(cmd_pdflatex, cwd=MYWD)
        subprocess.check_call(cmd_mpost, cwd=MYWD)
        subprocess.check_call(cmd_pdflatex, cwd=MYWD)
        subprocess.check_call(['pdfcrop', tmppdf, endpdf], cwd=MYWD)
        subprocess.check_call(['convert','-density','900','-alpha','off','-quality','100', endpdf, endpng], cwd=MYWD)

    # always remove the temporary files
    finally:
        pass
    return endpng, MYWD

