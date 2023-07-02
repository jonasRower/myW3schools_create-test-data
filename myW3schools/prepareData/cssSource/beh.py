import vytvarejSoubory
import dataProKeyValue

class nacitejCss:

    def __init__(self, adresaKamZapisovatData, adresaCss):

        dataCssArr = self.nactiHtml(adresaCss)
        radkyBezKomentaru = self.vytvorPoleBezKomentaru(dataCssArr)

        klicHodnotaArr = self.vytvorPoleKlicHodnota(radkyBezKomentaru)
        poleKlicu = self.vytvorPole1D(klicHodnotaArr, 0)
        polehodnot = self.vytvorPole1D(klicHodnotaArr, 1)
        poleKlicuUniq = self.unique(poleKlicu)

        poleVsechKlicuIndexu = self.vratPoleIndexuDleJednotlivychKlicu(poleKlicu, poleKlicuUniq)
        pocetIndexuArr = self.ziskejPocetIndexuArr(poleVsechKlicuIndexu)
        ocislovaneHtmlAll = self.vratPoleNazvuSouboruHtml(poleKlicuUniq, pocetIndexuArr)

        dataProKeyValue.vytvarejDataProKeyValueCsv(poleKlicuUniq, poleVsechKlicuIndexu, polehodnot, adresaKamZapisovatData)


        #vytvari souborovou strukturu - prazdne soubory
        vytvarejSoubory.vytvareniSouboroveStruktury(ocislovaneHtmlAll, adresaKamZapisovatData)

        print()


    def vratPoleNazvuSouboruHtml(self, poleKlicuUniq, pocetIndexuArr):

        ocislovaneHtmlAll = []

        for i in range(0, len(pocetIndexuArr)):
            pocetIndexu = pocetIndexuArr[i]
            nazevKlice = poleKlicuUniq[i]

            ocislovaneHtml = self.vratOcislovaneHtml(nazevKlice, pocetIndexu)
            ocislovaneHtmlAll.append(ocislovaneHtml)

        return(ocislovaneHtmlAll)


    def vratOcislovaneHtml(self, nazevKlice, pocetIndexu):

        ocislovaneHtml = []

        for i in range(1, pocetIndexu):
            cislo = i
            nazevHtml = nazevKlice + '_' + str(cislo) + '.html'
            ocislovaneHtml.append(nazevHtml)

        return(ocislovaneHtml)


    def ziskejPocetIndexuArr(self, poleVsechKlicuIndexu):

        pocetIndexuArr = []

        for i in range(0, len(poleVsechKlicuIndexu)):
            indexyArr = poleVsechKlicuIndexu[i]
            pocetIndexu = self.ziskejPocetIndexu(indexyArr)
            pocetIndexuArr.append(pocetIndexu)

        return(pocetIndexuArr)


    def ziskejPocetIndexu(self, indexyArr):

        pocetIndexu = len(indexyArr)
        return(pocetIndexu)


    def vratPoleIndexuDleJednotlivychKlicu(self, poleKlicu, poleKlicuUniq):

        poleVsechKlicuIndexu = []

        for i in range(0, len(poleKlicuUniq)):
            klicUniq = poleKlicuUniq[i]
            poleIndexu = self.vratPoleVsechIndexu(poleKlicu, klicUniq)
            poleVsechKlicuIndexu.append(poleIndexu)

        return(poleVsechKlicuIndexu)


    def vratPoleVsechIndexu(self, poleKlicu, nazevKliceExp):

        poleIndexu = []

        for i in range(0, len(poleKlicu)):
            nazevKlice = poleKlicu[i]

            if(nazevKlice == nazevKliceExp):
                poleIndexu.append(i)

        return(poleIndexu)


    def vytvorPole1D(self, pole2D, index):

        pole1D = []

        for i in range(0, len(pole2D)):
            radek = pole2D[i]
            try:
                polozka = radek[index]
            except:
                polozka = ""

            pole1D.append(polozka)

        return(pole1D)


    def vytvorPoleKlicHodnota(self, radkyBezKomentaru):

        klicHodnotaArr = []

        for i in range(0, len(radkyBezKomentaru)):
            radek = radkyBezKomentaru[i]
            klicHodnota = radek.split(':')
            klicHodnotaNew = self.trimArr(klicHodnota)
            klicHodnotaArr.append(klicHodnotaNew)

        return(klicHodnotaArr)


    def trimArr(self, klicHodnota):

        klicHodnotaNew = []

        for i in range(0, len(klicHodnota)):
            polozka = klicHodnota[i]
            polozkaNew = polozka.strip()

            klicHodnotaNew.append(polozkaNew)

        return(klicHodnotaNew)



    def vytvorPoleBezKomentaru(self, dataCssArr):

        radkyBezKomentaru = []

        for i in range(0, len(dataCssArr)):
            radek = dataCssArr[i]
            radekObsahujeKomentar = self.detekujZdaRadekObsahujeSubstr(radek, '/*')

            if(radekObsahujeKomentar == False):
                radekObsahujeKomentar = self.detekujZdaRadekObsahujeSubstr(radek, '*/')

            if(radekObsahujeKomentar == False):
                radkyBezKomentaru.append(radek)

        return(radkyBezKomentaru)



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



    def nactiHtml(self, adresaCss):

        pole = []

        #adresaHtml = adresaHtml.replace('/', '\\')

        try:
            r = -1
            with open(adresaCss, 'r') as f:
                for line in f:
                    r = r + 1

                    pole.append(line)
        except:
            pole.append(False)


        return (pole)



    def unique(self, list1):

        # initialize a null list
        unique_list = []

        # traverse for all elements
        for x in list1:
            # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)

        return (unique_list)