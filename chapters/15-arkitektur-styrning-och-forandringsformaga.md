# 15. Arkitektur, styrning och förändringsförmåga

En myndighet kan ha en välutvecklad digital strategi och samtidigt vara bunden av fragmenterade informationsmodeller, åldrande system och arbetssätt som är svåra att förändra. En ny skyldighet att utbyta uppgifter över nationsgränser kan beröra en självservicetjänst, ett ärendesystem, en riskmotor, ett behörighetsregister och ett operativt kontrollstöd. Om varje berörd enhet löser sin del för sig kan resultatet bli ett tekniskt fungerande men organisatoriskt svårstyrt lapptäcke.

Det är här arkitektur, styrning och förändringsförmåga möts. Arkitektur handlar inte bara om hur system är sammansatta. Den beskriver sambanden mellan myndighetens uppdrag, de förmågor som krävs, den information som används och de lösningar som ska hålla över tid. Styrningen avgör vad som prioriteras och vem som får fatta beslut. Förändringsförmågan avgör om ett beslutat vägval faktiskt blir verklighet.

I eSams radarbild från februari 2026 framträder AI, säkerhet och beredskap, digital identitet samt informationsutbyte som områden som utvecklas samtidigt. [K005] Tillsammans skapar de ett förändringstryck som inte ryms i en traditionell projektplan för enskilda it-system. Detta kapitel utvecklar ett sätt att hantera helheten för en samhällsviktig myndighet som både underlättar legitima flöden och har kontroll- och ingripandeuppgifter.

## Målarkitektur börjar i verksamhetsuppdraget

En målarkitektur beskriver ett eftersträvat framtida tillstånd och de principer som ska styra vägen dit. Den behöver inte vara en detaljerad ritning över varje framtida komponent. Tvärtom kan en alltför detaljerad och långsiktigt låst arkitektur bli oanvändbar när reglering, teknik eller omvärld förändras.

En användbar målarkitektur ger svar på fem grundfrågor: Vilka verksamhetsresultat ska uppnås? Vilka förmågor måste utvecklas? Vilken information ska kunna delas och förstås? Vilka rättsliga och säkerhetsmässiga krav begränsar lösningarna? Vilka tekniska och organisatoriska principer ska följas?

För en myndighet med gränsöverskridande flöden kan målbilden exempelvis vara att samma verifierade sakuppgift ska kunna användas i rätt sammanhang av en digital tjänst, en handläggare och en operativ kontrollfunktion. Det betyder inte att all information ska kopieras till en central databas. I många situationer är det lämpligare att bevara informationsansvar hos källan och göra kvalitetssäkrade uppgifter tillgängliga genom tydliga kontrakt och lagligt grundade åtkomster.

En målarkitektur måste också beskriva *icke-mål*: vilka data som inte ska återanvändas, vilka bedömningar som inte får automatiseras och vilka tekniska beroenden som inte är acceptabla i kritiska flöden. Utan avgränsningar blir arkitekturen lätt en önskelista snarare än ett styrinstrument.

## Förmågebaserad planering ger ett gemensamt språk

Organisationens enheter, projekt och system förändras över tid. Verksamhetsförmågorna är ofta mer stabila: att identifiera en aktör, ta emot uppgifter, bedöma risk, fatta beslut, genomföra en kontroll, dokumentera resultat och dela information med behörig part. En förmågekarta beskriver *vad* verksamheten behöver kunna göra, inte exakt *vem* som gör det eller i vilket system.

En förmåga kan bedömas med utgångspunkt i nuläge, strategisk betydelse och utvecklingsbehov. Om exempelvis förmågan att verifiera elektroniska intyg är starkt beroende av en viss integration, bör det synas som ett arkitektur- och kontinuitetsproblem även om den nuvarande tjänsten normalt fungerar väl.

Förmågekartan kan användas i portföljstyrningen: investeringar kopplas till förbättrade förmågor snarare än enbart leverans av funktioner. Därmed kan flera initiativ som påverkar samma förmåga upptäckas, samordnas eller avvecklas. Den kan också visa var en förändring i europeisk lagstiftning medför nya behov av kompetens, rättslig analys och samverkan utanför myndigheten.

