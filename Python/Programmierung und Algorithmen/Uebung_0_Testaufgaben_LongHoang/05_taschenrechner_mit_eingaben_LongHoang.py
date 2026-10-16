# Technische Informatik 1 - Woche 1
# Aufgabe 5: Taschenrechner mit Benutzereingaben
#
# Bisher standen die Zahlen direkt im Programm. Jetzt darf die Person,
# die das Programm benutzt, die Zahlen selbst eingeben.
#
# WICHTIG: input() liefert Text zurück.
# Mit int() wandeln wir eine Eingabe wie "12" in die ganze Zahl 12 um.
# Geben Sie deshalb nur ganze Zahlen ein (z. B. 12, 3 oder -5).
# Die Addition ist als Beispiel vollständig vorgegeben.

# Addition (+) - Beispiel
zahl_add1 = int(input("Addition - erste Zahl: "))
zahl_add2 = int(input("Addition - zweite Zahl: "))
print("Addition:", zahl_add1 + zahl_add2)

# Subtraktion (-)
# TODO 1: Fragen Sie mit input() zwei neue Zahlen ab.
# Wandeln Sie beide Eingaben mit int() in Zahlen um.
# Geben Sie dann mit print() das Ergebnis der Subtraktion aus.
zahl_sub1 = int(input("Subtraktion - erste Zahl: "))
zahl_sub2 = int(input("Subtraktion - zweite Zahl: "))
print("Subtraktion:", zahl_sub1 - zahl_sub2)

# Multiplikation (*)
# TODO 2: Fragen Sie erneut zwei Zahlen ab und geben Sie
# deren Produkt mit print() aus.
zahl_multi1 = int(input("Multiplikation - erste Zahl: "))
zahl_multi2 = int(input("Multiplikation - zweite Zahl: "))
print("Multi:", zahl_multi1 * zahl_multi2)

# Division (/)
# TODO 3: Fragen Sie erneut zwei Zahlen ab und geben Sie
# das Ergebnis der Division mit print() aus.
# Achtung: Geben Sie als zweite Zahl keine 0 ein!
zahl_div1 = int(input("Division - erste Zahl: "))
zahl_div2 = int(input("Division - zweite Zahl: "))
while zahl_div2 == 0:
    print("Bitte gib ein andere nummer")
    zahl_div2 = int(input("Addition - zweite Zahl: "))
print("Division:", zahl_div1 / zahl_div2)

# TODO 4: Führen Sie das fertige Programm aus und testen Sie
# alle vier Rechenoperationen mit verschiedenen Zahlen.
