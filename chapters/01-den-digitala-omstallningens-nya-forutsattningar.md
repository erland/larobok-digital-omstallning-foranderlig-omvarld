# 1. Den digitala omställningens nya förutsättningar

En gränsöverskridande försändelse kan färdas genom flera länder på kortare tid än det tar att klarlägga vilka uppgifter olika offentliga aktörer har rätt att utbyta om den. Ett företag kan lämna korrekta uppgifter i en digital tjänst men ändå behöva komplettera samma information hos en annan aktör. En analytiker kan identifiera ett avvikande mönster i stora datamängder men ha svårt att redovisa varför en viss signal bör leda till en närmare kontroll. Dessa situationer visar en central motsättning i vår tids offentliga förvaltning: den tekniska möjligheten att samordna information ökar, samtidigt som kraven på rättssäkerhet, säkerhet, spårbarhet och ansvar skärps.

Digital omställning handlar därför inte i första hand om att ersätta papper med elektroniska formulär. Den handlar om att förändra hur en myndighet använder information, fattar beslut, samverkar och kan fullgöra sitt uppdrag också när omständigheterna snabbt förändras. För en myndighet som verkar i gränslandet mellan samhällsservice, ekonomiska flöden, kontroll och brottsbekämpning blir förändringen särskilt påtaglig. Den behöver samtidigt underlätta legitima aktiviteter, upptäcka risker, skydda enskildas rättigheter och upprätthålla verksamheten vid störningar.

Detta kapitel ger en karta över de drivkrafter som formar utvecklingen. De följande kapitlen undersöker vart och ett av områdena på djupet.

## Från digitala system till sammanhängande verksamhet

Den tidigare digitaliseringsvågen beskrevs ofta med system och kanaler: en e-tjänst infördes, ett register moderniserades och ett manuellt ärendesteg automatiserades. Sådana förbättringar kan fortfarande ge stora vinster, men de räcker inte när ett uppdrag är beroende av ett helt nätverk av aktörer, uppgifter och beslut. En händelse hos en extern aktör kan påverka en annan myndighets riskbedömning, ett tillstånd eller behovet av en fysisk insats.

I en sammanhängande verksamhet måste minst fem nivåer fungera tillsammans. **Uppdraget** anger varför myndigheten får agera. **Processerna** beskriver hur arbetet utförs. **Informationen** visar vad myndigheten vet och med vilken kvalitet. **Tekniken** möjliggör behandling och utbyte. **Styrningen** säkerställer att den samlade lösningen är tillåten, säker och ändamålsenlig. Om en nivå saknas kan de övriga inte kompensera fullt ut. Ett tekniskt fungerande datautbyte är exempelvis inte liktydigt med att mottagaren har rätt att använda uppgifterna för ett nytt ändamål.

Detta ger en första utgångspunkt för boken: digital utveckling behöver ledas som verksamhetsförändring, inte enbart som en portfölj av it-projekt. Den behöver beskrivas i termer av förmågor: exempelvis att säkert kunna identifiera en aktör, förstå ett internationellt flöde, upptäcka en avvikelse, fatta ett motiverat beslut och följa upp en kontrollåtgärd.

## Fyra förändringsfält som möts

I sin radarbild från februari 2026 fokuserar eSam på fyra områden: artificiell intelligens, säkerhet och beredskap, digital identitet samt datadelning och informationsutbyte. Syftet är enligt rapporten att ge myndigheter bättre framförhållning och helhetssyn kring nya eller möjliga regelverk och att underlätta samverkansprioriteringar. Rapporten beskriver förändringar sedan september 2025, inte en uttömmande redovisning av alla rättsakter och initiativ. Radarbildens kompletterande kalkylblad uppgavs vid rapporttillfället innehålla 128 unika poster. [K001]

Dessa fyra fält bör inte betraktas som separata tekniktrender. De griper in i varandra.

**AI** ökar möjligheten att analysera text, mönster och händelser, men förstärker behovet av ändamålsenliga data, kontroll av beslutsstöd och kompetens hos användarna. **Säkerhet och beredskap** flyttar fokus från enskilt systemskydd till förmågan att upprätthålla hela tjänstekedjor och externa beroenden. **Digital identitet** handlar inte bara om vem som loggar in, utan också om vem som har rätt att företräda en organisation och utföra en viss handling. **Datadelning** förutsätter en kombination av juridisk grund, semantisk förståelse, tekniska gränssnitt och förtroende mellan organisationer.

