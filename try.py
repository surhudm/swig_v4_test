import sys
sys.path.append("install/lib64/python3.9/site-packages")

import weaklens

a = weaklens.weaklens(b=1, h=2)
a.test(h=1, b=3)
a.test(b=1, h=3)

