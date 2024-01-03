from model.livro import Livro
from view.visao import Visao


class Controlador:
    """Controldor para manter o fluxo entre modelo e visão"""
    def __init__(self, livro, visao):
        self.livro = livro
        self.visao = visao
        
    def exibir_detalhes(self):
        """Obtém detalhes do livro e solicita a visão que os exiba."""
        titulo, autor = self.livro.titulo, self.livro.autor
        self.visao.exibir_detalhes_livro(titulo, autor)
        
    def definir_detalhes_livro(self, titulo, autor):
        """Define os detalhes do livro."""
        if titulo and autor:
            self.livro.titulo = titulo
            self.livro.autor = autor
            self.visao.exibir_mensagem("Destalhes do livro atualizado")
        else:
            self.visao.exibir_mensagem("Erro: título e autor são obrigatórios")
            
            