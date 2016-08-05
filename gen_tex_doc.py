# -*- coding: utf-8 -*-
import argparse
import os

from preamble import pgf_with_custom_preamble

header = r"""\documentclass[{fontsize}pt, a4paper]{{article}}

""".format(fontsize=10)
# \usepackage{fontspec}
# \defaultfontfeatures{Mapping=tex-text}

begin = r"""

\begin{document}
"""
# \begin{equation}

end = r"""
\end{document}
"""
# \end{equation}

pre = pgf_with_custom_preamble['pgf.preamble']
pre = '\n'.join(pre)


ap = argparse.ArgumentParser(os.path.basename(__file__),
                             description=__doc__,
                             formatter_class=argparse.
                             ArgumentDefaultsHelpFormatter)
ap.add_argument('-s', '--tex_source', type=str, default='equations.tex',
                help='File with equations typeset in TeX')
ap.add_argument('-o', '--tex_output', type=str, default='texdoc.tex',
                help='Output TeX file')


def main(src_tex='equations.tex', out_tex='out.tex'):
    eqs = []
    with open(src_tex, 'r') as fin:
        for line in fin.read().splitlines():
            eq = r'${}$'.format(line)
            eqs.append(eq)

    eqs = ' '.join(eqs)

    texdoc = header + pre + begin + eqs + end
    with open(out_tex, 'w') as fout:
        fout.write(texdoc)

if __name__ == '__main__':
    args = ap.parse_args()

    main(src_tex=args.tex_source, out_tex=args.tex_output)
