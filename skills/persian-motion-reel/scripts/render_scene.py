# Usage: see ../SKILL.md. Run from the folder that holds film.html and fonts/.
import sys,subprocess,os
from playwright.sync_api import sync_playwright
import os
d=os.getcwd()+'/'
a,b,name=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3]
tmp=d+f'tmp_{name}.mp4'
ff=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','image2pipe','-framerate','60','-c:v','mjpeg','-i','-','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-r','60',tmp],stdin=subprocess.PIPE)
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+d+'film.html')
    if not pg.evaluate('fontsOK()'): ff.kill(); raise SystemExit('PERSIAN FONT NOT LOADED')
    for f in range(a,b):
        pg.evaluate(f'render({f})'); ff.stdin.write(pg.screenshot(type='jpeg',quality=92))
ff.stdin.close(); rc=ff.wait()
if rc==0: os.replace(tmp,d+f'{name}.mp4'); print(name,'ok')
else: print(name,'FAIL',rc)
