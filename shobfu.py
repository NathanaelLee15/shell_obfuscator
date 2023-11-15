
from shared import make_obfuscation
from build import compile


if __name__ == "__main__":
    from sys import argv

    if len(argv) > 2:
        the_file    = argv[1]
        the_cmd     = argv[2]
    
        do_gen      = input(f"Generate obfuscation? [Y]/n\n{the_cmd}\n-> ")
        if not do_gen.upper() == 'N':
            make_obfuscation(the_file, the_cmd)
            compile(the_file)
