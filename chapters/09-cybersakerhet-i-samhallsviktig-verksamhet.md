# 9. Cybersäkerhet i samhällsviktig verksamhet

Digitala förbindelser gör det möjligt att behandla stora informationsflöden nästan utan fördröjning. Samma förbindelser skapar beroenden: ett intrång i en leverantörs driftmiljö kan hindra en myndighet från att ta emot uppgifter, pröva tillstånd, följa upp avgifter eller förbereda kontroller. Cybersäkerhet handlar därför inte enbart om att skydda it-system. Den handlar om att upprätthålla myndighetens förmåga att fullgöra sitt uppdrag också under störda förhållanden.

För en statlig verksamhet med kontroll-, uppbörds- och brottsbekämpande uppdrag uppstår ett särskilt spänningsfält. Den behöver få information i tid och göra den tillgänglig för rätt aktörer, även över nationsgränser. Samtidigt kan felaktig, försenad eller röjd information leda till ekonomiska skador, osäkra kontrollbeslut eller förlorad operativ handlingsförmåga. Säkerhet får därför varken reduceras till en teknisk efterhandskontroll eller organiseras så att legitima verksamhetsflöden förlamas.

## Från informationssäkerhet till operativ motståndskraft

Tre klassiska skyddsmål används för att beskriva informationssäkerhet: **konfidentialitet**, **riktighet** och **tillgänglighet**. I en modern myndighet måste de prövas tillsammans. Ett system kan vara otillgängligt utan att information har stulits. Ett manipulerat intyg kan påverka en kontroll även om systemet i övrigt fungerar. En otillåten åtkomst till känsliga uppgifter kan röja planerade åtgärder utan att det märks i tjänstens svarstider.

Det räcker följaktligen inte att mäta hur snabbt en tjänst återstartar. Verksamheten behöver känna till vilka beslut, ärenden och kontrollmoment som kan genomföras under avbrottet, och hur man säkerställer riktigheten när data senare synkroniseras. En reservrutin som tillåter arbete men producerar oförenliga uppgifter kan skapa en ny kris när systemen återgår till normal drift.

Begreppet *cyberresiliens* används här för förmågan att förebygga, stå emot, upptäcka, hantera, återhämta sig från och lära av cyberrelaterade störningar. Det är både en teknisk och organisatorisk förmåga. Den omfattar även avtal, styrning, kompetens, övning och samverkan med andra myndigheter och företag.

## Ett förändrat regelverk i Sverige och EU

EU:s NIS2-direktiv, direktiv (EU) 2022/2555, ställer krav på cybersäkerhetsriskhantering och rapportering inom utpekade sektorer. Direktivet tar bland annat upp incidenthantering, kontinuitet, leveranskedjor, säkert utvecklingsarbete, sårbarhetshantering, åtkomstkontroll och utbildning. För betydande incidenter innehåller direktivet en stegvis rapporteringsordning med tidig varning inom 24 timmar, anmälan inom 72 timmar och slutrapport normalt inom en månad efter den senare anmälan. Detaljerna måste förstås i ljuset av vilka nationella skyldigheter som gäller för verksamhetsutövaren. [K025]

Den svenska cybersäkerhetslagen (2025:1506) och tillhörande förordning trädde i kraft den **15 januari 2026**. Lagen ersatte den tidigare svenska NIS-lagen och innebär skärpta krav för berörda offentliga och privata verksamhetsutövare. Regeringen framhåller särskilt systematisk riskhantering, skyddsåtgärder, incidentrapportering och ett tydligare ledningsansvar. [K026][K027]

En viktig gränsdragning är att **inte alla verksamheter eller system omfattas av exakt samma bestämmelser**. Man måste utreda om organisationen och dess tjänster ligger inom lagens tillämpningsområde, vilken roll den har och om annan särskild reglering gäller. Säkerhetsskyddslagstiftning, dataskydd, sekretessregler, beredskapsregler och sektorsspecifika krav kan aktualiseras parallellt. Denna bok ersätter inte den rättsliga prövningen för ett konkret användningsfall.

Regelverket bör betraktas som en lägstanivå för styrningen, inte som en fullständig arkitektur. Förmågan att fortsätta ett samhällsviktigt uppdrag vid ett sammansatt angrepp kan kräva ytterligare åtgärder än vad som framgår av en enskild checklista.

## Kartlägg de digitala beroendena

En myndighet kan ha god kontroll över de applikationer den äger men ändå vara starkt beroende av externa tjänster. Ett ärendeflöde kan exempelvis kräva e-legitimation, registeruppslag, en internationell meddelandetjänst, molnbaserad drift och en intern regelmotor. Om någon komponent fallerar kan hela kedjan stanna.

En användbar analys börjar med **verksamhetens förmågor**. Vilka uppgifter är mest tidskritiska? Vilka kontrollbeslut kan skjutas upp och vilka måste genomföras direkt? Vilka uppgifter måste finnas lokalt för att en tjänst ska kunna arbeta i begränsat läge? Härifrån kartläggs processer, informationsobjekt, system, identitetstjänster, nätförbindelser, leverantörer och personalberoenden.

