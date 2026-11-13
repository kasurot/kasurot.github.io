#!/usr/bin/env python3
"""Render a standalone figure HTML file to LinkedIn/site PNG sizes via Chromium.

Usage:
    python3 _visuals/render.py <figure.html> <out_basename> [--sizes 1200x627,1080x1080,1600x640]

Output files: <out_basename>-<W>x<H>.png next to out_basename's directory.
The figure HTML is expected to be a complete document (use a template).
"""
import argparse, os, subprocess, sys

CHROMIUM = "/usr/bin/chromium-browser"

def render(html_path, out_path, w, h):
    html_path = os.path.abspath(html_path)
    out_path = os.path.abspath(out_path)
    url = "file://" + html_path
    cmd = [CHROMIUM, "--headless", "--disable-gpu", "--hide-scrollbars",
           "--screenshot=" + out_path, "--window-size=%d,%d" % (w, h), url]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit("chromium failed: " + (r.stderr or r.stdout)[-500:])
    if not os.path.exists(out_path):
        raise SystemExit("no output file: " + out_path)
    return out_path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("out_basename")
    ap.add_argument("--sizes", default="1200x627,1080x1080")
    args = ap.parse_args()
    out_dir = os.path.dirname(os.path.abspath(args.out_basename)) or "."
    os.makedirs(out_dir, exist_ok=True)
    base = os.path.basename(args.out_basename)
    for s in args.sizes.split(","):
        w, h = s.lower().split("x")
        w, h = int(w), int(h)
        out = os.path.join(out_dir, "%s-%dx%d.png" % (base, w, h))
        p = render(args.html, out, w, h)
        print("wrote", p)

if __name__ == "__main__":
    main()
