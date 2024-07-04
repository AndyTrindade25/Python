##Agenda de contatos
from agenda import add_contacts, view_contacts, delete_contacts


print("\n================================")
print("Seja bem vindo a sua agenda....")

while True:
    print("1 - Para adcionar contatos")
    print("2 - Listar contatos")
    print("3 - Remover contatos")
    print("4 - Para encerrar aplicação.")

    choice = input("Digite o número da opção desejada")

    if choice == "1":
        #Adcionar contato
        print("Adicionando contatos\n")
        add_contacts()
    elif choice == "2":
        #Listar contatos
        print("Listando contatos\n")
        view_contacts()
    elif choice == "3":
        #Remover contato
        print("Removendo contatos\n")
        delete_contacts()
    elif choice == "4":
        #Encerrar aplicação
        print("Encerrando a aplicação...")
    else:
        print("Opção inválida!")