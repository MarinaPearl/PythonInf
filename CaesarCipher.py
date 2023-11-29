
def caesar_cipher(text, shift, language):
    result = ""
    alphabet = ""

    if language.lower() == "en":
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif language.lower() == "ru":
        alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else:
        print("Нет такого языка...")
        return

    for char in text:
        if char.upper() in alphabet:
            is_upper = char.isupper()
            index = (alphabet.index(char.upper()) + shift) % len(alphabet)
            if is_upper:
                result += alphabet[index]
            else:
                result += alphabet[index].lower()
        else:
            result += char

    return result


def write_file():
    try:
        input_file_path = input("Введите путь до файла: ")
        shift = int(input("Введите сдвиг: "))
        language = input("Введите язык (en/ru): ")

        with open(input_file_path, "r", encoding="utf-8") as file:
            text = file.read()

        encrypted_text = caesar_cipher(text, shift, language)

        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(encrypted_text)

    except Exception as e:
        print("УУПС, что-то пошло не так", e)


if __name__ == "__main__":
    write_file()