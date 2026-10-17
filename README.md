# ESGO Python SDK
German Version down below

Official Python client for the [ESGO API](https://es-go.de/developers): find
matching empty-run capacity for road freight and publish open transport
requests from your TMS or ERP.

> **Pre-release.** Version 0.0.1 covers `GET /v1/me` only. Matching search and
> open requests follow in 0.1.0. The API may still change before 1.0.

## Installation

```sh
pip install esgo
```

Requires Python 3.10 or newer.

## Access

API keys are issued by ESGO; there is no self-service sign-up yet. Request
access at [es-go.de/developers](https://es-go.de/developers). Keep your key
secret and never commit it to a repository.

## Usage

Set the key once and call the API through the `esgo` module, like the `stripe`
package:

```python
import esgo

esgo.api_key = "esgo_live_..."   # or set the ESGO_API_KEY environment variable

me = esgo.me.retrieve()
print(me["account_role"], me["quotas"])
```

Or create a client, which is useful when you work with several keys:

```python
import esgo

with esgo.Client(api_key="esgo_live_...") as client:
    me = client.me.retrieve()
```

## Errors

Every API error raises a subclass of `esgo.APIError` with the fields of the
ESGO error envelope:

```python
try:
    esgo.me.retrieve()
except esgo.RateLimitError as e:
    print("Try again in", e.retry_after, "seconds")
except esgo.APIError as e:
    print(e.status, e.code, e.message, e.param, e.request_id)
```

| Exception | HTTP status |
|---|---|
| `InvalidRequestError` | 400, 422 |
| `AuthenticationError` | 401 |
| `PermissionDeniedError` | 403 |
| `NotFoundError` | 404 |
| `RateLimitError` | 429 |
| `ServiceUnavailableError` | 503 |
| `InternalServerError` | other 5xx |
| `APIConnectionError` | network error, no response |

## Links

- API reference: [api.es-go.de/v1/docs](https://api.es-go.de/v1/docs)
- OpenAPI spec: [api.es-go.de/v1/openapi.json](https://api.es-go.de/v1/openapi.json)
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## License

MIT, see [LICENSE](LICENSE).









# ESGO Python SDK

*[Deutsche Version weiter unten](#esgo-python-sdk-deutsch)*

Official Python client for the [ESGO API](https://es-go.de/developers): find
matching empty-run capacity for road freight and publish open transport
requests from your TMS or ERP.

> **Pre-release.** Version 0.0.1 covers `GET /v1/me` only. Matching search and
> open requests follow in 0.1.0. The API may still change before 1.0.

## Installation

```sh
pip install esgo
```

Requires Python 3.10 or newer.

## Access

API keys are issued by ESGO; there is no self-service sign-up yet. Request
access at [es-go.de/developers](https://es-go.de/developers). Keep your key
secret and never commit it to a repository.

## Usage

Set the key once and call the API through the `esgo` module, like the `stripe`
package:

```python
import esgo

esgo.api_key = "esgo_live_..."   # or set the ESGO_API_KEY environment variable

me = esgo.me.retrieve()
print(me["account_role"], me["quotas"])
```

Or create a client, which is useful when you work with several keys:

```python
import esgo

with esgo.Client(api_key="esgo_live_...") as client:
    me = client.me.retrieve()
```

## Errors

Every API error raises a subclass of `esgo.APIError` with the fields of the
ESGO error envelope:

```python
try:
    esgo.me.retrieve()
except esgo.RateLimitError as e:
    print("Try again in", e.retry_after, "seconds")
except esgo.APIError as e:
    print(e.status, e.code, e.message, e.param, e.request_id)
```

| Exception | HTTP status |
|---|---|
| `InvalidRequestError` | 400, 422 |
| `AuthenticationError` | 401 |
| `PermissionDeniedError` | 403 |
| `NotFoundError` | 404 |
| `RateLimitError` | 429 |
| `ServiceUnavailableError` | 503 |
| `InternalServerError` | other 5xx |
| `APIConnectionError` | network error, no response |

## Links

- API reference: [api.es-go.de/v1/docs](https://api.es-go.de/v1/docs)
- OpenAPI spec: [api.es-go.de/v1/openapi.json](https://api.es-go.de/v1/openapi.json)
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## License

MIT, see [LICENSE](LICENSE).

---






# ESGO Python SDK (Deutsch)


Dies ist der offizielle Python-Client für die [ESGO API](https://es-go.de/developers):


Hier ein kleines Vorwort, weiter unten kommt der eigentlich wichtige Teil (17.10.2026):

Hi, mein Name ist Ivo Wundling, ich bin (stand heute) 20 Jahre alt und bin einer der Geschäftsführer der ESGO Logistics UG (haftungsbeschränkt) aus Bonn. 
Am 19 Mai 2025 haben wir begonnen, die Plattform ESGO zu entwickeln. Begonnen hat es über einen kleinen Prototypen zum Spaß, und über die Monate wurde daraus nach Pitches u.a. vor der NRW.Bank eine riesige SaaS-Enterprise Plattform (okay fairerweise wenn man jetzt nur die v.0.0.1 liest dann kommt das nicht wirklich so rüber da müsst ihr mir jz einfach vertrauen, bzw sobald das hier jemand liest sind weitaus mehr Schnistellen öffentlich hier verfügbar).

Hier ist der Standard Satz über ESGO, welchen ich immer gerne nutze, damit jeder direkt weiss was wir machen:
ESGO ist eine KI-Plattform zur automatisierten Erkennung, Vermittlung und Monetarisierung von LKW-Leerfahrten.

Jetzt weiss man circa um was es geht, nämlich um Leerfahrten Vermittlung. Vermittlung ist dabei ein wichtiges Wort, weil wir als Plattform Handelsmakler sind (nach §93 HGB) das ist wichtig für Spediteure, da diese somit die Preishoheit behalten. Denn digitale Speditionendrücken über Algorithmen die Preise und Spediteure werden gleichzeitig zur rein ausführenden Instanz.

Allgemein kann man sagen, dass wir versuchen mit ESGO die größten Probleme der Logistik zu lösen. Dazu gehören bspw. der hohe Margendruck, entstehend durch digitale Speditionen, aber auch hohe Energie & Spritkosten, Maut, Fahrermangel und vielem mehr. 

Kein Wunder dass in so ziemlich jeder Statistik die Speditions bzw. Logistikbranche immer knallend auf dem traurigen letzten (bzw. im negativem Sinne den ersten) Platz ergattert. Einige der vielen Vorzeigebeispiele sind die Insolvenzstatistik, die Zahlungsausfallstatistik sowie die Margenstatistiken.

Aktuell bootsstrappen wir die Plattform mit selbstständigen Vertrieberler, sobald das hier allerdings jemand wirklich liest, lässt sich davon ausgehen dass dies mittlerweile nicht mehr der Fall ist.

Dazu kommen wir auch eigentlich langsam zum technischen Teil, weil wenn das hier jemand liest bedeutet dass auch dass dieser jemand (ja genau du! der das hier liest) ESGO in sein Produkt bzw. Backend eines Produktes einbauen will. (oder muss lol)

Dann kommen wir mal zum eigentlichen Spass, was macht diese Python SDK überhaupt?

Damit Spediteure und Verlader sowie ERP & TMS Systeme ESGO auch per API Anbinden können, gibts hier einen python Client welcher als Thin Wrapper agiert. Er basiert auf der openapi.json, diese findest du unter https://es-go.de/developers bzw. unter https://es-go.de/v1/openapi.json

Die meisten TMS/ERP systeme sind auch nicht in python, deswegen kann es gut sein dass das hier niemand jemals lesen wird, aber python import esgo hat crazy viel Aura, und der Name war frei deswegen konnte ich nicht widerstehen. Ansonsten sind in Arbeit noch das gleiche für TypeScript/JavaScript & C#.
Sollte die SDK unzureichend sein oder nicht dokumentiert genug (entschuldige ich mich erstmal im Vorraus) und dann gibts alternativ immer die openapi.json für alle frei zugänglich


Viel gerede von mir (es ist grad 0 Uhr das ganz normal zu der Zeit) und jetzt zum eigentlichen technischen Teil, wenns irgendwo zu fragen gibt einfach nen Issue anlegen oder mir auf LinkedIn schreiben (https://www.linkedin.com/in/ivo-wundling-708068272/)

LG Ivo


> **Vorabversion (Pre-release).** Version 0.0.1 deckt zunächst nur `GET /v1/me`
> ab. Die Matching-Suche und offene Transportanfragen folgen in Version 0.1.0.
> Bis Version 1.0 können sich noch Änderungen an der API ergeben.

## Installation

```sh
pip install esgo
```

Erfordert Python 3.10 oder neuer.

## Zugang

API-Keys werden direkt von ESGO vergeben; eine Self-Service-Registrierung gibt
es aktuell noch nicht. Der Zugang kann unter
[es-go.de/developers](https://es-go.de/developers) angefragt werden. Halte
deinen Key geheim und committe ihn niemals in ein Repository. (logisch nh)

## Verwendung

Hinterlege den Key einmalig und rufe die API direkt über das `esgo`-Modul auf, alles ist analog zum `stripe`-Paket:

```python
import esgo

esgo.api_key = "esgo_live_..."   # oder über die Umgebungsvariable ESGO_API_KEY setzen

me = esgo.me.retrieve()
print(me["account_role"], me["quotas"])
```

Alternativ kann eine eigene Client-Instanz erstellt werden (praktisch, wenn mit
mehreren Keys parallel gearbeitet wird):

```python
import esgo

with esgo.Client(api_key="esgo_live_...") as client:
    me = client.me.retrieve()
```

## Fehlerbehandlung

Jeder API-Fehler wirft eine Subklasse von `esgo.APIError`, die alle Felder der
ESGO-Fehlerantwort enthält:

```python
try:
    esgo.me.retrieve()
except esgo.RateLimitError as e:
    print("Erneuter Versuch in", e.retry_after, "Sekunden möglich")
except esgo.APIError as e:
    print(e.status, e.code, e.message, e.param, e.request_id)
```

| Exception | HTTP-Status |
|---|---|
| `InvalidRequestError` | 400, 422 |
| `AuthenticationError` | 401 |
| `PermissionDeniedError` | 403 |
| `NotFoundError` | 404 |
| `RateLimitError` | 429 |
| `ServiceUnavailableError` | 503 |
| `InternalServerError` | andere 5xx |
| `APIConnectionError` | Netzwerkfehler, keine Antwort |

## Links

- API-Referenz: [api.es-go.de/v1/docs](https://api.es-go.de/v1/docs)
- OpenAPI-Spezifikation: [api.es-go.de/v1/openapi.json](https://api.es-go.de/v1/openapi.json)
- Changelog: [CHANGELOG.md](CHANGELOG.md)

## Lizenz

MIT, siehe [LICENSE](LICENSE).