""" here is a process that is executed when you import the library.
    this must not to use from util/* file.
    here method can be used in ipynb file.
    - expy-python ver.1.2.0 ©tseijp
"""

import math
import numpy as np
import sympy as sym
import pandas as pd
import matplotlib.pyplot as plt
from sympy import init_printing
from IPython.display import Latex
from sympy import sqrt,sin,cos,tan,exp,log,diff

### main
from .util.base  import *
from .util.symb  import *

from .df    import Md, Caption, Df, Fig
from .eq    import Var, Eq
from .func  import F

### for using in ipynb ---------------------------------------------------------
def newpage():display(Latex('\\newpage'))
def tiny()   :display(Latex(r'\tiny'))
def norm()   :display(Latex(r'\normalsize'))
def md(text= '')           :display( Md(text))
def caption(text= '')      :display( Caption(text) )
def figure(filepath,cap=''):display( Image(filepath), Caption(cap))
def table(data, cap='', text=None, index=None, is_sf= False, is_tiny=False):
    rslt= pd.DataFrame(data, index=index if index else ['']*len(list(data.values())[0])) if type(data) is type({}) else data
    if is_sf: rslt = df_to_sf(rslt)
    if text:display(Caption(text)) if type(text)==type('') else md('以上より, 以下の表を得る')
    if cap: display(Caption(cap))
    if is_tiny:tiny()
    display(rslt);
    if is_tiny:norm()

def freehand(text= '', line=10):
    for i in range(line):
        display(Markdown('<p style="page-break-after: always;">&nbsp;</p>'))
    display(Caption(text))

### init process in jupyter ----------------------------------------------------
init_printing()

def init_ep():
    #init_printing()
    init_pd()
    init_plt()
    global added

def init_pd():
    try:
        pd = globals()['pd']
        ### nbconvert: using pandas DataFrame by xelatex
        def _repr_html_(self):
            return '<center> %s </center>' % self.to_html()
        def _repr_latex_(self):
            return "\\begin{center} %s \\end{center}" % self.to_latex(escape=False)

        pd.set_option('display.notebook_repr_html', True)
        pd.set_option('display.max_colwidth', -1)
        pd.DataFrame._repr_html_  = _repr_html_
        pd.DataFrame._repr_latex_ = _repr_latex_  # monkey patch pandas DataFrame
    except:
        print('UserError: you can\'t init pd')


def init_plt(name='test.jpg'):#dx,dy):
    try:
        #plt.rcParams['font.family'] ='IPAGothic'### 'sans-serif'
        plt = globals()['plt']
        plt.rcParams['mathtext.default'] = 'regular'
        plt.rcParams['xtick.top'] = 'True'
        plt.rcParams['ytick.right'] = 'True'
        plt.rcParams['xtick.direction'] = 'in'#x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
        plt.rcParams['ytick.direction'] = 'in'#y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
        plt.rcParams['xtick.major.width'] = 1.0#x軸主目盛り線の線幅
        plt.rcParams['ytick.major.width'] = 1.0#y軸主目盛り線の線幅
        plt.rcParams['axes.grid'] = 'True'
        plt.rcParams['axes.xmargin'] = '0' #'.05'
        plt.rcParams['axes.ymargin'] = '.05'
        plt.rcParams['axes.linewidth'] = 1.0# 軸の線幅edge linewidth。囲みの太さ
        #plt.rcParams['savefig.facecolor'] = 'None'
        #plt.rcParams['savefig.edgecolor'] = 'None'
        plt.rcParams['savefig.bbox'] = 'tight'
        plt.rcParams['font.size'] = 8 #フォントの大きさ
        plt.rcParams['xtick.labelsize'] = 8 # 横軸のフォントサイズ
        plt.rcParams['ytick.labelsize'] = 8 # 縦軸のフォントサイズ
    except:
            print('UserError: you can\'t init plt')
