import cv2
import camera
import numpy as np
import Draw_Screen as ds
from mcpi import minecraft

mc = minecraft.Minecraft.create()

test = ds.RGBBlock()
test.setPaint128Location()#한번만 실행,도화지 그릴위치와 주변 환경정리
test.setPixLocation()#이미 맵이 완성되었으면 위치만 잡아주기


img = camera.capture()

rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
rgb = cv2.resize(rgb,(128,128))
pix = np.array(rgb)

test.print2DtoBlocks(pix)#128X128PIX데이터(RGB) 입력시 프린터 
