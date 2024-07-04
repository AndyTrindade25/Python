import os 


def add_contacts():
    name = input("Informe o nome do contato:\n")
    address = input("Informe o endereço do contato:\n")
    phone = input("Informe o telefone do contato:\n")


    contact = f"Nome: {name} | Telefone: {phone} | Endereço: {address}"

    with open("dados/contacts.txt", "a") as file:
        file.write(contact)
        print("Contatos adicionado com sucesso!")


def view_contacts():
    if not os.path.exists("dados/contacts.txt"):
        print("A lista de contatos está vázia...")
        return
    
    with open("dados/contacts.txt", "r") as file:
        contacts = file.read()

    print("Lista de contatos")
    print(contacts)


def delete_contacts():
    if not os.path.exists("dados/contacts.txt"):
        print("Lista de contatos está vázia")
        return
    with open("dados/contacts.txt", "w") as file:
        file.write("")
    print("Contatos excluidos com sucesso!")

