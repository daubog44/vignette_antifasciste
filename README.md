# vignette_antifasciste

**Satira contro il fascismo. Cent'anni di vignette contro il Duce, dall'Avanti! ai meme.**

Un excursus storico in una sola pagina web: 171 immagini dal 1914 a oggi, ognuna con quattro note brevi: cosa si vede, dove sta l'ironia, il contesto, il segno. Si legge scorrendo, oppure si sfoglia in carosello con zoom (pizzico, doppio tocco, rotella). Le immagini comprendono vignette, fotomontaggi, manifesti, dipinti, locandine, copertine e fotografie: le didascalie precisano quale documento viene mostrato.

## Contenuto

| Percorso | Cosa contiene |
|---|---|
| `index.html` | La pagina completa: testi, stile e visore in un solo file |
| `img/` | Immagini locali, normalmente con lato lungo massimo di 1920 px; le strisce molto lunghe mantengono la risoluzione originale |
| `tn/` | Le miniature per la striscia del carosello |
| `sorgenti/` | Lo script che genera `index.html` e i testi |
| `DA_COMPLETARE.md` | Tutte le 58 voci della lista di lavoro, con anno, rilevanza, diritti, verifica ed eventuali ricerche ancora aperte |

## Rigenerare la pagina

I testi stanno in `sorgenti/content.py` (titoli, date, capitoli, collegamenti), `sorgenti/testi.py` (le quattro note), `sorgenti/prot.py` e `sorgenti/completamenti.py` (opere aggiuntive e relative fonti). `sorgenti/immagini.json` registra le 86 immagini aggiuntive, le dimensioni, gli URL delle copie scaricate, i diritti, le note e lo stato della verifica. Dopo una modifica:

```sh
python3 sorgenti/build.py
python3 -m unittest discover -s sorgenti -p 'test_*.py'
```

Lo script riscrive `index.html` nella cartella principale. Non servono librerie esterne.

## Pubblicarla con GitHub Pages

Il sito è pubblicato su [GitHub Pages](https://daubog44.github.io/vignette_antifasciste/), dal branch `main`, cartella `/ (root)`. Dopo aver rigenerato la pagina, un push su `main` aggiorna la pubblicazione.

## Immagini e diritti

Le immagini vengono da Wikimedia Commons, Heartfield Online, musei, archivi, siti degli autori e riproduzioni bibliografiche. Le fonti storiche sono collegate nelle schede; fonti delle immagini e diritti sono anche nell'elenco «Crediti delle immagini». I dati sono in `sorgenti/credits.json` e `sorgenti/immagini.json`.

Tutte le 30 precedenti schede senza immagine hanno ora copie locali in `img/p-*.jpg` e miniature in `tn/p-*.jpg`; sono state aggiunte altre 56 opere o documenti di contesto. Si vedono nella pagina e nel carosello senza caricare immagini dai siti originali, mantenendo lo stile delle altre opere.

Le opere protette restano dei rispettivi titolari; la loro presenza nella repo non implica una licenza libera. Le copie sono compresse, le miniature ridimensionate e le filigrane conservate. I ritagli da scansioni di giornali sono dichiarati nelle didascalie e mantengono opera e attribuzione disponibili. Una foto dell'autore o una copertina sono indicate come immagini di riferimento, senza presentarle come la vignetta originale.

Sono inclusi una prima pagina di La Libertà del 1º gennaio 1931 per la stampa dei fuorusciti, Herblock del 22 aprile 1941 e una vignetta di Altan dalla raccolta Fianco-dest! del 2025. La ricerca resta aperta sui punti indicati in `DA_COMPLETARE.md`: una tavola del Male su MSI/neofascismo, il supplemento specifico GL e alcuni originali o fascicoli ancora da identificare. Le schede distinguono quanto è stato recuperato dalle piste non confermate.
