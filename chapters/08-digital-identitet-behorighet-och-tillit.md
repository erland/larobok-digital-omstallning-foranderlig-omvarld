# 8. Digital identitet, behörighet och tillit

En person loggar in med en giltig e-legitimation för att lämna uppgifter åt ett företag. Identiteten är verifierad, men en central fråga återstår: får personen agera för företaget, i just detta ärende och vid denna tidpunkt? När ärendet därefter går vidare till en annan myndighet, kanske i ett annat land, tillkommer ytterligare frågor. Kan mottagaren bedöma att identitetsuppgifterna är tillförlitliga? Kan ett elektroniskt intyg kontrolleras? Och kan en tidigare fullmakt ha upphört att gälla?

Detta är utgångspunkten för kapitlet. Digital identitet är inte liktydigt med behörighet, och en lyckad inloggning innebär inte automatiskt att en begärd åtgärd är tillåten. För en myndighet med internationella informationsflöden, företagstjänster och kontrolluppgifter behöver flera former av tillit samverka: till identiteten, till uppgiftens utfärdare, till representationsrätten och till själva transaktionen.

## Från inloggning till tillitskedja

I en enkel digital tjänst kan identitetsfrågan framstå som binär: användaren är antingen inloggad eller inte. I en komplex myndighetsprocess består den av separata kontroller.

**Identifiering** avser vilka uppgifter som knyts till en fysisk person, juridisk person eller teknisk aktör. **Autentisering** handlar om att kontrollera att en aktör vid ett visst tillfälle kan visa att den hör samman med en identifierad identitet. **Auktorisation** avgör vilka åtgärder den autentiserade aktören får utföra. **Representation** rör rätten att handla för någon annan. **Tillitsnivå** beskriver säkerhets- och tillförlitlighetskrav på identitets- och autentiseringslösningen.

Distinktionerna är praktiska. En tjänst kan vara säker på att en viss person loggat in men ändå sakna tillförlitligt underlag för att personen får signera en ansökan för ett bolag. Ett företags organisationsidentitet kan vara känd samtidigt som det är oklart vilken individ som har rätt att lämna uppgifter. Ett maskinellt API-anrop kan vara tekniskt autentiserat utan att den bakomliggande organisationen har den rättsliga behörighet som den begärda informationsåtkomsten förutsätter.

Den relevanta arkitekturprincipen är därför att bygga **identitetskontroll, representationskontroll och verksamhetsbehörighet som åtskilda men samverkande förmågor**. En kombination av giltiga tekniska inloggningsuppgifter bör aldrig betraktas som självständigt lagstöd för en viss behandling eller åtgärd.

## Det europeiska ramverket: reviderade eIDAS

EU:s förordning om elektronisk identifiering och betrodda tjänster, eIDAS, har ändrats genom förordning (EU) 2024/1183. Regelverket etablerar ett europeiskt ramverk för digital identitet där digitala identitetsplånböcker ska kunna användas över medlemsstatsgränserna. Plånböckerna är avsedda att ge användaren möjlighet att identifiera sig och presentera elektroniska intyg om egenskaper eller förhållanden, beroende på tillgängliga utfärdare och tjänster. [K020][K021]

En viktig förändring är att identitetsinformation och elektroniska attributsintyg kan presenteras på ett mer standardiserat sätt. Ett intyg kan exempelvis avse en viss yrkesroll, kompetens eller annan egenskap. Men **ett verifierbart attribut är inte nödvändigtvis en giltig fullmakt**. Om någon visar upp ett elektroniskt intyg om sin roll på ett företag återstår att avgöra om rollen ger rätt att utföra den specifika handlingen.

Plånböckerna ska fungera tillsammans med förlitande parter som begär och kontrollerar uppgifter. Mottagande myndigheter behöver därför förstå sin egen roll som förlitande part, vilka attribut som får efterfrågas, hur intygen valideras och hur personuppgifter minimeras. Förordningens bestämmelser och kompletterande genomförandeakter behöver tillämpas tillsammans; tekniska specifikationer är inte ett undantag från nationella befogenhets- eller sekretessregler. [K020][K022]

### Sverige: en stegvis utveckling

Enligt Diggs publicerade tidplan, uppdaterad den 30 september 2026, ska den första versionen av den statliga digitala identitetsplånboken lanseras i testmiljö i december 2026. En bredare användning planeras under 2027, en certifieringsredo plånbok under 2028 och en certifierad europeisk digital identitetsplånbok senast 2029. Det är **planerade milstolpar**, inte en beskrivning av funktionalitet som redan finns tillgänglig i oktober 2026. [K023]

Tidplanen visar varför en myndighet inte bör dimensionera sina integrationsprojekt enbart efter när den svenska statliga plånboken blir färdig. En europeisk tjänst kan möta plånböcker utfärdade av andra medlemsstater tidigare. Samtidigt måste en myndighet under en övergångsperiod kunna hantera befintliga svenska e-legitimationer, andra europeiska identifieringslösningar och användare med skilda möjligheter till digital identifikation.

