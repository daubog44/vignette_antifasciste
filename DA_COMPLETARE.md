# Satira contro il fascismo — cosa manca

Elenco di lavoro per completare l'excursus. Ogni voce ha:
- **Diritti**: `PD` = pubblico dominio (immagine ripubblicabile, va in `img/` con scheda normale); `PROT` = protetta (scheda in `sorgenti/prot.py`, immagine solo in `privato/`).
- **Stato**: `FATTO` = già nella pagina; `DA VERIFICARE` = pista nota ma ancora da controllare su una fonte primaria prima di scriverne; `PISTA` = so che esiste un filone, va cercata l'opera precisa.

Regola: niente schede senza fonte. Data, autore, testata e testo della battuta vanno controllati su un archivio, un museo, un catalogo o una fonte giornalistica seria.

Come aggiungere:
- immagine libera → scaricarla (Wikimedia Commons, Europeana, Library of Congress, archivi), metterla in `img/` e `tn/`, aggiungere la riga in `_EXTRA` di `sorgenti/content.py`, i testi in `sorgenti/testi.py`, dimensioni in `sorgenti/sizes.json`, licenza in `sorgenti/credits.json`;
- opera protetta → nuova voce `_P(...)` in `sorgenti/prot.py`;
- poi `python3 sorgenti/build.py`.

---

## 1. Italia 1919–1926: la satira prima del silenzio

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| Giuseppe Scalarini, «Il santo manganello» | Avanti!, 27 set 1924 | La sua tavola più dura sul fascismo: solo il manganello insanguinato | PD (morto 1948) | DA VERIFICARE: serve una copia leggibile (Centro studi Ustica, Fondazione Anna Kuliscioff, Biblioteca di via Senato) |
| Scalarini, altre vignette 1921–26 (squadrismo, olio di ricino, agrari) | 1921–26 | Codificano i simboli della satira antifascista | PD | PISTA: archivio digitale dell'Avanti! (Senato/Fondazione Nenni) |
| Gabriele Galantara, altre copertine dell'Asino 1921–25 | 1921–25 | L'Asino è il settimanale satirico chiave del periodo | PD (morto 1937) | PISTA: Commons ne ha solo una parte; cercare collezioni digitali (Biblioteca Braidense, Emeroteca) |
| Il Becco Giallo, copertina con Mussolini seduto sulla bara di Matteotti | 1924 | Citata spesso come «classica» | dipende dall'autore | DA VERIFICARE: non trovata in archivi affidabili |
| Il Becco Giallo, altre tavole 1924–26 | 1924–26 | Il giornale antifascista per eccellenza | autori vari (molti morti prima del 1955 → PD) | PISTA: antologia a cura di Oreste Del Buono e Lietta Tornabuoni |
| Ettore Petrolini, «Nerone» | teatro 1917, film 1930 | Letto come parodia di Mussolini e del rapporto con la folla («Bravo! Grazie!») | PD (morto 1936) | DA VERIFICARE: quanto la lettura antifascista è dell'epoca e quanto successiva |
| Trilussa, poesie romanesche sul potere | anni '20–'40 | Satira in versi tollerata ma pungente | PD (morto 1950) | PISTA: individuare i testi con riferimento esplicito al regime |
| Barzellette su Mussolini e processi per «offesa al Duce» | 1926–43 | La satira orale, punita dal Tribunale speciale | — | PISTA: studi di storici sull'umorismo popolare sotto il regime; Archivio centrale dello Stato |

## 2. Italia 1926–1943: sotto il regime e in esilio

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| Il Becco Giallo a Parigi | 1927–31 | Satira dall'esilio | PROT/PD misto | FATTO (scheda) |
| Vignette di Giustizia e Libertà e della stampa dei fuorusciti | 1929–40 | La satira dell'antifascismo organizzato | vari | PISTA: Istituto Ferruccio Parri, Archivio GL |
| «Pippo non lo sa» | canzone, 1940 | Hit radiofonico letto come presa in giro di Starace | PROT | DA VERIFICARE: autori e fonte dell'aneddoto |
| Bertoldo, Marc'Aurelio | 1931–43 | Umorismo tollerato, a volte allusivo; scuola di Guareschi, Mosca, Metz, Fellini | PROT | PISTA: solo come contesto, non è satira antifascista dichiarata |

