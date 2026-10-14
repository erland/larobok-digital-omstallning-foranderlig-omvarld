# 10. Digital suveränitet och tekniska beroenden

En myndighet kan ha välfungerande digitala tjänster och ändå sakna tillräcklig kontroll över de förutsättningar som håller tjänsterna vid liv. Ett internationellt informationsutbyte kan vara beroende av en enda identitetsleverantör. En avancerad analysfunktion kan kräva åtkomst till en utländsk AI-plattform. Ett avtal kan ge god driftsäkerhet i vardagen men otillräckliga möjligheter att flytta data, granska underleverantörer eller fortsätta verksamheten vid en geopolitisk störning.

Digital suveränitet handlar därför mindre om att all teknik måste ägas eller tillverkas inom landet och mer om **faktisk rådighet**: förmågan att fatta och verkställa nödvändiga beslut om information, teknik, åtkomst, leverantörer och kontinuitet. För en myndighet med kontroll-, uppbörds- och brottsbekämpande uppdrag är detta en konkret verksamhetsfråga. När tillgången till ett system upphör kan följden bli avbrutna legitima flöden, sämre möjligheter att upptäcka avvikelser och försämrad rättssäkerhet.

## Från digital självständighet till prövbar handlingsfrihet

Begreppen *digital suveränitet*, *strategisk autonomi* och *digital resiliens* används ibland som synonymer, men de beskriver delvis olika perspektiv. Suveränitet avser rådighet och bestämmanderätt, autonomi förmågan att välja handlingsväg utan oskäliga beroenden och resiliens förmågan att hantera störningar och återhämta sig.

En myndighet behöver inte ha maximal självförsörjning för varje komponent. Ett försök att ersätta alla etablerade plattformar kan tvärtom öka riskerna om ersättningarna saknar kapacitet, säkerhet eller fungerande förvaltning. Frågan bör i stället vara vilka beroenden som är acceptabla, vilka som måste kunna brytas och vilka kritiska funktioner som måste kunna upprätthållas även när en leverantör eller ett nätverk inte är tillgängligt.

Fyra frågor kan användas vid varje betydande teknikval: Vem kan se eller påverka myndighetens information? Vem kan ensidigt ändra villkoren för tjänsten? Vad kan myndigheten göra om tjänsten inte längre kan användas? Vilka kostnader, tidsåtgång och risker medför ett byte? Sådana frågor gör suveränitet till ett styrbart kvalitetskrav snarare än ett allmänt politiskt slagord.

## En föränderlig politisk och rättslig omvärld

Sveriges regering antog i maj 2026 en molnpolicy för offentlig förvaltning med syfte att stärka säkerhet, minska beroenden och öka kontrollen över data, samtidigt som molntjänsters möjligheter till effektivitet och innovation kan tas till vara. Policyn bör läsas som en strategisk riktning, inte som ett generellt rättsligt godkännande av enskilda molntjänster. [K029]

Europeiska kommissionen presenterade i juni 2026 en modell för att bedöma molnsuveränitet. Den omfattar bland annat juridiska och jurisdiktionella förhållanden, data och AI, drift, leveranskedja, tekniskt oberoende samt säkerhet och regelefterlevnad. Inom kommissionens upphandling av molntjänster användes nivåer för *Sovereignty Effectiveness Assurance* (SEAL). Modellen är ett illustrativt och användbart analysstöd, men är inte i sig ett universellt lagkrav för svenska myndigheters alla upphandlingar. [K030][K031]

I juni 2026 presenterade kommissionen också ett förslag till förordning om utveckling av moln och AI, COM(2026) 502. Förslaget syftar bland annat till att öka kapaciteten och stärka europeisk autonomi, med en modell för att bedöma suveränitet. **Per den 14 oktober 2026 är detta ett lagförslag, inte gällande rätt.** Myndigheter bör därför bevaka dess fortsatta behandling utan att utforma efterlevnadsbeslut som om den föreslagna förordningen redan hade trätt i kraft. [K032]

Det rättsliga läget måste också bedömas mot dataskydd, offentlighet och sekretess, upphandling, säkerhetsskydd och eventuella sektorsspecifika regler. Ett påstående om att en tjänst är ”EU-hostad”, ”svensk” eller ”suverän” avgör inte ensamt dessa frågor.

## Fem dimensioner av faktisk rådighet

### Juridisk och jurisdiktionell rådighet

Vem är avtalspart? Vilka jurisdiktioner kan påverka leverantören eller dess underleverantörer? Var finns supportpersonal, nyckelhantering och administratörsbehörigheter? Finns det möjligheter till åtkomst eller utlämnande som måste bedömas i en tredjelands- eller sekretessanalys? Svaret går inte att härleda enbart från datacentrets geografiska placering.

Rättsliga bedömningar behöver göras utifrån den faktiska behandlingen, inklusive fjärradministration, felsökning, loggar, säkerhetskopior och support. De bör dokumentera både kända förhållanden och osäkerheter. Kryptering, åtkomstkontroll och avtalsvillkor kan vara viktiga skyddsåtgärder men ersätter inte bedömningen av rättsliga krav.

