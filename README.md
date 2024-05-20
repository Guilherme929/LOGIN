# Etapa de opções
print('1. Registrar')
print('2. Verificar')
print('0. Remover')
escolha = int(input('Escolha uma das opções: '))

# Função de registros, para registrar
def registrar():
    nome_pacientes = input('Digite o nome do paciente: ')
    numero_paciente = int(input('Digite o numero do paciente: '))
    with open('Registros.txt', 'a') as arquivo:
        arquivo.write(f'Paciente: {nome_pacientes}, \n Numero: {numero_paciente}')

# Função verificar o que esta dentro do arquivo.
def verificar():
    with open('Registros.txt', 'r') as arquivo2:
        linha = arquivo2.read()
        print(linha)
        return linha
    
# Remover o conteudo que esta dentro do arquivo.
def remover():
    with open('Registros.txt', 'w') as arquivo3:
        arquivo3.write('')

while True:
    # Parte de decisão, e chamar as funções 
    if escolha == 1:
        registrar() # chamando funções
        print('Registro feito com sucesso!')
    elif escolha == 2:
        verificar() # chamando funções
    elif escolha == 0:
        remover() # chamando funções
        break
    else:
        print('Opção Invalida.') # encerrando.
