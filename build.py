from os import listdir
from subprocess import run
from shared import SRC_ROOT, SRC_PATH, EXT


OUT_PATH = f"{SRC_ROOT}/.bin"
CC = "gcc"


def compile(source_file):
    cmd = f"{CC} {SRC_PATH}/{source_file}{EXT} -o {OUT_PATH}/{source_file}"
    run(cmd, shell=True)


def build_source():
    entries = listdir(SRC_PATH)
    for e in entries:
        compile(e[:-len(EXT)])


if __name__ == "__main__":
    build_source()
