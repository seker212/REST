import re

def getCmd():
    stri = input()
    print('')

    stri = stri.split()
    nstr = ''
    tab = []
    s = False
    for x in stri:
        if re.match(r'^\".*', x):
            s = True
        if s:
            nstr+=' '+x
        else:
            tab.append(x)
        if re.match(r'.*\"$', x):
            s = False
            nstr=nstr.replace('"','')
            if nstr.startswith(" "):
                nstr = nstr[1:]
            tab.append(nstr)
    return tab