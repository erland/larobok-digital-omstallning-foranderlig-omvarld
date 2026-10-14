# 4. Artificiell intelligens i myndighetsverksamhet

En internationell försändelse har avvikande uppgifter i flera dokument. Samtidigt uppmärksammas ett nytt handelsmönster i ett annat informationsflöde. Det är möjligt för en erfaren handläggare att upptäcka sambandet, men sannolikheten minskar när tusentals ärenden passerar verksamheten varje dag. Artificiell intelligens kan här hjälpa till att sortera, sammanställa och uppmärksamma avvikelser. Men den kan inte på egen hand avgöra vilka uppgifter myndigheten får behandla, vilken rättslig betydelse de har eller hur kontrollbefogenheter får användas.

Detta kapitel handlar om AI som en del av myndighetens förmåga att utföra sitt uppdrag – inte som en fristående teknisk produkt. Utgångspunkten är eSams radarbild från februari 2026, kompletterad med senare verifierade rättsliga och organisatoriska förhållanden fram till oktober 2026. Där annat inte anges är resonemangen bokens egna analyser.

## Från teknikexperiment till verksamhetsförmåga

AI används som ett samlingsbegrepp för tekniker med olika egenskaper. Klassiska statistiska metoder och maskininlärning kan exempelvis förutsäga ett utfall utifrån träningsdata. Språkmodeller kan bearbeta och generera text. Bildanalys kan identifiera mönster i fotografier, skannade dokument och annan bildinformation. Vissa system kombinerar flera tekniker.

Det är avgörande att skilja på tre typer av uppgifter:

1. **Beskriva och organisera information:** klassificera inkomna handlingar, extrahera fält, identifiera språk, sammanfatta dokument.
2. **Föreslå och prioritera:** indikera sannolikheten för en avvikelse, rangordna granskningsbehov eller upptäcka avvikande transaktionsmönster.
3. **Påverka beslut och ingripanden:** stödja bedömningar där resultatet kan få rättsliga eller andra påtagliga konsekvenser för enskilda eller företag.

Även en sammanfattning kan påverka senare bedömningar. Kapitel 5 behandlar därför rättssäkerhet och ansvar utifrån systemets faktiska användning.

eSams radarbild beskriver ett ökande fokus på AI och nationell gemensam infrastruktur för offentlig förvaltning. Den redovisar bland annat planerna på en förvaltningsgemensam AI-verkstad. För en enskild myndighet innebär detta möjligheter att återanvända komponenter och metoder, men inte att ansvaret för information, rättslig grund och verksamhetsrisk flyttas till en gemensam plattform. [K005]

## Fem användningsområden med konkret verksamhetsnytta

### 1. Dokumentintag och informationskvalitet

En kontroll- eller uppbördsmyndighet tar emot stora mängder strukturerade uppgifter och ostrukturerade bilagor: intyg, fakturor, transporthandlingar, fullmakter och korrespondens. AI kan användas för att känna igen dokumenttyp, föreslå metadata, jämföra nyckelfält och markera motstridiga uppgifter.

Nyttan ligger ofta i att minska manuellt förarbete, inte i att ersätta en juridiskt kvalificerad bedömning. Ett OCR- eller språkmodellfel kan skapa en felaktig uppgift som senare sprids till ärendesystem, uppföljning och samverkansparter. Därför behövs dokumentets original, synlig osäkerhet, spårbarhet mellan extraherat värde och källa samt kontroll av särskilt betydelsefulla fält.

### 2. Riskanalys och urval för kontroll

Analysstöd kan identifiera ovanliga kombinationer av deklarerade varor, geografiska rutter, transaktionsmönster och tidigare kontroller. Det kan även kombinera regelbaserade indikatorer med statistiskt lärda samband. En modell kan prioritera ärenden för fortsatt granskning, men får inte förväxlas med ett konstaterande av fel eller brott.

**Den strategiska frågan är vad modellen optimerar.** Ett system som maximerar antalet träffar i tidigare kontrollutfall kan reproducera historiska kontrollmönster och missa sådant som myndigheten sällan har undersökt. Det behövs därför uppföljning av både träffsäkerhet och täckning, analys av felaktiga urval, kvalitetskontroll av träningsdata och en förmåga att upptäcka när omvärlden förändras.

För individinriktade riskmodeller krävs en särskild rättslig prövning. De tillåtna användningarna, förbuden och kontrollkraven behandlas i kapitel 5.

### 3. Ärendehandläggning och kunskapsstöd

