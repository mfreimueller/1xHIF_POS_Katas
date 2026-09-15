# Kata: Spielstatus vervollständigen

`Spielstatus.java` gibt drei Eigenschaften eines Spielcharakters aus, aber die dazugehörigen Variablen wurden noch nicht deklariert. Die Datei kompiliert deshalb nicht.

## Szenario

- Der Spieler ist noch am Leben.
- Der Spieler hat noch keinen Schlüssel gefunden.
- Die aktuelle Stufe wurde bereits abgeschlossen.

## Aufgabe

1. Deklariere und initialisiere im `TODO`-Bereich drei `boolean`-Variablen mit genau den Namen, die in den `println`-Aufrufen verwendet werden: `spielerLebt`, `hatSchluessel`, `stufeAbgeschlossen`.
2. Wähle die Werte (`true`/`false`) passend zum Szenario oben.
3. Entferne den `TODO`-Kommentar, sobald du fertig bist.

## Überprüfung

```
javac Spielstatus.java && java Spielstatus
```

Erwartete Ausgabe:

```
Spieler lebt: true
Hat Schluessel: false
Stufe abgeschlossen: true
```
