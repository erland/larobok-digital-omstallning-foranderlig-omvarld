# 7. Datadelning över organisatoriska och nationella gränser

En elektronisk uppgift om en försändelse kan uppstå hos ett företag, användas i ett transportflöde, ingå i en myndighets administrativa prövning och därefter behövas i ett annat lands kontrollverksamhet. Ändå är det inte självklart att uppgiften kan – eller får – föras vidare mellan dessa miljöer. Att dela data innebär mer än att koppla samman tekniska system. Det kräver gemensam förståelse, tydligt ändamål, rättsligt stöd, förtroende mellan parter och möjlighet att visa vad som hänt med uppgifterna.

Det föregående kapitlet behandlade informationen som en strategisk tillgång. Detta kapitel handlar om vad som händer när information ska användas utanför det system och den organisation där den först skapades. Perspektivet är en samhällsviktig myndighet med omfattande kontakter med företag, andra myndigheter och internationella samverkansparter. Exemplen är fiktiva och beskriver inte en viss myndighets arbetssätt.

## Ett digitalt ekosystem snarare än en samling integrationer

Ett traditionellt integrationsprojekt har ofta utgått från två system: ett sänder ett meddelande och ett annat tar emot det. I en digital förvaltning är informationsutbytet allt oftare ett ekosystem. En och samma uppgift kan behöva användas i flera verksamhetsprocesser och av aktörer med olika ansvar, lagstöd och tekniska förutsättningar.

Ett tillstånd utfärdat av en behörig aktör kan exempelvis behöva kontrolleras av en annan myndighet när en vara passerar en gräns. Företaget ska inte behöva återge samma redan verifierade information i varje kontakt, men mottagaren måste veta vad tillståndet avser, vem som utfärdade det, om det fortfarande gäller och vilken rättslig betydelse det har.

Den avgörande förmågan är därför inte enbart att *flytta uppgifter*, utan att skapa förutsättningar för att uppgifter används korrekt i ett nytt sammanhang. Detta innefattar minst fyra nivåer av interoperabilitet:

- **Rättslig:** finns stöd för att lämna ut, ta emot och använda informationen för det aktuella ändamålet?
- **Organisatorisk:** är ansvar, processer, servicenivåer och samverkansformer överenskomna?
- **Semantisk:** betyder begrepp, identiteter, statuskoder och informationsobjekt samma sak hos parterna?
- **Teknisk:** kan systemen faktiskt kommunicera säkert, pålitligt och med kontrollerade format?

EU:s förordning om ett interoperabelt Europa, förordning (EU) 2024/903, ska stärka interoperabiliteten i digitala offentliga tjänster över nationsgränserna och introducerar bland annat interoperabilitetsbedömningar för vissa förändringar av transeuropeiska digitala offentliga tjänster. Den ersätter inte sektorsspecifika regler om datatillgång eller sekretess. [K002]

## Från begäran till tillåten användning

En vanlig men riskabel förenkling är att likställa teknisk åtkomst med rätt att behandla information. Ett välskyddat API kan vara tekniskt säkert även om ett utlämnande i den enskilda situationen saknar rättsligt stöd. Omvänt kan en uppgift vara tillåten att lämna ut men ändå behöva skydd mot obehörig åtkomst och felaktig användning.

För varje etablerat informationsflöde behöver parterna bedöma åtminstone följande frågor:

1. **Varför?** Vilket konkret ändamål ska utbytet stödja, och vilken verksamhet har behovet?
2. **Vilka?** Vilka aktörer är uppgiftslämnare, mottagare, personuppgiftsansvariga eller andra relevanta roller?
3. **Vad?** Vilka uppgifter är nödvändiga, hur definieras de och vilka är särskilt skyddsvärda?
4. **På vilken grund?** Vilka bestämmelser tillåter eller kräver utlämnande och behandling, och gäller sekretess eller särskilda registerregler?
5. **Hur länge?** Vilka krav gäller för bevarande, gallring, loggning och rättelse?
6. **Hur kontrolleras det?** Hur hanteras identitet, behörighet, ändamålsbegränsning, revision och incidenter?

När informationsutbytet passerar nationsgränser räcker inte en generell hänvisning till GDPR eller till europeisk samverkan. EU-regler, nationell kompletteringslagstiftning, sekretess och verksamhetsspecifika behörigheter måste analyseras tillsammans. Särskilda regler gäller dessutom i delar av den brottsbekämpande verksamheten. En korrekt juridisk analys dokumenterar vilka typer av information och vilka behandlingar som faktiskt omfattas; den gör inte en svepande bedömning av hela systemets laglighet.

## Semantik: när samma ord betyder olika saker

En tekniskt korrekt överföring kan ändå ge ett felaktigt verksamhetsresultat. Begreppet ”aktör” kan exempelvis avse deklarant, varuägare eller transportansvarig. Kapitel 6 utvecklar informationsmodellerna; vid delning behöver avsändare och mottagare därför komma överens om **vilka definitioner och giltighetstider som faktiskt gäller vid gränssnittet**. Särskilt viktigt är att skilja en teknisk kvittens från en verifierad sakuppgift eller ett formellt beslut. Ett informationskontrakt behöver också ange hur ändrade kodverk, rättelser och versionsbyten förmedlas.

