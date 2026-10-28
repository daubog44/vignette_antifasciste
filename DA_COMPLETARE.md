# Satira contro il fascismo — registro di completamento

**28 ottobre 2026: 168 immagini locali nella pagina**, con lo stesso stile e lo stesso carosello. Le 30 precedenti schede senza immagine sono state integrate; sono state aggiunte altre 53 opere o documenti di contesto. I numeri includono vignette, fotomontaggi, dipinti, manifesti, locandine, copertine e fotografie, distinti nelle didascalie.

Tutte le 58 righe della lista precedente sono conservate qui sotto. **La ricerca non è conclusa:** la stampa GL in esilio non ha ancora una tavola originale recuperata; per Il Male manca l’esempio specifico su MSI/neofascismo. Restano inoltre singoli originali, fascicoli o attribuzioni da accertare (Altan, Effel 1935, Sennep su Monaco, Herblock, alcune tavole senza data). Una scheda di contesto non viene conteggiata come recupero della vignetta mancante.

- **INSERITO**: opera con immagine identificata, oppure locandina/copertina/fotogramma della relativa opera, quattro note e fonte.
- **CONTESTO**: immagine autentica della testata, edizione o autore; la scheda spiega il rapporto con la satira e ciò che non documenta.
- **PARZIALE**: riproduzione o testo trovati, ma data, attribuzione, fascicolo o immagine originale ancora da accertare.
- **DA COMPLETARE**: manca ancora un esempio identificato e consultabile del punto specifico.
- **Diritti**: PD riguarda l’opera, non automaticamente la fotografia, la scansione o tutta la pagina. PROT indica opera protetta; una copia locale non attribuisce una licenza libera. Condizioni e attribuzioni sono nei crediti del sito e in `sorgenti/immagini.json`.

Le opere aggiuntive sono in `sorgenti/prot.py` e `sorgenti/completamenti.py`; le immagini in `img/p-*.jpg`, le miniature in `tn/p-*.jpg`. `sorgenti/immagini.json` conserva URL della riproduzione, fonte, dimensioni, diritti, nota sull’immagine e stato della verifica. I collegamenti alla fonte della scheda sono visibili anche sotto ogni opera.

Per riprendere: cercare l’originale indicato come mancante, aggiornare testo e metadati senza eliminare le incertezze ancora aperte, poi eseguire `python3 sorgenti/build.py` e `python3 -m unittest discover -s sorgenti -p 'test_*.py'`.

---

## 1. Italia 1919–1926: la satira prima del silenzio

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| Giuseppe Scalarini, «Il bastone tarlato» / «Il santo manganello» | 27 settembre 1924 | Il manganello rivela gli affari e gli scandali che lo corrodono | PD dell'opera; riproduzione Senato | INSERITO: `p-santo`, ritaglio leggibile della prima pagina dell’Avanti!; titolo originale controllato sulla scansione |
| Scalarini, altre vignette | data dei due disegni da accertare | Censura e alleanze del regime rese visibili con oggetti e gesti | PD dell'opera | PARZIALE: `p-scalarini-finestra`, `p-scalarini-abbraccio`; immagini e attribuzione nel saggio di Giovanna Delfini, fascicoli originari non indicati |
| Gabriele Galantara, copertine dell’Asino | 1922–1925 | La costruzione visiva del Duce e la denuncia della violenza | PD dell'opera | INSERITO nel percorso esistente: «Violenze inutili», «Il problema di Mussolini», «Un incontro», «Vecchi pupazzi!», «Basta!», «LUI». Non sono nuove attribuzioni |
| Il Becco Giallo, Mussolini sulla bara di Matteotti | fascicolo originario non accertato; ripresa nel 1994 | Il delitto trasformato nel sostegno del potere | Attribuzione a Chancel nella ripresa; diritti da verificare | PARZIALE: immagine trovata e inserita in `p-beccogiallo-parigi`; l’Unità, 21 maggio 1994, Cultura & Società p. 3. Non confermati il 1924 e l’attribuzione a Galantara |
| Il Becco Giallo, altre tavole | anni Venti; fascicolo da identificare | La politica del comizio come spettacolo e imbonimento | Firma e diritti da verificare | PARZIALE: `p-beccoadunata`, «L’adunata di Milano», riproduzione nel volume di Patricia Gaborik; pagina originaria ancora da identificare |
| Ettore Petrolini, «Nerone» | 1917; film 1930 | La parodia del rapporto fra leader e folla, con una lettura politica discussa | Film e riproduzione: vedere la fonte | INSERITO: `p-nerone`, fotogramma con il titolo; la scheda segnala la vicinanza di Petrolini al regime e la lettura antimussoliniana controversa |
| Trilussa, «Nummeri» | prima del 1950; prima edizione da accertare | L’Uno diventa potente grazie agli zeri che lo seguono | Poesia PD; foto: condizioni nella fonte | PARZIALE: `p-trilussa`, testo verificato nel saggio di G. Della Vecchia; immagine illustrativa dell’autore, non una vignetta. Prima edizione ancora da reperire |
| Barzellette su Mussolini: Rochelio Del Curto | 1938–1942 | La repressione della satira orale documentata da un caso di confino | Repertorio archivistico: condizioni della fonte | CONTESTO: `p-barzellette`, copertina del repertorio e scheda a p. 186. La fonte menziona le barzellette ma non ne trascrive il testo, che non viene inventato |