### Informationsrådighet

Myndigheten måste veta var auktoritativa data finns, hur kopior uppstår och vilken information som kan exporteras. Här ingår metadata, historik, beviskedjor, loggar och modellutdata – inte bara tabeller med ärendeuppgifter. Ett avtalslöfte om ”dataexport” har begränsat värde om exporten saknar nödvändiga begreppsdefinitioner, behörighetsrelationer eller verifierbara kontrollspår.

### Teknisk rådighet

Systemet behöver tydliga gränssnitt, dokumenterade dataformat, portabla komponenter och möjlighet att bygga om kritiska funktioner. Öppna standarder och öppen källkod kan minska vissa beroenden, men förutsätter samtidigt kompetens, säkerhetsunderhåll och förvaltningsansvar. Att koden kan läsas betyder inte automatiskt att en tjänst kan driftsättas eller återställas.

### Operativ rådighet

Vem kan stoppa, återställa och felsöka tjänsten? Hur snabbt kan behörigheter återkallas? Vilka reservrutiner finns? En myndighet kan juridiskt äga data och ändå vara operativt beroende av en extern kontrollpanel för att över huvud taget komma åt dem.

### Ekonomisk och organisatorisk rådighet

Även långsiktiga kostnader, prissättningsmekanismer, kompetensberoenden och avtalsupphörande påverkar handlingsfriheten. Ett billigt införande kan följas av dyr migrering eller stigande kostnader för lagring och dataöverföring. Myndigheten bör därför betrakta utträdesförmåga som en del av investeringens livscykelkostnad.

## Molntjänster: välj efter informations- och verksamhetsrisk

Ett rimligt vägval kan vara en kombination av olika driftsformer. Kontorsstöd och publika informationssidor har andra krav än ett system som hanterar underrättelseuppgifter eller leder operativa kontroller. En intern miljö kan ge hög rådighet i vissa avseenden men samtidigt vara sårbar för kompetensbrist eller underdimensionerad kontinuitet. Externa leverantörer kan erbjuda teknisk robusthet men skapa beroenden som behöver hanteras.

Varje tjänst bör därför bedömas mot informationsklassning, lagstöd, verksamhetskritikalitet, hotbild, möjligheten till insyn samt återställnings- och migrationskrav. Samma myndighet kan behöva flera väl motiverade mönster i sin målarkitektur. Det viktiga är att valen följer en konsekvent metod och inte en generell princip om att allt ska ligga antingen lokalt eller i publikt moln.

Ett särskilt misstag är att blanda ihop leverantörsland, serverplacering och faktisk kontroll. En europeisk driftmiljö kan fortfarande ha utomeuropeiska teknik- eller supportberoenden. På motsvarande sätt måste användningen av en internationell leverantör bedömas utifrån den konkreta tjänstens avtalsvillkor, driftorganisation, tekniska skydd och rättsliga förutsättningar, inte enbart varumärket.

## AI skapar nya beroenden

AI-lösningar kan innehålla flera samtidigt rörliga delar: språkmodell, inferensmiljö, vektordatabas, embeddings, dokumentindex, säkerhetsfilter, verktygsintegrationer och modellövervakning. Även om myndigheten kan exportera sin egen ärendedata kanske den inte kan återskapa samma resultat när en modell byts eller en leverantör ändrar tjänstens beteende.

Det gör **utbytbarhet och reproducerbarhet** till viktiga kvaliteter. Prompter, datakällor, modellversioner, testfall och utvärderingsmått bör dokumenteras. Kritiska arbetsflöden ska inte vara beroende av en odokumenterad promptkedja eller en enda otillgänglig modell. Där det är lämpligt kan myndigheten ha en alternativ modell, en enklare regelbaserad reservfunktion eller ett manuellt förfarande.

Egna modeller och lokal AI-drift kan ge ökad kontroll, men kräver kapacitet, säkerhetsarbete, energiförsörjning, uppdateringar och specialkompetens. De är därför inte automatiskt det bästa valet. Bedömningen bör väga faktiska risker och verksamhetsnytta mot både kostnad och uthållighet.

## Fiktivt scenario: när en internationell plattform inte längre är tillgänglig

En myndighet använder en extern integrationsplattform för att ta emot och verifiera intyg om gränsöverskridande varor. Plattformen har god historisk tillgänglighet och förenklar anslutningen till flera internationella motparter. Under en period av förhöjda geopolitiska spänningar uppstår plötsligt begränsningar i leverantörens support och i myndighetens möjlighet att administrera nya certifikat.

Ärendena fortsätter att komma in, men verifieringen av vissa intyg kan inte genomföras. Verksamheten ställs inför en konflikt: stoppa alla flöden, släppa igenom uppgifter utan tillräcklig kontroll eller övergå till alternativa kontroller där det finns rättsligt stöd. Ingen av vägarna kan väljas enbart av teknikorganisationen.

