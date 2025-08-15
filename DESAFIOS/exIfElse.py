from colorama import Back, Fore, Style, init

init(autoreset = True)

nome = str(input(f'{Fore.CYAN}Informe o seu usuário: '))
senha = int(input(f'{Fore.CYAN}Informe sua senha: '))

if nome == "Alex" and senha == 1234:
    print(f'\n{Fore.GREEN}Login efetuado com sucesso.')
    print(f"{Style.BRIGHT}{Fore.MAGENTA}\nSeja bem vindo {nome}!")
    print('')

else:
    print(f'\n{Fore.RED}ACESSO NEGADO, tente novamente')
    print('')