## 2. Italia 1926–1943: sotto il regime e in esilio

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| Il Becco Giallo a Parigi | 1927–1931; vignetta senza fascicolo accertato | La satira diffusa clandestinamente dall’esilio | Vedi attribuzione e diritti di `p-beccogiallo-parigi` | PARZIALE: inserita la vignetta sulla bara di Matteotti riprodotta da l’Unità nel 1994. Sostituisce il precedente ritratto romano di Croce del 1925 |
| Vignette di Giustizia e Libertà e dei fuorusciti | 1929–1940 | La satira dell’antifascismo organizzato in esilio | Autori vari, da verificare | DA COMPLETARE: il catalogo Rosselli verifica il Becco Giallo n. 71 (20 dicembre 1930–20 gennaio 1931) e il supplemento GL «Massinelli e la crisi mondiale», ma non fornisce una tavola leggibile. `p-cacasenno` riguarda invece la GL partigiana del 1944, non questo periodo |
| «Pippo non lo sa» | 1939 | Una canzone letta come allusione a Starace, con una diversa spiegazione dell’autore | PROT; copertina dello spartito dalla fonte | INSERITO: `p-pippo`; corretto il precedente 1940. Immagine dello spartito e scheda con entrambe le interpretazioni |
| Bertoldo e Marc’Aurelio | 9 giugno 1939; 13 gennaio 1932 | Distinguere l’umorismo tollerato dall’opposizione antifascista | Autori vari; PROT o da verificare | CONTESTO: `p-bertoldo` e `p-marcaurelio`, prime pagine riprodotte nel catalogo «Matite appuntite» della Biblioteca del Senato |

## 3. Resistenza 1943–1945

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| «La Badoglieide» | notte 25–26 aprile 1944 | Satira partigiana contro Badoglio | Canzone e incisioni: diritti diversi, da verificare | INSERITO: `p-badoglieide`; immagine di edizioni discografiche successive, indicata come tale. Testimonianza di Revelli e ritornello piemontese nella scheda |
| Vignette nei fogli clandestini: Il Cacasenno | 31 ottobre 1944 | Polemica e umorismo anche dentro la comunità partigiana | Autori vari; condizioni dell’archivio Parri | INSERITO: `p-cacasenno`, n. 2, prima pagina completa; fonte e attribuzione della testata verificate nella banca dati della stampa clandestina |
| Francesco Olivucci, incisioni della Resistenza | corpus 1938–1948; tavola non datata | L’illustrazione come denuncia della repressione | Da verificare con l’istituto conservatore | PARZIALE: `p-olivucci`, riproduzione dell’Istituto storico di Forlì-Cesena; non si assegna alla singola tavola una data o una pubblicazione clandestina non attestate |
| Volantini alleati in italiano | luglio e agosto 1943 | Rovesciare la retorica dei capi e indurre a smettere di combattere per Hitler | Anonimi; diritti della riproduzione da verificare | INSERITO: `p-alleati` («Tiranni che ridono…») e `p-alleati-hitler` («Perché morire per Hitler?»), Archivio di Stato di Napoli / Metroart. Nessuna presunzione di PD solo perché propaganda alleata |
| Cantachiaro, «Tutto il potere ai C.L.N.» | 21 ottobre 1944 | La satira torna alla politica italiana nella Roma liberata | Firma non identificata; condizioni Senato | INSERITO: `p-cantachiaro`, prima pagina nell’Archivio storico del Senato, fondo Bonomi, unità 69; didascalia e commento riferiti all’immagine effettivamente mostrata |

