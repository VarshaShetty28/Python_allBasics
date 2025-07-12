#import library base64  to encode and decode 
import base64

def encoder():
    message = input("\nEnter a message you want to encode : ")
    message_in_bytes=bytes(message,"utf-8")
    encoded_msg = base64.b64encode(message_in_bytes)
    print(encoded_msg)

def decoder():
    message = input("\nEnter a message you want to decode : ")
    dec_msg_in_bytes=bytes(message,"utf-8")
    decoded_msg = base64.b64decode(dec_msg_in_bytes)
    print(decoded_msg)

print("Python Decoder and Encoder ")

print("1. Encoder\n2. Decoder")
option=int(input("Enter your option: "))

if option==1:
    encoder()
elif option==2:
    decoder()
else:
    print("Invalid option")


