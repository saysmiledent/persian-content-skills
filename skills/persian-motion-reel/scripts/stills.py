# Usage: see ../SKILL.md. Run from the folder that holds film.html and fonts/.
import sys
from playwright.sync_api import sync_playwright
import os
d=os.getcwd()+'/'
fr=[int(x) for x in sys.argv[1:]]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+d+'film.html')
    if not pg.evaluate('fontsOK()'): raise SystemExit('PERSIAN FONT NOT LOADED')
    for f in fr:
        pg.evaluate(f'render({f})'); pg.screenshot(path=d+f'still_{f:04d}.jpg',type='jpeg',quality=92)
    print(pg.evaluate('JSON.stringify([...document.querySelectorAll(".m")].filter(e=>e.scrollWidth>e.clientWidth+2).map(e=>e.textContent))'))