## 4. Germania, Austria, Europa centrale prima del 1933

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| Simplicissimus (Heine, Schilling) | 1929–1931 | Satira dei nazisti prima della conquista del potere | PD secondo le singole fonti | INSERITO: cinque immagini già nel percorso; fonti nei crediti |
| Karl Arnold, «Der Münchner» | 3 dicembre 1923 | Le svastiche occupano lo sguardo del normale avventore di birreria | PD dell’opera; riproduzione Kultur-Vollzug / VG Bild-Kunst | INSERITO: `p-arnold`; autore, data, n. 36 e p. 441 del Simplicissimus verificati nell’archivio Haus der Bayerischen Geschichte |
| Erich Ohser, «Dringend ruhebedürftig» | 1932 | Il Hitler del manifesto e quello reale messi in contrasto | PD dell’opera | INSERITO: `s08`, con immagine locale; ulteriori tavole del Vorwärts restano un ampliamento del corpus |
| George Grosz, «I pilastri della società» | 1926 | Le élite di Weimar e la violenza nazionalista come bersagli | PROT; riproduzione bpk / Nationalgalerie | INSERITO: `p-grosz`, immagine e fonte GHDI; è un dipinto, distinto dalle vignette di giornale |
| John Heartfield, altri fotomontaggi | 1932; ripresa espositiva 1964 | Denaro e guerra dietro il mito del nazismo | PROT; Akademie der Künste | INSERITO: `p-hf-super` («Adolf, der Übermensch») e `p-hf-war` («Krieg und Leichen»). Per il secondo è mostrato un volantino di mostra del 1964 che riprende l’opera del 1932 |

## 5. Mondo 1922–1945

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| David Low, «The Harmony Boys» | 2 maggio 1940 | Hitler dirige il coro di Mussolini, Stalin e Franco | PROT; fonte della riproduzione nei crediti | INSERITO: `p-low-harmony`; non viene presentata come una tavola della serie «Hit and Muss» |
| Sidney Strube ed E. H. Shepard | 2 settembre 1939; 18 marzo 1936 | Il carro verso la guerra e il falso ramoscello di pace | PROT nel 2026; riproduzioni e filigrane conservate | INSERITO: `p-strube`, «Juggernaut», e `p-shepard`, «The Goose-Step»; per Shepard data originale verificata dalla Library of Congress |
| Le Canard enchaîné, Le Rire, Sennep | 1933, 1935, 1938 | Diversi orientamenti della satira francese sui dittatori | PROT / autori diversi | INSERITO: `p-canard`, n. 871, 8 marzo 1933, e `p-lerire`, Paul Ordner, 30 novembre 1935. CONTESTO per Sennep: `p-sennep`, copertina dell’album Gassier–Sennep del 1938; tavola di Monaco da recuperare, non disponibile nella tesi consultata |
| Jean Effel e L’Os à moelle | 13 maggio 1938; pista album 1935 | L’assurdo del gruppo di Pierre Dac contro i dittatori | Autori vari; riproduzione mahJ / Archives Jacques Pessis | CONTESTO: `p-effel`, dettaglio del primo numero e collaborazione verificata dal museo. DA COMPLETARE l’identificazione dell’album antifascista del 1935; non attribuiti a Effel disegni senza firma |
| Leopoldo Méndez, Taller de Gráfica Popular | 1942; volume 1943 | La denuncia antifascista messicana delle deportazioni | PROT; Madison Museum of Contemporary Art | INSERITO: `p-mendez`, «Deportación a la muerte»; la scheda distingue denuncia e satira comica |
| Manifesti repubblicani spagnoli | 1936–1939 | L’immagine come mobilitazione contro il fascismo | Autori diversi; verificare singola fonte | INSERITO: aggiunto `p-spagna`, «Aixafem el feixisme» (Pere Català Pic, 1936, MNAC), oltre a «El generalísimo» già presente |
| L’Esquella de la Torratxa, Pere Calders | 3 giugno 1938 | Un falso Nobel per Hitler smonta la retorica della pace | PROT; fondo Pere Calders, UAB | INSERITO: `p-esquella`, ritaglio n. 3066, pp. 328–329. Notizia satirica, non candidatura storica attestata |
| Fitzpatrick, Kirby, Herblock | 1933–1941 | La satira americana prima dell’intervento in guerra | PROT / condizioni delle singole collezioni | INSERITO: `p-kirby`, 1 febbraio 1933, e `p-fitzpatrick`, 8 giugno 1940. DA COMPLETARE Herblock: scheda LOC «They’re still there, boss!», 22 aprile 1941, identificata; immagine non scaricata perché l’accesso disponibile non l’ha restituita |
| Three Stooges, «You Nazty Spy!» | 19 gennaio 1940 | Parodia hollywoodiana di Hitler precedente a Chaplin | Da verificare per film e locandina | INSERITO: `p-nazty`, locandina locale e scheda |
| Disney, «Education for Death»; Bugs Bunny, «Herr Meets Hare» | 1943; 1945 | Indottrinamento e gerarchia nazista nell’animazione | PROT | INSERITO: `p-education`, locandina; `p-herrhare`, cartello del titolo |
| Sapajou e Ding Cong | 1937 | Satira e guerra in Asia, con posizioni politiche diverse | Sapajou PD per il disegno; testi e riproduzioni da verificare. Ding Cong PROT | INSERITO: `p-dingcong`, tavola del 25 ottobre 1937, e `p-sapajou`, copertina di «Shanghai’s Schemozzle». Per Sapajou non si presume un antifascismo coerente |

