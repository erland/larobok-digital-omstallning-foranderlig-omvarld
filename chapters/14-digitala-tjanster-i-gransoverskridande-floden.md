# 14. Digitala tjänster i gränsöverskridande flöden

En företagare lämnar uppgifter om en internationell leverans. Uppgifterna behöver bedömas för avgifter, säkerhet, tillstånd och kontroll, ibland av olika aktörer i flera länder. För den som lämnar uppgifterna är det i grunden en och samma händelse. För myndigheterna kan den samtidigt vara flera ärenden i separata informationssystem. Skillnaden mellan dessa perspektiv förklarar varför digitalisering av gränsöverskridande tjänster är mer än att erbjuda ett nytt formulär på webben.

En modern digital tjänst behöver förena användarens behov av enkelhet och förutsägbarhet med myndighetens krav på korrekta uppgifter, laglig informationsbehandling, kontroll och spårbarhet. Kapitlet behandlar hur detta kan göras i en myndighet med omfattande kontakter med företag, ombud, transportörer och internationella samarbetspartner. Exemplen är fiktiva; de beskriver inte en bestämd myndighets organisation eller befogenheter.

## Tjänsten börjar utanför myndighetens organisationsgräns

Traditionellt har en e-tjänst ofta utformats som ett digitalt gränssnitt till en redan befintlig intern process. Den som lämnar uppgifter får då anpassa sig till ansvarsfördelningen mellan olika enheter och system. En internationell leveranskedja följer däremot en annan logik: en uppgift uppstår hos en aktör, används av flera andra, kompletteras vid en händelse och kan behöva verifieras i ett annat land.

Utgångspunkten bör därför vara den faktiska händelsen och aktörens uppgift, inte vilket system som råkar äga formuläret. Det innebär inte att en myndighet kan ta över en annan myndighets ansvar eller behandla information fritt. Det betyder att tjänstedesignen ska synliggöra och hantera ansvarsfördelningen på ett begripligt sätt, medan de rättsliga gränserna fortfarande respekteras.

En väl utformad tjänst kan svara på fyra frågor: vad behöver aktören lämna, varför behövs det, vad händer med uppgiften och hur kan aktören följa eller korrigera ärendet? När flera parter deltar behöver tjänsten också visa vem som företräder vem och vad ett visst meddelande eller beslut avser.

## Tre europeiska utvecklingsspår som måste hållas isär

Europeisk digitalisering utvecklas genom flera delvis överlappande regelverk och infrastrukturer. Deras namn liknar ibland varandra, men funktion och tillämpningsområde är olika.

**Single Digital Gateway**, enligt förordning (EU) 2018/1724, syftar till att ge medborgare och företag tillgång till information, förfaranden och stöd på den inre marknaden. Den innehåller också ett tekniskt system för gränsöverskridande bevisutbyte enligt den så kallade *once-only*-principen för de förfaranden som omfattas. Det är inte en generell rätt för alla myndigheter att hämta samtliga uppgifter utan ny prövning. Utbytet är knutet till tillämpliga förfaranden, rättsliga villkor och i relevanta fall användarens uttryckliga begäran. [K007][K040]

**EU Single Window Environment for Customs**, enligt förordning (EU) 2022/2399, rör elektroniskt informationsutbyte mellan tullsystem och vissa unionssystem som hanterar icke-tullrelaterade formaliteter. Det bygger på särskilda informations- och samverkansmekanismer. Olika funktioner tillämpas enligt olika tidpunkter; det är därför fel att beskriva hela miljön som fullt införd i alla delar från ett enda datum. [K019]

**Union Customs Code och dess elektroniska system** utgör ytterligare ett spår. Kommissionens arbetsprogram enligt genomförandebeslut (EU) 2023/2879 beskriver införandet av elektroniska tullsystem. Kommissionens lägesbeskrivning 2026 visar att huvuddelen av systemen har införts, men också att vissa nationella luckor och projektberoenden återstår. Det är en annan fråga än om en viss myndighet har ett helt sammanhållet användarflöde eller en enhetlig intern informationsmodell. [K041][K042]

Det finns en gemensam lärdom: en tjänst kan vara digitaliserad i en rättslig eller teknisk mening utan att hela användarresan är sammanhängande. Myndigheten bör därför följa både europeiska driftsättningar och den konkreta effekt de ger för den egna verksamheten.

## Uppgiftslämning en gång – användning med tydliga villkor

Principen att en uppgift inte ska behöva lämnas flera gånger kan minska administration och fel. Men det är skillnad mellan att återanvända uppgifter och att återanvända en tidigare rättslig bedömning. En företagsadress kan ofta vara relevant för flera processer, medan ett godkänt intyg, ett tillstånd eller en riskklassificering kan vara kopplad till en viss tidpunkt, ett särskilt ändamål och särskilda villkor.

