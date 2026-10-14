# 2. En myndighet i ett sammanlänkat samhälle

En försändelse passerar en gräns, ett företag lämnar en digital uppgift, en avgift ska fastställas och en avvikelse behöver bedömas. För den som berörs kan detta framstå som en enda sammanhängande händelse. För den offentliga förvaltningen kan den samtidigt beröra flera rättsliga regelverk, olika myndigheter, tekniska system och ansvarskedjor. Den digitala omställningens svåraste fråga är därför inte hur varje enskilt system blir snabbare. Den är hur ett offentligt uppdrag kan fungera rättssäkert, effektivt och robust när dess informationsflöden blir alltmer sammanlänkade.

Detta kapitel beskriver en tänkt statlig myndighet med uppgifter inom kontroll, tillsyn, tillstånd, uppbörd och brottsbekämpning. Exemplen är konstruerade och gör inte anspråk på att återge en viss organisations metoder, befogenheter eller informationsåtkomst. Syftet är att synliggöra spänningar som flera samhällsviktiga myndigheter kan känna igen. När en rättsregel eller ett EU-initiativ nämns måste dess faktiska tillämplighet bedömas separat för varje process och personuppgiftsbehandling.

## Det dubbla uppdraget: möjliggöra och skydda

En kontrollinriktad myndighet förväntas ofta utföra två uppgifter samtidigt. Den ska göra det enkelt för medborgare, företag och samverkansparter att göra rätt; samtidigt ska den upptäcka och hantera fel, missbruk och allvarliga hot. Uppgifterna är inte varandras motsatser. Välfungerande och tydliga förfaranden kan göra avvikelser lättare att urskilja. En kontroll som träffar mer rätt kan minska onödiga störningar för dem som följer reglerna.

En ensidig satsning på snabb handläggning riskerar emellertid att urholka kontrollkvaliteten. En ensidig satsning på kontroller riskerar i sin tur att orsaka oproportionerliga förseningar, ökad administration och sämre legitimitet. En väl avvägd styrning måste därför följa flera utfall: ledtid, kvalitet, regelefterlevnad, upptäckta avvikelser, överklaganden, informationssäkerhet och kostnader för berörda aktörer. Ett enda produktivitetsmått räcker inte.

Den digitala utvecklingen förstärker båda sidorna. Automatisering kan ge snabbare standardärenden, bättre tillgänglighet och mer konsekvent informationsinhämtning. Samma automatisering kan också skala upp fel i datamodeller, regler eller urvalskriterier. En felaktig uppgift som tidigare påverkade ett fåtal manuella ärenden kan fortplantas till många beslut om den återanvänds okritiskt i flera automatiserade led.

**Analytisk slutsats:** Myndighetens primära utvecklingsobjekt är inte ärendehanteringssystemet utan hela kedjan från en aktörs skyldighet eller rättighet till en rättsligt hållbar åtgärd och möjligheten att följa upp den.

## Sammanlänkning ändrar vad en myndighet måste kunna

Offentlig verksamhet har länge samverkat genom dokument, överenskommelser och manuella kontakter. I ett digitalt sammanlänkat samhälle flyttar samarbetet allt oftare in i löpande informationsflöden. En uppgift kan registreras hos en aktör, verifieras hos en annan, bedömas hos en tredje och användas som underlag för en åtgärd hos en fjärde. Då blir beroenden mellan juridik, informationssemantik, teknik och ansvar omedelbart operativa.

Det räcker inte att två system kan utbyta data över ett API. Mottagaren måste veta vad uppgiften betyder, hur den uppkommit, vilket tidsperspektiv den avser, vem som ansvarar för kvaliteten och på vilka villkor den får användas. En statuskod som betyder ”kontrollerad” i ett system kan exempelvis stå för en teknisk formatkontroll, medan mottagaren uppfattar den som en substantiell prövning. Det är ett semantiskt fel, inte ett transportfel.

För ett gränsöverskridande informationsutbyte tillkommer språk, skilda rättsliga kategorier, nationella registerstrukturer, tidszoner, identitetsmodeller och olika sätt att beskriva samma ekonomiska eller fysiska objekt. Hög interoperabilitet kräver därmed fyra samverkande förmågor:

- **Rättslig:** att fastställa befogenheter, ändamål, sekretess, dataskydd och ansvar.
- **Organisatorisk:** att klargöra vem som levererar, bedömer, följer upp och rättar information.
- **Semantisk:** att enas om begrepp, kodverk, datakvalitet och tolkning.
- **Teknisk:** att säkra tillgänglighet, identifiering, åtkomst, spårbarhet och drift.

