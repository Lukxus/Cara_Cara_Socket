import Classes.figuras
import Enums.figuras

def gerando_caras():
    caras = {
        "Luba" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto.name, 
                                        Enums.figuras.tipo_corte_cabelo.Liso.name,
                                        Enums.figuras.tem_barba.Verdadeiro.name,
                                        Enums.figuras.usa_oculos.Verdadeiro.name) , 
        "Kishimoto" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto.name, 
                                        Enums.figuras.tipo_corte_cabelo.Raspado,
                                        Enums.figuras.tem_barba.Verdadeiro.name,
                                        Enums.figuras.usa_oculos.Verdadeiro.name) , 
        "Orlando" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Cinza.name, 
                                        Enums.figuras.tipo_corte_cabelo.Liso.name,
                                        Enums.figuras.tem_barba.Falso.name,
                                        Enums.figuras.usa_oculos.Falso.name),
        "Gustavo" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto.name, 
                                        Enums.figuras.tipo_corte_cabelo.Baixo.name,
                                        Enums.figuras.tem_barba.Falso.name,
                                        Enums.figuras.usa_oculos.Verdadeiro.name) , 
        "Jamilson" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto.name, 
                                        Enums.figuras.tipo_corte_cabelo.Calvo.name,
                                        Enums.figuras.tem_barba.Verdadeiro.name,
                                        Enums.figuras.usa_oculos.Falso.name) , 
        "Leonardo" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto.name, 
                                        Enums.figuras.tipo_corte_cabelo.Liso.name,
                                        Enums.figuras.tem_barba.Falso.name,
                                        Enums.figuras.usa_oculos.Falso.name)
    }
    return caras