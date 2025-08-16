from colorama import Back, Fore, Style, init

init(autoreset = True)

username = 'Alex'
password = '1234'

nome = str(input(f'{Fore.CYAN}Informe o seu usuário: '))
senha = str(input(f'{Fore.CYAN}Informe sua senha: '))

if nome == username and senha == password:
    print(f'\n{Fore.GREEN}Login efetuado com sucesso.')
    print(f"{Style.BRIGHT}{Fore.MAGENTA}\nSeja bem vindo {nome}!")
    print('')

else:
    print(f'\n{Fore.RED}{Style.BRIGHT}{Back.YELLOW} ACESSO NEGADO, tente novamente ')
    print('')