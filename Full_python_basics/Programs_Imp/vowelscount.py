def Vowelscounte(str):
    count = 0
    # n = len(str)
    nstr = str.replace(" ","")
    if nstr is not None: # if nstr != Null in  c          for i in nstr:
            if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
                count +=1
    return count


def SimpleInpython(str):
    vowels = set("aeiouAEIOU") #set is fatser than multiple or checks
    cleaned_str = str.replace(" ","")
    if cleaned_str is not None: 
        count = sum(1 for i in cleaned_str if i in vowels)
    return count



str = input("Enter the word : ")
cnt = Vowelscounte(str)
print(f"Vowels count in the given string is : {cnt}")
cntpy = SimpleInpython(str)
print(f"Vowels count in the given string in SimpleInpython(str) is : {cntpy}")