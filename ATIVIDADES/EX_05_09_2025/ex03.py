while True:

    usuario = str(input("Informe o seu nome de usuário: "))
    senha = str(input("Informe o sua senha: "))

    if usuario in senha:
        print("Sua senha não pode conter partes do seu usuário")

    else:
        print("Cadastro realizado com sucesso")
        break

