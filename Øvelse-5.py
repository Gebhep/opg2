# Øvelse 5. Typecasting
# I et klimaprojekt måles temperatur fra forskellige sensorer over fem kvarter på Amager.
# Hvad er middeltal af temperatur fra de fem målningsstationerkl. 18?
# Lav typecasting til decimaltal og beregn gennemsnitlig temperatur i Celsius med en decimal.

# Vi behandler vores 5 datasæt. Først omdannes de 25 strings til floats. Derefter bliver de lagt sammen, og til sidst divideret.
amager_1 = (float("12.2") + float("19.1") + float("21.2") + float("14.1") + float("11.9")) / 5
amager_2 = (float("11.8") + float("18.2") + float("20.5") + float("14.0") + float("11.3")) / 5
amager_3 = (float("12.2") + float("19.2") + float("21.6") + float("14.9") + float("12.0")) / 5
amager_4 = (float("12.3") + float("19.8") + float("22.1") + float("15.1") + float("12.4")) / 5
amager_5 = (float("11.1") + float("18.4") + float("21.5") + float("14.5") + float("11.7")) / 5

# Vi printer vores 5 datasæt, med afrunding til 1 decimaltal.
print(round(amager_1,1), round(amager_2,1), round(amager_3,1), round(amager_4,1), round(amager_5,1))