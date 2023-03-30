class figuras():
    def __init__(self, nome, cor_cabelo, tipo_corte_cabelo, tem_barba, usa_oculos):
        self.nome = nome
        self.cor_cabelo = cor_cabelo
        self.tipo_corte_cabelo = tipo_corte_cabelo
        self.tem_barba = tem_barba
        self.usa_oculos = usa_oculos
    
    def getCorCabelo(self):
        return self.cor_cabelo.value
    
    def getTipoCorteCabelo(self):
        return self.tipo_corte_cabelo.value
    
    def getTemBarba(self):
        return self.tem_barba.value
    
    def getUsaOculos(self):
        return self.usa_oculos.value

    def getNome(self):
        return self.nome