Anta att en digital fullmakt gör det möjligt för en företrädare att skicka in uppgifter för ett företag. Uppgifterna ska kanske användas i en automatiserad kontroll, jämföras med information från en annan stat och därefter ligga till grund för en riskindikation. Varje steg påverkas av ett eller flera av radarbildens fyra fält. Om identiteten är korrekt men behörigheten inte går att styrka, stannar processen. Om informationsmodellerna skiljer sig åt, riskerar jämförelsen att bli missvisande. Om analysen saknar spårbarhet, blir det svårt att granska grunden för den efterföljande åtgärden. Om en central integrationsplattform ligger nere, kan hela kedjan påverkas.

Det är i dessa mötespunkter som många av de mest avgörande strategiska frågorna uppstår.

## Geopolitik blir en fråga om arkitektur

Internationella konflikter, försörjningsstörningar, ekonomiska påtryckningar och förändrade handelsmönster kan uppfattas som externa frågor. För en digitalt beroende myndighet blir de snabbt konkreta frågor om tillgång till nät, plattformar, komponenter, specialistkompetens och information. En tjänst kan fungera felfritt en vanlig dag men vara sårbar om en extern leverantör inte längre kan tillhandahålla en kritisk funktion eller om gränsöverskridande kommunikation störs.

Digital suveränitet kan i detta sammanhang förstås som graden av faktisk rådighet över avgörande digitala resurser. Det betyder inte att varje myndighet ska bygga egna datacenter eller avstå från internationella leverantörer. Det betyder att beroenden behöver vara kända, prövade och förenliga med uppdragets risker. En tjänst med låg kritikalitet kan rimligen acceptera andra beroenden än ett system som stödjer operativa kontroller dygnet runt.

Tre frågor är särskilt användbara i arkitekturarbetet. **Kan myndigheten byta eller komplettera leverantör utan orimliga kostnader eller långa avbrott?** **Kan den förklara var uppgifter behandlas och vilka aktörer som kan få tillgång till dem?** **Kan den fortsätta utföra sina prioriterade uppgifter när en betydande extern beroendekedja fallerar?** Svaren kan leda till krav på portabilitet, tydligare datakontrakt, reservrutiner, segmentering och kontinuitetstestning.

I februarirapporten lyfter eSam tekniksuveränitet och Sveriges behov av säkra tekniska plattformar som en del av den bredare säkerhets- och AI-utvecklingen. [K001] Slutsatsen för den enskilda myndigheten är däremot en analytisk bedömning: beroendehantering behöver bli en löpande del av verksamhets- och målarkitektur, inte en kontrollpunkt strax före upphandling.

## EU-reglering som förändringsmotor

En myndighets utveckling styrs inte enbart av nationella prioriteringar. EU-rätt påverkar hur organisationer behöver bedöma interoperabilitet, använda AI, hantera identiteter, skydda informationssystem och utbyta data. Regelverken har olika syften och gäller inte automatiskt varje myndighet eller varje system på samma sätt. Därför behöver en rättslig analys alltid börja med den konkreta verksamheten, den berörda aktören och det avsedda användningsfallet.

Ett exempel är förordning (EU) 2024/903, ofta benämnd **Interoperable Europe Act**. Den trädde i kraft den 11 april 2024 och började till stor del tillämpas den 12 juli 2024; vissa bestämmelser började tillämpas den 12 januari 2025. Den är avsedd att stärka interoperabilitet i offentlig sektor över nationsgränserna och innehåller bland annat krav på interoperabilitetsbedömningar i angivna situationer. [K002][K003] För en myndighet med omfattande internationella informationsflöden är den strategiska signalen tydlig: samverkansförmåga behöver beaktas när berörda digitala tjänster och system förändras. Vilken rättslig skyldighet som faktiskt aktualiseras beror på förordningens tillämpningsvillkor.

EU:s AI-förordning ger ett annat slags utmaning. Den reglerar AI-system utifrån bland annat risk och användningsområde, och olika bestämmelser har olika tillämpningsdatum. Att ett system använder AI betyder inte i sig att det tillhör en viss riskkategori. Ett verktyg som hjälper en handläggare att hitta relevanta texter måste därför bedömas separat från ett system vars resultat påverkar urval eller beslut om enskilda aktörer. För AI som används i kontrollnära miljöer behöver upphandling, informationssäkerhet, dokumentation och ansvar utformas med det konkreta ändamålet som utgångspunkt. Kommissionens vägledning och aktuella rättsläge behöver följas under det fortsatta bokarbetet. [K004]

Det är frestande att svara på varje nytt regelverk med ett separat efterlevnadsprojekt. Men flera regelverk kan beröra samma underliggande förmågor: informationsklassning, loggning, behörighetsstyrning, riskanalys, leverantörsuppföljning och dokumenterade beslut. Den mer hållbara strategin är att identifiera gemensamma förmågor där olika krav kan omsättas till sammanhängande styrning. Samtidigt får gemensam styrning inte sudda ut skillnader mellan rättsliga skyldigheter.

## AI förändrar både möjligheter och ansvar

