from tkinter import filedialog as fd

def compile(file: str):
    script = open(file, 'r').read()
    ## For functions
    script = script.replace('func', 'def')
    ## For literals
    script = script.replace('<', '{')
    script = script.replace('>', '}')
    ## Make this a curly braces language
    script = script.replace(']', ' ')
    script = script.replace('[', ':')
    ## For making comments //
    script = script.replace('//', '#')
    ## For making "inport" include
    script = script.replace('include', 'import')
    ## Remove ; to make code "pythonic"
    script = script.replace(';', '\n')
    ## Write the new file
    with open('new-earthscript-file.py', 'x') as new_file:
        new_file.write(script)


if __name__ == '__main__':
    compile(fd.askopenfilename(title='Select File You Want To Complie...', filetypes=[(
        'Earthscript', '*.es'
    )]))