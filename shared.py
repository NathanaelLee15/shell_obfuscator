
src_template="""
extern int system(const char* cstr);
const char* the_cmd="{{}}";
int main() {system(the_cmd);}
"""

SRC_ROOT = "."
SRC_PATH = f"{SRC_ROOT}/src"
EXT = ".c"


def generate_obfuscation(file_name, content:str):
    with open(f"{SRC_PATH}/{file_name}{EXT}", 'w') as outf:
        outf.write(content)

    print(f"Obfuscation ({file_name}) created!")


def make_obfuscation(file_name, cmd:str):
    print(f"Generating obfuscation for\n{cmd}")

    fcmd        = cmd.replace('"', '\\"')
    out_text    = src_template.replace('{{}}', fcmd)
    generate_obfuscation(file_name, out_text)
