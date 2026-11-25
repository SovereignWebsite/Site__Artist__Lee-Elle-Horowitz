#!/usr/bin/env python3
"""Turn the design screenshots into 640 x 400 WebP cards in site/assets/designs/: python3 tools/designs/thumbs.py <png dir>"""
import sys, os, glob
from PIL import Image
dst = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'site', 'assets', 'designs'); os.makedirs(dst, exist_ok=True)
for f in sorted(glob.glob(os.path.join(sys.argv[1], '*.png'))):
    n = os.path.splitext(os.path.basename(f))[0]
    Image.open(f).convert('RGB').resize((640, 400), Image.LANCZOS).save(os.path.join(dst, n + '.webp'), quality=80); print(n)
