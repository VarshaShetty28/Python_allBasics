#import colorama  #importing the library to change the priting color can change 4 kinds of color they are : 
#1.background color,2.text color,3.style,
from colorama import Fore,Back,Style
String = input("Enter a string: ")
backword_string=String[::-1]

if backword_string==String:
    print(Fore.GREEN + f"{backword_string } This is Palindrome"+ Fore.RESET)
else:
    print(Fore.RED + f"{backword_string } is Not a Palindrome"+ Fore.RESET)

print(Style.DIM + "This is the Dim text " + Style.RESET_ALL)
print(Style.BRIGHT + "This is the Bright text "+ Style.RESET_ALL)
print(Back.YELLOW + "Background color "+ Back.RESET)