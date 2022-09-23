import random

class Aquecedor:
    aquece = False    
    def retornaAquece():
        return Aquecedor.aquece

    def mudaAquece(aquecer: bool):
        Aquecedor.aquece = aquecer

# Função para receber dados da Temperatura
def temperatura():
    if Aquecedor.retornaAquece():
        return random.randrange(31, 36)
    else:
        return random.randrange(10, 30)

# Função para receber dados da Umidade
def umidade():
    return random.randrange(0, 100)

# Função para receber dados do Aquecedor
def aquecedor(estado: str):
    if estado == 'on':
        Aquecedor.mudaAquece(True)
        print('Aquecedor ON', '- Estufa 2')
    else:
        Aquecedor.mudaAquece(False)
        print('Aquecedor OFF', '- Estufa 2')