import getpass # Privacidade na senha.
import bcrypt # Mais privacidade, e prevenir ataques cibernéticas, ele vai criptografar as senhas no banco de dadoa
import os 


def cadastro():
    cadastro_email = input('Digite seu email: ')
    cadastro_senha = getpass.getpass('Digite sua senha: ')
    cadastro_regiao = input('Digite sua região: ')
    senha_hash = bcrypt.hashpw(cadastro_senha.encode(), bcrypt.gensalt())
    print()
    with open('banco_de_dados.txt', 'a') as arquivo1:
        arquivo1.write(f'Email: {cadastro_email}, Senha: {senha_hash.decode()}, Região: {cadastro_regiao}\n')

def login(email, senha):
    if not os.path.exists('banco_de_dados.txt'):
        return False
    with open('banco_de_dados.txt', 'r') as arquivo2:
        for line in arquivo2:
            if line.strip():
                armazenar_email, armazenar_senha, _ = line.strip().split(', ')
                if armazenar_email.split(': ')[1] == email:
                    senha_hash = armazenar_senha.split(': ')[1].encode()
                    if bcrypt.checkpw(senha.encode(), senha_hash):
                        return True    
    return False

def verificar():
    if not os.path.exists('banco_de_dados.txt'):
        print('Nenhum usuário cadastrado.')
        return
    print('Usuários cadastrados:')
    with open('banco_de_dados.txt', 'r') as arquivo3:
        for linha in arquivo3:
            armazenar_email, _, armazenar_regiao = linha.strip().split(', ')
            print(f'Email: {armazenar_email.split(": ")[1]}, Região: {armazenar_regiao.split(": ")[1]}')
    print()

def remover():
        with open('banco_de_dados.txt', 'w') as arquivo4:
            arquivo4.write('')

while True:
    # Opções do Usuario
    print('1. Cadastro')
    print('2. Login')
    print('3. Verificar')
    print('4. remover dados')
    print('0. sair')

    try:
        escolha = input('\nEscolha uma opção: ')
    
        if escolha == '1':
            cadastro()
            print('Cadastro feito com sucesso.')
        elif escolha == '2':
            login_email = input('Digite seu email: ')
            login_senha = getpass.getpass('Digite sua senha: ')
            if login(login_email == login_senha):
                print('Login Feito com sucesso.')
            else:
                print('Login invalido.')
        elif escolha == '3':
            verificar()
        elif escolha == '4':
            remover()
            print('Removendo dados.')
        elif escolha == '0':
            print('Saindo...')
            break
        else:
            print('\nOpção inválida.\n')
    except (ValueError, KeyboardInterrupt):
        print('\n\nProcesso interrompido pelo Usuario :(\n')
        continue

"""
Para compilar esse programa, segue esse passo a passo:
1. Abra o terminal do seu pc windows, Linux ou Mac...
2. Digite: pip install pyinstaller
3. No seu terminal msm vai até o diretorio onde se encontrar o seu script. Digite no seu terminal: pyinstaller --onefile nome_do_seu_script.py 
Exemplo:
   pyinstaller --onefile Projeto_de_ogin_completo.py
   
5. Vai até o diretorio que você compilou.  
4. procure pela pasta "dist", e lá dentro estara o programa compilado.


"""
