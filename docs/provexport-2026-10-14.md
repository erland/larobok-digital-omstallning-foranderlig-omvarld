# Provexport – 14 oktober 2026

## Resultat
- EPUB byggd med Pandoc 3.1.11.1. Arkivet öppnas och har EPUB-navigation; ingen extra läsbar innehållsförteckningssida har lagts in.
- PDF byggd med XeLaTeX i A5, 10 pt, 18 mm marginal, bokklass med separata kapitelstarter, kort innehållsförteckning (nivå 1).
- PDF: 157 sidor inklusive förtexter, kapitel och källavsnitt. Tidigare standardprov i Letter hade 108 sidor och alltför detaljerad innehållsförteckning.
- Test av EPUB ZIP-integritet lyckades. Kontroll av textrubrik och kapitelordning genomförd.
- Stickprov på sidorna visade läsbar text och god svensk teckenåtergivning. Fullständig manuell sid-för-sidagranskning och tester i e-boksläsare återstår.
- Boken saknar ännu omslagsbild enligt författarens beslut.

## Begränsningar och återstående publiceringskontroller
1. EPUB behöver sluttestas i faktiska läsappar; kontrollera navigationsposter och sidbrytningar.
2. PDF har inte blivit granskad visuellt på samtliga sidor. Kontrollera tabeller, ensamma rubriker och sidbrytningar vid slutlig sättning.
3. Individuell kontroll av samtliga källadresser samt juridisk sakkunniggranskning återstår.
4. Slutlig kontroll av förkortningar, referenser och skillnaden mellan underrättelse, misstanke, riskurval och bevisning kvarstår.
5. Sidantal är ett typografiskt utfall, inget innehållsmål. Ingen utfyllnad ska införas.

## Tekniska ändringar
- `scripts/export-book.py`: läser kapitellista och TOC-djup från `book.yaml`, exporterar A5/PDF och EPUB utan att duplicera manuset.
- `book.yaml`: PDF-innehållsförteckning justerad från nivå 3 till nivå 1.
- `exports/`: tillfälliga provfiler ingår i projektet för granskning.
