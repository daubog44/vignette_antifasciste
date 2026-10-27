# -*- coding: utf-8 -*-
# Versione a scorrimento continuo: tutte le immagini grandi, una dopo l'altra, senza schede né caroselli.
import json, html, importlib
import content as C
from testi import T as TX
importlib.reload(C)

import os
HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(HERE, 'sizes.json')))
CR = json.load(open(os.path.join(HERE, 'credits.json')))
esc = lambda s: html.escape(str(s), quote=True)

def src(idx):
    k = str(idx)
    if idx == "svg":
        return "img/frecce.svg", tuple(S[k][0])
    if k.startswith("m"):
        ext = "svg" if k == "m02" else "jpg"
        return f"img/{k}.{ext}", tuple(S[k][0])
    return f"img/{idx:02d}.jpg", tuple(S[k][0])

ALL = [(c, f) for c in C.CHAPTERS for f in c["figs"]]

CSS = r"""
:root{
  /* Carta da giornale e inchiostro; ogni immagine su una fascia scura a tutta larghezza, come in una sala espositiva.
     Accento unico: il giallo del Becco Giallo. Layout: una sola colonna che scorre, testo stretto, immagini larghe. */
  --paper:#f2f0ea; --ink:#16130f; --muted:#5f5a51; --rule:#c9c2b3; --accent:#e3a800;
  --stage:#11100d; --stage-ink:#efe9dc; --stage-muted:#a39c8e;
  --display:"Bodoni Moda", "Didot", "Bodoni 72", Georgia, serif;
  --body:"Literata", Georgia, "Times New Roman", serif;
  --label:"Archivo Narrow", "Arial Narrow", system-ui, sans-serif;
  color-scheme: light;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){ --paper:#14120f; --ink:#ece7dc; --muted:#a59e90; --rule:#3a352c; --accent:#f0bd2a; --stage:#0a0907; color-scheme: dark; }
}
:root[data-theme="dark"]{ --paper:#14120f; --ink:#ece7dc; --muted:#a59e90; --rule:#3a352c; --accent:#f0bd2a; --stage:#0a0907; color-scheme: dark; }
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0; background:var(--paper); color:var(--ink); font-family:var(--body); font-size:17px; line-height:1.62; overflow-x:hidden}
a{color:inherit; text-decoration-color:var(--accent); text-decoration-thickness:2px; text-underline-offset:3px}
a:focus-visible, button:focus-visible{outline:3px solid var(--accent); outline-offset:3px}
img{max-width:100%; display:block}
.wrap{max-width:700px; margin:0 auto; padding:0 18px}

.masthead{padding:26px 0 28px; border-bottom:3px double var(--ink)}
.dateline{font-family:var(--label); font-size:12px; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); display:flex; justify-content:space-between; gap:12px; border-top:1px solid var(--ink); border-bottom:1px solid var(--ink); padding:6px 0; margin-bottom:20px}
h1{font-family:var(--display); font-weight:800; font-size:clamp(46px, 12vw, 116px); line-height:.9; letter-spacing:-.02em; margin:0; text-wrap:balance}
h1 em{font-style:italic; font-weight:500}
.beak{display:inline-block; width:.62em; height:.36em; background:var(--accent); clip-path:polygon(0 0,100% 50%,0 100%); margin-left:.08em; vertical-align:.12em}
.sub{font-family:var(--display); font-style:italic; font-size:clamp(20px, 4.6vw, 30px); line-height:1.22; margin:14px 0 0; color:var(--muted); text-wrap:balance}
.lede{padding-top:30px}
.lede p{font-size:18px}
.lede p:first-child::first-letter{font-family:var(--display); font-weight:800; float:left; font-size:4.1em; line-height:.8; padding:6px 8px 0 0}

/* Intestazioni d'epoca dentro il flusso */
.era{padding-top:64px; padding-bottom:6px}
.era .y{font-family:var(--display); font-weight:800; font-size:clamp(56px, 15vw, 128px); line-height:.85; letter-spacing:-.02em; display:block}
.era h2{font-family:var(--display); font-weight:700; font-style:italic; font-size:clamp(28px, 6.4vw, 48px); line-height:1.05; margin:8px 0 18px; text-wrap:balance}
.era p{margin:0 0 1em}

/* Ogni immagine: fascia scura a tutta larghezza + didascalia */
figure.plate{margin:40px 0 0}
.stage{background:var(--stage); padding:clamp(14px, 3vw, 36px) 10px 10px; display:flex; flex-direction:column; align-items:center}
.stage button{all:unset; cursor:zoom-in; display:block; max-width:min(1500px, 100%)}
.stage img{width:auto; height:auto; max-width:100%; max-height:92vh; margin:0 auto; box-shadow:0 18px 50px rgba(0,0,0,.5); background:#fff}
.stage button:focus-visible{outline:3px solid var(--accent); outline-offset:4px}
figcaption{max-width:700px; margin:0 auto; padding:16px 18px 0}
.num{font-family:var(--label); font-size:12px; letter-spacing:.14em; color:var(--muted); font-variant-numeric:tabular-nums}
figcaption h3{font-family:var(--display); font-weight:700; font-size:clamp(25px, 5.4vw, 36px); line-height:1.08; margin:4px 0 6px; text-wrap:balance}
.meta{font-family:var(--label); font-size:13.5px; letter-spacing:.04em; color:var(--muted); margin:0 0 10px}
.star{display:inline-block; background:var(--accent); color:#16130f; font-weight:700; padding:0 6px; margin-right:6px; letter-spacing:.08em; text-transform:uppercase; font-size:11px}
figcaption p{margin:0}
.lab{display:block; font-family:var(--label); text-transform:uppercase; letter-spacing:.14em; font-size:11px; font-weight:700; color:var(--muted); margin:0 0 2px}
.blk{margin-top:14px !important}
.blk.iro{padding-left:12px; border-left:3px solid var(--accent)}

/* Coda */
.tail{padding-top:70px}
h3.sec{font-family:var(--label); text-transform:uppercase; letter-spacing:.14em; font-size:13px; color:var(--muted); margin:34px 0 0; border-top:1px solid var(--ink); padding-top:10px}
.tail h2{font-family:var(--display); font-weight:700; font-style:italic; font-size:clamp(28px, 6.4vw, 44px); line-height:1.05; margin:0 0 10px}
.cards{list-style:none; padding:0; margin:14px 0 0; display:grid; gap:10px}
.cards a{display:block; padding:13px 15px; border:1px solid var(--rule); text-decoration:none}
.cards a:hover{border-color:var(--ink)}
.cards strong{font-family:var(--display); font-size:19px; line-height:1.2; display:block; margin-bottom:3px}
.cards span{font-size:15px; color:var(--muted)}
.note{font-size:15px; color:var(--muted)}
.credits{font-family:var(--label); font-size:13px; color:var(--muted); padding-left:1.4em}
.credits li{margin-bottom:4px}
footer{margin-top:60px; padding:24px 0 56px; border-top:3px double var(--ink)}

/* Pulsante carosello */
.cta{display:inline-flex; align-items:center; gap:10px; margin-top:22px; font-family:var(--label); font-weight:700; font-size:16px; letter-spacing:.04em; text-transform:uppercase; background:var(--ink); color:var(--paper); border:0; border-radius:999px; padding:13px 22px; cursor:pointer}
.cta .tri{width:0; height:0; border-left:11px solid var(--accent); border-top:7px solid transparent; border-bottom:7px solid transparent}
.fab{position:fixed; right:14px; bottom:calc(14px + env(safe-area-inset-bottom)); z-index:20; font-family:var(--label); font-weight:700; font-size:14px; letter-spacing:.05em; text-transform:uppercase; background:var(--accent); color:#16130f; border:0; border-radius:999px; padding:12px 18px; box-shadow:0 6px 22px rgba(0,0,0,.35); cursor:pointer; opacity:0; transform:translateY(20px); pointer-events:none; transition:opacity .25s, transform .25s}
.fab.on{opacity:1; transform:none; pointer-events:auto}
.zoomhint{font-family:var(--label); font-size:12px; letter-spacing:.08em; text-transform:uppercase; color:var(--stage-muted); text-align:center; margin-top:8px}

/* Visore a schermo intero con zoom */
#vw{position:fixed; inset:0; z-index:50; background:#0a0907; color:#efe9dc; display:none; flex-direction:column; font-family:var(--label); overscroll-behavior:contain}
#vw.open{display:flex}
.vw-bar{display:flex; align-items:center; gap:8px; padding:8px 10px; padding-top:calc(8px + env(safe-area-inset-top)); border-bottom:1px solid #2a2620}
.vw-bar .t{flex:1; min-width:0; font-size:14px; line-height:1.25}
.vw-bar .t b{display:block; font-weight:700; white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.vw-bar .t span{color:#a39c8e; font-size:12.5px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; display:block}
#vw button{font:inherit; font-size:15px; border:0; min-width:40px; height:40px; padding:0 12px; border-radius:999px; cursor:pointer; background:#2a2620; color:#efe9dc; display:inline-flex; align-items:center; justify-content:center; gap:6px; flex:none}
#vw button.hi{background:#f0bd2a; color:#16130f; font-weight:700}
#vw button[aria-pressed="true"]{background:#efe9dc; color:#16130f}
.vw-stage{position:relative; flex:1; overflow:hidden; touch-action:none; cursor:grab; user-select:none; -webkit-user-select:none}
.vw-stage.drag{cursor:grabbing}
.vw-stage img{position:absolute; left:0; top:0; max-width:none; background:#fff; transform-origin:50% 50%; will-change:transform; -webkit-user-drag:none; pointer-events:none}
.vw-stage img.anim{transition:transform .22s ease}
.vw-nav{position:absolute; top:50%; transform:translateY(-50%); width:44px !important; height:64px !important; border-radius:10px !important; background:rgba(20,18,15,.55) !important; font-size:26px !important; z-index:2}
.vw-nav.p{left:6px} .vw-nav.n{right:6px}
.vw-zoom{position:absolute; right:10px; bottom:10px; display:flex; gap:6px; z-index:2}
.vw-zoom button{background:rgba(20,18,15,.75) !important}
.vw-pct{position:absolute; left:10px; bottom:12px; font-size:12px; color:#a39c8e; z-index:2; background:rgba(20,18,15,.6); padding:3px 8px; border-radius:99px}
.vw-hint{position:absolute; left:50%; top:14px; transform:translateX(-50%); background:rgba(20,18,15,.85); padding:7px 14px; border-radius:99px; font-size:13px; z-index:3; transition:opacity .5s; pointer-events:none; white-space:nowrap; opacity:0}
.vw-info{position:absolute; left:0; right:0; bottom:0; max-height:62%; overflow:auto; background:#0e0d0b; border-top:1px solid #3a352c; padding:16px 18px 24px; z-index:4; transform:translateY(102%); transition:transform .28s ease; font-family:var(--body); font-size:16px; line-height:1.55; -webkit-overflow-scrolling:touch}
.vw-info.on{transform:none}
.vw-info .in{max-width:700px; margin:0 auto}
.vw-info h3{font-family:var(--display); font-size:26px; line-height:1.1; margin:0 0 4px}
.vw-info .meta, .vw-info .lab, .vw-info .num{color:#a39c8e}
.vw-info .blk.iro{border-left-color:#f0bd2a}
.vw-strip{display:flex; gap:6px; overflow-x:auto; padding:8px 10px; padding-bottom:calc(8px + env(safe-area-inset-bottom)); border-top:1px solid #2a2620; scrollbar-width:thin; -webkit-overflow-scrolling:touch}
#vw .vw-strip button{flex:none; height:58px; min-width:0; padding:0; border-radius:3px; overflow:hidden; opacity:.45; outline:2px solid transparent; outline-offset:1px; background:#222}
#vw .vw-strip button.on{opacity:1; outline-color:#f0bd2a}
.vw-strip img{height:58px; width:auto; display:block}
@media (min-width:900px){ #vw .vw-strip button, .vw-strip img{height:70px} }
@media (max-width:520px){ .vw-bar .lbl{display:none} }
"""

