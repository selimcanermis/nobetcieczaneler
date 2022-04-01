from turtle import ht
import requests
from bs4 import BeautifulSoup
import json
from tabulate import tabulate

headers_driver = {'User-Agent': 'Mozilla/5.0 (x11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


class NobetciEczane:
    def __init__(self):
        self.il = self.ilInput()
        self.ilce = self.ilceInput()

        self.il     = self.il.replace('İ', "i").lower()
        self.ilce   = self.ilce.lower()

        tr_alphabet  = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
        self.il     = self.il.translate(tr_alphabet)
        self.ilce    = self.ilce.translate(tr_alphabet)

        source  = "eczaneler.gen.tr"
        self.url     = f"https://www.eczaneler.gen.tr/nobetci-{self.il}-{self.ilce}"
        request   = requests.get(self.url, headers=headers_driver)

        soup = BeautifulSoup(request.content, "lxml")
        eczaneler = soup.find('div', id='nav-bugun')

        data_json = {"source": source, 'data' : []}

        try:
            for bak in eczaneler.findAll('tr')[1:]:
                isim    = bak.find('span', class_='isim').text
                adres = bak.find('div', class_='col-lg-6').text
                tarif = (None if bak.find('span', class_='text-secondary font-italic') is None else bak.find('span', class_='text-secondary font-italic').text)
                tel  = bak.find('div', class_='col-lg-3 py-lg-2').text

                data_json['data'].append({
                    'isim'        : isim,
                    'adres'     : adres,
                    'tarif'     : tarif,
                    'telefon'   : tel
                })
        except AttributeError:
            pass

        veri = json.dumps(data_json['data'], indent=4)
        veri_load = json.loads(veri)

        """
        for info in range(0,len(veri_load),1):
            print("#"*50)
            print("Eczane Adi: ", veri_load[info]["isim"])
            print("Adres: ",veri_load[info]["adres"])
            print("Adres Tarifi: ",veri_load[info]["tarif"])
            print("Telefon: ",veri_load[info]["telefon"])
        """

        """
        print("\n")
        print(tabulate(veri_load, headers = data_json, showindex='always'))
        print("\n")
        print("\n")
        print(tabulate(veri_load, headers = data_json, showindex='always', tablefmt="github"))
        print("\n")
        print("\n")
        print(tabulate(veri_load, headers = data_json, showindex='always', tablefmt="grid"))
        print("\n")
        print("\n")
        print(tabulate(veri_load, headers = data_json, showindex='always', tablefmt="psql"))
        """
        
        print("\n")
        print(tabulate(veri_load, headers = data_json, showindex='always', tablefmt="pretty"))
        print("\n")
        

        

    def userInput(self):
        self.il1 = input("İl giriniz: ")
        self.ilce2 = input("İlçe giriniz: ")

        return self.il1, self.ilce2

    def ilInput(self):
        self.il = input("İl giriniz: ")
        return self.il
    def ilceInput(self):
        self.ilce = input("İlce giriniz: ")
        return self.ilce
    
ecz1 = NobetciEczane()

"""
def harf():
    a = "a"
    b = "b"

    return a, b

x , y = harf()

print(x)
print(y)
"""