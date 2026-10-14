# Digital omställning i en föränderlig omvärld

Analytisk faktabok av **Erland Lindmark**, version **0.4.3**.

Undertitel: *Från europeiska regelverk och teknikutveckling till strategiska vägval i samhällsviktig myndighetsverksamhet*.

Boken utgår från eSams radarbild från februari 2026 och innehåller en inledning, 16 kapitel och ett gemensamt källregister. Den behandlar digital omställning för samhällsviktiga myndigheter, med exempel från kontroll, uppbörd, tillsyn, informationsutbyte och brottsbekämpning utan att namnge någon enskild myndighet.

## Bygg och verifiera

```bash
python3 -m pip install pyyaml lxml
python3 scripts/validate_project.py .
python3 scripts/project_integrity.py verify .
python3 scripts/build_book.py
```

PDF-export kräver Pandoc och XeLaTeX inklusive relevanta TeX-paket. EPUB använder Pandoc. Omslaget finns i `assets/cover/omslag.png`. Byggfiler skapas i `exports/` och ingår inte i integritetskontrollen.

## GitHub Actions

- **Validate:** kör projektvalidering och integritetskontroll vid push och pull request.
- **Build Preview:** manuellt EPUB-/PDF-bygge med nedladdningsbara artefakter.
- **Release:** vid `v*`-tagg byggs EPUB/PDF och kontrollsummor och publiceras i GitHub Release.

## Publiceringsstatus

Manus och provexport finns. Slutlig juridisk sakkunniggranskning och fullständig kontroll av externa källor återstår före offentlig publicering. Arbetsdokument i `docs/` ingår inte i bokens läsflöde.
