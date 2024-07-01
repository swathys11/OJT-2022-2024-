str = ""
for Row in range(0,7):
    for col in range(0,7):
        if(col == 1 or ((Row == 0 or Row == 3 or Row == 6) and (col<5 and col>1)) or (col == 5 and (Row!= 0 and Row!= 3 and Row!= 6))):
            str = str+"*"
        else:
            str = str+" "
    str = str+"\n"
print(str)
            