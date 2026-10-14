# 11. Beredskap och operativ kontinuitet

En digital störning upphör inte att vara en verksamhetskris bara för att teknikerna kan beskriva dess orsak. När en myndighet förlorar tillgången till en central informationskälla påverkas inte enbart datorer och nätverk. Handläggning kan stanna, kontroller behöver prioriteras om och information som normalt delas i realtid kan plötsligt behöva utbytas på annat sätt. Ett avbrott kan samtidigt skapa betydande samhällskostnader om legitima varu- och transportflöden stoppas utan att det ger motsvarande nytta för skydd och kontroll.

Kapitlet behandlar därför kontinuitet som en förmåga hos hela myndigheten: att utföra de viktigaste uppgifterna på en acceptabel nivå, också när ordinarie system, personal, lokaler eller externa tjänster inte fungerar. Resonemangen utgår från en statlig verksamhet med kontroll, uppbörd, internationellt informationsutbyte och operativa uppgifter. Exemplen är fiktiva och avser ingen namngiven myndighet.

## Beredskap är mer än katastrofåterställning

It-återställning syftar till att få system och data tillbaka i drift. Kontinuitetshantering ställer en vidare fråga: vilka uppgifter måste kunna utföras under avbrottet, och på vilken nivå? Skillnaden har praktiska följder. Om ett ärendesystem ligger nere ett dygn kan en teknisk återställningsplan vara mycket bra, men verksamheten kan ändå ha saknat rutiner för tidskritiska beslut och kommunikation med berörda aktörer under samma dygn.

En genomtänkt kontinuitetsplan utgår därför från de tjänster och samhällseffekter som behöver skyddas. Målet är inte att hålla allt igång till varje pris. Målet är att med begränsade resurser bevara rätt verksamhet på en uttryckligen beslutad lägstanivå och sedan återgå till ordinarie förmåga utan att rättssäkerhet, säkerhet eller informationskvalitet åsidosätts.

I den svenska förordningen (2022:524) om statliga myndigheters beredskap anges att myndigheter ska identifiera samhällsviktig verksamhet, analysera sårbarheter och systematiskt arbeta för att upprätthålla den egna samhällsviktiga verksamheten. Förordningen ställer även krav på utbildning och övning vid fredstida krissituationer, och på att myndigheter i sin verksamhet beaktar totalförsvarets krav. Beredskapsmyndigheter har ytterligare uppgifter. Den aktuella tillämpningen måste alltid prövas mot myndighetens författningsreglerade ansvar och eventuella specialbestämmelser. [K034]

Myndigheten för civilt försvars material om samhällsviktig verksamhet framhåller att kontinuitetshantering ska kunna upprätthålla verksamheter och processer på en acceptabel nivå oavsett störningstyp. Det breda perspektivet är viktigt: en elstörning, ett cyberangrepp och brist på nyckelpersonal kan slå mot samma verksamhetsförmåga, även om orsakerna är helt olika. [K035]

## Börja med samhällseffekten

Det första steget är att identifiera vilka funktioner som inte kan vänta. För en myndighet som hanterar gränsöverskridande flöden kan det handla om möjligheten att ta emot grundläggande uppgifter, göra nödvändiga kontroller, hindra särskilt riskfyllda flöden eller lämna besked som får stor påverkan på samhällets försörjning. För en annan del av organisationen kan det vara viktigt att kunna fatta och dokumentera brådskande beslut eller hantera betalningar och säkerheter.

Alla uppgifter är inte lika tidskritiska. Ett arbete med långsiktig statistikproduktion kan ofta senareläggas, medan en pågående kontrollinsats eller hantering av vissa skyddsvärda varor kan behöva fortsätta omedelbart. Sådana avvägningar bör beslutas före störningen och grundas i lagliga befogenheter, verksamhetsrisk och samhällskonsekvenser. De kan inte lämnas helt till den som råkar ha jour när incidenten inträffar.

En verksamhetskonsekvensanalys kan ange när en störning blir oacceptabel, vilka resurser som krävs och vilka alternativa arbetssätt som finns. Praktiskt är det värdefullt att dokumentera:

