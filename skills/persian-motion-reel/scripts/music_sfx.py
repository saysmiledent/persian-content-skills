import numpy as np, wave
SR=48000; DUR=38.0; N=int(SR*DUR)
rng=np.random.default_rng(3)
mus=np.zeros(N); sfx=np.zeros(N)
def env(n,a=0.005,r=0.3):
    t=np.arange(n)/SR; e=np.minimum(1,t/a)*np.exp(-t/r); return e
def add(buf,t,x,g=1.0):
    i=int(t*SR); j=min(N,i+len(x)); buf[i:j]+=g*x[:j-i]
def tone(f,d,a=0.01,r=0.4,harm=((1,1),),vib=0):
    n=int(d*SR); t=np.arange(n)/SR; x=sum(w*np.sin(2*np.pi*f*h*t) for h,w in harm); return x*env(n,a,r)
def lp(x,k):  # simple one-pole lowpass
    y=np.zeros_like(x); c=0.0
    for i in range(len(x)): c+=k*(x[i]-c); y[i]=c
    return y
def noise(d): return rng.standard_normal(int(d*SR))
NOTE=lambda m:440*2**((m-69)/12)
BPM=120; BEAT=0.5; BAR=2.0
# --- music ---
chords=[[48,55,60,64],[43,50,55,59],[45,52,57,60],[41,48,53,57]]  # C G Am F
roots=[36,31,33,29]
for bar in range(19):
    t0=bar*BAR; c=chords[bar%4]
    if bar>=2:
        for m in c:  # warm pad
            n=int(BAR*SR); t=np.arange(n)/SR
            x=(np.sin(2*np.pi*NOTE(m+12)*t)+0.5*np.sin(2*np.pi*NOTE(m+12)*2.003*t)+0.25*np.sin(2*np.pi*NOTE(m)*t))
            e=np.minimum(1,t/0.35)*np.minimum(1,(BAR-t)/0.35)
            add(mus,t0,x*e,0.035)
        for k in range(8):  # bass 8ths
            add(mus,t0+k*0.25,tone(NOTE(roots[bar%4]),0.24,0.005,0.12,((1,1),(2,.3))),0.16 if k%2==0 else 0.09)
        for k in (0,2):  # soft kick beats 1,3
            n=int(0.3*SR); t=np.arange(n)/SR; f=55+70*np.exp(-t/0.03)
            add(mus,t0+k*BEAT,np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t/0.12),0.45)
    if bar>=5:
        for k in range(4):  # hats offbeat
            h=noise(0.05); h=h-lp(h,0.3); add(mus,t0+k*BEAT+0.25,h*env(len(h),0.001,0.015),0.06)
    if 13<=bar<=17:
        for k in range(8):  # arp sparkle
            m=c[k%4]+24; add(mus,t0+k*0.25,tone(NOTE(m),0.3,0.003,0.18,((1,1),(2,.2))),0.035)
# final chord
for m in [48,55,60,64,67,72]:
    add(mus,36.0,tone(NOTE(m+12),2.0,0.02,0.9,((1,1),(2,.25))),0.05)
# hook drone bars 1-2
n=int(4*SR); t=np.arange(n)/SR; add(mus,0,np.sin(2*np.pi*NOTE(36)*t)*np.minimum(1,t/0.5)*np.minimum(1,(4-t)/0.4),0.10)
# --- sfx ---
def thud():
    n=int(0.45*SR); t=np.arange(n)/SR; f=40+110*np.exp(-t/0.04)
    x=np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t/0.16); c=noise(0.02)*env(int(0.02*SR),0.0005,0.004); x[:len(c)]+=0.6*c; return x
def crack():
    x=noise(0.25); x=x-lp(x,0.15); return x*env(len(x),0.0005,0.05)
def tick(): return tone(2200,0.05,0.0005,0.012,((1,1),(2.7,.3)))
def chime(base=72):
    return sum(tone(NOTE(base+i),1.6,0.004,0.7,((1,1),(2.01,.35),(3.0,.12))) for i in (0,4,7))/3
def whoosh(d=0.45):
    x=noise(d); n=len(x); y=np.zeros(n); c=0.0
    for i in range(n):
        k=0.02+0.25*np.sin(np.pi*i/n); c+=k*(x[i]-c); y[i]=c
    return y*np.sin(np.pi*np.arange(n)/n)**2
def buzz(d):
    n=int(d*SR); t=np.arange(n)/SR
    x=np.sign(np.sin(2*np.pi*180*t))*0.3+np.sin(2*np.pi*360*t)*0.5; x=lp(x,0.08)
    x*=0.8+0.2*np.sin(2*np.pi*28*t); e=np.minimum(1,t/0.05)*np.minimum(1,(d-t)/0.08); return x*e
def shatter():
    out=np.zeros(int(0.9*SR))
    for k in range(9):
        p=tone(2000+rng.random()*2600,0.4,0.001,0.12+rng.random()*0.1); i=int(rng.random()*0.18*SR); out[i:i+len(p)]+=p[:len(out)-i]*0.5
    c=crack(); out[:len(c)]+=0.7*c; return out
def ding(m): return tone(NOTE(m),0.8,0.002,0.35,((1,1),(2.0,.3),(4.1,.1)))
for t in (0,0.5,1.0): add(sfx,t,thud(),0.9)
add(sfx,1.5,crack(),0.6); add(sfx,1.5,thud(),0.4)
add(sfx,2.0,tick(),0.35)
add(sfx,4.0,whoosh(0.5),0.9); add(sfx,4.3,chime(76),0.35)
for k in range(8): add(sfx,6.0+k*0.5,tone(NOTE(45),0.25,0.005,0.08,((1,1),(2,.4))),0.18)
add(sfx,10.0,thud(),0.55)
add(sfx,12.33,buzz(2.17),0.10)
add(sfx,13.0,shatter(),0.8)
add(sfx,14.0,tick(),0.35)
add(sfx,18.0,whoosh(0.4),0.6)
add(sfx,19.33,buzz(2.67),0.08)
add(sfx,20.0,chime(79),0.4)
add(sfx,22.0,tone(NOTE(84),0.6,0.01,0.3),0.12)
add(sfx,24.0,tick(),0.35)
add(sfx,26.5,tick(),0.3); add(sfx,29.5,tick(),0.3); add(sfx,29.67,tick(),0.25)
add(sfx,30.0,chime(72),0.35)
for i,m in enumerate((88,91,96)): add(sfx,30.0+0.5*i,ding(m),0.22)
for t in (32.5,34.0,35.5,36.0): add(sfx,t,tick(),0.3)
np.save('mus.npy',mus); np.save('sfx.npy',sfx)
def wr(name,x):
    x=x/max(1e-9,np.abs(x).max())*0.89; s=(np.stack([x,x],1)*32767).astype(np.int16)
    w=wave.open(name,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(s.tobytes()); w.close()
wr('music_sfx.wav',mus+sfx)
print('ok')
