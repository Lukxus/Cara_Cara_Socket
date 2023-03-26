from enum import Enum

cor_cabelo = Enum("cor_cabelo", [("Preto", 1), ("Cinza", 2), ("Marrom", 3)])
tipo_corte_cabelo = Enum("tipo_corte_cabelo", [("Calvo", 1), ("Raspado", 2), ("Liso", 3), ("Baixo", 4)])
tem_barba = Enum("tem_barba", [("Verdadeiro", True), ("Falso", False)])
usa_oculos = Enum("usa_oculos", [("Verdadeiro",True), ("Falso", False)])