Str = "12,67,56.90.88"
L = []

for i in range(0,len(Str)-1,1):
    if Str[i] == ".":
        L.append(i)

Str= Str.replace(',',".")
Lreplace = list(Str)
newstr = ""

for indx in L:
    Lreplace[indx] = ","

for val in Lreplace:
    newstr += str(val)

print(newstr)