## API:er är kontrakt, inte bara teknik

Ett API ger en kontrollerad ingång till funktioner eller information. För att stödja långsiktig samverkan måste dess kontrakt beskriva mer än anropsadress och fältnamn. Det behövs också regler för behörighet, belastning, felhantering, ändringsmeddelanden och vad mottagaren får förvänta sig av uppgifterna.

Ett väldefinierat API kan exempelvis tillhandahålla en verifiering av om ett tillstånd gäller, i stället för att överföra hela tillståndshistoriken till alla anslutna system. En sådan ändamålsanpassning kan minska informationsspridning och förenkla regelefterlevnad. Men också själva frågan, svaret och loggarna kan avslöja skyddsvärd information. Därför måste dataminimering, behörighet och övervakning omfatta hela anropets livscykel.

För realtidskritiska kontrollflöden behövs dessutom beslut om svarstider och reservrutiner. Vad gör handläggaren om ett internationellt register inte är tillgängligt? Är det tillåtet att använda en tidigare verifierad uppgift, eller måste processen avbrytas? Svaret beror på vilken juridisk betydelse uppgiften har och vilken risk åtgärden innebär. Den tekniska arkitekturen behöver stödja just den verksamhetsbedömningen.

**Händelsedriven datadelning** kan komplettera frågebaserade API:er. När en status ändras skickas en händelse till behöriga mottagare. Då måste parterna hantera försenade, dubbla och felordnade händelser samt kunna skilja mellan faktisk statusförändring och korrigering av en tidigare felaktig uppgift. För känsliga kontrollkedjor är kvittenser och idempotens – att samma meddelande kan behandlas flera gånger utan oönskade bieffekter – särskilt viktiga.

## Europeiska och nationella infrastrukturer

Ena, Sveriges digitala infrastruktur, omfattar nationella byggblock och samverkansformer som syftar till säker och effektiv digital informationsförsörjning. Digg beskriver interoperabilitet och förutsättningar för datadelning som centrala delar av utvecklingen. Det innebär dock inte att alla myndighetsuppgifter automatiskt ska delas eller att en gemensam teknisk komponent är tillämplig på varje verksamhetsprocess. [K011]

Ett tydligt europeiskt exempel på tvärsektoriellt informationsutbyte är förordning (EU) 2022/2399 om EU:s gemensamma digitala miljö för en enda kontaktpunkt för tullområdet, *EU Single Window Environment for Customs*. Förordningen etablerar bland annat informationsutbyte mellan nationella miljöer och EU-system för vissa formaliteter som administreras av andra ansvariga myndigheter. Genom komponenten EU CSW-CERTEX kan uppgifter som behövs för kontroller av sådana formaliteter göras tillgängliga mellan systemen enligt förordningens villkor. [K019]

Principen är bredare än det specifika sakområdet: den som lämnar uppgifter för en gränsöverskridande process ska så långt regelverket och tekniken medger möta ett sammanhållet förfarande, medan myndigheterna behåller sitt ansvar för respektive prövning. Ett gemensamt gränssnitt är inte detsamma som en gemensam juridisk beslutskompetens.

Nationella och europeiska infrastrukturer behöver därför betraktas som lager med olika ansvar. En gemensam tjänst kan underlätta identifiering, meddelandeutbyte eller upptäckt av informationskällor, medan varje uppgiftsansvarig fortfarande behöver kunna redovisa riktighet, utlämnande och förvaltning för den information den ansvarar för.

## Fiktivt fall: ett intyg i tre länder

*Följande situation är konstruerad som analysfall och beskriver ingen viss myndighets befintliga informationsutbyte.*

Ett företag skickar varor mellan flera länder. Vissa produkter omfattas av krav på ett särskilt elektroniskt intyg. Intyget registreras i ett europeiskt system som ansvarig myndighet i ursprungslandet använder. Ett annat lands myndighet behöver kontrollera att intyget är giltigt när varorna ska föras vidare.

I ett äldre arbetsflöde lämnar företaget ett dokument som personalen granskar manuellt. Det finns risk för att en äldre kopia visas upp, att uppgifter skrivs av fel eller att ett intyg används utanför sin giltighet. I ett förbättrat arbetsflöde anger företaget en referens och den mottagande myndighetens system efterfrågar relevanta intygsuppgifter via en behörig elektronisk kanal.

Tre typer av kontroll måste samverka:

**Identitetskontroll.** Vilken aktör har lämnat referensen, och vilka roller har olika parter? Företag, deklarant, ombud och transportör kan vara olika aktörer.

**Saklig kontroll.** Täcker intyget just den vara, mängd, tidsperiod och andra förhållanden som är relevanta? En lyckad teknisk träff säger ingenting om den rättsliga prövningen inte också görs.

**Kontroll av tillit och aktualitet.** Vem ansvarar för statusuppgiften, när verifierades den och hur upptäcks återkallelser eller rättelser? Om källsystemet inte nås kan ett tidigare sparat svar vara inaktuellt.

