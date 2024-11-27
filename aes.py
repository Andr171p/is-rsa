from cryptography.fernet import Fernet
from pathlib import Path
from typing import List, Optional


key: bytes = Fernet.generate_key()


def read_file(path: Path | str) -> List[bytes]:
    with open(
        file=path,
        mode='rb'
    ) as file:
        return file.readlines()


def save_file(data: bytes) -> bool:
    with open(
        file="output.enc",
        mode='wb'
    ) as file:
        file.write(data)
        return True


def encrypt(data: List[bytes], key: Fernet) -> bytes:
    rows: Optional[List[bytes]] = []
    for row in data:
        rows.append(key.encrypt(row))
    return b''.join(rows)


def decrypt(data: bytes, key: Fernet) -> bytes:
    return key.decrypt(data)


def main() -> None:
    data = read_file(path=r'C:\Users\andre\IS\input.txt')
    encrypted = encrypt(
        data=data,
        key=Fernet(key)
    )
    bool_var = save_file(data=encrypted)
    if bool_var:
        print("Файл сохранён")
    print(decrypt(data=encrypted, key=Fernet(key)))


if __name__ == "__main__":
    main()