## 3. Resistenza 1943–1945

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| «La Badoglieide» | canzone partigiana, 1944 | Satira in musica contro Badoglio, cantata dalle brigate GL in Piemonte | PROT/da verificare | DA VERIFICARE: autori (Nuto Revelli e altri), testo |
| Vignette nei fogli clandestini (stampa partigiana) | 1943–45 | Oltre 4.000 numeri di giornali e manifesti clandestini | autori spesso anonimi | PISTA: stampaclandestina.it (Istituto Parri), Istituti storici della Resistenza, Biblioteca Sormani |
| Francesco Olivucci, incisioni per la stampa clandestina (Forlì) | 1943–45 | Un illustratore della Resistenza documentato | da verificare | PISTA: articolo su Progetto Grafico (AIAP) |
| Volantini satirici alleati in italiano | 1943–45 | Propaganda che deride la Repubblica sociale | spesso PD (governativi) | PISTA: Commons, Imperial War Museum |
| Cantachiaro | 1944 | Prima satira libera dopo la Liberazione | — | FATTO (scheda) |

## 4. Germania, Austria, Europa centrale prima del 1933

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| Simplicissimus (Heine, Schilling) | 1929–31 | — | PD | FATTO (5 immagini) |
| Karl Arnold, tavole su Hitler dopo il putsch | 1923–32 | Primo sguardo satirico su Hitler a Monaco | PD (morto 1953) | DA VERIFICARE: cercare su Commons e simplicissimus.info |
| Erich Ohser (e.o.plauen), caricature di Hitler per il Vorwärts | 1929–33 | Satira socialdemocratica; Ohser fu arrestato nel 1944 e morì in carcere | PD (morto 1944) | DA VERIFICARE: copie digitali |
| George Grosz, disegni contro i nazisti | anni '20–'30 | Il grande grafico del dissenso di Weimar | PROT (morto 1959) | PISTA |
| John Heartfield, altri fotomontaggi (es. «Krieg und Leichen», «Adolf, der Übermensch») | 1932–38 | Il corpus antinazista più importante | PROT (fino al 2039) | PISTA: heartfield.adk.de |

## 5. Mondo 1922–1945

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| David Low, vignette su Mussolini (es. la striscia «Hit and Muss», 1937) | 1923–43 | Il vignettista più famoso del mondo contro i dittatori | PROT (fino al 2033) | PISTA: British Cartoon Archive (archive.cartoons.ac.uk) |
| Sidney Strube (Daily Express), E. H. Shepard (Punch) | anni '30 | Satira britannica su Mussolini | Strube PD? (morto 1956 → PD dal 2027); Shepard PROT | DA VERIFICARE |
| Le Canard enchaîné, Le Rire, Sennep | anni '30 | La satira francese su Mussolini e Hitler | PROT in gran parte | PISTA: Gallica (BnF) |
| Jean Effel | anni '30–'40 | Caricature antifasciste francesi | PROT | PISTA |
| Taller de Gráfica Popular (Messico), Leopoldo Méndez | 1937–45 | Incisioni antifasciste | PROT | PISTA |
| Manifesti repubblicani spagnoli (Renau, Bardasano, Arteche…) | 1936–39 | Satira visiva della guerra civile | per lo più PROT; anonimi PD | FATTO in parte («El generalísimo»); PISTA: Biblioteca Nacional de España, Pavelló de la República |
| L'Esquella de la Torratxa (Barcellona) | anni '30 | Satira catalana antifascista | misto | PISTA: ARCA (Arxiu de Revistes Catalanes Antigues) |
| Daniel Fitzpatrick (St. Louis Post-Dispatch), Rollin Kirby, Herblock | 1930–45 | Le grandi vignette americane sui dittatori | PROT/da verificare | PISTA: Library of Congress |
| Three Stooges, «You Nazty Spy!» | 1940 | Primo film hollywoodiano a deridere Hitler, prima di Chaplin | da verificare | DA VERIFICARE |
| Disney, «Education for Death»; Bugs Bunny, «Herr Meets Hare» | 1943–45 | Altri cartoni antinazisti | PROT | PISTA |
| Sapajou (Shanghai), Ding Cong | anni '30–'40 | Satira in Asia | da verificare | PISTA |