- Vilken verksamhetsförmåga och vilken samhällseffekt som är i riskzonen.
- Vilken lägsta servicenivå eller kontrollnivå som ska upprätthållas.
- Hur länge ett bortfall kan tolereras innan allvarliga konsekvenser uppstår.
- Vilka processer, uppgifter, roller, platser och informationsutbyten som behövs.
- Vilka författningskrav som begränsar möjliga nödrutiner.
- Hur återgång och efterregistrering ska genomföras.

Sådana tidsgränser ska inte vara godtyckliga. De måste vägas mot lagstadgade tidsfrister, rättigheter, säkerhet och den praktiska förmågan att hantera arbetsuppgifterna.

## Ett beroendelandskap som sträcker sig långt utanför it-avdelningen

En samhällsviktig myndighet arbetar ofta genom kedjor av interna och externa beroenden. En till synes lokal funktion kan kräva identitetstjänster, nätförbindelser, registeruppgifter, certifikat, specialiserad utrustning, meddelandeförmedling och informationsutbyte med nationella eller utländska aktörer.

En relevant beroendekarta behöver omfatta åtminstone sex kategorier:

**Människor och kompetens.** Vem får fatta brådskande beslut? Finns ersättare, utbildade operatörer och en uthållig bemanningsplan?

**Information.** Vilka uppgifter måste vara aktuella och tillförlitliga? Vilken information får lagras eller användas lokalt, och vilka uppgifter kan inte återskapas efter ett bortfall?

**Teknik och kommunikation.** Vilka system, identitetsfunktioner, API:er, terminaler, radioförbindelser och lokala nät behövs? Var finns gemensamma felpunkter?

**Externa tjänster.** Vilka molnleverantörer, driftpartners, betalningsförmedlare och internationella system påverkar verksamheten? Hur snabbt kan dessa aktörer ge besked vid störning?

**Fysiska resurser.** Vilka lokaler, kontrollplatser, fordon, reservkraftlösningar och kommunikationsmedel behövs?

**Juridiska och organisatoriska villkor.** Vilka befogenheter får användas vid störning? Vilka avsteg kräver särskilt beslut, och vilka lagkrav kan inte sättas åt sidan?

En beroendekarta måste utvecklas tillsammans med verksamheten. En teknisk applikationsförteckning visar sällan vilka arbetsmoment som faktiskt faller bort eller var en handläggare kan byta till ett alternativt arbetssätt.

## Fyra lägen i samma verksamhetsprocess

Ett användbart sätt att utforma operativ kontinuitet är att ange fyra tydliga lägen för varje kritisk process.

**Ordinarie läge.** Information flödar mellan tjänster och kan kontrolleras automatiskt. Ärenden prioriteras enligt normala regler och uppgifter registreras löpande.

**Begränsat läge.** Vissa externa uppgifter eller tekniska funktioner saknas. Processen fortsätter men med färre automatiska kontroller, utökad manuell verifiering och begränsningar för vilka ärenden som kan avgöras.

**Reservläge.** Kritiska digitala tjänster är inte tillgängliga. Endast uttryckligen prioriterade uppgifter utförs genom särskilda rutiner, behörigheter och dokumentationssätt.

**Återgångsläge.** Tekniken är åter tillgänglig men verksamheten är inte automatiskt återställd. Beslut, kontroller och händelser från reservläget måste stämmas av mot ordinarie register; köer ska behandlas och eventuella fel eller dubletter rättas.

Det sistnämnda läget är lätt att underskatta. Om uppgifter registreras på nytt utan kontroller kan samma handling eller transaktion förekomma två gånger. Om informationen från störningsperioden tappas bort förlorar myndigheten både spårbarhet och möjligheten till senare uppföljning.

## Verksamhetsexempel: störning i internationell intygsverifiering

*Följande scenario är konstruerat för boken och beskriver inte något befintligt system eller gällande dispensförfarande.*

En myndighet använder en internationell digital tjänst för att kontrollera att elektroniska intyg är giltiga. Tidigt på morgonen uppstår ett längre avbrott i tjänsten. Samtidigt kommer stora mängder uppgifter om ankommande transporter in som vanligt. Verksamheten måste avgöra vilka flöden som kan fortsätta och vilka som inte kan hanteras utan den externa verifieringen.

