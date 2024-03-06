import cv2
import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import os.path

def encode(impath, text):
  
  dirname, filename = os.path.split(impath)
  name, ext = os.path.splitext(filename)
  newname = f"{name}_modified.png"
  immodpath = os.path.join(dirname, newname)
  binaryText = ToBinary(text) 
  binaryToImg(binaryText, immodpath, impath)
  return immodpath

def decode(impath):
  binaryText = imgToBinary(impath)
  stringText = ToString(binaryText)
  return stringText



def ToBinary(plaintext):
    lenght = len(plaintext)
    binarytext = '{0:08b}'.format(lenght)
    for char in plaintext:
        unicodeChar = ord(char)
        binaryChar = f'{unicodeChar:08b}'
        binarytext += binaryChar
    return binarytext

def ToString(binarytext):
    plaintext = ""
    splitBinary = [binarytext[i:i+8] for i in range(0, len(binarytext), 8)]
    lenght = int(splitBinary[0], 2)
    for binaryChar in splitBinary[1:lenght+1]:
        unicodeChar = int(binaryChar, 2)
        char = chr(unicodeChar)
        plaintext += char
    return plaintext

def imgToBinary(immodpath):
  img = cv2.imread(immodpath)
  index=0
  index2 = 0
  lenghtBin = ""
  binaryString = ""
  lenght = None
  for row in range(len(img)):
    for pixel in range(len(img[0])):
      for channel in range(3):
        if index2<8:
           index2+=1
           lenghtBin+=str(img[row][pixel][channel]%2)
           bit = str(img[row][pixel][channel]%2)
           binaryString += bit
        elif index2 == 8:
           index2+=1
           lenght = int(lenghtBin, 2)
           bit = str(img[row][pixel][channel]%2)
           binaryString += bit
        else:  
           
          bit = str(img[row][pixel][channel]%2)
          binaryString += bit
          index += 1
          if index >= lenght*8-1:
            return(binaryString)

def binaryToImg(binaryString, immodpath, impath):
  img = cv2.imread(impath)
  i=0
  for row in range(len(img)):
    for pixel in range(len(img[0])):
      for channel in range(len(img[0][0])):
        if str(img[row][pixel][channel] % 2) != binaryString[i]:
          img[row][pixel][channel] += 1
        i+=1
        if i >= len(binaryString):
          cv2.imwrite(immodpath, img)
          break
      if i >= len(binaryString):
        break
    if i >= len(binaryString):
        break