EU:s förordning (EU) 2024/903, *Interoperable Europe Act*, syftar till att stärka interoperabiliteten i gränsöverskridande digitala offentliga tjänster. Den är en viktig omvärldssignal för myndigheters arkitektur- och samverkansarbete, men innebär inte att all offentlig information fritt får delas eller att varje nationellt kontrollförfarande automatiskt omfattas av samma utbytesmekanismer. Den konkreta rättsliga analysen är alltid nödvändig [K006].

## Från punktvisa ärenden till informationskedjor

En traditionell processbeskrivning börjar ofta med att en handling kommer in och slutar med att ett beslut expedieras. Den beskriver då myndighetens interna arbete, men inte alltid informationskedjan före och efter ärendet. I en sammanlänkad verksamhet kan uppgifter ha bildats långt tidigare, i andra system, och konsekvenserna av beslutet kan leva vidare hos externa aktörer.

Betrakta en hypotetisk kedja med följande led:

1. En verksamhetsutövare lämnar uppgifter om ett gränsöverskridande flöde.
2. Uppgifterna kontrolleras tekniskt och får ett kvitto.
3. Underlag kompletteras med tillåtna och relevanta uppgifter från andra aktörer.
4. Regler och riskindikatorer ger stöd för prioritering.
5. Ett ärende avgörs automatiserat eller av en tjänsteman inom den rättsliga ram som gäller.
6. En eventuell fysisk eller dokumentbaserad kontroll genomförs.
7. Resultatet dokumenteras och används för tillåten uppföljning samt förbättring av processens kvalitet.

Varje led kräver tydliga gränssnitt, men kedjan behöver dessutom gemensamma identifikatorer, spårbara händelser och ett sätt att skilja ett påstående från ett verifierat sakförhållande. Teknisk kvittens är till exempel inte detsamma som materiellt godkännande. Ett riskutfall är inte bevis för ett regelbrott. En senare rättelse måste kunna nå de processer där en tidigare felaktig uppgift haft betydelse.

Här uppstår en central arkitekturfråga: ska information kopieras till ett gemensamt lager, hämtas vid behov från källan eller kombineras genom händelsestyrda tjänster? Inget svar är universellt. Kopior kan möjliggöra kontinuitet och analys men ökar risken för inaktualitet och otydligt informationsansvar. Realtidsanrop kan ge färskare data men ökar beroendet av andra system och nätförbindelser. Valet måste därför baseras på beslutets tidskrav, informationsklassning, rättsliga möjligheter och verksamhetens tolerans för avbrott.

## Engångsprincipen och dess gränser

Engångsprincipen uttrycker ambitionen att medborgare och företag inte i onödan ska behöva lämna samma uppgifter till offentlig sektor flera gånger. Den är särskilt relevant när verksamheter möter återkommande rapporteringsskyldigheter eller när uppgifter redan finns i ett annat offentligt register.

EU:s regler om en gemensam digital ingång, *Single Digital Gateway* (förordning (EU) 2018/1724), omfattar bland annat vissa administrativa förfaranden och gränsöverskridande tillgång till information. Det tillhörande *Once-Only Technical System* har bestämda tillämpningsområden och tekniska regler enligt genomförandeförordning (EU) 2022/1463 [3–5]. Det vore fel att tolka systemen som ett generellt mandat för all slags informationsdelning.

I Sverige meddelade regeringen den 11 juni 2026 att en nationell tjänst för sådant gränsöverskridande informationsutbyte skulle lanseras under juni. Detta är en händelse efter eSams radarbild från februari och redovisas därför som en senare uppdatering, inte som ett faktum i februarirapporten [K010].

För en kontroll- och uppbördsmyndighet innebär engångsprincipen en nyttig designfråga: vilka uppgifter behöver den berörda aktören faktiskt lämna, och vilka kan – där lagstöd och teknik medger det – hämtas eller verifieras från en kvalitetssäkrad källa? Men principen får inte förväxlas med frånvaro av uppgiftsskyldighet, beviskrav eller kontrollansvar. Samma uppgift kan behöva styrkas för olika ändamål, vid olika tidpunkter eller enligt olika regelverk.

## Riskbaserad kontroll utan automatiserad misstanke

