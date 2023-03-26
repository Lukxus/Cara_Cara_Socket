import Classes.figuras
import Enums.figuras

def gerando_caras():
    caras = {
        "Luba" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto, 
                                        Enums.figuras.tipo_corte_cabelo.Liso,
                                        Enums.figuras.tem_barba.Verdadeiro,
                                        Enums.figuras.usa_oculos.Verdadeiro) , 
        "Kishimoto" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto, 
                                        Enums.figuras.tipo_corte_cabelo.Raspado,
                                        Enums.figuras.tem_barba.Verdadeiro,
                                        Enums.figuras.usa_oculos.Verdadeiro) , 
        "Orlando" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Cinza, 
                                        Enums.figuras.tipo_corte_cabelo.Liso,
                                        Enums.figuras.tem_barba.Falso,
                                        Enums.figuras.usa_oculos.Falso),
        "Gustavo" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto, 
                                        Enums.figuras.tipo_corte_cabelo.Baixo,
                                        Enums.figuras.tem_barba.Falso,
                                        Enums.figuras.usa_oculos.Verdadeiro) , 
        "Jamilson" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto, 
                                        Enums.figuras.tipo_corte_cabelo.Calvo,
                                        Enums.figuras.tem_barba.Verdadeiro,
                                        Enums.figuras.usa_oculos.Falso) , 
        "Leonardo" : Classes.figuras.figuras(Enums.figuras.cor_cabelo.Preto, 
                                        Enums.figuras.tipo_corte_cabelo.Liso,
                                        Enums.figuras.tem_barba.Falso,
                                        Enums.figuras.usa_oculos.Falso)
    }
    return caras