För att återanvändning ska vara tillförlitlig krävs åtminstone gemensamma begrepp, känt informationsursprung, kontrollerad aktualitet och rättsligt stöd. Det måste också gå att hantera motsägande uppgifter. Om ett ombud lämnar en uppdaterad adress samtidigt som ett nationellt register visar en äldre uppgift behöver tjänsten kunna skilja mellan ny information, auktoritativ information och ännu inte verifierade påståenden.

En viktig designprincip är att inte belasta användaren med organisatoriska dubbelregistreringar, men heller inte dölja att samma uppgift kan ha olika rättslig betydelse. För vissa fält kan återanvändning ske automatiskt inom givna villkor; för andra krävs en ny bekräftelse, en komplettering eller en separat prövning.

## Företag, ombud och behörighet

Företag företräds ofta av ombud och systemleverantörer. Tjänsten måste därför veta **vem som agerar, för vems räkning och inom vilket uppdrag**. Identitets- och behörighetsarkitekturen beskrivs i kapitel 8. Här är den särskilda tjänstedesignfrågan att användaren tydligt ska se vilket företag ett formulär eller API-anrop gäller, och att både automatiska och manuella ärendesteg ska respektera ändrad eller återkallad behörighet.

## Ärendets livscykel som sammanhängande tjänst

Ett digitalt ärende kan beskrivas med tillstånd som *utkast*, *inlämnat*, *mottaget*, *under validering*, *komplettering begärd*, *under prövning* och *avslutat*. Detta är ett exempel på designbegrepp och ska inte tolkas som rättsligt fastställda statusvärden.

För aktören är varje tillstånd en fråga om förväntan och ansvar. Har myndigheten tagit emot informationen? Behöver något göras? Är ett meddelande endast en teknisk kvittens eller ett formellt beslut? Vilket datum gäller för en frist? Tjänsten måste tydligt skilja mellan teknisk mottagning, registrering, materiell prövning och rättsligt bindande ställningstaganden.

Även när hela processen är automatiserad i normala fall måste ett ärende kunna lämnas över till manuell handläggning. Automatiseringen bör därför vila på ett informations- och händelseflöde som bevarar varje ändring och den som initierat den. Det gör det möjligt att förklara en korrigering, återuppta en prövning eller granska vad som faktiskt låg till grund för en åtgärd.

## Tillstånd, avgifter och betalningar

Gränsöverskridande aktiviteter kan bero på tillstånd, licenser, certifikat eller uppgiftsskyldigheter. I en sammanhållen digital tjänst bör användaren kunna se vad som krävs, vilka uppgifter som redan finns och vilken aktör som fattar beslut. Samtidigt måste tjänsten förhindra att ett elektroniskt dokument misstas för en fortfarande giltig rättighet. Ett tillstånd kan vara återkallat, begränsat eller beroende av ett villkor som inte uppfyllts.

För avgifter, tullar eller andra betalningsskyldigheter är transparensen lika viktig. Tjänsten behöver skilja mellan preliminär beräkning, fastställt belopp, betalning och återbetalning. Olika begrepp får inte slås samman till ett enda saldo utan dokumenterade regler. Den som agerar för flera företag ska dessutom kunna följa vilket betalningsansvar och vilken transaktion som hör till respektive ärende.

Det kan finnas stor nytta i att samordna beräkning, avisering och betalningsinformation, men rättssäkerhet kräver att beslutsgrunder, rättelser och rättsmedel bevaras. Att något visas i samma användargränssnitt betyder inte att alla delar av ärendet styrs av samma regelverk.

## API:er och digitala ekosystem

Professionella aktörer integrerar ofta direkt från sina verksamhetssystem. Därför behöver tjänsten erbjuda väl dokumenterade och versionerade API:er, testmiljöer och förutsägbara övergångsperioder. Kapitel 7 beskriver informationskontrakt och gränsöverskridande utbyte mer utförligt. Här ligger tyngdpunkten på **tjänstelöftet gentemot användaren**: samma ärendestatus, validering och möjligheter till rättelse ska gälla oavsett om ett företag använder webbgränssnitt, ombud eller API. Vid avbrott behöver också kommunikationen till externa aktörer fungera.

## Fiktivt verksamhetsexempel: ett ärende genom tre länder

Ett företag planerar en varuleverans som berör tre medlemsstater. Företaget anlitar ett ombud som lämnar uppgifter via sitt eget logistiksystem. Vissa uppgifter behövs för en deklaration, andra för att kontrollera att ett elektroniskt intyg är giltigt. Under transporten ändras en uppgift om mottagaren.

I ett fragmenterat arbetssätt behöver ombudet lämna samma grunduppgifter i flera portaler. Vid en avvikelse skickas meddelanden mellan olika enheter, och företaget får svårt att förstå om leveransen är försenad på grund av en teknisk felaktighet, ett saknat intyg eller en beslutad kontroll.