Ett avgränsat AI-stöd kan söka i interna rättsliga vägledningar, beskriva skillnader mellan versioner och föreslå frågor som handläggaren bör kontrollera. Med källanknuten sökning kan relevanta dokumentavsnitt visas tillsammans med svaret.

En sådan lösning bör inte presentera modellgenererad text som säker rättskälla. Svaren behöver länkas till auktoritativa, versionshanterade dokument. Saknas stöd i källmaterialet ska systemet kunna svara att informationen är otillräcklig. Det bör också vara lätt för en användare att rapportera ett fel och få det åtgärdat i källor, instruktioner eller modellkonfiguration.

### 4. Underrättelse- och analysarbete

AI kan bistå analytiker med att finna samband mellan stora mängder i sig lagligen tillgängliga uppgifter, exempelvis mönster över tid eller skillnader mellan uppgiftslämningar. Tekniken ändrar emellertid inte regler om sekretess, ändamålsbegränsning, åtkomst eller vad olika samverkansparter får dela.

En särskild risk är sammanblandning av osäker underrättelseinformation och verifierade sakuppgifter. Ett användbart analysstöd behöver därför kunna ange ursprung, tidpunkt, tillförlitlighet och vilken analys som är automatgenererad. AI får inte skapa skenbar säkerhet genom att formulera hypoteser i ett auktoritativt språk.

### 5. Intern produktivitet och utveckling

Textbearbetning, översättning, kodassistans, testfall och sammanfattningar kan ge nytta även utan att AI deltar i myndighetsutövning. Detta är ofta lämpliga tidiga användningsfall, förutsatt att informationsklassning, sekretess, personuppgifter, upphovsrätt, upphandlingsvillkor och loggning hanteras.

Det enklaste pilotprojektet är inte nödvändigtvis det bästa. Pilotvärdet måste också bedömas utifrån om arbetssättet går att införa säkert, drifta långsiktigt och sprida utan att skapa ogenomlysta informationskopior hos externa leverantörer.

## Verksamhetsexempel: från inkommande handling till prioriterad granskning

*Fiktivt scenario. Exemplet beskriver ett tänkbart arbetsflöde och inte en existerande myndighets tekniska lösning eller rättsliga behörighet.*

En verksamhet tar emot digitala anmälningar om gränsöverskridande varuflöden. Till varje anmälan kan flera dokument bifogas. Tidigare har en handläggare behövt öppna dokumenten, jämföra uppgifter och manuellt välja vilka ärenden som kräver en djupare granskning.

I ett nytt förfarande läser ett AI-stöd ut dokumenttyp och föreslår relevanta uppgiftsfält. En regelmotor granskar obligatoriska formatkrav. En separat analysmodell kan därefter föreslå att vissa ärenden bör prioriteras, exempelvis när uppgifter inte stämmer mellan källor. Handläggaren ser både förslaget, underlaget och de osäkerheter som systemet markerat.

Arbetsflödet får en tydlig ansvarsfördelning:

- **Automatiserad informationsberedning** skapar förslag, inte oåterkalleliga fakta.
- **Regelkontroller** kontrollerar objektivt definierade krav.
- **Analysstöd** pekar ut förhållanden som kan motivera mer granskning.
- **Behörig tjänsteman** bedömer om underlaget motiverar fortsatt granskning.
- **Uppföljningsfunktionen** granskar felutfall, avvikelser, dataskift och eventuella osakliga skillnader mellan grupper.

Det viktiga är inte antalet AI-komponenter utan att varje steg har en känd uppgift, avgränsning och ansvarig aktör. Om ett genererat värde visar sig vara fel ska det gå att se om felet uppstod vid dokumenttolkning, datamappning, riskberäkning eller mänsklig hantering.

### När scenariot misslyckas

Anta att en dokumenttolkningsmodell läser en viktangivelse fel. Felvärdet förs vidare till riskmodellen, som föreslår en kontroll. Handläggaren får ett trovärdigt riskresultat men saknar länk till originalhandlingens fält. Avvikelsen upptäcks först efter att kontrollresurser har använts.

Här har felet inte i första hand uppstått i själva riskmodellen. Det uppstod genom en **obruten kedja av tillit till ett osäkert mellanresultat**. Rätt åtgärd är därför inte bara att finjustera modellen, utan att införa fältnivåspårbarhet, rimlighetskontroller och tydliga gränser för vilka automatiskt extraherade värden som får påverka ett urval.

## Arkitektur: AI måste ingå i en styrd informationskedja

