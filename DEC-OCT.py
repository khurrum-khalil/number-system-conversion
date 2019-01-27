def dec_oct(decimal):
    octal=[]
    if decimal<8:
        print("Octal Equivalent:",decimal)
    else:
        while decimal!=0:
            octal.append(str(decimal%8))
            decimal//=8
        octal.reverse()
        print("Octal Equivalent:","".join(octal))