Beroendekartan bör visa även sådant som normalt blir osynligt i en traditionell systemförteckning: gemensamma certifikat, namnuppslagning, tidsstämpling, logghantering, uppdateringskanaler och administrativa verktyg. Flera till synes separata system kan dela en sårbar komponent. Det är då den gemensamma komponenten, inte en enskild applikation, som blir den egentliga felpunkten.

## Hot, angreppsvägar och försvarsprinciper

En angripare kan försöka stjäla uppgifter, manipulera informationsflöden, låsa system genom utpressningsprogram eller utnyttja brister i en leverantörs mjukvara. Felkonfigurationer, mänskliga misstag och större infrastrukturstörningar kan ge liknande verksamhetskonsekvenser utan att en antagonist ligger bakom. Hotanalysen ska därför inte bara fråga *vem* som kan angripa utan också *hur processen kan sluta fungera*.

En arkitektur med flera skyddslager minskar beroendet av att en enda kontroll alltid lyckas. Hit hör segmentering, stark autentisering, minsta privilegium, säkra integrationsgränssnitt, kontrollerade uppdateringar och övervakning av avvikande händelser. Kryptering skyddar information under transport och vid lagring, men kompenserar inte för felaktigt utdelade åtkomsträttigheter.

För en myndighet som utbyter data internationellt är det särskilt viktigt att skilja på en tekniskt betrodd förbindelse och ett rättsligt tillåtet informationsutbyte. Att en extern aktör kan autentisera sig betyder inte att aktören har rätt till varje uppgift. Åtkomstbeslut behöver därför beakta organisation, roll, ändamål, ärendesammanhang och ibland särskilda befogenheter.

## Säkerhet i API:er och gränsöverskridande informationsflöden

Det moderna myndighetslandskapet bygger allt oftare på maskinella gränssnitt. API:er och meddelandetjänster förkortar handläggningstiden, men kan också sprida fel mycket snabbt. Om en felaktig uppgift godtas och vidarebefordras automatiskt kan flera verksamheter fatta beslut utifrån samma bristfälliga underlag.

Ett säkert informationsflöde behöver därför skydd i flera nivåer: identifikation av avsändare, auktorisation för viss informationsmängd, integritetskontroll, robust validering av innehåll, begränsning av anropsvolymer, loggning och tydlig hantering av fördröjningar eller dubletter. Det bör gå att avgöra om ett mottaget meddelande är nytt, återutsänt eller ändrat efter avsändandet.

**Informationsriktighet är också en kontrollfråga.** Ett misstänkt dokument eller en avvikande deklarationsuppgift får inte automatiskt behandlas som en systemincident. Omvänt måste ett intrång som manipulerar underlaget kunna upptäckas även när varje enskilt meddelande ser syntaktiskt korrekt ut. Tekniska valideringar behöver kompletteras med kontroller av rimlighet, proveniens och verksamhetslogik.

## Leverantörskedjan: ansvar kan inte outsourcas

En extern driftleverantör kan ha bättre resurser och specialistkompetens än en enskild myndighet. Men myndighetens beroende blir samtidigt en risk som måste hanteras. Om en tjänst ändrar underleverantörer, lagringsplats eller åtkomstmodell kan informationsklassning och avtalsförutsättningar påverkas.

Leverantörsstyrning bör därför omfatta insyn i kritiska underleverantörer, krav på incidentkommunikation, tester av återläsning och kontinuitet, hantering av sårbarheter, säker utveckling och villkor för avveckling. Det bör vara möjligt att exportera data och konfigurationer utan att en kris tvingar fram osäkra, improviserade lösningar.

En så kallad *exitplan* behöver vara mer än en paragraf i ett avtal. Den måste prövas mot faktiskt genomförande: vem har kompetens att flytta tjänsten, vilka dataformat används, vilka nycklar och identiteter behöver bytas och hur lång tid kan verksamheten arbeta utan leverantören? Samma frågor gäller molntjänster, AI-tjänster och centrala plattformar som andra myndigheter tillhandahåller.

## Fiktivt scenario: när en extern integration komprometteras

En statlig kontrollmyndighet använder ett digitalt informationsutbyte för att verifiera intyg som hör till inkommande varuflöden. En morgon upptäcker driftövervakningen att tjänstens svarsmönster har förändrats. Vissa intyg besvaras ovanligt snabbt, samtidigt som ett mindre antal svar innehåller uppgifter som inte överensstämmer med tidigare versioner.

Verksamheten kan inte omedelbart avgöra om det handlar om ett tekniskt fel, en bristande synkronisering eller ett angrepp mot en extern leverantör. Den första frestelsen är att koppla bort tjänsten helt. Men då stoppas också stora mängder legitima ärenden.

En i förväg beslutad reservprocess ger ett bättre handlingsutrymme. Nya automatiska godkännanden från den misstänkta källan pausas. Berörda svar märks med osäkerhetsstatus. En begränsad grupp behöriga handläggare kan begära manuell verifiering via en separat kontaktväg. Ärenden där underlaget inte kan verifieras hanteras efter dokumenterade prioriteringar och befintliga rättsliga befogenheter.