I en långsiktigt hållbar målarkitektur bör AI-komponenter kunna bytas utan att myndigheten förlorar förståelsen för information, beslut eller processer. Det kräver tydliga gränssnitt och ansvar.

**Informationslager.** Källsystemen ansvarar för definierade informationsobjekt och datakvalitet. Uppgifter som levereras till en modell behöver dokumenterade ursprung, versions- och åtkomstregler. En kopia till en AI-tjänst är fortfarande myndighetsinformation som kräver styrning.

**Modell- och tjänstelager.** Modeller, promptmallar, sökindex och andra konfigurationer versionshanteras. Det måste framgå vilken version som användes för en viss sammanställning eller rekommendation. Övervakning av kvalitet, säkerhet, kostnad och felutfall byggs in från början.

**Process- och beslutslager.** Resultat presenteras där den ansvariga funktionen arbetar. Det ska framgå om en uppgift är originaldata, en härledning, en regelträff eller en AI-genererad uppskattning. Beslutsstöd ska inte kunna skriva över sakuppgifter utan kontroll.

**Styrnings- och kontrollager.** Organisationen behöver ett aktuellt register över AI-användningsfall, ansvariga ägare, dokumenterad riskklassificering, förändringshistorik och godkända driftsmiljöer. Kontroller ska kunna följas upp av juridik, informationssäkerhet, verksamhet och intern revision.

**Kontinuitetslager.** Verksamheten måste veta vad som sker när modellen, den externa tjänsten eller nätförbindelsen inte fungerar. I vissa flöden räcker det med manuell reservrutin; i andra måste en enklare regelbaserad funktion kunna ta över utan att kontrolluppdraget äventyras.

## Säkerhet och beroenden

Språkmodeller kan påverkas av instruktioner som gömts i dokument eller andra datakällor. En sådan promptinjektion kan försöka få systemet att avslöja information eller lämna sin avsedda uppgift. AI-lösningar behöver därför skilja data från styrande instruktioner, begränsa verktygsbehörigheter och skydda mot att modellens svar får verkställa obehöriga åtgärder.

Beroenden till externa AI-tjänster behöver beskrivas redan vid införandet. Cybersäkerhet och leverantörsberoenden behandlas närmare i kapitel 9–10.

Det följer inte av dessa risker att extern AI alltid är olämplig. Slutsatsen är att driftsform, avtalskrav och tekniska skydd måste anpassas till varje användningsfalls informationsklass och rättsliga villkor.

## Från pilot till förvaltad tjänst

Ett vanligt misstag är att bedöma en AI-pilot efter hur övertygande dess demonstration är. En myndighet behöver i stället skilja mellan minst fyra mått:

| Dimension | Fråga | Exempel på uppföljning |
|---|---|---|
| Verksamhetsnytta | Blir uppdraget bättre utfört? | Kortare genomloppstid, högre kvalitet, färre omtag |
| Rättssäkerhet | Kan rekommendationer granskas och ifrågasättas? | Spårbara underlag, dokumenterade rättelser |
| Risk och säkerhet | Håller användningen inom fastställda gränser? | Avvikelser, läckageförsök, felaktiga resultat |
| Förvaltningsbarhet | Kan lösningen drivas och förändras långsiktigt? | Versionering, driftskostnad, reservrutiner |

Både jämförelsegruppen och definitionen av framgång måste vara tydliga. Om AI minskar handläggningstiden men samtidigt höjer andelen felaktiga kontrollurval har nyttan inte nödvändigtvis ökat. Om en modell framstår som träffsäker därför att den bara testas på historiska ärenden med tydliga utfall säger det begränsat om verklig användning.

Införande kräver dessutom förändrat arbete: utbildning, ansvarsfördelning, instruktioner, uppföljning och möjlighet att avbryta en lösning som inte längre uppfyller sina krav. En gemensam AI-verkstad eller ett centralt plattformsteam kan minska teknisk dubbelutveckling, men varje verksamhetsägare behöver ansvara för sitt syfte, sitt underlag och sina risker.

## Sammanfattning

AI:s största potentiella värde i en samhällsviktig kontrollmyndighet är att förbättra hur information blir användbar för verksamheten. Den största organisatoriska risken är att AI-resultat uppfattas som objektiva svar trots att de bygger på ofullständiga data, antaganden och osäkra samband.

Därför behöver en pilot prövas mot verksamhetens faktiska resultat och möjliga felutfall – inte mot hur övertygande modellen verkar i en demonstration. Nästa kapitel behandlar de rättsliga gränserna och den mänskliga kontrollen.
