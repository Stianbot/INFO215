#Viktig

Før du bruker noe av denne koden:
lim inn følgende i ``items.py`` filen din: ``CLOSESPIDER_PAGECOUNT = 15``.
Dette gjør at crawling spiders du lager ikke besøker mer enn 15 sider.
Legg merke til at ``simple_crawling_spider_0.py`` kjører helt til den blir stoppet
om ikke denne kommandoen er tilstede i ``items.py``.

Har du spørsmål til koden: ta kontakt.

Kjør koden på eget ansvar.

Ikke kjør kode du ikke forstår.

## Forklaring til koden

Koden vil ikke fungere om den lastes ned og blir forsøkt kjørt.
Grunnen til dette er at den ikke er i miljøet som gjør at den fungerer.

## Hvordan bruke koden
Bruk koden som inspirasjon. Se på kommentarene hva koden gjør.
Se på elementer ved koden og implementer det i egne Scrapy-prosjekter.

##Filer
* ``simple_spider_0.py``er en enkel spider som henter første overskrift
fra tre wikipedia-sider. Her brukes ``start_request()``
* ``simple_spider_1.py``er en enkel spider. Her brukes
`start_urls``-variabelen.
* `items.py`simulerer items.py i deres scrapy prosjekt. Denne brukes
i forbindelse med ``simple_crawling_spider_0.py`` se linje
  `29-33` i denne filen.
* ``simple_crawling_spider_0.py``er en crawler som henter ned diverse info
fra BT.no sine sider.