eSams radarbild beskriver ökat nationellt fokus på AI, bland annat en planerad förvaltningsgemensam AI-verkstad, satsningar på AI och data samt regeringens AI-strategi från februari 2026. [K001] Dessa uppgifter är en historisk lägesbild från rapportens publicering; ett planerat uppdrag eller driftsdatum där ska inte utan ny verifiering framställas som genomfört i oktober 2026.

Potentialen i en verksamhet med stora informationsvolymer är lätt att se. AI kan stödja sortering av handlingar, sökning i omfattande regelverk, identifiering av datakvalitetsproblem och framtagning av underlag till utredning. Mer avancerade analysmodeller kan bidra till att uppmärksamma avvikande samband. Men den värdefulla frågan är inte hur många AI-verktyg myndigheten kan införa. Den är vilka arbetsmoment där en väl avgränsad användning skapar dokumenterbar nytta utan att sänka kvalitet, rättssäkerhet eller skyddet för information.

Föreställ dig en handläggare som får ett automatiskt genererat förslag till sammanfattning av dokument från flera källor. Om sammanfattningen är korrekt kan den spara tid. Om den missar en tidsangivelse, sammanblandar två aktörer eller lägger till ett obelagt påstående kan samma verktyg skapa nya risker. Därför bör ett sådant stöd utformas så att användaren kan spåra centrala slutsatser tillbaka till källmaterialet och så att dess begränsningar är kända. Förslagets roll i beslutsprocessen måste vara tydlig.

En andra risk är att uppmärksamheten koncentreras på modellen medan den omgivande informationshanteringen lämnas oförändrad. Då kan verksamheten få en kraftfull analysfunktion ovanpå fragmenterade begreppsmodeller, otillräckliga metadata och otydliga rättigheter. AI mognar inte isolerat; den är beroende av myndighetens förmåga att veta vad en uppgift betyder, varifrån den kommer och hur den får användas.

## Säkerhet och beredskap som verksamhetsegenskaper

Digitala tjänster är ofta så centrala att tillgänglighetsavbrott direkt påverkar myndighetens möjlighet att utföra sitt uppdrag. Det kan gälla mottagning av information från företag, operativa kontroller, samverkan mellan länder eller tillgång till tidigare beslut. En beredskapsplan som enbart beskriver återstart av servrar fångar inte alltid vad som krävs för att verksamheten ska fungera.

En verksamhetsorienterad analys börjar i stället med frågor om vilka tjänster som måste fortsätta fungera, hur länge de kan vara otillgängliga och vilka manuella eller alternativa arbetssätt som är tillåtna. Därifrån kan krav härledas till kommunikation, datalagring, lokala stöd, externa integrationer och människor med nödvändig kompetens. Detta är också en anledning att samordna cybersäkerhetsarbete med kontinuitets- och beredskapsplanering.

eSam beskriver i sin februaribild skärpta krav på cybersäkerhet och incidentrapportering. [K001] Här måste boken konsekvent skilja på att ett regelverk finns, vilka verksamheter som omfattas och hur tillsyn, rapportering och andra skyldigheter gäller för den aktuella organisationen. En generell myndighetsprofil ger inte i sig ett tillräckligt rättsligt svar.

## Digital identitet är också frågan om att företräda någon

En offentlig tjänst behöver ofta veta mer än vem en person är. Den behöver avgöra om personen har rätt att lämna uppgifter, företräda ett företag, ta emot ett beslut eller utföra en viss åtgärd. Det är en skillnad mellan **identifiering** (vem är du?), **autentisering** (kan du visa att du är den du utger dig för att vara?) och **auktorisation** (vad får du göra i denna situation?).

I ett internationellt flöde tillkommer frågor om erkännande av elektroniska identiteter, behörighetsunderlag och hur ändringar får genomslag. En person kan ha haft behörighet när ett ärende påbörjades men förlorat den innan ett bindande steg ska utföras. En arkitektur som bara kontrollerar behörighet vid första inloggningen kan då vara otillräcklig.

Den utveckling mot digitala behörighetshandlingar och mer federerad identitetshantering som eSam tar upp [K001] kan få betydande praktisk nytta. Samtidigt ökar kraven på att ansvar, tillit, uppdatering av behörigheter och spårbarhet hanteras mellan organisationer. För verksamheten är detta inte ett sidospår inom inloggningsteknik utan en central del av rättssäkra digitala processer.

## Datadelning kräver gemensam mening

Två myndigheter kan tekniskt dela ett informationsfält utan att mena samma sak med det. En status kan beskriva ett pågående ärende hos den ena aktören men ett avslutat moment hos den andra. En identifierare kan avse ett juridiskt företag, en fysisk anläggning eller ett enskilt tillstånd. Denna typ av skillnader är svåra att upptäcka när ett datautbyte endast beskrivs som en överföring mellan API:er.

