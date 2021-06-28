#!/usr/bin/env python

"""
setup.py file for weaklens
"""

from distutils.core import setup, Extension
import numpy

weaklens_module = Extension('_weaklens',
                           sources=['src/weaklens.i', 'src/weaklens.cpp'],
                           swig_opts=["-c++"],
                           libraries=['m'],
                           )


setup (name        = 'weaklens',
       version     = '0.01',
       author      = "Surhud More",
       url         = "http://member.ipmu.jp/surhud.more/research",
       author_email= "surhud.more@ipmu.jp",
       description = """Weak lensing pipeline tools""",
       ext_modules = [weaklens_module],
       license     = ['GPL'],
       py_modules  = ["weaklens"],
       package_dir = { '':'src'},
       )
