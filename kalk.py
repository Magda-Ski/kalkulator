import logging
logging.basicConfig(level=logging.DEBUG)

print("Witaj w moim kalkulatorze")
first_number = int(input("Prosze podaj pierwsza liczbe: "))
second_number = int(input("Prosze podaj drugą liczbę: "))
operation = int(input("Jakie działanie chcesz wykonać\n Wybierz liczbę od 1 do 4 ?\n 1.dodawanie\n 2.odejmowanie\n 3.mnożenie\n 4.dzielenie\n"))
if operation == 1:
    logging.info("Wybrałeś dodawanie\nTwoj wynik to:")
    logging.info(first_number + second_number)
elif operation == 2:
    logging.info("Wybrałeś odejmowanie\nTwoj wynik to:")
    logging.info(first_number - second_number)
elif operation == 3:
    logging.info("Wybrałeś mnożenie\nTwoj wynik to:")
    logging.info(first_number * second_number)
elif operation == 4:
    logging.info("Wybrałeś dzielenie\nTwoj wynik to:")
    logging.info(first_number / second_number)
else:
    logging.info("Nie ma takiego działania")
    exit(1)