Den första reaktionen kan vara att antingen stoppa alla berörda flöden eller att temporärt hoppa över kontrollen. Båda alternativen kan vara olämpliga. Ett generellt stopp kan få oproportionerliga samhällskonsekvenser. En okontrollerad passage kan vara oförenlig med rättsliga krav eller skapa säkerhetsrisker.

Den förberedda kontinuitetsplanen gör i stället tre saker. Först identifieras de ärendekategorier där verifieringen rättsligt eller operativt är nödvändig. Därefter används en godkänd reservrutin för de situationer där ett alternativt förfarande faktiskt är tillåtet. Slutligen registreras alla berörda ärenden med tydlig markering om vilken verifiering som saknades och vilka åtgärder som vidtogs.

Verksamhetsledningen gör återkommande bedömningar av belastning och risk, i samverkan med it-funktionen, jurister och berörda operativa chefer. Kommunikationsfunktionen ger tydlig information till företag och samarbetspartner om vad som gäller, utan att lämna ut skyddsvärda uppgifter. När tjänsten återkommer påbörjas inte bara normal drift. Myndigheten måste också kontrollera vilka ärenden som fortfarande behöver verifieras och om tidigare åtgärder kräver rättelse eller komplettering.

I detta scenario är framgång inte enbart att verksamheten kunde fortsätta. Framgång är att den kunde fortsätta **på ett rättsligt tillåtet, säkerhetsmässigt kontrollerat och i efterhand spårbart sätt**.

## Rättssäkerhet under störning

En kritisk störning kan skapa tidspress men ändrar inte automatiskt en myndighets befogenheter. Handläggare behöver veta vilka förenklade arbetssätt som har uttryckligt stöd och vilka beslut som alltid måste göras enligt ordinarie regler. En reservrutin bör därför granskas juridiskt innan den behöver användas.

Tre risker behöver särskilt hanteras. Den första är att ofullständiga uppgifter behandlas som om de vore verifierade. Den andra är att tillfälliga bedömningar inte dokumenteras så att de kan prövas i efterhand. Den tredje är att ansvaret blir oklart när arbetet fördelas mellan olika arbetsplatser eller samverkande aktörer.

Ett praktiskt krav är att varje reservförfarande dokumenterar vem som gjorde vad, på vilket underlag och med vilket mandat. Där digital loggning saknas måste en säker alternativ dokumentation finnas. När digitala tjänster återupptas ska den informationen införas eller kopplas tillbaka på ett kontrollerat sätt, utan att originaldokumentation förstörs.

## Beredskapsplanering måste vara informationssäker

Det är inte givet att en reservlösning är säker bara för att den är separat från ordinarie it-miljö. En lokal kopia av känsliga uppgifter kan minska beroendet av nätanslutning men öka risken för otillåten åtkomst eller föråldrad information. Ett manuellt blankettflöde kan vara enkelt att starta men svårt att skydda, följa upp och överföra tillbaka till ordinarie system.

Reservförfaranden behöver därför informationsklassas, behörighetsstyras och övas. Åtkomst till nöduppgifter bör vara begränsad och loggas så långt det är möjligt. Planen behöver även beakta vilka kommunikationskanaler som får användas när ordinarie meddelandesystem ligger nere. Särskilt skyddsvärd information får inte flyttas till osäkra kanaler av ren bekvämlighet.

Övergången till reservläge bör ha tydliga beslutskriterier, exempelvis att en kritisk informationskälla bedöms opålitlig. Detta kan vara lika viktigt som att den inte går att nå. Vid en cyberincident kan tillgängliga data vara manipulerade, och då är en snabb återstart utan integritetskontroll inte nödvändigtvis ett säkert alternativ.

## Kontinuitet, återställning och teknisk arkitektur

Tekniska återställningsmål uttrycks ofta som hur länge en tjänst får vara nere och hur mycket information som maximalt får gå förlorad. Dessa mål är användbara men behöver härledas från verksamhetens konsekvensanalys. Om en process kräver nästintill obruten åtkomst hjälper det inte att ett återställningsmål sätts för systemet utan finansiering eller en prövad reservprocess.

