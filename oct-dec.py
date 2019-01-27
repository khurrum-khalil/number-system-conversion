def oct_dec(octal):
    decimal=[]
    octal_lst=list(octal)
    octal_lst.reverse()
    sum=0
    if int(octal)<8:
        print("Octal Equivalent:",decimal)
    elif int(octal)<10 and int(octal)>7:
        print("Invalid octal number!")
    else:
        for val in range(len(octal_lst)):
            sum+=(8**val) * (int(octal_lst[val]))
        print(sum)
