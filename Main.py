def read_phonebook(filename="phonebook.txt"):
    """Эта функция считывает телефонный справочник из файла."""
    with open(filename, "a+"):
        pass

    with open(filename, "r") as file:
        lines = file.readlines()

    phonebook = {}
    for line in lines:
        surname, name, phone = line.strip().split(";")
        phonebook[surname] = (name, phone)
    return phonebook


def write_phonebook(phonebook, filename="phonebook.txt"):
    """А эта Записывает телефонный справочник в файл."""
    with open(filename, "w") as file:
        for surname, (name, phone) in phonebook.items():
            file.write(f"{surname};{name};{phone}\n")


def add_entry(surname, name, phone):
    phonebook = read_phonebook()
    phonebook[surname] = (name, phone)
    write_phonebook(phonebook)


def update_entry(surname, name=None, phone=None):
    phonebook = read_phonebook()
    if surname in phonebook:
        current_name, current_phone = phonebook[surname]
        phonebook[surname] = (name if name else current_name, phone if phone else current_phone)
        write_phonebook(phonebook)


def delete_entry(surname):
    phonebook = read_phonebook()
    if surname in phonebook:
        del phonebook[surname]
        write_phonebook(phonebook)


def find_entry(surname):
    phonebook = read_phonebook()
    return phonebook.get(surname, None)