# -*- coding: utf-8 -*-
from preamble import load
load()
import argparse  # NOQA
import matplotlib.pyplot as plt  # NOQA
import matplotlib.patheffects as PathEffects  # NOQA
import numpy as np  # NOQA
import os  # NOQA


ap = argparse.ArgumentParser(os.path.basename(__file__),
                             description=__doc__,
                             formatter_class=argparse.
                             ArgumentDefaultsHelpFormatter)
ap.add_argument('-s', '--tex_source', type=str, default='equations.tex',
                help='File with equations typeset in TeX')
ap.add_argument('-r', '--repeat', action='count', default=1,
                help='Repeat equations r times')
ap.add_argument('-a', '--alpha', type=str,
                default='random', choices=['random', 'logspace'],
                help='Alpha distribution: random uniform or log-spaced')

facecolor = '#fff9ff'
fontcolor = '#333333'
# strokecolor = '#FFFFFF'

txt_dict = dict(ha='center', va='center', color=fontcolor,
                clip_on=True)
# pe_dict = dict(linewidth=1, foreground=strokecolor)


def main(src_tex='equations.tex', repeat=1, alpha_mode='random'):
    eqs = []
    with open(src_tex) as f:
        for line in f.read().splitlines():
            eq = r'${}$'.format(line)
            eqs.append(eq)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_axes([0, 0, 1, 1])

    if alpha_mode == 'logspace':
        alphas = np.logspace(-2, 0, len(eqs*repeat))
    elif alpha_mode == 'random':
        alphas = np.random.rand(len(eqs*repeat))

    for i, eq in enumerate(eqs*repeat):
        size = np.random.uniform(10, 30)
        x, y = np.random.uniform(0.0, 1.0, 2)
        alpha = alphas[i]  # np.random.uniform(0, 1)
        ax.text(x, y, eq, alpha=alpha, size=size,
                transform=ax.transAxes, **txt_dict)
        # t.set_path_effects([PathEffects.withStroke(**pe_dict)])

    ax.axis('off')
    fig.savefig('figure.pdf', facecolor=facecolor)

if __name__ == '__main__':
    args = ap.parse_args()
    main(src_tex=args.tex_source, repeat=args.repeat, alpha_mode=args.alpha)