När antalet ärenden eller informationshändelser ökar snabbare än kontrollresurserna blir prioritering en nödvändig förmåga. Riskbaserade arbetssätt kan koncentrera uppmärksamhet till områden där en avvikelse sannolikt får större betydelse. Men själva riskbedömningen måste kunna skiljas från den efterföljande rättsliga prövningen.

En analysmodell kan ge en indikator på att ett visst ärende behöver granskas. Indikatorn bör då betraktas som ett beslutsstöd inom sitt dokumenterade användningsområde. Den säger inte automatiskt att någon har agerat felaktigt. Även en statistiskt välkalibrerad modell kan ge många falska positiva utfall när den faktiska förekomsten av en viss avvikelse är låg. Om modellen förändrar vilka ärenden som granskas förändrar den också vilka utfall myndigheten får tillbaka som tränings- eller uppföljningsdata: urvalet kan därmed skapa en återkopplingsbias.

För att behålla legitimiteten bör en myndighet kunna redogöra för modellens ändamål, vilka datakategorier den bygger på, hur kvaliteten övervakas och vad som händer vid fel. Kraven påverkas av exakt tillämpning och tillämplig rätt; de ska inte generaliseras från en viss AI-klassificering till alla analysverktyg. Det operativa arbetssättet behöver dessutom ange när en människa ska överpröva eller komplettera en maskinell signal.

Ännu viktigare är att kunna utvärdera resultatet av prioriteringen utan att endast mäta antal utförda kontroller. För en rättvisande bedömning måste man också analysera träffsäkerhet, undanträngda kontroller, effekter för berörda företag, klagomål och om vissa grupper systematiskt behandlas annorlunda utan sakligt stöd.

## Samverkan utan att ansvar löses upp

Ett sammanlänkat arbetssätt kan ge intrycket av en enda offentlig förvaltning. Men rättsligt ansvar, mandat och tillsyn är fortfarande fördelade. En organisation kan ansvara för insamlingen av en uppgift, en annan för den tekniska överföringen och en tredje för ett beslut som grundas på uppgiften. Det ansvar som följer av respektive behandling och beslut måste klarläggas, inte suddas ut av ett gemensamt användargränssnitt.

Detta ställer krav på samverkansöverenskommelser och förvaltningsmodeller som är mer precisa än ”vi delar data”. En fungerande ansvarskedja behöver beskriva informationsägarskap, rättelseförfaranden, incidenthantering, förändringsavisering, tillgänglighetsnivåer, gallring och loggning. Den behöver också göra skillnad mellan att någon tekniskt kan få åtkomst och att personen eller organisationen har laglig rätt att använda informationen för ett visst ändamål.

På detta område är det frestande att lansera gemensamma plattformar före gemensamma definitioner. Resultatet blir ofta att en teknisk samordning döljer semantiska och rättsliga olikheter som senare försvårar förändring. Ett mer uthålligt tillvägagångssätt är att först beskriva informationsutbytet som ett gemensamt verksamhetskontrakt: vilka händelser utlöser det, vilka uppgifter behövs, vad betyder de och vem ansvarar vid avvikelser?

## När kontrollen flyttar mellan digitala och fysiska miljöer

Samhällsviktiga kontrolluppdrag har ofta en materiell dimension. En digital uppgift kan avse ett faktiskt föremål, ett transportmedel, en leverans, en anläggning eller en persons rättsliga ställning. Därför är den digitala och den fysiska verksamheten inte två separata världar.

Ett väl utformat operativt stöd gör det möjligt att identifiera vilket objekt kontrollen avser, se tillåtna relevanta uppgifter och dokumentera iakttagelser med tydlig proveniens. Det måste fungera även när uppkopplingen är bristfällig och när medarbetare byter arbetsplats eller skift. Samtidigt får den mobila tillgången inte skapa onödiga personuppgiftssamlingar eller lämna känsliga uppgifter kvar på fel enheter.

Det finns också en tidsskaleproblematik. Digitala uppgifter kan ändras på sekunder, medan fysiska flöden och rättslig handläggning har andra förlopp. System och processer måste kunna besvara frågan: *vilken uppgift gällde när beslutet fattades?* En senare uppdaterad status får inte skriva över den historik som krävs för att förstå det ursprungliga ställningstagandet.

## Uppbörd, kontroll och god service är en helhet

