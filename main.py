from turtle import ht
import requests
from bs4 import BeautifulSoup
import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


class NobetciEczane:
    def __init__(self):
        self.il = self.ilInput()
        self.ilce = self.ilceInput()

        self.il     = self.il.replace('İ', "i").lower()
        self.ilce   = self.ilce.lower()

        tr_alphabet  = str.maketrans(" .,-*/+-ıİüÜöÖçÇşŞğĞ", "________iIuUoOcCsSgG")
        self.il     = self.il.translate(tr_alphabet)
        self.ilce    = self.ilce.translate(tr_alphabet)

        """
        tempil = self.ilInput()
        print(tempil)
        tempilce = self.ilceInput()
        print(tempilce)
        """

        source  = "eczaneler.gen.tr"
        self.url     = f"https://www.eczaneler.gen.tr/nobetci-{self.il}-{self.ilce}"
        request   = requests.get(self.url, headers=headers)

        soup = BeautifulSoup(request.content, "lxml")
        eczaneler = soup.find('div', id='nav-bugun')

        data_json = {"source": source, 'data' : []}

        try:
            for bak in eczaneler.findAll('tr')[1:]:
                isim    = bak.find('span', class_='isim').text
                mah   = (None if bak.find('div', class_='my-2') is None else bak.find('div', class_='my-2').text)
                adres = bak.find('div', class_='col-lg-6').text
                tarif = (None if bak.find('span', class_='text-secondary font-italic') is None else bak.find('span', class_='text-secondary font-italic').text)
                tel  = bak.find('div', class_='col-lg-3 py-lg-2').text

                data_json['data'].append({
                    'ad'        : isim,
                    'mahalle'   : mah,
                    'adres'     : adres,
                    'tarif'     : tarif,
                    'telefon'   : tel
                })
            print("for bitti")
        except AttributeError:
            pass

        print(data_json)
        print("*"*50)
        print(type(data_json))
        print("*"*50)
        print(data_json['data'])
        print("*"*50)
        print(data_json['source'])
        print("*"*50)
        dataeczanee = data_json['data']
        print(dataeczanee)
        print("*"*50)
        print(type(dataeczanee))
        print("*"*50)
        
        print(data_json['data'][0])
        print("*"*50)
        #print(data_json['data']['ad'])
        print("*"*50)
        #print(dataeczanee['ad'])
        #print(data_json['ad'])

        print("="*50)
        print(type(data_json))
        for i in data_json['data']:
            print(i)
        print("="*50)
        print("="*50)
        print("="*50)
        
        print("%"*50)
        veri = json.dumps(data_json['data'], indent=4)
        print(type(veri))
        print(veri)
        print("%"*50)
        #print(veri['ad'])
        print("?"*50)

        veri_load = json.loads(veri)
        print(veri_load)
        print("?"*50)
        print("Eczane Adi: ", veri_load[0]["ad"])
        print("Mahalle Adi: ",veri_load[0]["mahalle"])
        print("Adres: ",veri_load[0]["adres"])
        print("Adres Tarifi: ",veri_load[0]["tarif"])
        print("Telefon: ",veri_load[0]["telefon"])


    def userInput(self):
        il = input("İl giriniz: ")
        ilce = input("İlçe giriniz: ")

    def ilInput(self):
        self.il = input("İl giriniz: ")
        return self.il
    def ilceInput(self):
        self.ilce = input("İlce giriniz: ")
        return self.ilce
    




"""
il = input("İl giriniz: ")
ilce = input("İlçe giriniz: ")
"""

ecz1 = NobetciEczane()

