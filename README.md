# vignette_antifasciste

**Satira contro il fascismo. Cent'anni di vignette contro il Duce, dall'Avanti! ai meme.**

Un excursus storico in una sola pagina web: 77 immagini dal 1914 a oggi, ognuna con quattro note brevi: cosa si vede, dove sta l'ironia, il contesto, il segno. Si legge scorrendo, oppure si sfoglia in carosello con zoom (pizzico, doppio tocco, rotella).

## Contenuto

| Percorso | Cosa contiene |
|---|---|
| `index.html` | La pagina completa: testi, stile e visore in un solo file |
| `img/` | Le immagini in alta risoluzione (lato lungo max 1920 px) |
| `tn/` | Le miniature per la striscia del carosello |
| `sorgenti/` | Lo script che genera `index.html` e i testi |

## Rigenerare la pagina

I testi stanno in due file: `sorgenti/content.py` (titoli, date, capitoli, collegamenti) e `sorgenti/testi.py` (per ogni immagine: cosa si vede, l'ironia, il contesto, il segno). Dopo una modifica:

```sh
python3 sorgenti/build.py
```

Lo script riscrive `index.html` nella cartella principale. Non servono librerie esterne.

## Pubblicarla con GitHub Pages

Settings → Pages → Source: *Deploy from a branch* → branch `main`, cartella `/ (root)`. La pagina sarà su `https://daubog44.github.io/vignette_antifasciste/`.

## Immagini e diritti

Tutte le immagini vengono da Wikimedia Commons e sono di pubblico dominio oppure sotto licenza Creative Commons. Per quelle CC l'attribuzione completa è nell'elenco «Crediti delle immagini» in fondo alla pagina, con il collegamento alla scheda di Commons (i dati sono anche in `sorgenti/credits.json`).

Le opere ancora protette da diritto d'autore (David Low, John Heartfield, Disney, i vignettisti e i meme contemporanei) non sono incluse: la pagina le cita con un collegamento alla fonte.
