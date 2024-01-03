
class Livro:
    """Modelo que representa um livro"""
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def get_detalhes(self):
        """Retorna detalhes do livros"""
        return f"Livro: {self.titulo}, Autor: {self.autor}"
    
    