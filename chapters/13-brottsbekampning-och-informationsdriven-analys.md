# 13. Brottsbekämpning och informationsdriven analys

En till synes vardaglig avvikelse i ett handelsflöde får sällan en entydig förklaring. En oriktig uppgift kan bero på ett misstag, otydliga instruktioner eller medvetet vilseledande. Flera avvikelser som var för sig framstår som obetydliga kan däremot tillsammans väcka en berättigad fråga. För myndigheter med både administrativt kontrolluppdrag och brottsbekämpande uppgifter uppstår därför ett särskilt problem: hur kan stora och fragmenterade informationsmängder bidra till att upptäcka brottslighet utan att osäker analys omvandlas till obefogade misstankar?

Svaret är inte enbart mer data eller mer avancerad teknik. Det krävs också laglig informationshantering, professionell analytisk metod, rättssäker dokumentation, fungerande samverkan och en tydlig gräns mellan hypotes, underrättelseuppgift och faktiskt belagd omständighet. Detta kapitel analyserar sambanden, med utgångspunkt i digitaliseringsfrågorna i eSams radarbild från februari 2026 och med särskilt fokus på en myndighet som arbetar nära internationell handel, kontrollverksamhet och gränsöverskridande flöden.

## Brottsbekämpning är inte samma sak som administrativ kontroll

En myndighet kan utföra flera uppgifter inom samma övergripande verksamhetsområde: ge service och fatta tillståndsbeslut, säkerställa korrekta avgifter, göra riskbaserade kontroller och – när särskilda befogenheter finns – förebygga, upptäcka eller utreda brott. Dessa uppgifter kan använda näraliggande information men omfattas inte alltid av samma rättsliga regler.

En uppgift som samlats in för att handlägga ett administrativt ärende är inte automatiskt tillgänglig för varje brottsbekämpande ändamål. Att ett datasystem tekniskt kan sammanföra uppgifter innebär inte att en viss sammanföring är rättsligt tillåten. Myndigheten behöver analysera ändamålet, behandlingsgrunden, sekretessreglerna, speciallagstiftningen och befogenheterna för varje tänkt informationsflöde. Brottsdatalagen (2018:1177) genomför EU:s dataskyddsdirektiv för brottsbekämpande verksamhet och innehåller bland annat krav på rättslig grund, angivna ändamål, korrekthet och säker behandling. Vilket regelverk som blir tillämpligt beror på verksamheten och behandlingen, inte bara organisationens namn. [K037][K038]

Det är därför ändamålsenligt att i arkitekturen skilja mellan administrativ information, kontrollunderlag, underrättelseinformation och material som har tillförts en brottsutredning. Skillnaden behöver synas i åtkomst, metadata, gallrings- och bevarandebedömningar, loggning och informationsutlämnande.

## Från signal till underrättelse – en kedja av prövningar

Informationsdriven analys kan beskrivas som en process med sex steg:

1. **Inhämtning:** information tas emot eller hämtas in inom ramen för rättsliga befogenheter och ett dokumenterat ändamål.
2. **Kvalitetssäkring:** identifierare, tidsangivelser, ursprung, fullständighet och kända felkällor bedöms.
3. **Bearbetning:** uppgifter struktureras och jämförs, exempelvis i tidslinjer, nätverksbilder eller mönsteröversikter.
4. **Analys:** hypoteser prövas mot både stödjande och motsägande information, med bedömning av osäkerhet.
5. **Åtgärdsförslag:** analyserade resultat kan bidra till prioriteringar eller fortsatta åtgärder där mandat och proportionalitet prövas separat.
6. **Återkoppling:** utfallen återförs till metoderna så att felaktiga antaganden, missvisande indikatorer och informationsluckor kan upptäckas.

Det sista steget är avgörande. Om myndigheten bara samlar återkoppling från ärenden som redan valts ut för kontroll riskerar den att träna analysmetoder på sina egna tidigare prioriteringar. En ökad andel träffar är heller inte nödvändigtvis ett mått på att mer brottslighet upptäcks; urvalets sammansättning och kontrollresurserna kan ha förändrats.

