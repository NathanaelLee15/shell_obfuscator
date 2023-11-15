
from os import mkdir
from os.path import exists


def setup():
    if not exists("./src"):
        mkdir("./src")

    if not exists("./scripts"):
        mkdir("./scripts")
        
    if not exists("./.bin"):
        mkdir("./.bin")

if __name__ == "__main__":
    setup()
