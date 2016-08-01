# -*- coding: utf-8 -*-
"""
Font config via pgf backend. Needs to be loaded before importing pyplot
Source: http://matplotlib.org/users/pgf.html
"""
import matplotlib as mpl


def load():
    mpl.use("pgf")

    pgf_with_custom_preamble = {
        "font.family": "serif",  # use serif/main font for text elements
        "figure.facecolor": "0",
        "text.usetex": True,  # use inline math for ticks
        "pgf.rcfonts": False,  # don't setup fonts from rc parameters
        "pgf.preamble": [
                         # "\\usepackage{mathspec}",
                         # r"\setmainfont{whatever it takes}",
                         # r"\setmathsfont(Digits,Latin,Greek)"
                         # + r"[Numbers={Lining,Proportional}]"
                         # + r"{whatever it takes}"
                         "\\usepackage{eulervm}",
                         # "\\usepackage{units}",  # load additional packages
                         # "\\usepackage{metalogo}",
                         # "\\usepackage{unicode-math}",  # unicode math setup
                         # r"\setmathfont{xits-math.otf}",
                         # r"\setmainfont{DejaVu Serif}",
                         ]
    }

    mpl.rcParams.update(pgf_with_custom_preamble)