I en myndighet som hanterar avgifter, pålagor eller andra ekonomiska skyldigheter kan en smidig digital process ge nytta åt både staten och den uppgiftsskyldige. Korrekt information tidigt minskar behovet av kompletteringar, rättelser och tvister. Men ett digitalt gränssnitt kan inte på egen hand lösa oklarheter i materiella regler eller brister i underlagens kvalitet.

Om en automatisk beräkning bygger på felklassificerade data kan felet återkomma systematiskt. Myndigheten behöver därför en kedja från normtolkning och kodifierade regler till testfall, förändringskontroll, avvikelseuppföljning och förståeliga beslut. Författningsändringar måste kunna spåras till vilka regeltabeller, beräkningar, mallar och integrationer som har ändrats. Denna styrning är lika viktig som själva programvaran.

God service är inte bara kort svarstid. Den innebär att den som berörs förstår vilka uppgifter som krävs, hur uppgifterna används, hur status kan följas och hur en felaktighet kan påtalas. I en sammanlänkad process måste även de digitala kontaktvägarna beskriva när ett mottaget meddelande fått rättslig effekt och när det enbart är en teknisk bekräftelse.

## Verksamhetsexempel: ett avvikande gränsöverskridande flöde

*Fiktivt scenario, inte en beskrivning av ett faktiskt ärende eller en existerande myndighets tekniska lösning.*

Ett företag lämnar digitala uppgifter inför en planerad gränsöverskridande leverans. Flödet uppfyller de tekniska formatkraven men flera uppgifter behöver jämföras med äldre handlingar och med en tillåten extern uppgiftskälla. En automatisk regel identifierar en möjlig inkonsekvens. Den får inte behandlas som bevis för ett regelbrott, men kan föranleda ett kontrollsteg enligt gällande befogenheter.

En handläggare får en sammanfattning av varför ärendet valts ut, vilka uppgifter som har jämförts, hur aktuella källorna är och vilken osäkerhet som finns. En operativ kollega kan vid behov se de uppgifter som behövs för den egna kontrollåtgärden, men inte alla underliggande uppgifter utan relevant behörighet. Den faktiska iakttagelsen dokumenteras på ett sätt som kan kopplas tillbaka till ärendet utan att källdata skrivs över.

Senare konstateras att en kod i ett externt system hade annan betydelse än den som importerats. Den tekniska överföringen var korrekt, men tolkningen felaktig. Det inträffade visar varför en fullständig lösning måste omfatta mer än API:er: begreppsmodell, testning mot verkliga förfaranden, felrättning, ansvar, dokumentation och möjlighet att ompröva den fortsatta hanteringen.

### Vad scenariot visar

För det första ligger den största nyttan inte i att en enda kontroll automatiseras utan i att rätt information når rätt funktion vid rätt tidpunkt. För det andra är den viktigaste risken ofta ett osynligt antagande om datats innebörd snarare än en spektakulär it-incident. För det tredje blir det möjligt att utveckla kontrollkvalitet och service samtidigt när myndigheten följer hela kedjans effekter.

## Uppdragets särskilda avvägningar

Sammanlänkning kan förbättra service och träffsäkerhet men förutsätter att informationsutbyte har ett tydligt ändamål och att myndighetens befogenheter inte sammanblandas med andra aktörers. Att felaktigt tolkade uppgifter påverkar ett kontrollurval illustrerar varför kvalitet och ansvar behöver följas längs hela kedjan. Kapitel 6–8 fördjupar informationsmodeller, utbyte och behörighet; kapitel 12 följer den operativa kontrollkedjan.

## Från sammanlänkning till ansvarstagande

Att vara en del av ett sammanlänkat samhälle innebär inte att en myndighet ska överge sina gränser eller avsäga sig sitt ansvar. Tvärtom kräver fler beroenden en tydligare förståelse för det egna uppdraget och för vad andra aktörer kan, får och förväntas leverera.

En hållbar digital omställning måste därför klara två frågor samtidigt: *Vad blir möjligt när information kan röra sig snabbare?* och *Vad måste förbli kontrollerat, begripligt och rättsligt hållbart när informationen gör det?* Den som besvarar enbart den första riskerar att bygga ett snabbt men bräckligt system. Den som besvarar enbart den andra riskerar att bevara ineffektivitet och onödiga hinder.

Nästa kapitel undersöker hur myndigheten kan omvandla den här typen av omvärldsförändringar till en långsiktig strategisk förmåga – från enskilda signaler i en radarbild till en sammanhållen prioritering av utvecklingsinsatser.
