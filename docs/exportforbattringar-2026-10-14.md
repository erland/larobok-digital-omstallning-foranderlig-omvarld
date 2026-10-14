# Exportförbättringar – 14 oktober 2026

Version 0.4.0: Exportmotorn skapar interna källhänvisningar (K001–K045) i PDF och EPUB; källornas långa adresser visas som klickbara länkar med kort text för att undvika radbrytningsproblem. Källregistret är fortfarande ett enda kapitel på slutet.

PDF har två centrerade rader för nummer och titel på kapitel 1–16 och sidhuvud med löpande kapitelrubriker är borttagna. Sidnummer finns kvar. Samma kapitelstruktur gäller EPUB, där faktisk placering påverkas av läsarens inställningar.

GitHub Actions: `01-validate.yml` kör projektvalidering och integritetskontroll vid push/PR; `02-build-preview.yml` bygger PDF+EPUB manuellt; `03-release.yml` bygger PDF+EPUB och publicerar dem med SHA256SUMS vid tagg `v*`. Dessa Actions har granskats statiskt och testats lokalt via exportskript, men ännu inte provkörts på GitHub.

Notering: PDF och EPUB är provutgåvor. Extern fullständig länk- och juridisk kontroll kvarstår.