En viktig begränsning är att kartan inte får behandlas som en objektiv sanning. Förmågornas gränser och mognadsbedömningar är analytiska val. De ska därför prövas med personer från både ledning och operativ verksamhet.

## Från omvärldssignal till styrbar förändring

Kapitel 3 beskrev hur omvärldsbevakning kan bli en strategisk förmåga. I praktisk portföljstyrning behöver den översättningen ske i flera steg:

1. **Identifiera signalen.** Beskriv förändringen, dess källa, status och sannolika tidslinje. Skilj beslutade krav från förslag och prognoser.
2. **Pröva relevansen.** Visa vilka uppdrag, informationsflöden och aktörer som kan påverkas. Bedöm även konsekvensen av att avvakta.
3. **Bedöm förmågegapet.** Identifiera brister i juridisk förmåga, verksamhetsprocesser, informationskvalitet, säkerhet, kompetens och teknik.
4. **Skapa handlingsalternativ.** Jämför samverkan, återanvändning av gemensam infrastruktur, förändrade processer och egen utveckling.
5. **Fatta ett spårbart beslut.** Dokumentera ansvar, antaganden, risker, prioritering, förväntade nyttor och omprövningspunkter.
6. **Följ upp verkliga effekter.** Pröva om förändringen förbättrade uppdragets genomförande och inte bara levererade en ny teknisk komponent.

Detta är en analytisk modell för boken, inte ett föreskrivet myndighetsgemensamt arbetssätt. Poängen är att varje steg ska gå att följa, ifrågasätta och revidera.

## Arkitekturens olika perspektiv måste samverka

**Verksamhetsarkitektur** visar uppdrag, förmågor, processer, tjänster och ansvar. Den synliggör exempelvis var en informationskontroll är ett verksamhetsmoment och var den enbart är en teknisk validering.

**Informationsarkitektur** beskriver begrepp, objekt, relationer, livscykler, informationsägarskap och datakvalitet. Utan gemensam förståelse kan en status som ”godkänd” få olika betydelse i ett tillståndssystem, ett ärendesystem och ett operativt kontrollstöd.

**Applikations- och integrationsarkitektur** beskriver tjänster, API:er, händelser och systemberoenden. Här blir kontrakt, versionshantering och observerbarhet viktiga för att förhindra att ett systembyte bryter hela informationskedjan.

**Teknisk arkitektur** omfattar drift, identitet, plattformar, lagring och kommunikation. Val av moln- och AI-tjänster behöver prövas utifrån informationsklassning, geografiska och juridiska beroenden, upphandling och återställningsförmåga.

**Säkerhets- och rättsligt perspektiv** ska inte ligga som separata kontroller sist i ett projekt. Sekretess, behörighet, spårbarhet, proportionalitet och beredskap påverkar redan hur informationsflöden och ansvar ska utformas. Arkitekturarbete kan underlätta rättsliga bedömningar men ersätter dem inte.

Gränsen mellan dessa perspektiv är ett samarbetsområde. När en ny tjänst införs bör exempelvis informationsägaren, verksamhetsägaren, juristen, säkerhetsfunktionen och arkitekten tillsammans kunna beskriva informationsflödet från källa till användning.

## Gemensam infrastruktur och myndighetens eget ansvar

Digg beskriver Ena – Sveriges digitala infrastruktur – som gemensamma lösningar för enklare, säkrare och effektivare digitalisering. Syftet är bland annat att minska dubbelutveckling och stödja informationsutbyte i offentlig sektor. [K011] Det skapar ett tydligt arkitekturval: en myndighet bör undersöka om ett behov kan mötas genom gemensamma komponenter innan en egen parallell lösning byggs.

Det betyder inte att allt ska centraliseras. Myndigheten ansvarar fortfarande för sitt verksamhetsändamål, sina befogenheter, informationsklassning och hur den använder uppgifter. En gemensam identitets- eller förmedlingsfunktion kan till exempel ge en säker teknisk byggsten utan att avgöra om en viss användare får se en viss uppgift i ett konkret ärende.