Säkerhetsfunktionen säkrar loggar och identifierar potentiellt påverkade informationsobjekt. Juridik och verksamhet bedömer vilka beslut som kan behöva omprövas och vilka externa parter som behöver kontaktas. Incidentansvariga utreder separat om rapporteringskriterierna enligt tillämpliga regler är uppfyllda. Det är inte incidentens tekniska etikett utan dess faktiska och möjliga påverkan som är avgörande i denna bedömning.

När tjänsten återställs måste myndigheten kunna jämföra inkomna uppgifter med verifierade källor och identifiera vilka ärenden som faktiskt påverkats. Om historiken saknas kan verksamheten tvingas ompröva långt fler ärenden än nödvändigt.

*Scenariot är konstruerat för boken och avser inte en identifierbar myndighet, leverantör eller faktisk incident.*

### Lärdomar av scenariot

Fallet visar varför incidenthantering måste vara verksamhetsförankrad. En teknisk isoleringsåtgärd kan vara nödvändig men samtidigt skapa operativa risker. En försvarbar hantering kräver att verksamhet, it, säkerhet, juridik, kommunikation och berörda externa parter kan fatta samordnade beslut under osäkerhet. Det visar också betydelsen av proveniens: när informationsobjekt är spårbara kan återställningen rikta sig mot berörda ärenden i stället för att hela verksamheten behöver börja om.

## Incidenthantering och rapportering

En incidentprocess bör ge snabba svar på sex frågor: vad har hänt, vad är påverkat, vad kan fortfarande göras, hur begränsas skadan, vem måste informeras och hur återställs tjänsten säkert? De tekniska detaljerna är bara en del av bedömningen.

NIS2 innehåller som nämnts tydliga tidsramar för rapportering av betydande incidenter. Organisationen måste på förhand klarlägga vilka svenska bestämmelser och föreskrifter som är tillämpliga, vem som beslutar om rapportering och hur tidsfrister ska bevakas även på kvällar, helger och under längre störningar. Rapporteringsskyldighet, polisanmälan, personuppgiftsincident och intern avvikelsehantering är skilda processer som ibland kan behöva genomföras parallellt.

Förberedda kontaktvägar och mallar minskar risken att viktig information tappas bort. Men en incidentplan är inte färdig förrän den har övats med samma beroenden och aktörer som finns i den verkliga verksamheten.

## Ledningens ansvar och styrning

Cybersäkerhet behöver ägas på ledningsnivå eftersom skydd, tillgänglighet och kostnader ofta kräver avvägningar mellan flera verksamhetsområden. Ledningen bör känna till de mest kritiska förmågorna, koncentrerade leverantörsberoenden och vilka risker myndigheten accepterar under en begränsad tid.

En samlad lägesbild kan beskriva fyra dimensioner: verksamhetskritiska beroenden, identifierade risker, genomförda skyddsåtgärder och förmåga att återhämta sig. För att undvika missvisande mått bör rapporteringen inte enbart ange antal sårbarheter eller incidenter. Mängden registrerade incidenter kan exempelvis öka när detektionen förbättras.

| Perspektiv | Ledningsfråga | Möjlig indikator |
|---|---|---|
| Verksamhet | Kan kritiska uppdrag utföras vid störning? | Testad reservförmåga per process |
| Information | Kan uppgifternas riktighet kontrolleras? | Andel kritiska flöden med spårbar proveniens |
| Teknik | Finns koncentrerade felpunkter? | Kritiska beroenden utan prövad reservväg |
| Leverantörer | Kan tjänsten återtas eller ersättas? | Genomförda återställnings- och exitövningar |
| Organisation | Kan incidentbeslut fattas i tid? | Övad jour-, besluts- och rapporteringskedja |

## Avgränsning mot de följande kapitlen

Detta kapitel har behandlat hur myndigheten förebygger, upptäcker och hanterar cyberincidenter. Frågan om **handlingsfrihet gentemot teknikleverantörer** utvecklas i kapitel 10, medan **förmågan att genomföra uppdraget under långvariga störningar och återgången därefter** behandlas i kapitel 11. Den samlade strategiska prioriteringen återkommer i kapitel 16.

## Sammanfattning

Cybersäkerhet är en förutsättning för att en samhällsviktig myndighet ska kunna utföra sitt uppdrag pålitligt. NIS2 och den svenska cybersäkerhetslagen (2025:1506), som trädde i kraft den 15 januari 2026, stärker kraven, men det praktiska arbetet måste utgå från verksamhetens beroenden och konsekvenser. Skydd av informationsflöden, verifiering av uppgiftsriktighet och övad incidenthantering är därför centrala delar av säkerhetsarbetet.

Cybersäkerhet handlar om att skydda verksamhetens digitala förmågor. Nära sammanhängande är frågan om digital suveränitet: vem som ytterst kontrollerar teknikens drift, vidareutveckling och tillgänglighet. Det perspektivet fördjupas i nästa kapitel.
