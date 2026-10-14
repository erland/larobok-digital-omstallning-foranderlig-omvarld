# 5. AI, rättssäkerhet och mänsklig kontroll

När en analytiker får ett förslag om att en försändelse bör granskas närmare kan resultatet framstå som precist: en risknivå, några indikatorer och ett kort motiverande stycke. Men bakom ett sådant resultat ligger flera val. Vilka uppgifter har använts? Vilka tidigare utfall har modellen tränats på? Vad betyder risknivån? Och framför allt: vem bär ansvaret när analysen får konsekvenser för en enskild person eller ett företag?

Kapitel 4 beskrev AI:s användningsområden och nyttopotential. Här står de rättsliga gränserna och ansvarsförhållandena i centrum. En verksamhet som utövar offentlig makt behöver kunna visa att en åtgärd är laglig, saklig och proportionerlig även när en modell har medverkat. Tekniken kan förändra hur underlag skapas, men inte avskaffa kraven på myndighetens ansvar.

## Rättssäkerhet är en egenskap hos hela arbetsprocessen

Rättssäker AI kräver att kedjan från underlag till prövning, beslut och möjlighet till rättelse kan kontrolleras. Modellen är bara en del av denna kedja.

I en verksamhet med kontroll-, tillsyns- eller brottsbekämpande uppgifter kan konsekvenserna vara betydande även före ett formellt beslut. Ett riskurval kan medföra fördjupad dokumentkontroll, försening eller en mer ingripande undersökning. Myndigheten måste därför skilja mellan ett statistiskt resultat, en misstanke som kräver saklig prövning och ett rättsligt ställningstagande. Dessa begrepp får inte smälta samman i ett användargränssnitt.

Legalitet innebär att myndighetens åtgärder måste ha stöd i rättsordningen. Objektivitet kräver saklighet och opartiskhet. Proportionalitet kräver att en åtgärd inte går längre än vad som behövs i förhållande till sitt ändamål. Dessa krav gäller oavsett om underlaget har sammanställts manuellt, med fasta regler eller genom maskininlärning. [K013]

Ett återkommande misstag är att utvärdera AI-systemets prediktiva träffsäkerhet och samtidigt lämna själva myndighetsprocessens rättssäkerhet utanför bedömningen. Ett system kan vara relativt bra på att förutsäga ett visst utfall och ändå användas på ett rättsligt olämpligt sätt.

## AI-förordningen: klassificera användningen, inte myndigheten

EU:s AI-förordning använder en riskbaserad struktur. Vissa AI-praktiker är förbjudna. Vissa användningar omfattas av särskilda krav för högriskssystem. Andra kan omfattas av transparensregler eller allmänna skyldigheter. Huruvida ett system är ett högrisksystem beror bland annat på dess avsedda användning och förutsättningarna i bilaga III – inte på att organisationen i största allmänhet arbetar med kontroll eller brottsbekämpning. [K014]

För vissa användningar på områden som brottsbekämpning, migration och gränskontroll anger bilaga III särskilda kategorier. Ett dokumentstöd, ett logistiskt planeringsverktyg och ett individinriktat riskverktyg kan därmed få helt olika rättslig klassificering trots att de används inom samma organisation. Därtill finns uttryckliga förbud, bland annat mot vissa former av prediktiv brottsbedömning av individer som enbart grundas på profilering eller bedömning av personliga egenskaper. [K014]

I oktober 2026 gäller reglerna stegvis. EU-kommissionens genomgång, uppdaterad 6 oktober 2026, anger att bestämmelserna om vissa förbjudna användningar och transparenskrav redan tillämpas, medan högriskreglerna för system i bilaga III börjar tillämpas den 2 december 2027 och vissa produktanknutna högriskregler den 2 augusti 2028. Det är därför viktigt att dokumentera både vilka regler som redan gäller och vilka krav organisationen bör förbereda sig för. Övergångsbestämmelser för redan införda system och särskilda undantag måste bedömas separat. [K014][K015]

För högriskssystem innehåller förordningen bland annat krav på riskhantering, datahantering, teknisk dokumentation, loggning, transparens och mänsklig kontroll. Regler om leverantörers och användarorganisationers ansvar måste särskiljas. Ett inköpt AI-system befriar inte myndigheten från ansvar för den användning som sker i dess verksamhet. [K014]

## Vad mänsklig kontroll måste innebära

Mänsklig kontroll är inte detsamma som att ett system har en knapp märkt ”Godkänn”. Den ansvariga personen måste faktiskt kunna granska och vid behov ifrågasätta resultatet, förstå sitt mandat och använda en alternativ väg när modellen ger osäkra eller olämpliga förslag.