## 6. Italia dal 1945 a oggi

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| «Tutti a casa» | 1960 | Dall’obbedienza senza ordini alla scelta della Resistenza | PROT | INSERITO: `p-tuttiacasa`, immagine locale e scheda |
| «Il federale», «La marcia su Roma», «Amarcord», «Vogliamo i colonnelli» | 1961–1973 | Autorità, conformismo e memoria fascista nella commedia | PROT | INSERITO: `p-federale`, `p-marcia`, `p-amarcord`, `p-colonnelli`, tutte con immagini locali |
| «Pasqualino Settebellezze» | 1975 | Grottesco, opportunismo e sopravvivenza nel lager | PROT | INSERITO: `p-pasqualino`, fotogramma e scheda |
| «La vita è bella» | 1997 | Il linguaggio comico come protezione fragile del bambino | PROT | INSERITO: `p-vitabella`, fotogramma e scheda; discussione della scelta fiabesca nel contesto |
| Il Male | 1978–1982; riproduzione 2019 | Falsi quotidiani, provocazioni e controinformazione | PROT | CONTESTO: `p-male`, «Tutti gli uomini del presidente», dalla mostra WeGil. DA COMPLETARE una tavola precisa su MSI o neofascismo: il ritratto della redazione non viene spacciato per quella tavola |
| Altan, «Ci tocca vedere un’altra volta i fasci al governo» | 1994; fascicolo da identificare | La longevità trasformata nella condanna a rivedere la storia | Vignetta PROT; foto Maurizio Codogno CC BY 4.0 | PARZIALE: `p-altan`, battuta e anno verificati nell’Espresso del 9 novembre 2022; ritratto illustrativo, originale della vignetta non ancora trovato |
| Cuore | 1989–1996; pagina del 5 marzo 1990 | L’autocritica della sinistra e il settimanale di resistenza umana | PROT / autori diversi | CONTESTO: `p-cuore`, prima pagina n. 9, «Stiamo con voi!», verificata nella scansione de l’Unità. Non presentata come una copertina del 1994 |
| Vauro, Mauro Biani, Makkox, Staino | 2006, 2011, 2021, 2022 | La memoria del 25 aprile messa alla prova dal presente | Biani CC BY-NC-ND 4.0; altri PROT | INSERITO: `p-biani` (25 aprile 2006), `p-makkox` (25 aprile 2011, tavola completa), `p-staino` (24 aprile 2021), `p-vauro` (26 aprile 2022), con fonti e date |
| Andrea Pazienza, «Pertini» | ottobre 1983 | Il presidente partigiano diventa compagno di avventure comiche | PROT | INSERITO: `p-pazienza`, copertina della prima edizione, supplemento a Frigidaire 35/36; fonte L’Arengario |
| «Fascisti su Marte» | 2002–2006 | La retorica fascista trasferita nella fantascienza | PROT per l’opera; foto del cast CC BY-SA 3.0 | INSERITO: `p-guzzanti`, foto del cast locale e scheda |
| Zerocalcare, «La banalità del nazi» | 14 gennaio 2018 | Il neofascismo contemporaneo oltre la retorica dell’eccezione | PROT | INSERITO: `p-zerocalcare`, copertina dell’Espresso, non le quattordici pagine del fumetto |
| Francesco Filippi, «Mussolini ha fatto anche cose buone» | 2019 | Il titolo ironico introduce la verifica dei miti sul regime | PROT | CONTESTO: `p-filippi`, copertina Bollati Boringhieri; libro di storia, non raccolta di satira |
| «Sono tornato», «M. Il figlio del secolo» | 2018; 2025 | Il ritorno immaginario e la rappresentazione contemporanea del fascismo | PROT | INSERITO: `p-sonotornato`, fotogramma, e `p-mfiglio`, cartello del titolo |
| Lercio, La Russa e il busto del Duce | 15 gennaio 2024 | La finta notizia porta all’assurdo le giustificazioni dei nostalgici | Testo PROT; foto LucaFazPhoto CC BY-SA 4.0 | INSERITO: `p-lercio`, articolo di Gianni Zoccheddu verificato nella fonte originale. Foto illustrativa del 2025, non immagine dell’articolo; dichiarazioni inventate chiaramente segnalate |

