from model.dados_geo import DadosGeo
from view.mapa_gui import MapaGUI


class MapaController:
    def __init__(self, file_path):
        self.modelo = DadosGeo(file_path)
        self.visao = MapaGUI()
        
    
    def exibir_mapa(self):
        self.modelo.carregar_dados()
        dados = self.modelo.get_dados()
        self.visao.criar_mapa(dados)
        