Meningsfull kontroll kräver fyra förutsättningar. För det första behöver handläggaren relevanta underlag och information om osäkerhet. För det andra krävs tid och kompetens att pröva uppgifterna. För det tredje måste det finnas faktisk befogenhet att avvika från modellens förslag. För det fjärde måste arbetsmiljön och uppföljningen inte ensidigt belöna att modellförslaget följs.

Mänskliga kontrollåtgärder måste anpassas till risknivån. För en intern sammanfattning kan stickprov och källkontroll vara tillräckligt. För ett ingripande där en person eller ett företag kan drabbas av påtagliga konsekvenser behöver granskningen vara betydligt mer omfattande, med kontroll av rättslig grund, kvalitet och proportionalitet.

Ett system bör dokumentera om användaren bekräftade, ändrade eller avvisade en rekommendation. Syftet är inte att tvinga fram en viss andel avslag utan att göra det möjligt att upptäcka mönster som tyder på antingen övertro eller återkommande systematiska fel.

## Automatiserade individuella beslut och dataskydd

Artikel 22 i GDPR begränsar, med angivna undantag och skyddsåtgärder, beslut som grundas enbart på automatiserad behandling och som har rättsliga eller liknande betydande följder för en registrerad. IMY betonar att det är själva beslutsfattandet som ska prövas. Ett AI-stöd följt av en verklig mänsklig bedömning är som utgångspunkt inte ett sådant helt automatiserat beslut. En person som endast formellt fastställer ett AI-resultat utan verklig prövning kan däremot innebära att skyddet kring automatiserade beslut aktualiseras. [K016]

Detta är inte en generell beskrivning av alla myndighetsbeslut. Förvaltningsrättsliga regler, specialförfattningar och särskilda dataskyddsregimer kan vara avgörande. Vid personuppgiftsbehandling för brottsbekämpande ändamål kan brottsdatalagstiftningen vara tillämplig i stället för GDPR. Varje tillämpning måste därför identifiera vilka rättsregler som faktiskt gäller. [K017]

Integritetsskyddet omfattar även ändamålsbegränsning, uppgiftsminimering, riktighet, lagring, behörighetsstyrning och bedömning av risker. Det måste bedömas om uppgifter som samlats in för ett ändamål får användas för modellträning eller vidare analys. Tillgång till uppgifterna i ett myndighetssystem är inte automatiskt rätt att använda dem för alla nya AI-ändamål.

## Förklarbarhet, motivering och transparens

Förklarbarhet kan betyda flera saker. En tekniker kan behöva förstå modellens beteende. En verksamhetsansvarig behöver veta när modellen fungerar sämre. En handläggare måste kunna se vilka sakuppgifter och regler som är relevanta. Den som berörs av en åtgärd kan behöva en begriplig motivering och möjlighet att tillvarata sina rättigheter.

Det innebär inte alltid att modellens interna matematiska parametrar måste offentliggöras. En praktiskt användbar förklaring bör i stället visa vilka konkreta omständigheter som haft betydelse för det faktiska ärendet, vilket utrymme för mänsklig prövning som funnits och hur uppgifter kan rättas eller resultat angripas. Det som rättsligt får eller ska lämnas ut avgörs av de tillämpliga reglerna, inklusive sekretessbestämmelser. [K016]

Myndigheten bör skilja mellan **spårbarhet** – att i efterhand rekonstruera behandlingen – och **begriplighet** – att kunna beskriva varför ett visst steg togs. Båda behövs. En fullständig teknisk logg är inte i sig en god begriplig motivering, medan en välskriven motivering kan dölja bristande spårbarhet.

## Snedvridning och diskriminerande effekter

Maskininlärning tränas ofta på historiska data. Dessa återspeglar inte nödvändigtvis hela verkligheten, utan också vad verksamheten tidigare valt att undersöka. Om särskilda aktörer oftare har kontrollerats kan modellen lära sig kontrollhistoriken snarare än faktisk risk.

Det betyder att datakvalitet inte bara handlar om korrekta fält. Det handlar även om representativitet, bortfall, ändrade förutsättningar och om möjligheten att upptäcka fel på grupper som sällan finns representerade i träningsdata.

En ansvarstagande verksamhet följer därför upp felaktiga positiva och negativa utfall, analyserar om till synes neutrala variabler fungerar som olämpliga indirekta markörer och kontrollerar om modellerna påverkas av förändringar i omvärlden. Sådana analyser måste utformas inom ramen för gällande rätt och regler om känsliga personuppgifter.

