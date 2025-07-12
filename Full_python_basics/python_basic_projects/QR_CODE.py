#Before running this cpode please make sure that qrcode library is in your system id not 
# install it by the following process 
# 1. Open command prompt in your system
# 2. Run the command i.e :  pip install qrcode
# 3.this will install the required library to your system
import qrcode
print("QR code Generator")
print("Created  by @varsha")
data = input("Enter input >> ")
qr=qrcode.make(data)
qr.save("D:/Python/Full_python/python_basic_projects/qrnew.png")
print("QR code is generated and saved successfully !!!")