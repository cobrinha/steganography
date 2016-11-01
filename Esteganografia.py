#!/usr/bin/env python
#Boa:PyApp:main
#cobrinha@gmail.com - 12/08/2008
#Hard(coded) as a ROCK!

import os
import binascii
import struct
import shutil
from baseconvert import baseconvert

def CharCount(sArquivo):
    fpin  = open(sArquivo.GetValue(), "rb")
    fpin.seek(0)
    cont = 0
    while 1:
        sBuffer = fpin.read(128)
        if not sBuffer:
            break          
        else:
            if len(sBuffer) >= 128:
              cont = cont + 1
    return cont / 8

def CriarArquivo(sArquivo, lBytes):
    try:
      os.remove(sArquivo.GetValue()+".wav")
    except:
      pass
    shutil.copy2(sArquivo.GetValue(), sArquivo.GetValue()+".wav")
    fpin  = open(sArquivo.GetValue(), "rb")
    fpin.seek(0)
    fpout = open(sArquivo.GetValue()+".wav", "wb")
    contBufferAux = 0
    contAux = 0
    while 1:
        sBuffer = fpin.read(128)
        if not sBuffer:
            break          
        else:
            if len(sBuffer) >= 128:
              if contAux < 8: #se nao fecharam 8 bytes
                if len(lBytes) > contBufferAux:
                  iByte = int(binascii.b2a_hex(sBuffer[127]),16)
                  iBit  = baseconvert(iByte,"0123456789","01")
                  iBit  = iBit.rjust(8 ,"0")

                  if str(lBytes[contBufferAux]) == "00000000":                  
                    iByte2  = 0
                  else:
                    iByte2  = baseconvert(lBytes[contBufferAux],"01","0123456789")

                  hBuffer = struct.pack("B", int(iByte2))
                  sBuffer = sBuffer[0:-1]
                  sBuffer = sBuffer + hBuffer                
                  fpout.write(sBuffer)
                  contBufferAux = contBufferAux + 1
                  contAux = contAux + 1

                else:
                  fpout.write(sBuffer)
              else:
                fpout.write(sBuffer)
                contAux = 0

            else:
              fpout.write(sBuffer)
              pass

    fpin.close()
    fpout.close()
 
        
def Ocultar(sMsg, sArquivo, sChave=''):
    fpin  = open(sArquivo.GetValue(), "rb")
    fpin.seek(0)
    contMsg = 0
    contBuffer = 0
    contBufferAux = 0
    lBytes  = []
    lBytes2 = []
    contMsg = len(sMsg.GetValue())

    while 1:
        sBuffer = fpin.read(128)
        if not sBuffer:
            break          
        else:
            if len(sBuffer) >= 128:
              if contBufferAux >= 8: #se fecharam 8 bytes
                if contBuffer <= contMsg: 

                  if contBuffer > 1: #se nao for o primeiro, escreve a mensagem
                    sChar = ord(sMsg.GetValue()[contBuffer-1])
                    sBin  = baseconvert(sChar,"0123456789","01")
                    sBin  = sBin.rjust(8 ,"0")
                    for contBit in range(8): #varrendo bits do char
                      iBit  = baseconvert(lBytes[contBit],"0123456789","01")
                      iBit  = iBit.rjust(8 ,"0")
                      iBit2 = int(iBit[7])
                      if int(sBin[contBit]) != iBit2:
                        iBit2 = iBit2 ^ 1

                      iBit = iBit[0:7]
                      iBit = iBit+str(iBit2)
                      lBytes2.append(iBit) 
                    contBuffer = contBuffer + 1
                    contBufferAux = 0
                    lBytes = []

                  else: #se for primeiro byte, escreve o tamanho
                    sSize  = baseconvert(contMsg,"0123456789","01")
                    sSize  = sSize.rjust(16,"0")
                    try: #dando no rim
                      for contBit in range(16): #varrendo bits do char
                        iBit  = baseconvert(lBytes[contBit],"0123456789","01")
                        iBit  = iBit.rjust(8,"0")
                        iBit2 = int(iBit[7])
                        if int(sSize[contBit]) != iBit2:
                          iBit2 = iBit2 ^ 1

                        iBit = iBit[0:7]
                        iBit = iBit+str(iBit2)
                        lBytes2.append(iBit)
                    except:
                      pass

                    contBuffer = contBuffer + 1
                    contBufferAux = 0

              else:
                iByte = int(binascii.b2a_hex(sBuffer[127]),16)                
                lBytes.append(iByte)
                contBufferAux = contBufferAux + 1
            else:
              pass

    CriarArquivo(sArquivo, lBytes2)
    fpin.close()

def Recuperar(sArquivo, sChave=''):
    fpin  = open(sArquivo.GetValue(), "rb")
    fpin.seek(0)
    contMsg = 0
    contAux = 0
    lChars  = []
    sChar   = ""
    iSize   = 0
    cByte   = 0
    
    while 1:
        sBuffer = fpin.read(128)
        if not sBuffer:
            break          
        else:
            if len(sBuffer) >= 128:
              iByte = int(binascii.b2a_hex(sBuffer[127]),16)
              iBit  = baseconvert(iByte,"0123456789","01")
              iBit  = iBit.rjust(8 ,"0")
              if contAux < 8:              
                sChar = sChar + iBit[7]
                contAux = contAux + 1
              else:
                if cByte < 3:
                  contAux = 0
                  if len(sChar) == 24:
                    iSize = baseconvert(sChar[8:24],"01","0123456789")                  
                    sChar = ""
                    print iSize
                  cByte = cByte + 1
                  contAux = 0
                else:
                  sChar = baseconvert(sChar,"01","0123456789")
                  lChars.append(chr(int(sChar)))
                  sChar = ""
                  contMsg = contMsg + 1
                  contAux = 0
                  if contMsg >= int(iSize)-1:
                    sText = "".join(lChars)
                    return sText            