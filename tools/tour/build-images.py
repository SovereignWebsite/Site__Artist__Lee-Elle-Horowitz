#!/usr/bin/env python3
"""Convert the tour screenshots (PNG) to WebP in site/tour/img/: python3 tools/tour/build-images.py <png dir>"""
import sys, os, glob
from PIL import Image
src = sys.argv[1]; dst = os.path.join(os.path.dirname(__file__), '..', '..', 'site', 'tour', 'img'); os.makedirs(dst, exist_ok=True)
for f in glob.glob(os.path.join(src, '*.png')):
    im = Image.open(f).convert('RGB'); n = os.path.splitext(os.path.basename(f))[0]
    if n == 'phone': im = im.resize((390, 844))
    im.save(os.path.join(dst, n + '.webp'), quality=82); print(n, im.size)
