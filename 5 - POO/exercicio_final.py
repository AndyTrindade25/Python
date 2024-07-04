from contato import Contact
from contato_agenda import ContactBook


contato_agenda = ContactBook()

while True:
    print("\n --- Opções agenda de contatos ---")
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Listar contatos")
    print("4 - Pesquisar contato")
    print("5 - Sair")


    choice = input("Digite a opção desejada: ")


    if choice == "1":
        name = input("Digite o nome do contato: ")
        phone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")

        contact = Contact(name, phone, email)
        contato_agenda.add_contact(contact)
        print("Contato adicionado com sucesso")

    elif choice == "2":
        name = input("Digite o nome do contato que deseja remover: ")
        contato_agenda.search_contact(name)
        if contact:
            contato_agenda.remove_contact(contact)
            print("Contato removido com sucesso")
        

    elif choice == "3":
        contato_agenda.display_contact()


    elif choice == "4":
        name = input("Digite o nome do contato que deseja pesquisar: ")
        contato_agenda.search_contact(name)


    elif choice == "5":
        break

    else:
        print("Opção inválida.")