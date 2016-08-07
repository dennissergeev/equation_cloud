# -*- coding: utf-8 -*-
from preamble import load
load(mode='latex')
import argparse  # NOQA
import matplotlib.image as mpimg  # NOQA
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
ap.add_argument('-b', '--background_image', type=str,
                help='Path to an image file to use as a background')
ap.add_argument('-m', '--mode', type=str,
                default='cloud', choices=['cloud', 'para'],
                help='Generate image as a cloud as a paragraph')


fontcolor = '#fff9ff'
facecolor = '#333333'
# fontcolor, facecolor = facecolor, fontcolor
# strokecolor = '#FFFFFF'

txt_dict_cloud = dict(color=fontcolor,
                      ha='center', va='center', clip_on=True)
txt_dict_para = dict(size=80, rotation=10, linespacing=0.6,
                     color=fontcolor, wrap=True,
                     ha='center', va='center', clip_on=True)
# pe_dict = dict(linewidth=1, foreground=strokecolor)


def main(src_tex='equations.tex', mode='cloud',
         repeat=1, alpha_mode='random', background_image=None):
    eqs = []
    with open(src_tex) as f:
        for line in f.read().splitlines():
            eq = r'${}$'.format(line)
            eqs.append(eq)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_axes([0, 0, 1, 1])

    if background_image is not None:
        img = mpimg.imread(background_image)
        ax.imshow(img, alpha=0.2, zorder=0, extent=[0, 1, 0, 1])

    if mode == 'cloud':
        if alpha_mode == 'logspace':
            alphas = np.logspace(-2, 0, len(eqs*repeat))
        elif alpha_mode == 'random':
            alphas = np.random.rand(len(eqs*repeat))

        for i, eq in enumerate(eqs*repeat):
            size = np.random.uniform(50, 60)
            x, y = np.random.uniform(0.0, 1.0, 2)
            alpha = alphas[i]  # np.random.uniform(0, 1)
            ax.text(x, y, eq, alpha=alpha, size=size,
                    transform=ax.transAxes, **txt_dict_cloud)
            # t.set_path_effects([PathEffects.withStroke(**pe_dict)])

    elif mode == 'para':
        eqs_ = []
        np.random.shuffle(eqs)
        for i, eq in enumerate(eqs):
            if i % 5 == 0:
                eqs_.append(eq+'\n')
            else:
                eqs_.append(eq)
        eq_str = ' '.join(eqs_*repeat)
        ax.text(0.5, 0.5, eq_str,
                transform=ax.transAxes, **txt_dict_para)

    ax.axis('off')
    fig.savefig('figure.pdf', facecolor=facecolor)


if __name__ == '__main__':
    args = ap.parse_args()
    main(src_tex=args.tex_source, mode=args.mode,
         repeat=args.repeat, alpha_mode=args.alpha,
         background_image=args.background_image)
