import os


class vytvareniSouboroveStruktury:

    def __init__(self, ocislovaneHtmlAll, adresaKamZapisovatData):

        self.adresaGenerovane = adresaKamZapisovatData
        self.vytvarejVsechnySoubory(ocislovaneHtmlAll)


    def vytvarejVsechnySoubory(self, ocislovaneHtmlAll):

        for i in range(0, len(ocislovaneHtmlAll)):
            souboryVJedneSlozce = ocislovaneHtmlAll[i]
            self.vytvarejSouboryVJedneSlozce(souboryVJedneSlozce)


    def vytvarejSouboryVJedneSlozce(self, souboryVJedneSlozce):

        for i in range(0, len(souboryVJedneSlozce)):
            nazevSouboru = souboryVJedneSlozce[i]
            prvniPismeno = nazevSouboru[0]

            if(prvniPismeno != '_'):
                if(i == 0):
                    nazevSlozky = self.ziskejNazevSlozky(nazevSouboru)
                    nazevSlozkyComplet = self.adresaGenerovane + nazevSlozky

                    #vytvori slozku
                    try:
                        os.mkdir(nazevSlozkyComplet)
                    except:
                        slozkaJizExistuje = True

                nazevSouboruComplet = nazevSlozkyComplet + '\\' + nazevSouboru
                self.vytvorSoubor(nazevSouboruComplet)


    # ziska nazev slozky, tak aby ji mohl vytvaret
    def ziskejNazevSlozky(self, nazevSouboru):

        nazevSouboruSpl = nazevSouboru.split('_')
        nazevSlozky = nazevSouboruSpl[0]

        return(nazevSlozky)



    def vytvorSoubor(self, nazevSouboru):

        # Creating a file at specified location
        with open(nazevSouboru, 'w') as fp:
            pass
            # To write data to new file uncomment
            # this fp.write("New file created")