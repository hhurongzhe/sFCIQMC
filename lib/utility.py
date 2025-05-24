# layout when executing code
printwidthleftmargin = 10
printwidth = 100

headerwidth = printwidth + printwidthleftmargin
headersymbol = "!"
sectionsymbol = "="

author = ": Rongzhe Hu "
affiliation = " Peking University, China "
email = " rongzhe_hu@pku.edu.cn "


def header_message():
    print("\n\n")
    print(headersymbol * headerwidth)
    print(headersymbol)
    print(headersymbol + " fciqmc slover for quantum many-fermion problems")
    print(headersymbol + " written by " + author)
    print(headersymbol + " affiliation:" + affiliation)
    print(headersymbol + " email      :" + email)
    print(headersymbol)
    print(headersymbol * headerwidth)


def footer_message():
    section_message("pyFCIQMC ends successfully!")


def section_message(x):
    print("\n" + sectionsymbol * (printwidthleftmargin) + " " + x + " " + sectionsymbol * (printwidth - len(x)) + "\n")