För vissa funktioner kan redundanta driftmiljöer eller reservförbindelser vara lämpliga. För andra är en enklare fristående lösning, begränsad offlinefunktion eller ett förberett manuellt arbetsflöde mer robust. Arkitekturen bör motverka att en gemensam identitetstjänst, integrationsplattform eller extern leverantör blir en dold felpunkt för många kritiska processer.

Det är också viktigt att kunna återställa **tillförlitlig information**, inte bara filer och servrar. Säkerhetskopior behöver kunna prövas, och verksamheten behöver veta från vilken tidpunkt data kan betraktas som riktiga. Incidentutredning och återstart kan därför behöva ske i flera steg.

## Samverkan och ledning vid en händelse

En myndighet kan sällan lösa en omfattande störning ensam. Den är beroende av näringsliv, andra myndigheter, kommunikationsoperatörer och ibland aktörer i andra länder. Beredskapsplanering bör därför omfatta kontaktvägar, alternativa kommunikationskanaler och rutiner för att dela lägesbilder med rätt mottagare.

Det bör vara fastlagt vem som får aktivera reservrutiner, vem som prioriterar konkurrerande verksamhetsbehov och hur beslut om återgång fattas. Ett gemensamt lägesunderlag kan skilja mellan tekniska fakta, verksamhetskonsekvenser, osäkerheter och beslutade åtgärder. Om flera funktioner publicerar egna lägesbilder utan samordning finns risk för motstridiga besked både internt och externt.

Förordningen om statliga myndigheters beredskap anger också att myndigheter ska samverka och stödja varandra vid fredstida krissituationer. För beredskapsmyndigheter tillkommer särskilda skyldigheter som rör bland annat samverkan, övning och planering. [K034]

## Öva hela kedjan – även återgången

En plan som aldrig har prövats är en hypotes. Kontinuitetsövningar bör därför omfatta mer än att teknikgruppen återskapar en server. En trovärdig övning kan låta ett kontrollställe tappa nätförbindelsen samtidigt som centrala system lämnar ofullständiga uppgifter och en viktig samverkanspart inte kan nås.

Övningen ska visa om personalen vet vilka uppgifter som prioriteras, hur beslut dokumenteras, när juridisk kompetens kopplas in och hur kontakt med berörda aktörer sker. Därefter bör ett separat moment testa återgången: kan handläggarna hitta tillfälliga handlingar, registrera dem säkert och verifiera att inga beslut eller åtgärder försvinner?

Utvärderingen bör mäta hur väl verksamheten upprätthölls, inte bara hur snabbt systemen startade. Exempel på indikatorer är tid till fungerande reservrutin, antal brådskande ärenden som kunde hanteras lagenligt, andel korrekt återregistrerade händelser och tid till kontrollerad normaldrift. Lärdomarna måste leda till ändrade instruktioner, förbättrad arkitektur eller tydligare ansvar – annars riskerar övningen att bli en årlig ritual.

## Från kontinuitetsplan till prövad förmåga

Den avgörande kontrollen är om verksamheten klarar att arbeta rättssäkert i begränsat läge, dokumentera beslut under reservdrift och återföra information utan förlust eller dubblering. Varje reservrutin behöver därför en ägare, en start- och stoppregel och en övad återgång. Kapitel 16 samlar de långsiktiga strategiska vägvalen.

## Sammanfattning

Digital beredskap betyder att en samhällsviktig myndighet kan fortsätta utföra prioriterade uppgifter när de normala förutsättningarna försvinner. En återställd server är inte detsamma som en återställd samhällsfunktion: också beslut, dokumentation och prioriterade uppgifter måste fungera.

För myndigheter med omfattande kontrollverksamhet och gränsöverskridande flöden är den centrala utmaningen att både värna samhällets skydd och undvika onödiga stopp i legitima flöden. Därför måste reservrutiner vara beslutade i förväg, rättsligt prövade, informationssäkra och möjliga att följa upp i efterhand. Det är förmågan att hantera **störningen och återgången** som avgör den operativa motståndskraften.