Den statliga e-legitimationen Sverige-id är en närliggande men separat komponent. Digg meddelade i april 2026 att Sverige-id godkänts enligt myndighetens tillitsramverk på nivå 4. Att en lösning uppfyller en hög tillitsnivå förändrar inte i sig reglerna för vem som får företräda ett företag eller ta del av en viss uppgift. [K024]

## Företag, ombud och digitala fullmakter

Många offentliga tjänster riktar sig formellt till en juridisk person men används av en fysisk person. Det kan vara en anställd, firmatecknare, extern konsult, deklarationsombud eller transportör. Aktören kan dessutom företräda flera företag och ha olika behörigheter för olika uppgifter.

I praktiken kan representationskedjan bestå av flera led: företaget ger ett ombud ett avgränsat uppdrag; ombudsföretaget utser en medarbetare; medarbetaren identifierar sig digitalt; tjänsten kontrollerar att det aktuella uppdraget tillåter just den begärda transaktionen. En lösning som bara känner igen medarbetaren som användare riskerar att förbise att kunduppdraget upphört, att uppdraget enbart gällde en viss ärendetyp eller att befogenheten inte får vidaredelegeras.

En robust modell för digitala fullmakter bör kunna beskriva **fullmaktsgivare, fullmaktstagare, omfattning, giltighetstid, eventuell delegeringsrätt, återkallelse och verifierbart ursprung**. Modellen behöver även hantera hur ett uppdrag kan begränsas till en viss roll, ett visst informationsslag eller en viss verksamhetshändelse.

Här uppstår en viktig avvägning: rättsliga relationsförhållanden ska inte förenklas så långt att de blir felaktiga bara för att en behörighetsmotor behöver ett ja-eller-nej-svar. Vid osäkerhet behöver arbetsprocessen kunna begära kompletterande underlag eller lämna frågan till manuell prövning.

## Federerad identitet och behörighet

Federation innebär att flera organisationer kan använda gemensamma tillits- och utbytesmekanismer utan att varje organisation behöver skapa ett helt eget identitetssystem för alla externa användare. I en federerad lösning kan autentiseringen ske hos en betrodd part, medan den mottagande myndigheten fattar sitt eget beslut om tillträde och behörighet.

Federation är emellertid inte samma sak som gemensamma verksamhetsregler. Myndigheter kan enas om tekniska format för autentiseringspåståenden, men de måste ändå avgöra vilka roller och uppdrag som har rättslig och verksamhetsmässig betydelse i den egna tjänsten. När en utländsk organisation skickar uppgifter om en användares roll kan rollen behöva mappas till ett lokalt behörighetsbegrepp – med dokumenterade regler och undantag.

Detta gäller också maskin-till-maskin-kommunikation. Ett systemcertifikat, en teknisk klientidentitet eller en åtkomsttoken styrker bara den egenskap som tillitsmodellen faktiskt omfattar. Tekniska API-behörigheter behöver kopplas till organisationens uppdrag, informationsklass och ändamål. Åtkomst ska dessutom begränsas och kunna återkallas även när en integration annars fungerar korrekt.

## Behörighet som en tidsbunden verksamhetsregel

Många behörighetsproblem uppstår därför att uppgifter om representation och roller ändras snabbare än lokala kopior hinner uppdateras. En anställning upphör. Ett avtal sägs upp. Ett ombud får ett nytt uppdrag. Ett företag byter företrädare. Samtidigt kan ett redan inlett ärende behöva bevaras med uppgifter om vem som hade rätt att agera vid en tidigare tidpunkt.

En myndighet behöver därför skilja mellan **aktuell behörighet** och **historiskt giltig behörighet**. Den första avgör om en åtgärd får utföras nu. Den andra förklarar varför en tidigare åtgärd var tillåten när den gjordes. För tillståndsbeslut, avgiftsärenden och kontroller kan båda vara betydelsefulla.

Det innebär att en behörighetsarkitektur bör stödja kontroll mot auktoritativa register, kortlivade behörighetsuppgifter där det är lämpligt, registrering av relevanta beslutsgrunder och rutiner för att återkalla åtkomst. Det behövs också en tydlig fördelning mellan den som utfärdar behörighetsuppgiften och den myndighet som ansvarar för att använda den rätt.

## Fiktivt scenario: ett ombud företräder tre företag

Ett företag anlitar en extern tjänsteleverantör för att lämna digitala uppgifter om varuflöden. Leverantörens handläggare sköter motsvarande rapportering för ytterligare två företag. Samtliga uppdrag använder en gemensam digital tjänst hos myndigheten.

När handläggaren loggar in styrker en erkänd identifieringslösning personens identitet. Därefter visar tjänsten vilka företag personen får företräda och inom vilka ärendetyper. För två företag finns aktuella fullmakter som tillåter registrering och ändring av uppgifter. För det tredje har fullmakten nyligen återkallats.