En robust analysprocess behöver därför också redovisa vad som inte är känt. Avsaknad av information kan bero på att uppgifter inte finns, inte får behandlas, inte har delats, ännu inte har inkommit eller har registrerats under annan identitet. Dessa situationer bör inte kodas som samma typ av tomt värde.

## Informationskällor, proveniens och kvalitet

En brottsbekämpande analys kan innehålla många slags information: strukturerade uppgifter från ärenden och anmälningar, dokument, resultat från fysiska kontroller, verksamhetsobservationer och lagligen erhållna uppgifter från andra myndigheter eller internationella aktörer. Vart och ett av dessa informationsslag har sin egen tillkomsthistoria och sin egen osäkerhet.

**Informationsproveniens** – uppgiftens ursprung och bearbetningshistoria – gör det möjligt att förstå vem som lämnade den, när den gällde, när myndigheten fick den och om den senare har kompletterats eller rättats. I en miljö med både administrativa och brottsbekämpande ändamål behöver proveniensen även beskriva eventuella begränsningar för fortsatt användning eller utlämnande.

En särskild kvalitetsutmaning gäller kopplingen mellan identiteter. Företag kan företrädas av olika ombud; varor kan passera genom flera transportled; olika system kan använda egna referensnummer. En teknisk träff mellan två namn eller adresser är inte liktydig med att de avser samma person eller samma händelse. För samband bör det därför finnas uppgift om metod, styrka, tidsmässig giltighet och mänsklig bekräftelse där sådan krävs.

Vid analys av personuppgifter är riktighet ett uttryckligt rättsligt krav. Inom brottsdataskyddet har även åtskillnaden mellan olika kategorier av registrerade och mellan faktiska uppgifter och personliga bedömningar betydelse. En analysplattform bör därför kunna ange att ett påstående är obekräftat, att en identitetskoppling är preliminär eller att en uppgift har motsagts av senare material. [K037]

## Analysmetoder: vad tekniken kan och inte kan göra

En myndighet kan ha nytta av olika metoder som förstärker varandra. Regelbaserad analys kan fånga upp tydligt definierade avvikelser, som att obligatoriska uppgifter motsäger varandra. Statistisk analys kan upptäcka förändringar över tid och skillnader mellan grupper av händelser. Nätverksanalys kan synliggöra relationer mellan ärenden, aktörer och flöden. Textanalys kan strukturera stora mängder dokument, och kartbaserad visualisering kan göra tids- och platsmässiga samband lättare att undersöka.

Ingen metod skapar automatiskt bevis. En graf där två aktörer förekommer nära varandra visar en datamässig relation, inte nödvändigtvis ett rättsligt relevant samarbete. Ett högt statistiskt avvikelsevärde betyder inte att ett brott har begåtts. En språkmodell som genererar en sammanfattning kan introducera felaktiga samband eller lägga till detaljer som saknas i källan. Därför behöver analytikern se vad analysen bygger på och kunna gå tillbaka till materialets ursprung.

AI kan vara särskilt användbar för att hitta dokument som rör samma sak, föreslå möjliga dubbletter eller ge stöd i flerspråkiga material. Användningen blir mer riskfylld om den utan tydliga skyddsåtgärder börjar tillskriva personer brottsliga avsikter. AI-förordningen innehåller bland annat förbud mot vissa former av individuella riskbedömningar av brottslighet som enbart grundas på profilering eller personlighetsdrag; den rättsliga klassificeringen måste alltid utgå från det konkreta användningsfallet. [K014]

## Fiktivt scenario: en kedja av varuflöden

*Följande scenario är konstruerat för boken. Det beskriver inte en viss myndighets verkliga data, system, analysmetoder eller befogenheter.*

En analytiker ser ett antal ärenden med liknande dokumentuppgifter men olika registrerade transportörer. Ärendena har uppstått under flera månader. Några kontroller har visat administrativa avvikelser; i andra finns inga konstaterade fel. En analysplattform föreslår att vissa ärenden kan höra samman eftersom uppgifter om tid, dokumentreferenser och företrädare delvis sammanfaller.