def build():
    o = [f"""<!DOCTYPE html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(C.TITLE)}</title><meta name="description" content="{esc(C.SUBTITLE)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500;0,6..96,700;0,6..96,800;1,6..96,500;1,6..96,700&family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,600;1,7..72,400&family=Archivo+Narrow:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<header class="masthead"><div class="wrap">
<div class="dateline"><span>Numero unico · {len(ALL)} immagini</span><span>1914 – oggi</span></div>
<h1>Satira <em>contro</em> il fascismo<span class="beak" aria-hidden="true"></span></h1>
<p class="sub">{esc(C.SUBTITLE)}</p><button type="button" class="cta" data-carousel="0"><span class="tri"></span>Sfoglia le {len(ALL)} immagini in carosello</button></div></header><main>
<div class="wrap lede">"""]
    for p in C.INTRO: o.append(f"<p>{esc(p)}</p>")
    o.append('</div>')
    n = 0
    for c in C.CHAPTERS:
        o.append(f'<div class="wrap era" id="{c["id"]}"><span class="y">{esc(c["years"])}</span><h2>{esc(c["title"])}</h2>')
        for p in c["text"]: o.append(f"<p>{esc(p)}</p>")
        o.append('</div>')
        for f in c["figs"]:
            idx, title, author, date, pub, text, big = f
            s, (w, h) = src(idx)
            meta = " · ".join(x for x in [author, date, pub] if x)
            star = '<span class="star">Da vedere</span>' if big else ""
            load = "eager" if n < 2 else "lazy"
            o.append(f'<figure class="plate"><div class="stage"><button type="button" data-g="{n}" aria-label="Apri a schermo intero: {esc(title)}">'
                     f'<img src="{s}" width="{w}" height="{h}" loading="{load}" decoding="async" alt="{esc(title)} – {esc(author)}{(", " + esc(date)) if date else ""}"></button><p class="zoomhint">Tocca per ingrandire</p></div>'
                     f'<figcaption><span class="num">{n+1:02d} / {len(ALL)}</span><h3>{esc(title)}</h3><p class="meta">{star}{esc(meta)}</p><p class="blk"><span class="lab">Cosa si vede</span>{esc(TX[idx]['d'])}</p><p class="blk iro"><span class="lab">{esc(TX[idx].get('il', "L'ironia"))}</span>{esc(TX[idx]['i'])}</p><p class="blk"><span class="lab">Il contesto</span>{esc(TX[idx]['s'])}</p><p class="blk"><span class="lab">Il segno</span>{esc(TX[idx]['a'])}</p></figcaption></figure>')
            n += 1
    o.append('<div class="wrap tail" id="altro"><h2>Le vignette che mancano</h2>')
    for title, intro, items in C.LINKS:
        o.append(f'<h3 class="sec">{esc(title)}</h3>')
        if intro: o.append(f'<p class="note">{esc(intro)}</p>')
        o.append('<ul class="cards">')
        for nm, d, u in items:
            o.append(f'<li><a href="{esc(u)}" target="_blank" rel="noopener"><strong>{esc(nm)}</strong><span>{esc(d)}</span></a></li>')
        o.append('</ul>')
    o.append('<h3 class="sec">Una nota sulle fonti</h3>')
    for p in C.NOTE: o.append(f'<p class="note">{esc(p)}</p>')
    o.append('</div></main><footer><div class="wrap"><h3 class="sec" style="margin-top:0">Crediti delle immagini</h3><p class="note">Tutte le immagini vengono da Wikimedia Commons. Sono di pubblico dominio salvo dove indicato; per quelle sotto licenza Creative Commons l\'attribuzione completa è nella scheda collegata.</p><ol class="credits">')
    for c, f in ALL:
        cr = CR[str(f[0])]
        o.append(f'<li><a href="{esc(cr["page"])}" target="_blank" rel="noopener">{esc(f[1])}</a> – {esc(f[2])}, {esc(cr["lic"])}</li>')
    o.append('</ol><h3 class="sec">Fonti</h3><ul class="credits">')
    for nm, u in C.SOURCES:
        o.append(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(nm)}</a></li>')
    o.append('</ul></div></footer>')
    def th(idx):
        p = src(idx)[0]
        return p if p.endswith(".svg") else p.replace("img/", "tn/")
    data = [{"s": src(f[0])[0], "th": th(f[0]), "w": src(f[0])[1][0], "h": src(f[0])[1][1], "t": f[1], "m": " · ".join(x for x in [f[2], f[3]] if x)} for c, f in ALL]
    o.append('<button type="button" class="fab" id="fab" data-carousel="here">▶ Carosello</button>')
    o.append('<div id="vw" role="dialog" aria-modal="true" aria-label="Visore immagini" hidden>'
             '<div class="vw-bar"><span class="t"><b id="vw-t"></b><span id="vw-m"></span></span>'
             '<button type="button" id="vw-play" aria-pressed="false" title="Scorrimento automatico">▶<span class="lbl"> Auto</span></button>'
             '<button type="button" id="vw-i" aria-pressed="false" title="Didascalia e storia">Testi</button>'
             '<button type="button" class="hi" id="vw-x" aria-label="Chiudi">✕</button></div>'
             '<div class="vw-stage" id="vw-s"><img id="vw-img" alt="" draggable="false">'
             '<button type="button" class="vw-nav p" id="vw-p" aria-label="Precedente">‹</button><button type="button" class="vw-nav n" id="vw-n" aria-label="Successiva">›</button>'
             '<span class="vw-pct" id="vw-c"></span>'
             '<div class="vw-zoom"><button type="button" id="vw-zo" aria-label="Riduci">−</button><button type="button" id="vw-z0" aria-label="Adatta allo schermo">⤢</button><button type="button" id="vw-zi" aria-label="Ingrandisci">+</button></div>'
             '<div class="vw-hint" id="vw-h">Pizzica, doppio tocco o rotella per ingrandire</div>'
             '<div class="vw-info" id="vw-info"><div class="in" id="vw-info-in"></div></div></div>'
             '<div class="vw-strip" id="vw-strip"></div></div>')
    o.append('<script>var ALL=' + json.dumps(data, ensure_ascii=False) + ';</script>')
    o.append(r"""<script>
(function(){
  try{ history.scrollRestoration='manual'; }catch(e){}
  var V=document.getElementById('vw'), S=document.getElementById('vw-s'), I=document.getElementById('vw-img'),
      T=document.getElementById('vw-t'), M=document.getElementById('vw-m'), C=document.getElementById('vw-c'),
      H=document.getElementById('vw-h'), INFO=document.getElementById('vw-info'), INFOIN=document.getElementById('vw-info-in'),
      STRIP=document.getElementById('vw-strip'), BI=document.getElementById('vw-i'), BP=document.getElementById('vw-play'),
      CAPS=document.querySelectorAll('figure.plate figcaption'), FIGS=document.querySelectorAll('figure.plate');
  var g=0, sc=1, tx=0, ty=0, fw=0, fh=0, MAX=6, open=false, timer=null, built=false, hinted=false;

  function buildStrip(){ if(built) return; built=true;
    ALL.forEach(function(a,i){ var b=document.createElement('button'); b.type='button'; b.setAttribute('aria-label',(i+1)+'. '+a.t);
      var im=document.createElement('img'); im.loading='lazy'; im.src=a.th; im.alt=''; b.appendChild(im);
      b.addEventListener('click',function(){ stopPlay(); show(i); }); STRIP.appendChild(b); }); }
  function layout(){ var W=S.clientWidth, Hh=S.clientHeight, a=ALL[g], r=Math.min(W/a.w, Hh/a.h);
    fw=a.w*r; fh=a.h*r; I.style.width=fw+'px'; I.style.height=fh+'px'; I.style.left=((W-fw)/2)+'px'; I.style.top=((Hh-fh)/2)+'px'; apply(); }
  function clamp(){ var W=S.clientWidth, Hh=S.clientHeight, mx=Math.max(0,(fw*sc-W)/2), my=Math.max(0,(fh*sc-Hh)/2);
    tx=Math.max(-mx,Math.min(mx,tx)); ty=Math.max(-my,Math.min(my,ty)); }
  function apply(anim){ clamp(); I.classList.toggle('anim',!!anim); I.style.transform='translate('+tx+'px,'+ty+'px) scale('+sc+')';
    C.textContent=(g+1)+' / '+ALL.length+(sc>1.01?'  ·  '+Math.round(sc*100)+'%':''); }
  function zoomAt(ns,px,py,anim){ ns=Math.max(1,Math.min(MAX,ns)); var r=S.getBoundingClientRect(), cx=px-r.left-r.width/2, cy=py-r.top-r.height/2;
    tx=cx-(ns/sc)*(cx-tx); ty=cy-(ns/sc)*(cy-ty); sc=ns; if(sc===1){tx=0;ty=0;} apply(anim); }
  function zoomCenter(f){ var r=S.getBoundingClientRect(); zoomAt(sc*f, r.left+r.width/2, r.top+r.height/2, true); }
  function show(i){ g=(i+ALL.length)%ALL.length; sc=1; tx=0; ty=0; var a=ALL[g];
    I.src=a.s; I.alt=a.t; T.textContent=a.t; M.textContent=a.m; layout();
    INFOIN.innerHTML=CAPS[g]?CAPS[g].innerHTML:'';  INFO.scrollTop=0;
    var bs=STRIP.children; for(var k=0;k<bs.length;k++) bs[k].classList.toggle('on',k===g);
    var b=bs[g]; if(b){ STRIP.scrollLeft=b.offsetLeft-STRIP.clientWidth/2+b.offsetWidth/2; }
    new Image().src=ALL[(g+1)%ALL.length].s; }
  function openAt(i){ buildStrip(); V.hidden=false; V.classList.add('open'); open=true; document.documentElement.style.overflow='hidden';
    show(i); try{ history.pushState({vw:1},''); }catch(e){}
    if(!hinted){ hinted=true; H.style.opacity=1; setTimeout(function(){H.style.opacity=0;},2600);} else H.style.opacity=0;
    document.getElementById('vw-x').focus({preventScroll:true}); }
  function closeV(fromPop){ if(!open) return; open=false; stopPlay(); V.classList.remove('open'); V.hidden=true; document.documentElement.style.overflow='';
    var f=FIGS[g]; if(f) f.scrollIntoView({block:'center'}); if(!fromPop){ try{ if(history.state&&history.state.vw) history.back(); }catch(e){} } }
  window.addEventListener('popstate',function(){ closeV(true); });
  window.addEventListener('resize',function(){ if(open) layout(); });

  function stopPlay(){ if(timer){clearInterval(timer); timer=null;} BP.setAttribute('aria-pressed','false'); }
  BP.addEventListener('click',function(){ if(timer){stopPlay();return;} BP.setAttribute('aria-pressed','true'); timer=setInterval(function(){ if(sc===1) show(g+1); },5000); });
  BI.addEventListener('click',function(){ var on=!INFO.classList.contains('on'); INFO.classList.toggle('on',on); BI.setAttribute('aria-pressed',on?'true':'false'); });
  document.getElementById('vw-x').addEventListener('click',function(){closeV(false)});
  document.getElementById('vw-p').addEventListener('click',function(){stopPlay(); show(g-1)});
  document.getElementById('vw-n').addEventListener('click',function(){stopPlay(); show(g+1)});
  document.getElementById('vw-zi').addEventListener('click',function(){zoomCenter(1.6)});
  document.getElementById('vw-zo').addEventListener('click',function(){zoomCenter(1/1.6)});
  document.getElementById('vw-z0').addEventListener('click',function(){sc=1;tx=0;ty=0;apply(true)});

  document.addEventListener('click',function(e){
    var c=e.target.closest('[data-carousel]');
    if(c){ var v=c.getAttribute('data-carousel'), i=0;
      if(v==='here'){ for(var k=0;k<FIGS.length;k++){ var r=FIGS[k].getBoundingClientRect(); if(r.bottom>innerHeight*0.25){ i=k; break; } } }
      openAt(i); return; }
    var b=e.target.closest('[data-g]'); if(b){ openAt(parseInt(b.getAttribute('data-g'),10)); } });
  document.addEventListener('keydown',function(e){ if(!open) return;
    if(e.key==='Escape') closeV(false); else if(e.key==='ArrowRight'&&sc===1) show(g+1); else if(e.key==='ArrowLeft'&&sc===1) show(g-1);
    else if(e.key==='+'||e.key==='=') zoomCenter(1.6); else if(e.key==='-') zoomCenter(1/1.6); else if(e.key==='0'){sc=1;tx=0;ty=0;apply(true);} });

  // Rotella / trackpad
  S.addEventListener('wheel',function(e){ e.preventDefault(); var f=Math.exp(-e.deltaY*(e.ctrlKey?0.01:0.0025)); zoomAt(sc*f,e.clientX,e.clientY,false); },{passive:false});

  // Puntatori: pizzico, trascinamento, swipe, doppio tocco
  var P={}, pinch=null, pan=null, swipe=null, lastTap=0, lastX=0, lastY=0;
  function pts(){ var a=[]; for(var k in P) a.push(P[k]); return a; }
  S.addEventListener('pointerdown',function(e){ if(e.target.closest('button')) return; S.setPointerCapture(e.pointerId); P[e.pointerId]={x:e.clientX,y:e.clientY};
    var p=pts(); stopPlay();
    if(p.length===2){ var dx=p[0].x-p[1].x, dy=p[0].y-p[1].y; pinch={d:Math.hypot(dx,dy)||1, s:sc, mx:(p[0].x+p[1].x)/2, my:(p[0].y+p[1].y)/2, tx:tx, ty:ty}; pan=null; swipe=null; }
    else if(p.length===1){ pan={x:e.clientX,y:e.clientY,tx:tx,ty:ty,t:Date.now(),moved:0}; swipe=(sc===1)?{x:e.clientX,y:e.clientY}:null; S.classList.add('drag'); } });
  S.addEventListener('pointermove',function(e){ if(!P[e.pointerId]) return; P[e.pointerId]={x:e.clientX,y:e.clientY}; var p=pts();
    if(pinch&&p.length>=2){ var dx=p[0].x-p[1].x, dy=p[0].y-p[1].y, ns=Math.max(1,Math.min(MAX,pinch.s*Math.hypot(dx,dy)/pinch.d));
      var r=S.getBoundingClientRect(), mx=(p[0].x+p[1].x)/2-r.left-r.width/2, my=(p[0].y+p[1].y)/2-r.top-r.height/2,
          m0x=pinch.mx-r.left-r.width/2, m0y=pinch.my-r.top-r.height/2, qx=(m0x-pinch.tx)/pinch.s, qy=(m0y-pinch.ty)/pinch.s;
      sc=ns; tx=mx-sc*qx; ty=my-sc*qy; if(sc===1){tx=0;ty=0;} apply(false); }
    else if(pan){ var ddx=e.clientX-pan.x, ddy=e.clientY-pan.y; pan.moved=Math.max(pan.moved,Math.hypot(ddx,ddy));
      if(sc>1){ tx=pan.tx+ddx; ty=pan.ty+ddy; apply(false); }
      else if(swipe){ I.style.transform='translate('+ddx+'px,0)'; } } });
  function end(e){ if(!P[e.pointerId]) return; delete P[e.pointerId]; var p=pts();
    if(pinch){ if(p.length<2){ pinch=null; if(p.length===1){ pan={x:p[0].x,y:p[0].y,tx:tx,ty:ty,t:Date.now(),moved:99}; } } return; }
    if(pan&&p.length===0){ S.classList.remove('drag');
      var dx=e.clientX-pan.x, dy=e.clientY-pan.y;
      if(swipe&&sc===1&&Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)){ pan=null; swipe=null; show(g+(dx<0?1:-1)); return; }
      if(swipe&&sc===1) apply(true);
      if(pan.moved<10&&Date.now()-pan.t<350){ var now=Date.now();
        if(now-lastTap<320&&Math.hypot(e.clientX-lastX,e.clientY-lastY)<40){ lastTap=0; if(sc>1.05){sc=1;tx=0;ty=0;apply(true);} else zoomAt(2.6,e.clientX,e.clientY,true); }
        else { lastTap=now; lastX=e.clientX; lastY=e.clientY; } }
      pan=null; swipe=null; } }
  S.addEventListener('pointerup',end); S.addEventListener('pointercancel',end);
  S.addEventListener('dblclick',function(e){ e.preventDefault(); });

  // Pulsante flottante
  var fab=document.getElementById('fab'), first=FIGS[0];
  function fabUpd(){ fab.classList.toggle('on', first && first.getBoundingClientRect().top<innerHeight*0.6 && !open); }
  addEventListener('scroll',fabUpd,{passive:true}); fabUpd();
})();
</script></body></html>""")
    return "\n".join(o)

open(os.path.join(HERE, '..', 'index.html'), 'w', encoding='utf-8').write(build())
print('ok', len(ALL))
