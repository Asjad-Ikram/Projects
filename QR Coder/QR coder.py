#QR Code Encoder/Decoder

import pandas as pd
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode




file_path="D:\Projects\QR Coder\pokemon_data.csv"

def qr_encoder():
    df=pd.read_csv(file_path)

    img=qrcode.make(df)

    save_name=input("Name the image file: ")
    save_path=(f"D:\Projects\QR Coder\{save_name}.png")

    img.save(save_path)

def qr_decoder():
    location=input("Enter file path: ")
    img=Image.open(location)
    result= decode(img)
    print(result)

job=input("\nWould you like to encode or decode?: ")
if job == "encode":
    qr_encoder()
elif job == "decode":
    qr_decoder()
else:
    print("Invalid Operation")
