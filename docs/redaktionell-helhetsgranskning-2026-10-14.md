# Redaktionell helhetsgranskning – manus 0.2.6

Datum: 2026-10-14. Granskningsstatus: strukturell och redaktionell genomgång, **inte** slutlig käll- eller fackgranskning.

## Övergripande slutsats

**Rekommendation: behåll kortare bok hellre än att fylla ut till 180–240 sidor.** Manus omfattar **35,831 ord i kapitel 1–16** och **36,137 ord inklusive inledningen**, mätt med ordgränser i Markdown. Sidantalet kan först fastställas genom sättning. Grovt kan detta motsvara cirka 110–150 textsidor beroende på typografi, notapparat och kapitelstarter; uppskattningen är inte en uppmätt PDF-sidlängd.

Manuset har en tydlig röd tråd: omvärld → data och AI → säkerhet och beredskap → operativ verksamhet → styrning och vägval. Det har samtidigt återkommande formuleringar och strukturer som riskerar att göra läsningen schematisk. **Redigera ned upprepningar först; fördjupa bara när läsaren får ny sakinformation, ett nytt perspektiv eller ett mer användbart konkret exempel.** Ingen siffra i ett tidigare sidmål ska användas för att motivera mer text.

## Faktisk omfattning

| Kapitel | Ord (ungefärligt) |
|---|---:|
| 00 | 306 |
| 01 | 2,850 |
| 02 | 2,562 |
| 03 | 2,571 |
| 04 | 2,278 |
| 05 | 2,095 |
| 06 | 2,281 |
| 07 | 2,203 |
| 08 | 2,151 |
| 09 | 2,008 |
| 10 | 2,032 |
| 11 | 2,214 |
| 12 | 1,986 |
| 13 | 2,152 |
| 14 | 2,212 |
| 15 | 2,118 |
| 16 | 2,118 |
| **Totalt** | **36,137** |

## Risker för repetition och redaktionella åtgärder

| Kapitelytor | Identifierad överlappning | Rekommenderad åtgärd |
|---|---|---|
| 1–3 och 15–16 | Omvärldssignaler, förmågeplanering, prioriteringar och framtida vägval återkommer | Låt kap. 1 beskriva omvärldsläget, kap. 2 uppdragets särskilda villkor, kap. 3 metod för omvärldsanalys, kap. 15 genomförandets arkitektur och kap. 16 syntesen. Korta generiska upprepningar. |
| 4–5 och 12–13 | AI-stöd, riskindikatorer, mänsklig bedömning och rättssäkerhet behandlas på flera ställen | Låt kap. 4 förklara AI-användningar, kap. 5 rättsliga kontrollmekanismer, kap. 12 kontrollkedjans arbetssätt och kap. 13 underrättelseinformationens särskilda regler. Använd korta hänvisningar hellre än omförklaringar. |
| 6–8 och 14 | Informationsmodeller, identifierare, datadelning, behörighet och API:er beskrivs upprepade gånger | Gör kap. 6 till semantisk/datarelaterad grund, kap. 7 till informationsutbyte, kap. 8 till identitet/representation och kap. 14 till tjänster ur användarens perspektiv. Ta bort omtag av samma definitioner. |
| 9–11 | Säkerhet, leverantörsrisk, molnberoende och kontinuitet glider in i varandra | Behåll kap. 9 om cyberrisk, kap. 10 om strategisk kontroll över leverantörsberoenden och kap. 11 om verksamhetens funktion under avbrott. |
| 1–16 | Återkommande avslutande rubriker om ”fem/sex strategiska vägval” följda av generiska sammanfattningar | Ersätt rutinmässig formel med en kort, ämnesspecifik slutsats. Samla bokövergripande vägval främst i kapitel 16. |
| Flera kapitel | Likartade fiktiva varu- och intygsflöden riskerar att kännas som samma fall | Behåll endast de case som visar en ny konflikt eller en ny mekanism; variera perspektiv mellan företag, operativ tjänsteman, jurist, arkitekt och ledning. |

## Principer för den följande bearbetningen

1. **Ingen obligatorisk längd.** Sidmålet 180–240 ersätts av "den längd som sakligt och redaktionellt motiveras".
2. **Varje stycke ska tillföra något.** Behåll fakta, förklaring, analys, empiri eller exempel; stryk allmänna formuleringar som upprepar något tidigare.
3. **En tydlig hemvist per begrepp.** Definitioner förklaras ordentligt första gången. Senare kapitel hänvisar vid behov tillbaka.
4. **Case med unik funktion.** Varje fiktivt exempel ska göra en särskild fråga begriplig och inte återberätta den generella kontrollkedjan.
5. **Strategiska slutsatser koncentreras.** Temaspecifika konsekvenser där de hör hemma, sammanhållen prioritering i kapitel 16.
6. **Respektera den neutrala målgruppen.** Undvik namnet på en utpekad svensk myndighet; behåll relevant kontroll-, uppbörds-, brottsbekämpnings- och internationellt flödesperspektiv.
7. **Faktagranskning före publicering.** Verifiera källor, tidsplaner, författningarnas status och påståenden om EU-reformer var för sig. En godkänd filintegritet är inte en faktakontroll.

## Prioriterad redigeringsordning

**Pass 1 – nedkortning och konsekvens (högst prioritet).** Rensa duplicerade generella resonemang, omtag av ordlistan och återkommande standardfraser i kapitelavslut. Ändra ett kapitel åt gången och bevara revisionskedjan.

**Pass 2 – konceptuell granskning.** Kontrollera att kapitelparens avgränsningar ovan verkligen håller. Lägg till bara enstaka övergångar där läsaren annars tappar sammanhang.

**Pass 3 – faktakontroll.** Gör en punkt-för-punkt kontroll av primärkällor. Märk tidsberoende rättsliga uppgifter med verifieringsdatum; skilj beslutad rätt från förslag och planering.

**Pass 4 – korrektur och export.** Kontrollera språk, rubriker, konsekvent terminologi, referenshantering, innehållsförteckning och hur PDF/EPUB faktiskt ser ut.

## Ändringsbeslut i denna revision

Denna revision ändrar **inga manuskapitel**. Bara bokspecifikation, projektstatus, revisionslogg, projektindex och denna redaktionella granskningsrapport ändras. Beslutet är att **inte förlänga för att nå det ursprungliga sidmålet**. Innehållet ska i kommande redigering göras mer koncentrerat utan att substantiella analyser går förlorade.