En första implementation visar sig skapa långa svarstider och många manuella undantag. En granskning visar att de största problemen inte är nätverksfel utan otydliga begrepp: fältet ”mängd” avser i ett system tillåten totalmängd, i ett annat återstående kvantitet. Genom att förtydliga informationsmodellen och koppla kontrollen till rätt händelser kan parterna minska både felaktiga avslag och onödiga förfrågningar.

Detta illustrerar en generell slutsats: värdet av internationell datadelning avgörs lika mycket av gemensam betydelse och operativ förvaltning som av själva kommunikationskanalen.

## Säkerhetsarkitektur för distribuerad tillit

När information passerar organisationsgränser behöver flera tillitsfrågor besvaras separat. Är det anropande systemet äkta? Representerar det en behörig organisation? Har den aktuella användaren eller tjänsten rätt att begära uppgiften? Gäller behörigheten just detta ändamål? Kan uppgiftslämnaren och mottagaren i efterhand verifiera utbytet?

Tekniska mekanismer såsom stark tjänsteidentifiering, krypterad transport, begränsade åtkomsttoken, behörighetsbeslut och revisionsloggar kan stödja dessa krav. Men teknik ersätter inte överenskommelser om ansvar eller beslut om tillåten behandling. En säkerhetsdesign bör därför utgå från en dokumenterad tillitsmodell mellan aktörerna.

Särskild uppmärksamhet behövs för loggar och metadata. Ett svar som innehåller ett enda statusvärde kan förefalla okänsligt, medan loggen över vem som frågade om vilken aktör och vid vilken tidpunkt kan avslöja underrättelsearbete eller kontrollintressen. Loggning behöver balansera spårbarhet med informationsminimering, åtkomstbegränsning och relevanta regler om bevarande.

När datadelning stödjer samhällsviktig verksamhet krävs planering för avbrott, incidenter, ändrad tillit och komprometterade anslutna parter. Det bör finnas förmåga att tillfälligt begränsa anslutningar utan att hela verksamheten slutar fungera. Kontinuitetsplanen måste innehålla beslut om vad verksamheten får göra med ofullständiga eller inaktuella data.

## Styrning av informationsutbyte som en varaktig förmåga

I stora myndigheter kan integrationer växa fram ett projekt i taget. Resultatet blir en omfattande mängd punkt-till-punkt-förbindelser som är svåra att överblicka, ändra och säkra. Ett mer långsiktigt arbetssätt är att etablera datadelning som en förvaltningsförmåga med gemensamma principer och tydligt utpekade informationsansvariga.

En sådan förmåga kan omfatta ett register över informationsflöden, beskrivna kontrakt, godkända teknikmönster, gemensamma testmiljöer och en process för ändrings- och avvikelsehantering. Detta behöver förenas med en ansvarskarta: vem beslutar om att information får lämnas ut, vem ändrar informationsmodellen, vem larmas vid avbrott och vem informerar en extern part om att ett felaktigt värde redan har spridits?

Det går att förena decentraliserat informationsansvar med gemensam styrning. Varje informationsdomän kan svara för sina uppgifter och sin verksamhetslogik, medan organisationen som helhet erbjuder återanvändbara lösningar för identitet, spårbarhet, katalogisering och säker kommunikation.

**Resultat bör mätas i verksamhetseffekter**, inte enbart i antalet API:er. Exempel på mått är färre onödiga uppgiftslämningar, kortare väntetider, färre felaktiga kontroller, snabbare rättelser, bättre spårbarhet och högre tillgänglighet i kritiska informationsflöden. Måtten måste relateras till rättsliga och säkerhetsmässiga krav så att effektivitet inte uppnås genom otillåten informationsspridning.

## Sammanfattning

Datadelning över organisations- och nationsgränser förutsätter fyra former av interoperabilitet: rättslig, organisatorisk, semantisk och teknisk. Tekniken kan skapa en förbindelse, men först ett gemensamt ansvarstagande för ändamål, betydelse och kvalitet gör informationsutbytet användbart.

För en myndighet som ska förena smidiga flöden med effektiva kontroller är informationsutbyte en kärnförmåga. Dess kvalitet påverkar service, kontrollträffsäkerhet, rättssäkerhet och förmågan att samarbeta internationellt. Den mest hållbara utvecklingen sker därför genom verksamhetsnära informationskontrakt, tydlig ansvarsfördelning och styrd användning av gemensamma infrastrukturer.

Nästa kapitel behandlar en särskilt avgörande förutsättning för dessa flöden: digital identitet, behörighet och tillit.

### Rättslig tidsavgränsning (oktober 2026)

Förordning (EU) 2024/903 började tillämpas den 12 juli 2024. Bestämmelser om bland annat interoperabilitetsbedömningar började tillämpas den 12 januari 2025. Det innebär inte att varje integration automatiskt omfattas av en särskild bedömningsskyldighet; tillämpningsområdet måste prövas för respektive förändring och tjänst. [K002]

**Tidsavgränsning:** Vissa bestämmelser i förordning (EU) 2022/2399 börjar tillämpas först den 13 december 2031. Den stegvisa tillämpningen bör skiljas från att rättsakten redan är i kraft. [K019]
