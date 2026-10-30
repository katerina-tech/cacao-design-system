"""Generates the cacao background illustrations in assets/img/ (original artwork, poster palette).
Run from the repo root: python3 tools/cacao-art.py"""
import math
DEFS='''<defs>
<linearGradient id="pod" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7A4426"/><stop offset=".55" stop-color="#4A2614"/><stop offset="1" stop-color="#26130A"/></linearGradient>
<linearGradient id="pod2" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8A5530"/><stop offset=".6" stop-color="#55301A"/><stop offset="1" stop-color="#2A150B"/></linearGradient>
<radialGradient id="bean" cx=".35" cy=".35" r=".8"><stop offset="0" stop-color="#6B3B22"/><stop offset="1" stop-color="#2A150B"/></radialGradient>
<linearGradient id="leaf" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#1E1A0E"/><stop offset="1" stop-color="#3A3118"/></linearGradient>
<linearGradient id="pulp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C9AE8C"/><stop offset="1" stop-color="#8E7155"/></linearGradient>
</defs>'''
G='stroke="#DDB47C"'
def pod_path(L,w):
    return (f"M0,{-L/2} C{w*1.15},{-L*0.4} {w*1.25},{-L*0.05} {w*0.95},{L*0.22} "
            f"C{w*0.7},{L*0.42} {w*0.25},{L*0.5} 0,{L/2} C{-w*0.25},{L*0.5} {-w*0.7},{L*0.42} {-w*0.95},{L*0.22} "
            f"C{-w*1.25},{-L*0.05} {-w*1.15},{-L*0.4} 0,{-L/2}Z")
def pod(x,y,L,w,rot):
    s=f'<g transform="translate({x} {y}) rotate({rot})"><path d="{pod_path(L,w)}" fill="url(#pod)" {G} stroke-opacity=".55" stroke-width="1.5"/>'
    for k in (-0.62,-0.3,0.02,0.34,0.66):
        s+=f'<path d="M{k*w*0.3},{-L*0.46} C{k*w*1.45},{-L*0.2} {k*w*1.35},{L*0.25} {k*w*0.3},{L*0.47}" fill="none" {G} stroke-opacity=".28" stroke-width="1.2"/>'
    return s+f'<path d="M0,{-L/2} q6,-26 -4,-48" fill="none" stroke="#5A3A20" stroke-width="7" stroke-linecap="round"/></g>'
def bean(x,y,rx,ry,rot):
    return (f'<g transform="translate({x} {y}) rotate({rot})"><ellipse rx="{rx}" ry="{ry}" fill="url(#bean)" {G} stroke-opacity=".45" stroke-width="1"/>'
            f'<path d="M{-rx*0.7},0 C{-rx*0.2},{-ry*0.25} {rx*0.2},{ry*0.25} {rx*0.7},0" fill="none" {G} stroke-opacity=".35" stroke-width="1"/></g>')
def leaf(x,y,L,w,rot):
    s=f'<g transform="translate({x} {y}) rotate({rot})"><path d="M0,0 C{w},{-L*0.25} {w*0.75},{-L*0.75} 0,{-L} C{-w*0.75},{-L*0.75} {-w},{-L*0.25} 0,0Z" fill="url(#leaf)" {G} stroke-opacity=".25" stroke-width="1.2"/><path d="M0,0 L0,{-L*0.97}" {G} stroke-opacity=".3" stroke-width="1.2"/>'
    for i in range(1,7):
        t=i/7; yy=-L*t; ww=w*0.62*math.sin(math.pi*t)
        s+=f'<path d="M0,{yy} q{ww*0.6},{-L*0.04} {ww},{-L*0.09} M0,{yy} q{-ww*0.6},{-L*0.04} {-ww},{-L*0.09}" fill="none" {G} stroke-opacity=".18" stroke-width="1"/>'
    return s+'</g>'
def split_pod(x,y,L,w,rot):
    s=f'<g transform="translate({x} {y}) rotate({rot})"><path d="{pod_path(L,w)}" fill="url(#pod2)" {G} stroke-opacity=".55" stroke-width="1.5"/><path d="{pod_path(L*0.84,w*0.72)}" fill="url(#pulp)" fill-opacity=".85" {G} stroke-opacity=".4" stroke-width="1"/>'
    for r in range(7):
        for c in (-1,1): s+=bean(c*w*0.3,-L*0.3+r*L*0.095,w*0.28,w*0.19,c*-18)
    return s+f'<path d="M0,{-L/2} q-6,-26 4,-48" fill="none" stroke="#5A3A20" stroke-width="7" stroke-linecap="round"/></g>'
def svg(body,vb="0 0 600 800"): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{DEFS}{body}</svg>'
left=leaf(70,820,520,120,28)+leaf(10,700,420,100,58)+pod(300,410,560,118,-24)+bean(150,730,26,17,20)+bean(240,765,24,16,-15)+bean(90,650,22,15,60)
right=leaf(560,-20,500,115,200)+leaf(620,140,380,90,232)+split_pod(330,430,520,118,22)+bean(140,720,26,17,-30)+bean(230,770,23,15,15)+bean(330,745,25,16,70)
beans=''.join(bean(x,y,22,14,r) for x,y,r in [(40,30,20),(150,60,-30),(260,25,70),(90,130,-10),(220,140,40)])
for name,body,vb in [('cacao-left',left,"0 0 600 800"),('cacao-right',right,"0 0 600 800"),('cacao-beans',beans,"0 0 300 180")]:
    open(f'assets/img/{name}.svg','w').write(svg(body,vb))
