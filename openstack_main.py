# from os import strerror
# from openstack import parse
# from openstack import savetodb as openstack_save
from logmodules import apache
from logmodules import menu
from logmodules import dbc

# parsed = parse('openstack.log')

# openstack_save(parse('openstack.log'))

con = dbc.conn()
# parser = apache.parser()
# apache.savetodb(con, apache.parseLog(parser))

def print_menu():
    print("===============================================================")
    print("Maak een keuze")
    print("1. Overzicht van top 10 meest gebruikte browsers")
    print("1. Overzicht van top 10 traagste pagina's")
    print("===============================================================")
    try:
        keuze = int(input("Maak een keuze: "))
        if keuze < 0 or keuze > 5:
            raise Exception()
        if keuze == 1:
            query = "select useragent, count(useragent) as aantal from apache_log group by useragent order by aantal desc";
            menu.select_query(con, query)

        if keuze == 2:
            query = ""
            menu.select_query(con, query)
    except ValueError as e:
        print("Voer een nummer in tussen 1 en 5")
    except:
        print("Voer een nummer in tussen 1 en 5")



print_menu()
