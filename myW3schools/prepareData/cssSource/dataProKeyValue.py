class vytvarejDataProKeyValueCsv:

    def __init__(self, poleKlicuUniq, poleVsechKlicuIndexu, polehodnot, adresaKamZapisovatData):

        dataKCsv = self.vytvarejDataKCsv(poleKlicuUniq, poleVsechKlicuIndexu, polehodnot)
        dataCsvRadkyAll = self.vytvarejPoleRadkuCsv(dataKCsv)

        nazevSouboruCsv = adresaKamZapisovatData + '\\keyValue.csv'

        self.tiskniCsv(dataCsvRadkyAll, nazevSouboruCsv)
        print()


    def vytvarejPoleRadkuCsv(self, dataKCsv):

        dataCsvRadkyAll = []

        for i in range(0, len(dataKCsv)):
            dataJednohoKlice = dataKCsv[i]
            dataCsvRadky = self.vratPoleRadkuJednohoKlice(dataJednohoKlice)
            dataCsvRadkyAll = dataCsvRadkyAll + dataCsvRadky

        dataCsvRadkyAll.append('%%%%%%%%%%')

        return(dataCsvRadkyAll)



    def vratPoleRadkuJednohoKlice(self, dataJednohoKlice):

        poleRadkuJednohoKlice = []
        nazevKlice = dataJednohoKlice[0]

        poleRadkuJednohoKlice.append('%%%%%%%%%%')
        poleRadkuJednohoKlice.append(nazevKlice)
        poleRadkuJednohoKlice.append('----------')

        for i in range(1, len(dataJednohoKlice)):
            hodnoty = dataJednohoKlice[i]
            poleRadkuJednohoKlice.append(hodnoty)

        return(poleRadkuJednohoKlice)


    def vytvarejDataKCsv(self, poleKlicuUniq, poleVsechKlicuIndexu, polehodnot):

        dataKCsv = []

        for i in range(0, len(poleKlicuUniq)):
            klic = poleKlicuUniq[i]
            if(klic != ''):
                vsechnyIndexyKlice = poleVsechKlicuIndexu[i]
                hodnotyKeKlici = self.vratPoleVsechHodnotKeKlici(vsechnyIndexyKlice, polehodnot, klic)

                dataKCsv.append(hodnotyKeKlici)

        return(dataKCsv)


    def vratPoleVsechHodnotKeKlici(self, vsechnyIndexyKlice, polehodnot, klic):

        hodnotyKeKlici = []
        hodnotyKeKlici.append(klic)

        for i in range(0, len(vsechnyIndexyKlice)):
            index = vsechnyIndexyKlice[i]
            hodnota = polehodnot[index]

            hodnotaJizExistujeVPoli = self.detekujPolozkuVPoli(hodnotyKeKlici, hodnota)

            #pokud hodnota jeste neni zapsana v poli, pak se zapise
            if(hodnotaJizExistujeVPoli == False):

                # muze obsahovat rgb(255, 255, 255), pak je treba pridat uvozovky
                hodnotaObsahujeZavorku = self.detekujZdaRadekObsahujeSubstr(hodnota, '(')
                if(hodnotaObsahujeZavorku == True):
                    hodnota = '"' + hodnota + '"'
                else:
                    # pokud je vice clenu css pak se k mezeram pridavaji carky, aby se csv zapisovalo do dalsich bunek na radku
                    hodnota = hodnota.replace(' ', ', ')

                # odmaze strednik
                hodnota = hodnota.replace(';', '')
                hodnotyKeKlici.append(hodnota)


        return(hodnotyKeKlici)



    def detekujPolozkuVPoli(self, pole, polozkaExp):

        poleObsahujePolozku = False
        polozkaExp = polozkaExp.replace(';', '')

        for polozka in pole:
            if (polozka == polozkaExp):
                poleObsahujePolozku = True
                break

        return(poleObsahujePolozku)


    def detekujZdaRadekObsahujeSubstr(self, radek, substr):

        radek = radek.lower()

        try:
            ind = radek.index(substr)
            if (ind > -1):
                radekObsahujeSubstr = True
            else:
                radekObsahujeSubstr = False

        except:
            radekObsahujeSubstr = False

        return (radekObsahujeSubstr)


    def tiskniCsv(self, dataKTisku, nazevSouboru):

        dataWrite = ""

        f = open(nazevSouboru, 'w')

        for i in range(0, len(dataKTisku)):
            radek = str(dataKTisku[i])
            dataWrite = dataWrite + radek + '\n'

        f.write(dataWrite)
        f.close()

    print("")