## 6. Italia dal 1945 a oggi

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| «Tutti a casa» (Comencini) | 1960 | L'8 settembre come commedia amara | PROT | DA VERIFICARE |
| «Il federale», «La marcia su Roma», «Amarcord», «Vogliamo i colonnelli» | 1961–73 | — | PROT | FATTO |
| «Pasqualino Settebellezze» (Wertmüller) | 1975 | Grottesco sul fascismo e sui lager | PROT | DA VERIFICARE |
| «La vita è bella» (Benigni) | 1997 | Comicità dentro il lager, tre Oscar | PROT | DA VERIFICARE |
| Il Male | 1978–82 | Le false prime pagine; serve una tavola precisa sul neofascismo o sull'MSI | PROT | PISTA: «Gli anni del Male» (DeriveApprodi 2024), mostra WeGil 2019 |
| Altan | dal 1975 | Il «1994» citato nel testo va verificato: serve testo esatto e data | PROT | DA VERIFICARE |
| Cuore (Michele Serra) | 1989–96 | Satira degli anni del ritorno della destra al governo | PROT | PISTA |
| Vauro, Mauro Biani, Makkox, Staino | 1980–oggi | Vignettisti antifascisti contemporanei | PROT | PISTA: cercare vignette su neofascismo datate (25 aprile, Predappio, saluti romani di Acca Larenzia) |
| Andrea Pazienza | 1977–88 | Fumetto e satira politica | PROT | PISTA |
| «Fascisti su Marte» | 2002–06 | — | PROT | FATTO |
| Zerocalcare | 2018 | — | PROT | FATTO |
| Francesco Filippi, «Mussolini ha fatto anche cose buone» | 2019 | Il titolo ironico contro il luogo comune | PROT | PISTA (libro di storia, non satira in senso stretto) |
| «Sono tornato», «M. Il figlio del secolo» | 2018, 2025 | — | PROT | FATTO |
| Lercio | dal 2012 | Satira in forma di finta notizia, spesso sui nostalgici | PROT | PISTA |

## 7. Mondo dal 1945 a oggi

| Opera / autore | Anno | Perché conta | Diritti | Stato |
|---|---|---|---|---|
| Monty Python, «Mr. Hilter» | 1970 | Hitler in vacanza in una pensione inglese | PROT | DA VERIFICARE |
| «Fawlty Towers», episodio «The Germans» | 1975 | «Don't mention the war!» | PROT | DA VERIFICARE |
| «'Allo 'Allo!» | 1982–92 | Sitcom della BBC sull'occupazione in Francia | PROT | DA VERIFICARE |
| «Hogan's Heroes» | 1965–71 | Sitcom americana in un campo di prigionia | PROT | PISTA |
| Mel Brooks, «To Be or Not to Be» (remake) | 1983 | — | PROT | PISTA |
| Art Spiegelman, «Maus» | 1980–91 | Non è satira, ma usa la metafora animale della propaganda nazista | PROT | PISTA (da valutare se includere) |
| «Inglourious Basterds» (Tarantino) | 2009 | La storia riscritta: Hitler ucciso in un cinema | PROT | DA VERIFICARE |
| «Iron Sky» | 2012 | Nazisti sulla Luna | PROT | PISTA |
| «Lui è tornato», «Jojo Rabbit» | 2015, 2019 | — | PROT | FATTO |
| Meme: Downfall, «Are we the baddies», FCK NZS, «punch a Nazi», Popper | 2006–oggi | — | — | FATTO |
| Contro-esempio: l'appropriazione dell'ironia da parte dell'estrema destra (Pepe the Frog, l'«Hitler buffo») | 2015–oggi | Mostra il limite dell'ironia come arma | — | PISTA (il testo dell'epoca «oggi» ne parla; si potrebbe dare una scheda) |

---

Ultimo aggiornamento: ottobre 2026.
