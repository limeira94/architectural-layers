from model.livro import Livro
from view.visao import Visao
from controller.controlador import Controlador


def main():
    
    # Criando instâncias de modelo e visão
    livro = Livro("Dom Casmurro", "Machado de Assis")
    visao = Visao()

    # Criando a instância do controlador e passando o modelo e a visão para ele
    controlador = Controlador(livro, visao)

    # Interagindo com o controlador
    controlador.exibir_detalhes()
    controlador.definir_detalhes_livro("Memórias Póstumas de Brás Cubas", "Machado de Assis")
    controlador.exibir_detalhes()
    
    
if __name__ == '__main__':
    main()