## 7. Mondo dal 1945 a oggi

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| Monty Python, «Mr. Hilter» | 4 gennaio 1970 | Hitler e i complici nascosti in una pensione inglese | PROT | INSERITO: `p-hilter`, copertina dell’album del 1970 che contiene lo sketch, non fotogramma dell’episodio |
| Fawlty Towers, «The Germans» | 24 ottobre 1975 | Il personaggio che vieta di parlare della guerra continua a evocarla | PROT | INSERITO: `p-fawlty`, fotogramma e scheda |
| «’Allo ’Allo!» | 1982–1992 | L’occupazione trasformata in una macchina di equivoci | PROT | INSERITO: `p-allo`, immagine con il titolo e scheda |
| «Hogan’s Heroes» | 1965–1971 | I prigionieri manipolano carcerieri incapaci | PROT | INSERITO: `p-hogan`, logo della serie; distinta l’ambientazione in uno Stalag da un campo di sterminio |
| «To Be or Not to Be», remake | 1983 | Travestimenti teatrali contro la gerarchia nazista | PROT | INSERITO: `p-brooks1983`, locandina; regia di Alan Johnson, Brooks protagonista e produttore |
| Art Spiegelman, «Maus» | 1980–1991 | La metafora animale rovescia la disumanizzazione della propaganda | PROT | CONTESTO: `p-maus`, copertina e scheda; testimonianza sulla Shoah, non satira del lager |
| «Inglourious Basterds» | 2009 | La propaganda distrutta dentro un cinema, in una storia alternativa | PROT | INSERITO: `p-basterds`, locandina; finale esplicitamente distinto dalla morte storica di Hitler |
| «Iron Sky» | 2012 | Nazisti sulla Luna e riciclo terrestre della propaganda | PROT | INSERITO: `p-ironsky`, locandina e scheda |
| «Lui è tornato», «Jojo Rabbit» | 2015; 2019 | Il dittatore come ritorno mediatico e amico immaginario | PROT | INSERITO: `p-luietornato`, `p-jojo`, locandine locali |
| Meme: Downfall, «Are we the baddies», FCK NZS, «punch a Nazi», Popper | 2006–oggi | La satira circola per citazioni, remix e simboli | Diritti diversi: vedere i singoli crediti | INSERITO nel percorso esistente; anche `p-downfall` e `p-baddies` hanno ora fotogrammi locali |
| Pepe the Frog: appropriazione e riappropriazione | personaggio 2004; appropriazione 2016 | L’ironia può essere usata anche dall’estrema destra | Matt Furie, PROT | CONTESTO: `p-pepe`, disegno pacifico di Furie per SAVE THE FROGS!; immagine dell’autore, non una variante nazista del personaggio |

---

Ultimo aggiornamento: 28 ottobre 2026.
