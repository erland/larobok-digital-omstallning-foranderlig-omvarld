# 6. Data som strategisk tillgång

En aktör förekommer i ett register med sitt organisationsnummer, i ett annat med ett utländskt registreringsnummer och i ett tredje under namnet på en lokal filial. En deklaration hänvisar till den första identiteten, ett tillstånd till den andra och ett äldre kontrollärende till den tredje. För en erfaren medarbetare kan det ibland vara uppenbart att uppgifterna gäller samma verksamhet. För ett automatiserat informationsflöde är sambandet långt ifrån självklart.

När myndigheter diskuterar datadriven verksamhetsutveckling handlar samtalet ofta om att samla mer data eller använda mer avancerad analys. Men i verksamheter där korrekt uppgiftsbehandling, kontroll och rättssäkra beslut måste fungera tillsammans är den viktigare frågan ofta enklare: **Vet vi vad våra uppgifter betyder, varifrån de kommer och när de kan användas?**

Detta kapitel analyserar data som strategisk verksamhetsförmåga. Utgångspunkten är eSams radarbild från februari 2026 och dess betoning på datadelning och interoperabilitet. Resonemangen kompletteras med Diggs ramverk för nationella grunddata och EU:s förordning om interoperabilitet inom den offentliga sektorn. [K1–K3] Kapitlets modeller och konsekvensbedömningar är bokens egna förslag, inte beskrivningar av en bestämd myndighets befintliga system.

## Data blir strategiska först när de kan användas ansvarsfullt

Data har inget självständigt verksamhetsvärde enbart genom att lagras. Värdet uppstår när informationen kan användas för att utföra uppdraget bättre: lämna korrekta besked, minska onödiga kompletteringar, uppbära rätt belopp, välja proportionerliga kontrollåtgärder eller upptäcka otillåtna mönster. Användningen måste samtidigt hålla sig inom rättsliga och säkerhetsmässiga ramar.

En strategisk datatillgång behöver därför fyra egenskaper. Den måste vara **begriplig** för mottagaren, **tillräckligt korrekt** för ändamålet, **tillgänglig för behöriga** och **spårbar** så att ursprung, förändringar och användning kan följas. Till detta kommer en femte fråga: är den aktuella användningen **tillåten**? En informationsmängd kan vara av hög kvalitet men ändå inte få användas i ett nytt analysändamål.

Skillnaden mellan *data*, *information* och *kunskap* är användbar. Data kan vara ett identitetsnummer och ett datum. Information uppstår när uppgifterna sätts i ett sammanhang: vilket subjekt avses och vad representerar datumet? Kunskap uppstår när en handläggare förstår vilka slutsatser som rimligen kan dras, vilka undantag som gäller och hur säker bedömningen är. AI kan stödja förflyttningen mellan nivåerna men upphäver inte behovet av definitioner eller professionell prövning.

## Informationsmodeller beskriver verksamhetens verklighet

Informationsarkitektur börjar med gemensam förståelse, inte med en databas. Ett informationsobjekt som *aktör*, *vara*, *försändelse*, *tillstånd*, *kontroll* eller *beslut* behöver en överenskommen betydelse. Annars kan två system utbyta samma fältnamn men avse olika saker.

Betrakta begreppet **avsändare**. Det kan avse den som lämnar en elektronisk uppgift, den part som har rättsligt ansvar, den som fysiskt överlämnar gods eller den aktör som anges i ett transportdokument. Om alla dessa roller lagras i ett enda fält uppstår fel när data används utanför den ursprungliga processen. En tydlig begreppsmodell skiljer rollerna åt och beskriver relationerna mellan dem.

En mogen informationsmodell omfattar därför:

- **Begreppsmodell:** verksamhetens termer, definitioner och relationer.
- **Informationsmodell:** vilka informationsobjekt, egenskaper, regler och samband som behöver hanteras.
- **Utbytesmodell:** hur informationen representeras i meddelanden, API:er och externa informationsflöden.
- **Lagringsmodell:** hur data faktiskt lagras och versionshanteras i tekniska system.

Modellerna har olika syften och ska inte slås samman till en enda teknisk tabellstruktur. Ett API-format som blivit etablerat i ett internationellt samarbete kan exempelvis behöva översättas till en myndighets interna informationsmodell. Översättningen ska vara dokumenterad, så att betydelseskillnader inte döljs bakom likartade fältnamn.

Diggs nationella grunddataramverk betonar bland annat standardisering, interoperabilitet, tillgängliga beskrivningar och säker behandling. Det stödjer synsättet att informationsmodeller är gemensamma överenskommelser, snarare än interna teknikartefakter. [K018]

## Datakvalitet är ändamålsberoende

En uppgift kan vara riktig i ett register och samtidigt otillräcklig för en viss kontroll. Ett företagsnamn kan vara korrekt återgivet men sakna koppling till den rättsliga enhet som faktiskt ansvarar för uppgiftslämningen. En geografisk plats kan anges med tillräcklig precision för statistik men inte för ett operativt ingripande.

Det är därför missvisande att eftersträva en enda siffra för ”datakvalitet”. Minst sex dimensioner är relevanta:

| Dimension | Kontrollfråga | Verksamhetskonsekvens vid brist |
|---|---|---|
| Riktighet | Stämmer uppgiften med det den avser att beskriva? | Felaktigt underlag för beslut och kontroller |
| Fullständighet | Finns de nödvändiga uppgifterna? | Extra kompletteringar och osäkra analyser |
| Aktualitet | Gäller uppgiften fortfarande, och när gällde den? | Gamla förhållanden behandlas som nuvarande |
| Konsistens | Går uppgifter och definitioner ihop mellan källor? | Motstridiga identiteter och oklara samband |
| Unikhet och identifierbarhet | Kan samma objekt särskiljas från andra? | Dubbletter eller felaktiga sammanslagningar |
| Spårbarhet | Kan källa och förändringshistorik fastställas? | Svagare kontrollbarhet och svårare rättelse |

Vilka nivåer som är tillräckliga avgörs av användningsfallet. En automatisk publicering av generell statistik kan tåla andra osäkerheter än ett system som föreslår en fysisk kontroll. Därför bör varje informationsprodukt ha deklarerade kvalitetskrav och tydliga regler för vad som händer när kraven inte uppfylls.

Datakvalitet ska också mätas nära verksamhetsprocessen. Om felaktig information ständigt måste korrigeras i efterhand kan orsaken finnas i utformningen av den digitala tjänsten, oklara begrepp eller bristande validering vid inrapporteringen. En central dataplattform löser sällan sådana grundproblem ensam.