## Fiktivt scenario: en prioriterad kontroll

En myndighet tar emot elektroniska uppgifter om gränsöverskridande varuflöden. Ett AI-baserat riskstöd identifierar avvikelser mellan handlingar, historiska mönster och uppgifter från flera aktörer. Ett ärende hamnar högt på en lista för kontroll.

I den första utformningen ser handläggaren bara ett riskscore och en färgad signal. Ett kontrollbeslut riskerar då att uppfattas som en följd av modellens bedömning utan självständig prövning. Ansvarsfördelningen blir otydlig.

Efter omarbetning visar systemet i stället de kontrollerbara sakomständigheterna, vilka uppgifter som är osäkra och vilket underlag som inte kunnat verifieras. Handläggaren kan välja fortsatt dokumentgranskning, begära komplettering, avstå från åtgärd eller – när lagstöd och proportionalitet medger det – föreslå en fysisk kontroll. Den valda åtgärdens grunder dokumenteras separat från modellens rekommendation.

Ett senare kvalitetstest visar att ett visst dokumentformat ibland feltolkas. Myndigheten kan då hitta berörda ärenden genom versions- och händelseloggar, stoppa den aktuella komponenten och rätta processen. Det är denna kombination av kontrollbar teknik och organiserad ansvarighet som gör användningen mer robust.

*Scenariot är konstruerat för boken. Det beskriver inte en viss myndighets faktiska system, befogenheter eller rutiner.*

## Ansvarsfördelning genom hela livscykeln

Ansvaret behöver fördelas innan införandet. Verksamhetsägaren svarar för ändamål, nytta och användningssätt. Juridisk kompetens bedömer lagstöd, rättigheter och rättsliga begränsningar. Informationsägare och dataskyddsfunktion bedömer uppgifter och skyddsåtgärder. Säkerhetsfunktionen hanterar hot och driftsrisker. Teknik- och arkitekturfunktioner säkerställer spårbarhet, testbarhet, versionering och förvaltning.

För varje betydande AI-användning bör det finnas ett dokumenterat beslut som anger:

- Avsett ändamål och uttryckliga icke-tillåtna användningar.
- Informationskällor, rättslig grund och datakvalitetskrav.
- AI-rättslig klassificering och eventuella sektorsregler.
- Mänskliga kontroller och ansvar för beslut eller åtgärder.
- Metoder för test, mätning och återkommande granskning.
- Loggning, incidenthantering och möjlighet att stänga av stödet.
- Information till berörda och hantering av rättelse eller klagomål.

Ett sådant beslut är inte en engångsblankett. När modellversioner, dataflöden, målgrupper eller arbetsprocesser ändras behöver relevanta delar omprövas.

## En praktisk granskningsmodell

Ett genomförbart styrsystem kan organiseras i fem steg.

**1. Förhandsbedömning.** Fastställ vilket verksamhetsproblem som ska lösas, vilka åtgärder AI kan påverka och vilka som kan beröras negativt.

**2. Rättslig och etisk prövning.** Klassificera AI-användningen och identifiera relevant dataskydd, sektorsrätt, sekretess och grundläggande principer.

**3. Kontrollerad utvärdering.** Testa mot representativa och svåra fall, mät både nytta och oönskade konsekvenser, och dokumentera kända begränsningar.

**4. Införande med mänskligt ansvar.** Utbilda medarbetare, inför granskningsstöd, spårbarhet och tydliga stoppmekanismer.

**5. Löpande uppföljning.** Granska felutfall, verksamhetsförändringar, incidenter och rättsliga förändringar. Återkalla eller ändra användningen när förutsättningarna inte längre håller.

Modellen är ett stöd för dokumenterad prövning, inte ett generellt godkännande.

## Sammanfattning

Rättssäker AI är i grunden en fråga om myndighetsansvar. Modeller kan stödja bearbetning, analys och prioritering, men de får inte göra det oklart vem som prövar sakförhållanden, använder befogenheter eller svarar för en åtgärd.

Särskilt för verksamheter som kombinerar service med kontroll och ingripanden är det avgörande att separera information, riskindikator och rättsligt ställningstagande. Spårbarhet, meningsfull mänsklig granskning, dataskydd, förklarbarhet och fortlöpande uppföljning behöver därför byggas in i hela arbetsprocessen.

Nästa kapitel behandlar den information som AI och andra digitala tjänster är beroende av: data som strategisk tillgång, informationskvalitet och styrning.