EU:s interoperabilitetsförordning, Interoperable Europe Act, förstärker behovet av samordning vid digitala offentliga tjänster med gränsöverskridande betydelse. Förordningen omfattar bland annat interoperabilitetsbedömningar under vissa förutsättningar. EU:s vägledning lyfter rättsliga, organisatoriska, semantiska och tekniska dimensioner. [K043][K044] En integration kan alltså inte förklaras färdig enbart därför att två API:er utbyter ett tekniskt giltigt meddelande.

Arkitekturstyrningen bör därför innehålla återanvändningsprinciper, tydliga undantagsbeslut och möjlighet att följa när en gemensam tjänst ändras eller upphör att vara lämplig.

## Fiktivt scenario: en äldre integrationsplattform ska ersättas

*Det följande exemplet är konstruerat och beskriver inte något faktiskt myndighetssystem.*

En myndighet förmedlar uppgifter mellan företagens digitala rapportering, ett äldre ärendesystem, en riskanalysfunktion och ett operativt kontrollstöd. En central integrationsplattform har vuxit fram genom många separata projekt. Den klarar de dagliga volymerna men har svag dokumentation och ett stort antal dolda beroenden. Samtidigt väntas nya internationella informationskrav och ökad användning av digitala identiteter.

Det första förslaget är att byta plattform rakt av. Kostnadsbedömningen utgår från antal integrationer och servermiljöer. Men en kartläggning visar att systemen använder olika definitioner av aktör, försändelse, ärendestatus och kontrollutfall. Flera integrationer innehåller också verksamhetsregler som inte är dokumenterade någon annanstans.

Myndigheten omprövar därför projektet. I stället för ett rent teknikbyte formuleras tre förmågemål: spårbart informationsutbyte, gemensam förståelse av centrala informationsobjekt och möjlighet att ändra internationella anslutningar utan att bygga om hela kontrollkedjan.

Moderniseringen delas in i kontrollerade etapper. Först dokumenteras meddelanden och datakontrakt. Därefter byggs en ny anslutning för ett begränsat flöde med parallell uppföljning. Skillnader mellan gamla och nya resultat analyseras innan fler flöden flyttas. Varje etapp har en återgångsplan som omfattar även verksamhetens manuella rutiner.

Projektets styrgrupp följer inte bara antal migrerade integrationer, utan också datakvalitet, åtgärdstider, incidenter, förmågan att upptäcka fel och hur väl de operativa medarbetarna kan förstå informationsunderlaget.

### Vad scenariot visar

En teknisk modernisering kan i själva verket vara ett informations- och verksamhetsförändringsprojekt. Om arkitekturen reduceras till teknik riskerar organisationen att flytta gamla begreppskonflikter och oklara ansvar till en ny plattform. Om hela verksamhetsprocessen måste vara färdigdesignad innan något får levereras kan förändringen å andra sidan bli alltför långsam. Den praktiska lösningen är en övergripande målbild, styrda informationskontrakt och etappvis införande med återkoppling från verklig verksamhet.

## Styrning som förenar strategiskt och operativt ansvar

En myndighet behöver skilja mellan beslut om *riktning*, *prioritering*, *lösningsutformning* och *drift*. Ledningen måste kunna fastställa principer och acceptabla risknivåer. Portföljstyrningen måste jämföra nyttor och beroenden. Arkitekturforum behöver kunna bedöma konsekvenser av lösningsval. Verksamhetsägare måste bära ansvar för resultat och användning, och förvaltningen för kontinuerlig kvalitet och säkerhet.

Styrningen blir ineffektiv om alla vägval eskaleras till samma forum. Principbeslut och avvikelser med stora verksamhetskonsekvenser bör hanteras centralt, medan genomförandeteam kan få mandat att välja inom beslutade ramar. Det förutsätter transparens om beslut, tydliga arkitekturprinciper och kontrollerbar efterlevnad.

Finansieringen är också avgörande. Gemensamma informationsmodeller, loggningsfunktioner och plattformskomponenter saknar ibland en enskild förmånstagare, trots att de är nödvändiga för många senare förbättringar. Portföljen behöver därför avsätta medel för gemensamma förutsättningar, modernisering och teknisk skuld – inte enbart kortsiktiga synliga tjänsteförbättringar.

