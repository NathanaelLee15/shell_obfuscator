
from shared import make_obfuscation
from build import compile


def main():
    from sys import argv

    # AA = python shobfu.py
    if len(argv) > 2:
        # AA += example_name
        the_file    = argv[1]

        try:
            if argv[2] != "-f":
                # AA += (raw command) "sudo ls -l /"
                the_cmd = argv[2]

            else: # AA += -f
                # AA += input_file_path
                input_file = argv[3]

                with open(input_file, 'r') as inf:
                    lines = inf.read().split('\n')
                    while '' in lines:
                        lines.remove('')

                # handle #!/bin/bash
                if lines[0][0:2] == '#!':
                    lines.pop(0)

                if len(lines) == 1:
                    the_cmd = lines[0]
                else:
                    str_buff = ""
                    last_line = lines[-1]
                    for line in lines:
                        if line != last_line:
                            str_buff += line
                            str_buff += " && "
                        else:
                            # dont concat " && " 
                            str_buff += line

                    the_cmd = str_buff
        
            make_obfuscation(the_file, the_cmd)
            compile(the_file)
            
        except Exception as e:
            print(f"Unexpected error!\n{e}\n")


if __name__ == "__main__":
    main()