I ett mer sammanhållet arbetssätt kan tjänsten återanvända redan tillgängliga uppgifter där detta är rättsligt tillåtet. Den visar varifrån uppgifterna kommer, vilka intyg som ska verifieras och vilka delar av prövningen som utförs av olika myndigheter. När mottagaruppgiften ändras registreras både den nya uppgiften och dess ursprung. Ett kontrollbehov bedöms separat från den tekniska avvikelsen.

Vid ett avbrott i den internationella intygstjänsten blir det särskilt tydligt varför kontinuitet behövs: ett lyckat meddelandeutbyte kan inte antas bara för att ett anrop har skickats. Det måste finnas ett känt läge för osäker verifiering, en rättsligt möjlig reservhantering och efterföljande avstämning. Därmed knyter scenariot samman kapitlets tjänsteperspektiv med kapitel 11 om beredskap och kapitel 12 om kontrollkedjor.

Detta är ett konstruerat exempel, inte en beskrivning av gällande operativa rutiner i någon viss myndighet.

## Målarkitektur: från portal till digital tjänsteförmåga

Den långsiktiga arkitekturen bör särskilja användargränssnitt, ärendeprocess, informationsobjekt, behörighetskontroll och externa anslutningar. En sådan uppdelning gör det möjligt att erbjuda flera kanaler – till exempel webb, API och assisterad service – utan att skapa olika rättsliga processer i varje kanal.

I ett tänkbart målläge finns ett gemensamt tjänstekontrakt för inlämning och kvittens, en förmåga att hantera behörigheter och representation, ett ärendeflöde med spårbara statusändringar samt informationsutbyte genom kontrollerade gränssnitt. Ett separat besluts- och kontrollstöd får bara använda uppgifter enligt fastställda regler. En tydlig informationsmodell gör det möjligt att återanvända grundläggande data utan att osynliggöra källornas skillnader.

Arkitekturen behöver också hantera funktionella och organisatoriska gränser. En myndighet kan ansvara för att tillhandahålla en tjänst utan att äga varje bakomliggande register. En leverantör kan drifta en komponent utan att få bestämma informationsändamål. En internationell samverkanspart kan lämna en uppgift utan att vara ansvarig för mottagarens senare beslut. Dessa ansvar måste vara beskrivna i både avtal, processer och tekniska gränssnitt.

## Så kan verksamhetsnyttan följas upp

Mätning bör inte begränsas till antalet inloggningar eller digitala formulär. En myndighet behöver följa om den sammanhängande tjänsten faktiskt förbättrar både service och kontroll.

| Perspektiv | Möjligt mått | Tolkningsrisk |
|---|---|---|
| Företag och ombud | Antal kompletteringar per ärende | Färre kompletteringar kan också dölja svagare granskning |
| Handläggning | Tid från komplett underlag till åtgärd | Säger lite om kvalitet eller olika ärendetyper |
| Informationskvalitet | Andel uppgifter med känt ursprung och giltighet | Kräver gemensamma definitioner och kvalitetsprov |
| Interoperabilitet | Lyckade verifieringar och återhämtning vid fel | Ett tekniskt lyckat anrop behöver inte vara rättsligt användbar information |
| Rättssäkerhet | Spårbarhet, rättelser och motiverade beslut | Få registrerade fel betyder inte säkert få faktiska fel |
| Motståndskraft | Tid till fungerande reservhantering | Behöver prövas i övningar, inte bara i dokumentation |

Måtten bör kompletteras med dialog med företag och ombud, stickprov av ärenden och kvalitetsgranskning. En ny tjänst kan minska den administrativa bördan för en aktör och samtidigt skapa mer arbete för en annan. Nyttan måste bedömas för hela kedjan.

## Sammanfattning

Framtidens gränsöverskridande myndighetstjänster formas i mötet mellan användarbehov, regelverk och gemensamma informationsflöden. EU:s olika digitaliseringsinitiativ kan skapa viktiga förutsättningar, men gör inte automatiskt verksamhetsprocesserna sammanhängande. Myndigheten behöver själv knyta samman uppgiftslämning, behörighet, informationskvalitet, ärendehantering, kontroll och beslut.

Det avgörande steget är övergången från digitala formulär till **sammanhållna, spårbara tjänsteförmågor**. Nästa kapitel fördjupar hur myndighetens styrning, arkitektur och förändringsarbete behöver organiseras för att möjliggöra den utvecklingen.

**Tidsavgränsning:** Vissa bestämmelser i förordning (EU) 2022/2399 börjar tillämpas först den 13 december 2031. Den stegvisa tillämpningen bör skiljas från att rättsakten redan är i kraft. [K019]
