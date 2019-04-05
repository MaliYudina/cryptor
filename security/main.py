from user.user_interface import Interface
from reader.reader import Reader
from serialize.serialize import Parser
from cryptor.cryptor import Crypt


user_command = {
    'collect': Interface.collect_input(),
    'display': Interface.display_record(),
    'del': Interface.delete_record(),
    'encrypt': Crypt.encrypt(),
    'decrypt': Crypt.decrypt(),
}


def _main():
    # 1. чтение пользовательского ввода
    file_route = ''
    user_raw_data = Reader.read(file_route)
    yaml_result = Reader.write_result(user_raw_data)

    # 2. сериализация yml в бинарные строки
    deserialized = Parser.yaml_to_string(yaml_result)

    # 3. (1.)шифрование пользовательских данных
    # или (2.)дешифрование, в зависимости от выбора пользователя
    encrypted = Crypt.encrypt(deserialized)

    # в каком виде хранятся зашифрованные данные?
    # как их десериализовать перед дешифровкой?
    decrypted_string = Crypt.decrypt(file_with_encrypted)
    deserialized = Parser.deserialize(decrypted_string)


if __name__ == '__main__':
    _main()
