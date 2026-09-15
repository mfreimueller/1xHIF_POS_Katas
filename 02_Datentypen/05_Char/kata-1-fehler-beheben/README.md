# Kata: Fehler bei einzelnen Zeichen beheben

`Symbole.java` kompiliert nicht. In jeder Zeile wurde einer `char`-Variable ein Wert gegeben, der so nicht funktioniert.

## Aufgabe

1. Behebe alle drei Fehler.
2. Ändere dabei **nicht** den Datentyp `char` — nur den zugewiesenen Wert.
3. Denk daran: Ein einzelnes Zeichen (`char`) steht in einfachen Anführungszeichen `'...'` und besteht aus genau **einem** Zeichen.

## Überprüfung

```
javac Symbole.java && java Symbole
```

Das Programm soll fehlerfrei kompilieren und drei Zeilen mit einzelnen Zeichen ausgeben.