Hållbar interoperabilitet omfattar därför minst juridiska, organisatoriska, semantiska och tekniska dimensioner. Den juridiska dimensionen gäller möjligheten och villkoren att dela och använda uppgifter. Den organisatoriska gäller ansvar, roller, rutiner och överenskommelser. Den semantiska gäller gemensam förståelse av innehållet. Den tekniska gäller exempelvis protokoll, format, säker anslutning och tillgänglighet.

För en kontroll- och flödesorienterad myndighet blir konsekvensen konkret: värdet av ett nytt datagränssnitt avgörs inte enbart av hur snabbt det kan leverera uppgifter. Värdet avgörs av om verksamheten kan tolka dem korrekt, bedöma tillförlitligheten, följa deras ursprung och använda dem lagligt. Denna insikt är central för kommande kapitel om informationsarkitektur och internationellt utbyte.

## Verksamhetsfall: från ny EU-signal till förändrad kontrollkedja

*Följande scenario är fiktivt och beskriver inte en viss myndighets pågående verksamhet.*

En myndighet får information om ett planerat europeiskt initiativ som kan förändra vilka transportrelaterade uppgifter som görs tillgängliga för offentliga aktörer. Den första reaktionen är att undersöka möjligheten att bygga ett nytt gränssnitt. Verksamhetsanalysen visar emellertid att frågan är bredare. Nya data kan påverka hur företag lämnar uppgifter, hur riskindikatorer beräknas, hur kontroller väljs ut och hur genomförda åtgärder återkopplas till internationella samarbetspartner.

Arbetsgruppen kartlägger fem möjliga förändringar. **För det första** behöver verksamheten fastställa vilka beslut den nya informationen faktiskt ska stödja. **För det andra** måste rättsliga förutsättningar och sekretessfrågor analyseras innan data tas i bruk. **För det tredje** behöver informationsarkitekter definiera betydelsen av nya fält och relationer till befintliga begrepp. **För det fjärde** behöver säkerhets- och kontinuitetsansvariga undersöka vad som händer om leveransen blir felaktig eller otillgänglig. **För det femte** måste utvecklingsportföljen väga nyttan mot kostnaderna för anpassning av processer, system och kompetens.

Resultatet blir inte enbart ett integrationsprojekt. Det blir ett beslutsunderlag för en utvecklad verksamhetsförmåga, med flera möjliga genomförandevägar. Kanske ska myndigheten först förbättra datakvaliteten i befintliga processer. Kanske krävs gemensamt arbete med andra aktörer. Kanske är den mest angelägna åtgärden att utveckla kontrollpersonalens tillgång till kvalitetssäkrad information i rätt ögonblick.

Scenariot visar skillnaden mellan att *reagera på en omvärldssignal* och att *omsätta den i en verifierbar förmågeförändring*.

## Frågor som följer av omvärldsläget

Den sammanfallande utvecklingen gör tre frågor särskilt angelägna: vilka informations- och leverantörsberoenden är kritiska, vilka nya rättsliga villkor förändrar verksamhetens handlingsutrymme och var behöver samarbete med andra aktörer fördjupas? Svaren skiljer sig mellan myndighetens olika uppgifter. Det viktiga i detta inledande kapitel är att identifiera drivkrafterna; hur de omsätts i prioriterade initiativ behandlas i kapitel 3 och 16.

## Från nuläge till förändringsförmåga

Omvärldsbilden får betydelse först när den jämförs med myndighetens faktiska förutsättningar: beroenden som kan fallera, uppgifter som behöver tolkas gemensamt och arbetsmoment där förändringen skapar både nytta och risk. Kapitel 2 fördjupar uppdragets särskilda villkor. Kapitel 3 beskriver hur sådana iakttagelser kan bli användbara beslutsunderlag.

## Sammanfattning: en ny helhetssyn

Den digitala omställningens nya förutsättningar kännetecknas av att teknik, rättsliga krav, internationellt beroende och samhällssäkerhet allt mindre kan hanteras var för sig. eSams radarbild från februari 2026 illustrerar detta genom sina fyra sammanflätade områden. [K001] För en myndighet med gränsöverskridande informationsflöden och kontrolluppgifter blir de strategiska konsekvenserna särskilt tydliga: information måste kunna användas ansvarsfullt, beslut kunna förklaras, digitala tjänster fungera under störningar och samverkan ske på en gemensam grund.

Den viktigaste omställningen är därför organisatorisk och styrningsmässig lika mycket som teknisk. Framtidens kapacitet byggs inte bara genom nya system, utan genom förmågan att samordna uppdrag, data, människor, rättsliga ramar och teknik. Nästa kapitel går närmare in på vad detta innebär för en myndighet som både möjliggör samhällsflöden och utövar kontroll.
