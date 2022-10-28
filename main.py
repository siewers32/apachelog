from logmodules import apache
from logmodules import menu
from logmodules import dbc

con = dbc.conn()
keuze = 10

print("===============================================================")
print("Maak een keuze")
print("0. Maak MySQL-tabel apache-log leeg")
print("1. Laadt het apache-log in mysql")
print("2. Overzicht van top 10 meest gebruikte browsers")
print("3. Overzicht van top 10 traagste pagina's")
print("4. Stoppen")
print("===============================================================")

try:
    keuze = int(input("Maak een keuze: "))
    if keuze < 0 or keuze > 4:
        raise Exception()

    if keuze == 0:
        apache.cleardb(con)

    if keuze == 1:
        parser = apache.parser()
        apache.savetodb(con, apache.parseLog(parser, "small_apache.log"))

    if keuze == 2:
        query = "select useragent, count(useragent) as aantal from apache_log group by useragent order by aantal desc";
        menu.select_query(con, query)

    if keuze == 3:
        query = ""
        menu.select_query(con, query)

    if keuze == 4:
        print("We stoppen ermee!")

except ValueError as e:
    print("Voer een nummer in tussen 1 en 5")
except:
    print("Voer een nummer in tussen 1 en 5")




