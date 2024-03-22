# Sistema de login e cadastro.

nome_cadastro = "DIGITE SEU NOME"
email = "DIGITE_SEU_EMAIL@gmail.com"
senha_cadastro = 1217
codigo_PIN = "13R7G"
afirma_senha = 1217

while True: # um código de repetição de início.
    nome1 = input("Crie um nome:")
    
    if nome1 == nome_cadastro:
        print("Agora você tem que passar na etapa do email!")
        email1 = input("Crie um novo email:")
        
        
        if email1 == email:
            print("Agora você tem que passar na etapa de criar uma nova senha!")
            senha1 = int(input("Criar nova senha:"))
            confirma_senha1 = int(input("Confirme a senha novamente:"))
            autenticacao_PIN = input("Crie um 'PIN':")
            
            if senha1 == confirma_senha1 and autenticacao_PIN == codigo_PIN:
                print("Cadastro efetuado com sucesso!")
                
                while True:
                    login = input("Insira seu login:")
                    senha = int(input("insira sua senha:"))
                    
                    if login == email and senha == senha_cadastro:
                        print("Você tem que passar para uma outra etapa")
                        
                        login_de_autenticacao = input("Insira seu login de autenticação:")
                        
                        if login_de_autenticacao == codigo_PIN:
                            print("Você passou na etapa de 'Autenticação'. Agora precisamos que você afirme sua senha!")
                            
                            confirma_senha = int(input("Insira sua senha de afirmação:"))
                            
                            if confirma_senha == afirma_senha:
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

