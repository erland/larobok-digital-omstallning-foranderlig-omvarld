# Digital omställning i en föränderlig omvärld

Bokprojekt för en fördjupad faktabok. **Version 0.1.0 avser planering, inte en färdig bok.**

- Författare: Erland Lindmark
- Inriktning: myndighetsneutral analys för kontroll, uppbörd, tillsyn, gränsöverskridande flöden och brottsbekämpning
- Källbaslinje: eSam, *Radarbilden – eSams halvårsrapport 2026*, februari 2026, ES2026-03
- Status: Inledningen är utkast; kapitel 1–16 har endast dispositionsmarkörer och får inte presenteras som färdigskrivna.

## Arbetsflöde
1. Läs `docs/bokspecifikation.md`, `docs/kapitelplan.md` och `docs/kallpolicy.md`.
2. Utveckla ett kapitel i taget; verifiera påståenden mot primärkällor.
3. Kör `python3 scripts/validate_project.py .` och `python3 scripts/project_integrity.py verify .` före ändringar.
4. Efter ändringar kör `python3 scripts/project_integrity.py revise .` och verifiera.
5. Skapa EPUB/PDF först när boktexten är klar.

Ingen intern illustration eller omslagsbild ingår.