En väl förberedd myndighet har redan definierat vilka intyg som kan prövas genom ett alternativt verifieringssätt, hur risknivån kan bedömas utan den externa plattformen och vilka beslutsfattare som har mandat att aktivera reservförfarandet. Den har testat att återställa nödvändiga integrationskonfigurationer i en annan miljö och dokumenterat hur händelser ska efterregistreras. För de ärenden där säker verifiering inte är möjlig finns en rättsligt förankrad hantering som skyddar både kontrolluppdrag och enskildas intressen.

Vid efteranalysen visar det sig att myndigheten hade full möjlighet att exportera affärsdata, men inte de certifikatkopplingar och konfigurationsregler som krävdes för en snabb flytt. Beroendet låg alltså inte främst i databasens innehåll utan i förmågan att återskapa en fungerande och betrodd tjänst.

*Scenariot är fiktivt och beskriver inte faktiska system eller händelser vid en viss myndighet.*

## Från leverantörsregister till beroendekarta

Traditionella register visar vilka avtal och applikationer som finns. De säger mindre om vilka samhällsviktiga förmågor som slutar fungera om en gemensam tjänst fallerar. En beroendekarta behöver därför binda samman verksamhetsförmåga, process, informationsobjekt, integration, teknisk tjänst, leverantör och underleverantör.

För varje kritiskt beroende kan myndigheten dokumentera vilken störning som är dimensionerande, hur länge verksamheten kan avvara tjänsten, vilken alternativ funktion som finns och vad som krävs för att återuppta arbetet. Det är värdefullt att skilja mellan **återställning hos samma leverantör** och **förmåga att lämna leverantören**. Den första kan fungera väl samtidigt som den andra saknas.

| Förmåga | Typiskt beroende | Möjlig skyddsåtgärd |
|---|---|---|
| Digital uppgiftslämning | Extern identitets- eller formulärtjänst | Reservkanal och kontrollerad återregistrering |
| Internationell intygsverifiering | Gemensamt gränssnitt och tillitskedja | Alternativ verifieringsrutin och certifikatinventering |
| Riskanalys | AI-modell, datatillgång och modellkonfiguration | Versionsstyrning, alternativa urvalsregler och återkommande tester |
| Operativ kontroll | Mobil åtkomst till ärendeuppgifter | Begränsat offline-stöd och fastställda reservprocesser |
| Betalnings- och uppbördsflöden | Extern betalningsintegration | Avstämning, köhantering och rättssäker felhantering |

Tabellen visar typiska designval, inte rättsliga tillstånd att använda en viss reservprocess. Sådana beslut behöver förankras i myndighetens faktiska befogenheter.

## Upphandling och avtal som arkitekturverktyg

Suveränitet kan inte läggas till i efterhand enbart genom en ny säkerhetsfunktion. Krav på insyn i underleverantörer, förändringsavisering, dataexport, förutsättningar för revision, incidentrapportering, jurisdiktion, underhåll av säkerhetsfunktioner och stöd vid avveckling behöver föras in redan vid anskaffningen.

Ett utträdesavtal bör ange vilka data, metadata, loggar och konfigurationer som ska lämnas tillbaka, i vilka format och inom vilka tider. Det behöver också reglera beroenden till identitetsfederationer, certifikat, API-nycklar och proprietära funktioner. En praktisk migreringsövning före avtalsförlängning kan avslöja brister som aldrig hade synts vid en vanlig leverantörsuppföljning.

Krav bör vara proportionerliga och verifierbara. Om en upphandling använder ett suveränitetsmått behöver myndigheten beskriva vilka risker som måttet avser att hantera, hur det ska bedömas och varför kraven är relevanta. Ett allmänt krav på ”europeisk suveränitet” kan vara mindre användbart än konkreta krav på administrativ kontroll, datalokalitet, revisionsmöjligheter och flyttbarhet.

## Arkitekturens krav på handlingsfrihet

En målarkitektur för en samhällsviktig verksamhet måste visa vilka teknikberoenden som kan ersättas, vilka data och konfigurationer som kan flyttas och vilka avtalsmässiga eller rättsliga begränsningar som kan hindra en förflyttning. Den viktigaste kontrollen är praktiskt verifierad flyttbarhet – inte enbart en klausul om rätt till export.

Valet av driftsform behöver utgå från informationens skyddsvärde och verksamhetens behov. Kontinuitetskrav vid störningar utvecklas i kapitel 11, medan långsiktiga investeringar och prioriteringar behandlas samlat i kapitel 16.

## Sammanfattning

Digital suveränitet är inte en fråga om att välja mellan isolering och moln. Det är förmågan att behålla verklig handlingsfrihet när teknik, avtal, jurisdiktion eller geopolitik förändras. För en myndighet som möjliggör flöden och samtidigt utövar kontroll kan ett brustet teknikberoende få konsekvenser långt utanför it-miljön.

Den hållbara vägen går genom genomlysta beroenden, rättsligt grundade teknikval, kontrollerbar informationshantering, realistiska och testade utträdesmöjligheter. Kapitel 11 fördjupar beredskap och operativ kontinuitet: hur myndigheten faktiskt kan fortsätta fullgöra sina uppgifter när det ordinarie stödet inte fungerar.
