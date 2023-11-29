
def caesar_cipher(input_text, shift, language):
    result_coder = ""
    alphabet = ""

    if language.lower() == "en":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif language.lower() == "ru":
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else:
        print("Нет такого языка...")
        return

    for char in input_text:
        if char.upper() in alphabet:
            is_upper = char.isupper()
            index = (alphabet.index(char.upper()) + shift) % len(alphabet)
            if is_upper:
                result_coder += alphabet[index]
            else:
                result_coder += alphabet[index].lower()
        else:
            result_coder += char

    return result_coder


def write_to_file():
    try:
        input_file_path = input("Введите путь до файла: ")
        shift = int(input("Введите сдвиг(число): "))
        language = input("Введите язык (en/ru): ")

        with open(input_file_path, "r", encoding="utf-8") as file:
            input_text = file.read()

        encrypted_text = caesar_cipher(input_text, shift, language)

        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(encrypted_text)

    except Exception as e:
        print("Ошибка, попробуйте снова", e)


if __name__ == "__main__":
    write_to_file()