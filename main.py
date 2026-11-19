"""news-image-20261119 entry: copy the bundled image to /output/entry.png.

Deterministic: a pure file copy, no network, no randomness — both runs
write the same bytes. The image (entry.png, beside this file) is a
1024x1024 infographic summing up Thursday 19 November 2026's world news,
composed programmatically with PIL (see build_image.py).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(DST_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(DST_DIR, "entry.png"))
