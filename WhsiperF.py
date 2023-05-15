import cv2
import numpy as np
from PIL import Image

#it convert data in binary formate


def data2binary(data):
    if type(data) == str:
        p = ''.join([format(ord(i), '08b')for i in data])                      #using 'ord' to covert the ASCII value of message to binary
    elif type(data) == bytes or type(data) == np.ndarray:                      #which will further divide the message into blocks of 8bits and join all blocks
        p = [format(i, '08b')for i in data]
    return p


#concealing the data in the image 

def hidedata(img, data):
    data += "$$"                                                               #'$$'--> secrete key
    d_index = 0
    b_data = data2binary(data)
    len_data = len(b_data)

#the below defines the algo for hiding  the data in the image using LSB (Least Significant Bit) technique
#dividing the RBG into groups of 8 and setting a condition 
#if the index value is less than the data length value then will be modified usimg LSB else break
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            if d_index < len_data:
                pix[0] = int(r[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[1] = int(g[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[2] = int(b[:-1] + b_data[d_index])
                d_index += 1
            if d_index >= len_data:
                break
    return img


#for hiding the message into the image by reading the image using OpenCV module
def encode(data):
    img_name ='C:/Users/91981/Desktop/Minor Project/chatroom/main.png'
    image = cv2.imread(img_name)
    img = Image.open(img_name, 'r')
    w, h = img.size
    if len(data) == 0:
        raise ValueError("Empty data")
    enc_img = "out.png"
    enc_data = hidedata(image, data)
    cv2.imwrite(enc_img, enc_data)
    img1 = Image.open(enc_img, 'r')
    img1 = img1.resize((w, h),Image.Resampling.LANCZOS)                        #maintaining the image acceptance value
    # optimize with 65% quality
    if w != h:
        img1.save('C:/Users/91981/Desktop/Minor Project/chatroom/'+enc_img, optimize=True, quality=65)
    else:
        img1.save(enc_img)

# decoding the message from the encoded image be reversing the techinque of LSB (Least Significant Bit)
# taking empty string then whatever binary data we have; will split it into 8-bits format
def find_data(img):
    bin_data = ""
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]

    all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]
# bringing the data into readable format
    readable_data = ""
    for x in all_bytes:
        readable_data += chr(int(x, 2))
        if readable_data[-2:] == "$$":                                         #secret key is used; if the key matches the data the function will break
            break
    return readable_data[:-2]

#opening the image in read mode
def decode():
    img_name = 'C:/Users/91981/Desktop/Minor Project/chatroom/' + 'fin_msg.jpg'
    image = cv2.imread(img_name)
    img=Image.open(img_name,'r')
    msg = find_data(image)                                                     #data will be searched and will return the message
    return msg

#here we are giving the choice to the user whether the user wants to encode or decode the message
