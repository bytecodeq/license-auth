import os

class Utils:
    def __init__(self):
        self.clear = self._clear

    def _clear(self):
        os.system('cls')

keys  = {
    "ABCDEFGJKLMNOP",
    "AJXIUEKASLX",
    "AJUEUIAKKZ",
    "ISOEOZMMSK",
    "IEIOWKAMNZ"
}

def main():
    utils = Utils()
    utils.clear()
    key = input("Your key: ")

    if key in keys:
        valid(key)
    else:
        invalid(key)

def valid(key):
    while True:
        print(f"Succes -> Your key is valid | {key}")

def invalid(key):
    while True:
        print(f"Failure -> Your key is invalid | {key}")

if __name__ == "__main__":
    main()