En rekommenderad uppföljning kan dela indikatorerna i tre nivåer: verksamhetsresultat, förmågeutveckling och teknisk leverans. Fler driftsatta API:er är ett leveransmått; färre motstridiga uppgifter är ett förmågemått; kortare och mer rättssäkra kontrollprocesser är ett verksamhetsresultat. Dessa mått ska inte blandas samman.

## Förändringsledning är mer än kommunikation

När information börjar delas på nya sätt förändras ofta arbetet. Handläggare behöver veta vad som är primärkälla och vad som är härlett. Analytiker behöver kunna bedöma osäkerhet. Operativa kontrollfunktioner behöver tillgång till rätt information även vid störningar. Säkerhetsfunktioner kan behöva nya övervaknings- och incidentrutiner.

En förändring har därför inte lyckats enbart för att ett system har produktionssatts. Den måste följas av tydliga arbetsinstruktioner, utbildning, rätt kompetensförsörjning, användarstöd och systematisk återkoppling. Medarbetarnas erfarenheter är särskilt viktiga där formella processer och faktisk verksamhet skiljer sig åt.

Motstånd mot förändring ska inte automatiskt tolkas som ovilja. Det kan vara en signal om att nya arbetssätt skapar kvalitetsbrister, oklara befogenheter eller extra dubbelarbete. Förändringsledningen måste kunna identifiera denna typ av invändningar och pröva dem mot målbild och fakta.

## Modernisering med bibehållen operativ förmåga

Myndigheter med kritiska kontroll- och informationsuppdrag kan sällan avveckla ett äldre system och sedan börja om. Modernisering måste ofta ske medan verksamheten fortsätter. Det talar för stegvis frikoppling, parallell verifiering, tydliga gränssnitt och reversibla införanden.

En sådan strategi kräver att målarkitekturen kompletteras med en *övergångsarkitektur*: vilket tillstånd gäller under migrationen, vilka gamla och nya system samverkar, hur undviks dubbla sanningskällor och när får en komponent avvecklas? Varje etapp bör ha mätbara acceptanskriterier och en plan för att hantera informationsskillnader.

Teknisk skuld bör inte behandlas som enbart gammal kod. Den omfattar även odokumenterade verksamhetsregler, beroenden till enskilda specialister, oklara informationsdefinitioner och kontrakt som inte går att ändra utan långa samordningskedjor.

Här möts kapitlets arkitekturperspektiv och föregående kapitels beredskapsanalys. En modern lösning är inte automatiskt robust; den behöver vara byggd så att fel kan upptäckas, isoleras och återställas utan att myndighetens kärnuppdrag upphör.

## Från arkitekturprinciper till beslut

Förmågekartor, målarkitektur och portföljstyrning ger en gemensam grund för prioritering, men blir verkningsfulla först när ansvar, finansiering och övergångslösningar beslutas. Det avslutande kapitlet omsätter dessa arbetssätt i en möjlig färdplan för 2026–2030.

## Sammanfattning

Den viktigaste arkitekturförmågan är att kunna beskriva sambanden mellan uppdrag, människor, processer, information, rättsliga krav och teknik. Utan den helhetsbilden riskerar myndigheten att genomföra många lyckade projekt utan att utveckla en sammanhängande verksamhet.

Förmågebaserad planering, styrda informationskontrakt, arkitekturprinciper och effektorienterad portföljstyrning ger en praktisk grund. Men de får verklig betydelse först när de omsätts i vardagliga beslut, resurssättning, förvaltning och förändrade arbetssätt.

I det avslutande kapitlet övergår vi från arkitekturprinciper till en möjlig strategisk färdplan för 2026–2030, med prioriterade initiativ, beroenden, vägval och indikatorer.

### Rättslig tidsavgränsning (oktober 2026)

Förordning (EU) 2024/903 började tillämpas den 12 juli 2024. Bestämmelser om bland annat interoperabilitetsbedömningar började tillämpas den 12 januari 2025. Det innebär inte att varje integration automatiskt omfattas av en särskild bedömningsskyldighet; tillämpningsområdet måste prövas för respektive förändring och tjänst. [K005]
