# Restaurangsystem

## Beskrivning
Ett enkelt restaurangsystem utvecklat i Python med objektorienterad programmering (OOP).

Programmet hanterar menyobjekt, bord, beställningar och betalningar.

## Funktioner
- Hantera förrätter, huvudrätter, desserter och drycker.
- Skapa och hantera beställningar för olika bord.
- Beräkna priser med extra avgifter.
- Skapa kvitton och beräkna totalbelopp.

## Objektorienterad programmering (OOP)
- **Klasser och objekt:** Representerar menyobjekt, bord, beställningar och restaurangen.
- **Arv:** Menyklasserna ärver från `MenuItem`.
- **Polymorfism:** Olika menyobjekt kan beräkna slutpriser på olika sätt.
- **Komposition:** Restaurangen innehåller menyobjekt och bord, medan borden hanterar beställningar.

## Köra programmet
Kör Python-filen med följande kommando:

```bash
python3 app.py