Det första arbetsmomentet är att granska sambanden. Ett gemensamt ombud kan agera för många oberoende företag. En återanvänd referens kan bero på ett systemfel. En avvikande transportväg kan ha en fullt legitim förklaring. Analytikern antecknar därför både alternativa förklaringar och vilka uppgifter som behöver kontrolleras innan mönstret kan värderas.

I ett andra steg upptäcks att en serie dokument har samma tekniska fel, medan en annan serie har en annan bakomliggande förklaring. Den automatiska grupperingen måste delas upp. Endast den återstående delen ger skäl för fortsatt analys inom det tillämpliga uppdraget. Beslut om eventuell operativ kontroll tas separat av behörig funktion efter prövning av lagstöd, syfte och proportionalitet.

Om information senare delas med en annan behörig myndighet anges dess ursprung, osäkerhet och tillämpliga användningsbegränsningar. Mottagaren ska inte behöva tolka en maskinproducerad graf som en lista över fastställda gärningspersoner. Det som förmedlas är en kvalificerad analys med redovisade reservationer.

Scenariot visar tre värdefulla förmågor: teknik som hjälper till att identifiera möjliga samband, analytisk metod som prövar alternativa förklaringar och en styrd process där rättsliga befogenheter avgör vad som får ske därefter.

## Rättssäkerhet och skillnaden mellan underrättelse och bevis

En underrättelse kan ge anledning att närmare undersöka ett förhållande, men den har inte automatiskt samma funktion som bevisning i ett rättsligt förfarande. För analysen måste det därför vara tydligt om ett innehåll är en råuppgift, en analytisk slutsats, ett påstående från en extern källa eller en verifierad observation.

Om digitala analysresultat används i en senare utredning behöver metoden och materialets integritet kunna prövas. Det kan kräva möjlighet att rekonstruera den relevanta analysen, förstå vilka data och modellversioner som användes samt upptäcka om uppgifterna har ändrats. Detta är särskilt angeläget när automatiserade verktyg producerar sammanställningar som annars kan ge ett sken av större precision än underlaget motiverar.

Rättssäkerhet innebär också skydd mot att hypoteser fastnar som permanenta identitetsetiketter. Uppgifter behöver kunna rättas, kompletteras, avskiljas eller tas bort enligt tillämpliga regler. Begränsningar av insyn som motiveras av brottsbekämpande intressen får inte förväxlas med avsaknad av ansvar och dokumentation. [K037][K038]

## Internationellt informationsutbyte

Brottslighet kan organiseras över nationsgränser, medan myndigheters uppdrag är definierade i nationella och unionsrättsliga regelverk. Internationellt samarbete kräver därför både teknisk och rättslig interoperabilitet. Det kan omfatta säkra kommunikationskanaler, överenskomna informationsformat, tydliga kontaktpunkter, dokumenterad informationskvalitet och regler för utlämnande och vidareanvändning.

Det är viktigt att inte utgå från att varje internationell part har rätt till samma uppgifter. Reglerna kan skilja sig beroende på mottagare, rättslig grund, uppgiftstyp och om överföringen sker inom EU eller till ett tredjeland. Brottsdatalagens åttonde kapitel reglerar under särskilda förutsättningar överföring av personuppgifter till tredjeland och internationella organisationer. Där kan även användningsbegränsningar aktualiseras. [K037]

Europols regelverk är ett exempel på hur särskilda unionsrättsliga ramar styr informationsbehandling vid europeiskt brottsbekämpande samarbete, men det innebär inte att alla kontrollmyndigheter eller alla informationsflöden automatiskt omfattas av samma samverkanskanaler. Den rättsliga och organisatoriska kopplingen måste bedömas konkret. [K039]