Ett mindre genomarbetat system skulle kunna ha kvar en lokal markering om att personen är ett godkänt ombud. Användaren skulle då riskera att få åtkomst till ett uppdrag som inte längre gäller. I den genomarbetade lösningen hämtas eller valideras relevant representationsinformation vid en bestämd kontrollpunkt. När den återkallade fullmakten upptäcks får användaren inte utföra den begärda åtgärden för det tredje företaget.

Samtidigt kan en granskare senare behöva fastställa att en tidigare inlämning var behörig. Systemet bevarar därför ett spårbart underlag om vilken identitet som användes, vilken representation som validerades, vilken transaktion som genomfördes och vilken tidpunkt bedömningen avsåg. Underlagen skyddas enligt gällande krav på sekretess, dataskydd och arkivhantering.

Scenariot belyser att tre skilda frågor måste besvaras: **Vem är användaren? Vem företräder användaren? Vad får användaren göra här och nu?** Ett lyckat identitetsutbyte besvarar i normalfallet bara den första.

*Scenariot är fiktivt och beskriver ingen särskild myndighets faktiska system eller regler för ombudsbehörighet.*

## Integritet, informationsminimering och säkerhet

Digital identitet berör ofta personuppgifter och kan dessutom avslöja känsliga verksamhetssamband: vem som företräder ett visst företag, vilka ärenden som hanteras och när ett visst uppdrag genomförts. Därför behövs rättslig grund, ändamålsbegränsning, behovsanpassad loggning och säker hantering av identitets- och attributsuppgifter.

Ett grundläggande designval är att en tjänst inte ska begära fler uppgifter än den behöver. Om ett visst behörighetsbeslut kan fattas genom ett verifierbart påstående om att ett uppdrag gäller behöver myndigheten inte alltid lagra hela dokumentet som ligger bakom. Samtidigt måste den dokumentation som faktiskt krävs för rättssäkerhet och efterhandskontroll bevaras. Det är en avvägning mellan uppgiftsminimering och spårbarhet, inte ett val mellan två absoluta principer.

Säkerheten omfattar hela kedjan från utfärdande till verifiering. Relevanta risker är bland annat kapade användarkonton, förlorade autentiseringsmedel, felaktigt utfärdade intyg, bristande spärrkontroller, komprometterade tekniska nycklar och manipulation av behörighetsuppgifter under överföring.

En myndighet bör planera för incidenter där en betrodd tjänst temporärt inte går att använda. För vissa ärenden kan detta innebära uppskjuten digital åtkomst. För tidskritiska kontroll- eller säkerhetsuppgifter kan en reglerad reservrutin behövas. Reservrutinen får dock inte innebära att centrala identitets- och behörighetskontroller tyst kopplas bort.

## Arkitektur för sammanhängande tillit

En långsiktigt användbar målarkitektur behöver åtminstone fem förmågor:

1. **Identitetsfederation.** Hantering av flera betrodda identifieringslösningar med dokumenterade tillitskrav och möjlighet till nya europeiska utfärdare.
2. **Verifiering av intyg.** Validering av utfärdare, teknisk integritet, giltighet och relevant status för presenterade attribut.
3. **Representations- och fullmaktskontroll.** Bedömning av uppdrag, delegeringar och återkallelser med hänsyn till juridiska och organisatoriska regler.
4. **Verksamhetsstyrd auktorisation.** Beslut om åtkomst och åtgärdsrätt utifrån ärende, roll, organisation, ändamål och aktuellt sammanhang.
5. **Revision och kontinuitet.** Spårbar dokumentation av relevanta kontroller, övervakning av tillitstjänster och säkra reservrutiner.

Komponenterna bör i möjligaste mån vara löst kopplade, så att en ny plånbokstyp eller ett nytt autentiseringsprotokoll inte tvingar fram ändringar i varje ärendesystems verksamhetsregler. Samtidigt måste gränssnitten mellan komponenterna innehålla tillräckligt med kontext för en korrekt behörighetsprövning.

En renodlad teknisk lösning kan därför inte ersätta begreppsarbete. Myndigheten behöver gemensamma definitioner av exempelvis företrädare, ombud, uppdragsgivare, teknisk aktör, behörighetsgrund och giltighetsperiod. Dessa begrepp bör kopplas till informationsmodellerna som behandlats i kapitel 6 och till datadelningsavtalen och integrationskontrakten i kapitel 7.

## Sammanfattning

Digital identitet är en nödvändig grund för många framtida myndighetstjänster, men den löser bara en del av tillitsfrågan. Myndigheter som arbetar med företag, externa ombud och internationell samverkan måste också veta vem som har rätt att företräda vem, i vilket sammanhang och vid vilken tidpunkt.

Den europeiska utvecklingen skapar bättre förutsättningar för verifierbara identitets- och attributuppgifter över gränserna. Det strategiska värdet uppstår först när dessa uppgifter kan användas i rättsligt hållbara och tekniskt robusta behörighetsprocesser. Nästa kapitel behandlar cybersäkerhet och skyddet av just dessa sammanhängande informations- och tillitskedjor.
