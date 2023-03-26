class figuras():
    def __init__(self, cor_cabelo, tipo_corte_cabelo, tem_barba, usa_oculos):
        self.cor_cabelo = cor_cabelo
        self.tipo_corte_cabelo = tipo_corte_cabelo
        self.tem_barba = tem_barba
        self.usa_oculos = usa_oculos
    
    def getCorCabelo(self):
        return self.cor_cabelo
    
    def getTipoCorteCabelo(self):
        return self.tipo_corte_cabelo
    
    def getTemBarba(self):
        return self.tem_barba
    
    def getUsaOculos(self):
        return self.usa_oculos