En myndighet behöver därmed upprätta informationskontrakt där det inte bara står vilka fält som tekniskt kan överföras. De behöver även ange ändamål, mottagare, klassning, begreppsdefinitioner, användningsvillkor, uppgiftskvalitet och ansvar vid rättelser eller incidenter.

## Målarkitektur för informationsdriven brottsbekämpning

Ett hållbart arkitekturmönster kan delas in i fem funktionella lager:

**Käll- och åtkomstlager.** Källsystem hanterar sin information och dokumenterar juridiska samt tekniska åtkomstvillkor. Tillgänglig data är inte liktydigt med fritt återanvändbar data.

**Informations- och kvalitetslager.** Gemensamma begrepp, referenser, datakataloger och ursprungsmetadata gör information möjlig att tolka. Preliminära relationer behöver skiljas från verifierade identitetskopplingar.

**Analyslager.** Regler, statistiska modeller, grafanalys och textanalys används med versionshantering och mätbara kvalitetskrav. Analysresultat märks utifrån säkerhet och relevans.

**Verksamhets- och beslutsstöd.** Resultaten presenteras för behöriga användare i den process där de ska bedömas. Gränssnitt skiljer indikator, hypotes, bedömning och beslut åt.

**Kontroll- och revisionslager.** Loggning, åtkomstprövning, incidenthantering, testning och periodisk rättslig uppföljning möjliggör ansvar och omprövning. Integritet och behörighetskontroll gäller även utvecklings-, test- och analysmiljöer.

Arkitekturen bör möjliggöra separata informationsdomäner när verksamheten omfattas av olika ändamål och dataskyddsregimer. En central analysplattform får inte bli en genväg runt regelverken. Samtidigt kan standardiserade metoder, metadataformat och tekniska kontroller återanvändas mellan flera lagligt avgränsade tillämpningar.

## Styrning och kompetens

Informationsdriven analys kräver andra kompetenser än enbart datavetenskap. Jurister behöver kunna granska ändamål, åtkomst och befogenheter. Analytiker behöver förstå metodernas begränsningar och arbeta systematiskt med alternativa hypoteser. Informationsarkitekter behöver utforma identifierare, metadata och datakontrakt. Säkerhetsfunktioner behöver bedöma informationsskydd, och verksamhetsansvariga måste kunna värdera faktiska resultat och bieffekter.

En fungerande styrmodell bör innehålla en dokumenterad ansvarig för varje analysanvändning, ett register över informationskällor och ändamål, ett granskningsförfarande för nya modeller och informationskombinationer samt rutiner för avvikelsehantering. Användningen av känsliga analysstöd behöver regelbundet prövas mot både verksamhetsnytta och risken för felaktiga slutsatser.

Uppföljningen bör omfatta mer än hur många indikatorer som har genererats. Exempel på relevanta frågor är hur ofta en hypotes har kunnat verifieras, hur många felkopplingar som upptäckts, hur lång tid det tar att korrigera missvisande information och om analysen faktiskt bidrar till bättre prioriteringar inom lagens ram.

## Från analysresultat till ansvarsfull användning

Ett samband får inte ges större bevisvärde än underlaget medger. Det måste vara möjligt att granska alternativa förklaringar, informationskällor och behandlingsändamål. Frågorna om vilka organisatoriska förmågor som behöver prioriteras återkommer i bokens strategiska slutkapitel.

## Sammanfattning

Informationsdriven brottsbekämpning kan förbättra möjligheten att identifiera relevanta samband i stora informationsmängder och stödja samarbete över organisatoriska och nationella gränser. Men teknisk kapacitet är inte likvärdig med rättslig befogenhet, och statistiska samband är inte samma sak som bevis.

För den samhällsviktiga myndigheten ligger den långsiktiga utvecklingsmöjligheten i en spårbar kedja från lagligt inhämtade uppgifter och tydlig ändamålsstyrning till kvalificerad analys, mänsklig prövning, avgränsade åtgärder och systematisk lärande. Detta gör det möjligt att kombinera effektiv brottsbekämpning med förutsebarhet, proportionalitet och respekt för grundläggande rättigheter.
