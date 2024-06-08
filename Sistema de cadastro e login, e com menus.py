# Sistema de login e cadastro, em outro dispositivo.

nome_cadastro = "Digite_seu_nome"
email = "Digite_seu_email@gmail.com"
senha = 1317
codigo_PIN = "13R7G"


while True: # um código de repetição de início.
    nome1 = input("Crie um nome: ")
    
    if nome1 == nome_cadastro:
        print("Agora você tem que passar na etapa do email!")
        email1 = input("Crie um novo email: ")
        
        
        if email1 == email:
            print("Agora você tem que passar na etapa de criar uma nova senha!")
            senha1 = int(input("Criar nova senha:"))
            confirma_senha1 = int(input("Confirme a senha novamente: "))
            autenticacao_PIN = input("Crie um 'PIN': ")
            
            if senha1 == confirma_senha1 and autenticacao_PIN == codigo_PIN:
                print("Cadastro efetuado com sucesso!")
                
                while True:
                    login = input("Insira seu login: ")
                    senha = int(input("insira sua senha: "))
                    
                    if login == email and senha == senha:
                        print("Você tem que passar para uma outra etapa")
                        
                        login_de_autenticacao = input("Insira seu login de autenticação: ")
                        
                        if login_de_autenticacao == codigo_PIN:
                            print("Você passou na etapa de 'Autenticação'. Agora precisamos que você afirme sua senha!")
                            
                            confirma_senha = int(input("Insira sua senha de afirmação: "))
                            
                            if confirma_senha == senha:
                                print("Você acessou sua 'Conta'!")
                                break  # Saída do loop de repetição! 
                            else:
                                print("Senha inválida!")
                        else:
                            print("Autenticação inválida!")
                    else:
                        print("Login ou Senha Inválida") 
            else:
                print("Cadastro Inválido, ou autenticação inválida!")
        else:
            print("Já tem algum outro usuário com esse, tente novamente")
    else:
        print("Já tem um usuário com esse nome!")
    break

# 'Aba' do Usuario.
Usuario1 = ('Home','Notificação','Histórico','Configuração')
while True:
    Usuario2 = input('Insira uma aba: ')
    if Usuario2 in Usuario1:
        print(f'Você acessou {Usuario2}')
        break
    else:
        print('Aba não encontrado!')
