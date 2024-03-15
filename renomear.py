# import re
import unicodedata
# import bs4


class Renomear:
    def __init__(self, *args, **kwargs):
        self.inf = kwargs.get('inf')
        self.editInf = kwargs.get('editInf')

    def planoMarcaModelo(self):
        self.inf = self.inf.encode('ascii', 'ignore').decode('utf8')
        for n in range(10):
            self.inf = self.inf.replace('    ', ' ')
            self.inf = self.inf.replace('   ', ' ')
            self.inf = self.inf.replace('  ', ' ')
        self.inf = self.inf.replace('	', '')
        self.inf = self.inf.replace(',', ' ')
        self.inf = self.inf.replace(';', ' ')
        self.inf = self.inf.replace('\n', '')
        self.inf = self.inf.replace(') - MULHER D+ (', ' - ')
        self.inf = self.inf.replace('PLANO INTEGRAL 24 - PLANO LIGHT 24', 'PLANO (INTEGRAL - LIGHT) 24')
        self.inf = self.inf.replace('PLANO INTEGRAL 20 - PLANO LIGHT 20', 'PLANO (INTEGRAL - LIGHT) 20')
        self.inf = self.inf.replace('PLANO INTEGRAL 15 - PLANO LIGHT 15', 'PLANO (INTEGRAL - LIGHT) 15')
        self.inf = self.inf.replace('PLANO INTEGRAL 20 - PLANO INTEGRAL 24 - PLANO LIGHT 20 - PLANO LIGHT 24', 'PLANO (INTEGRAL - LIGHT)(20 - 24)')
        self.inf = self.inf.replace('MULHER D+ (INTEGRAL - LIGHT) - PLANO (INTEGRAL - LIGHT)', '(MULHER D+ - PLANO)(INTEGRAL - LIGHT)')
        self.inf = self.inf.replace('VOLKSWAGEN', 'VW')
        self.inf = self.inf.replace('RENAULT', 'RENO')
        self.inf = self.inf.replace('KIA MOTORS', 'KIA')
        self.inf = self.inf.replace('PEUGEOT', 'PEUG')
        self.inf = self.inf.replace('MITSUBISHI', 'MITS')
        self.inf = self.inf.replace('CITROEN', 'CITR')
        self.inf = self.inf.replace('HYUNDAI', 'HYUN')
        self.inf = self.inf.replace('NISSAN', 'NISS')
        self.inf = self.inf.replace('TOYOTA', 'TOYO')
        self.inf = self.inf.replace('HONDA', 'HOND')
        self.inf = self.inf.replace('SAVEIRO', 'SAV')
        self.inf = self.inf.replace('TRENDLINE', 'TREN')
        self.inf = self.inf.replace('NTENSE', 'NTE')
        self.inf = self.inf.replace('AUTOMTICO', 'AUT')
        self.inf = self.inf.replace('AUTOMATICO', 'AUT')
        self.inf = self.inf.replace('FREEDOM', 'FRE')
        self.inf = self.inf.replace('TURBO', 'TB')
        self.inf = self.inf.replace('PREMIER', 'PREM')
        self.inf = self.inf.replace('COMFORTLINE', 'COMF')
        self.inf = self.inf.replace('RENEGADE', 'RENEG')
        self.inf = self.inf.replace('LONGITUDE', 'LONG')
        self.inf = self.inf.replace('NOVO', 'NV')
        self.inf = self.inf.replace('ENDURANCE', 'ENDU')
        self.inf = self.inf.replace('CROSS', 'CROS')
        self.inf = self.inf.replace('VOLCANO', 'VOLC')
        self.inf = self.inf.replace('HIGHLINE', 'HIGH')
        self.inf = self.inf.replace('TRAILHAWK', 'TRAI')
        self.inf = self.inf.replace('ULTIMATE', 'ULT')
        self.inf = self.inf.replace('LIMITED', 'LIMIT')
        self.inf = self.inf.replace('ECLIPSE', 'ECLIP')
        self.inf = self.inf.replace('ACTIVE', 'ACT')
        self.inf = self.inf.replace('COMPASS', 'COMP')
        self.inf = self.inf.replace('TRACKER', 'TRACK')
        return self.inf
    
    def modelo(self):
        # self.inf = self.inf.encode('ascii', 'ignore').decode('utf8')
        self.inf = self.inf.replace('  ', ' ')
        self.inf = self.inf.replace('	', '')
        # self.inf = self.inf.replace(',', ' ')
        self.inf = self.inf.replace(';', ' ')
        self.inf = self.inf.replace('\n', '')
        self.inf = self.inf.replace('VOLKSWAGEN', 'VW')
        self.inf = self.inf.replace('RENAULT', 'RENO')
        self.inf = self.inf.replace('KIA MOTORS', 'KIA')
        self.inf = self.inf.replace('PEUGEOT', 'PEUG')
        self.inf = self.inf.replace('MITSUBISHI', 'MITS')
        self.inf = self.inf.replace('CITROEN', 'CITR')
        self.inf = self.inf.replace('HYUNDAI', 'HYUN')
        self.inf = self.inf.replace('NISSAN', 'NISS')
        self.inf = self.inf.replace('TOYOTA', 'TOYO')
        self.inf = self.inf.replace('HONDA', 'HOND')
        self.inf = self.inf.replace('SAVEIRO', 'SAV')
        self.inf = self.inf.replace('TRENDLINE', 'TREN')
        self.inf = self.inf.replace('NTENSE', 'NTE')
        self.inf = self.inf.replace('AUTOMTICO', 'AUT')
        self.inf = self.inf.replace('AUTOMATICO', 'AUT')
        self.inf = self.inf.replace('FREEDOM', 'FRE')
        self.inf = self.inf.replace('TURBO', 'TB')
        self.inf = self.inf.replace('PREMIER', 'PREM')
        self.inf = self.inf.replace('COMFORTLINE', 'COMF')
        self.inf = self.inf.replace('RENEGADE', 'RENEG')
        self.inf = self.inf.replace('LONGITUDE', 'LONG')
        self.inf = self.inf.replace('NOVO', 'NV')
        self.inf = self.inf.replace('ENDURANCE', 'ENDU')
        self.inf = self.inf.replace('CROSS', 'CROS')
        self.inf = self.inf.replace('VOLCANO', 'VOLC')
        self.inf = self.inf.replace('HIGHLINE', 'HIGH')
        self.inf = self.inf.replace('TRAILHAWK', 'TRAI')
        self.inf = self.inf.replace('ULTIMATE', 'ULT')
        self.inf = self.inf.replace('LIMITED', 'LIMT')
        self.inf = self.inf.replace('ECLIPSE', 'ECLIP')
        self.inf = self.inf.replace('ACTIVE', 'ACT')
        self.inf = self.inf.replace('COMPASS', 'COMP')
        self.inf = self.inf.replace('TRACKER', 'TRACK')
        return self.inf
    
    def vazio(self):
        self.inf = str(self.inf)
        self.inf = self.inf.replace('\xa0', ' ')
        self.inf = self.inf.replace('Â ', ' ')
        self.inf = self.inf.replace('Â ', ' ')
        self.inf = self.inf.replace('Â\xa0', ' ')
        self.inf = self.inf.replace('nan', ' ')
        # self.inf = ''.join([l for l in unicodedata.normalize('NFD', self.inf) if not unicodedata.combining(l)]).casefold()
        # self.inf = unicodedata.normalize('NFD', self.inf).encode('ascii', 'ignore').decode('utf8').casefold()
        # print(f'variavel: ({self.inf})')
        # print(f'type: {type(self.inf)}')
        self.inf = self.inf.replace(' ', '')
        self.inf = self.inf.replace('vazio', '')
        return self.inf


    def valor(self):
        # self.inf = self.inf.encode('ascii', 'ignore').decode('utf8')
        self.inf = str(self.inf)
        self.inf = self.inf.replace(' ', '')
        self.inf = self.inf.replace('R$', '')
        ponto = False
        virgula = False
        for x in self.inf:
            if x == '.':
                ponto = True
            if x == ',':
                virgula = True
        if ponto is True and virgula is True:
            self.inf = self.inf.replace('.', '')
            self.inf = self.inf.replace(',', '.')
        elif virgula is True:
            self.inf = self.inf.replace(',', '.')
        return self.inf

    def pontoVirgula(self):
        self.inf = str(self.inf)
        self.inf = self.inf.replace('.', ',')       
        return self.inf
    
    def virgulaPonto(self):
        self.inf = self.inf.replace(',', '.')
        if self.inf == 'X':
            self.inf = ''
        if self.inf != '':
            self.inf = float(self.inf)
        return self.inf

    def virgulaPontoInt(self):
        self.inf = str(self.inf)
        self.inf = self.inf.replace(',', '.')
        try:
            self.inf = int(self.inf)
        except ValueError:
            pass
        self.inf = str(self.inf)
        self.inf = self.inf.replace('.', ',')
        return self.inf
    
    def tempo(self):
        self.inf = self.inf.replace('.', ',')
        return self.inf

    def coluna(self):
        self.inf = self.inf.replace(' ', '')
        self.inf = self.inf.replace('%', '')
        self.inf = self.inf.replace('º', '')
        self.inf = self.inf.replace('ª', '')
        self.inf = self.inf.replace('*', '')
        # self.inf = re.sub(r'[\u0300-\u036f]', '', unicodedata.normalize('NFD', self.inf)).casefold()  # regex
        self.inf = ''.join([l for l in unicodedata.normalize('NFD', self.inf) if not unicodedata.combining(l)]).casefold()   # fluent
        self.inf = self.inf.capitalize() 
        self.inf = self.inf.replace('ontemplacao', 'ontp')
        self.inf = self.inf.replace('onfirmacao', 'onfir')
        # self.inf = self.inf.replace('onfirmacao', 'onfm')
        self.inf = self.inf.replace('dobem', '')
        self.inf = self.inf.replace('Valor1parcela', 'Parcela1')
        self.inf = self.inf.replace('Ta', 'TA')
        self.inf = self.inf.replace('esclassificacao', 'escla')
        self.inf = self.inf.replace('Percentual','Lance')
        # self.inf = self.inf.replace('esclassificacao', 'escl')
        return self.inf
    
    def editTextoColuna(self):
        alteraInf = False
        inf1 = ''
        inf2 = ''
        for x in self.inf:
            if x == self.editInf and alteraInf is False:
                alteraInf = True
            else:
                if alteraInf is False:
                    inf1 += x
                else:
                    inf2 += x
        return inf1, inf2

    def edit_Texto3(self):
        alteraTexto = False
        text1 = ''
        text2 = ''
        nLetra = len(self.inf)
        while nLetra >= 1:
            nLetra -= 1
            x = self.inf[nLetra]
            if x == '-':
                alteraTexto = True
            else:
                if alteraTexto is False:
                    text2 = x + text2
                else:
                    text1 = x + text1
        # text2 = Renomear(inf=text2).valor()
        return text1, text2


if __name__ == '__main__':
    import main
