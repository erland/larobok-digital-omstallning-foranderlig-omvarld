# Projektstatus – 0.3.7

- Fas: faktagranskning; etapp 1–2 genomförda för samtliga kapitel; juridisk slutgranskning återstår.
- Bokinriktning: godkänd; 16 planerade kapitel.
- Inledning: första utkast.
- Kapitel 1: redaktionellt koncentrerat; slutlig faktagranskning återstår.
- Kapitel 2: redaktionellt koncentrerat; juridisk slutgranskning återstår.
- Kapitel 3: redaktionellt koncentrerat; slutlig faktagranskning återstår.
- Kapitel 4: sammanhängande manus; slutlig juridisk och redaktionell faktagranskning återstår.
- Kapitel 5: sammanhängande manus; slutlig rättslig och redaktionell granskning återstår.
- Kapitel 6: sammanhängande manus; slutlig faktagranskning återstår.
- Kapitel 7: sammanhängande manus; slutlig faktagranskning återstår.
- Kapitel 8: sammanhängande manus; slutlig juridisk och redaktionell faktagranskning återstår.
- Kapitel 9: sammanhängande manus; slutlig faktagranskning återstår.
- Kapitel 10: sammanhängande manus, slutlig granskning återstår.
- Kapitel 11: sammanhängande manus; slutlig faktagranskning återstår.
- Kapitel 12: sammanhängande manus; slutlig faktagranskning återstår.
- Kapitel 13: sammanhängande manus; slutlig juridisk och redaktionell faktagranskning återstår.
- Kapitel 14: sammanhängande manus; slutlig juridisk och redaktionell granskning återstår.
- Kapitel 15: sammanhängande manus; slutlig faktagranskning återstår.
- Kapitel 16: sammanhängande manus; slutlig faktagranskning återstår.
- Omslag: uppskjutet. Inre bilder: ej beslutade.
- EPUB/PDF: ingen slutlig export.

## Redaktionellt nuläge, revision 24

- Kapitel 1–16 är skrivna och genomgångna i en första redaktionell koncentrering.
- Samlad helhetsläsning genomförd: `docs/redaktionell-slutlasning-2026-10-14.md`.
- Ingen utfyllnad för att nå ett sidmål. Kapitlen behöver inte förlängas.
- Slutlig käll-/faktakontroll, korrektur, EPUB/PDF och omslag återstår.

## Nästa steg

Fortsätt påståendebaserad faktagranskning i återstående kapitel och slutpröva identifierade juridiska tillämpningsfrågor. Rätta endast belagda fel och dokumentera verifieringsstatus innan korrektur och provexport.

## Källgranskning – etapp 1

Fyra lokala textpreciseringar i kapitel 5, 8, 9 och 10. Kapitel 4 kontrollerat utan textändring. Se `docs/faktagranskning-etapp-1-2026-10-14.md`.

## Faktagranskning – etapp 2

Se `docs/faktagranskning-etapp-2-2026-10-14.md` för granskning av kapitel 1–3, 6–7 och 11–16. Käll- och juridisk slutkontroll återstår före publicering.

## Käll- och referenskontroll

Se `docs/kall-och-referenskontroll-2026-10-14.md`. Intern K-referensstruktur kontrollerad; fullständig extern länkverifiering och juridisk sakkunniggranskning återstår. Nästa steg: slutkorrektur och provexport.

## Slutkorrektur och kontroll av tidigare åtgärder

Referensformat för kapitel 1–3 harmoniserat och kapitel 3:s underrubriker normaliserade. Se `docs/slutkorrektur-och-avstamning-2026-10-14.md` för kvarvarande punkter från den tidigare slutläsningen. Extern länk-/sakverifiering, juridisk sakkunniggranskning och provexport återstår.

## Provexport 0.4.0
EPUB/PDF provbyggda. Se `docs/provexport-2026-10-14.md`. Slutlig publicering blockerad av käll- och juridisk kontroll samt fullständig layoutgranskning.

## Provutgåva 0.4.0
- Kapitelvisa källavsnitt ersatta av gemensamt register efter kapitel 16.
- Publiceringsinterna granskningsanmärkningar borttagna ur exporterad text.
- PDF-tabeller har radlinjer och EPUB-tabeller har kanter och växlande radbakgrund.
- Fullständig juridisk slutgranskning och extern länkkontroll återstår före publicering.

## Export 0.4.0
Klickbara interna källhänvisningar, centrerade kapitelstarter och GitHub Actions för förhandsbygge och release. Actions ej körda på GitHub ännu.

## Layoutjustering 0.4.1

PDF och EPUB provbyggda. EPUB:s navigeringsdokument ligger inte i den linjära läsordningen. Se `docs/layoutjustering-0.4.1.md`.

## Omslag i export – version 0.4.3

Omslagsbilden `assets/cover/omslag.png` används automatiskt av exportskriptet för både EPUB och PDF. Lokal provexport verifierad 2026-10-14. GitHub Actions använder samma `scripts/build_book.py` som anropar exportskriptet; GitHub-körning återstår att verifiera i GitHub.
