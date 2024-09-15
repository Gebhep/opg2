# Øvelse 4. Typecasting

# Et shoppingcenteri Taastrup har butikker med forskellige systemer til at beregne antallet af besøgende kunder.
# Beregn hvor mange kunder der var den 3. August med typecasting.

# Data fra kolonne 20240803
cartema = "129"
maleri_alt = 143
toejforalle = 223.0
planter = "87"
el_mer = 86.0

# De forskellige typer data fra kolonne 20240803 omdannes til integers
val1 = int(cartema)
val2 = int(maleri_alt)
val3 = int(toejforalle)
val4 = int(planter)
val5 = int(el_mer)

# Udprint af alle vores værdier sammenlagt, i integer
print("Der var: ", val1 + val2 + val3 + val4 + val5, " kunder d. 08 august")