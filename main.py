import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist


path = '/content/drive/MyDrive/PIM/'
verticalBars = imread(path+'verticalBars.png')
verticalBars15 = imread(path+'verticalBars15.png')
verticalBars30 = imread(path+'verticalBars30.png')
verticalBars45 = imread(path+'verticalBars45.png')
verticalBars60 = imread(path+'verticalBars60.png')
verticalBars75 = imread(path+'verticalBars75.png')
verticalBars90 = imread(path+'verticalBars90.png')


def fourier(img):
  dark_image_grey = rgb2gray(img)
  #plt.figure(num=None, figsize=(8, 6), dpi=80)
  
  dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(dark_image_grey))
  #plt.figure(num=None, figsize=(8, 6), dpi=80)
  
  fig, ax = plt.subplots(1,2,figsize=(15,15))
  ax[0].imshow(dark_image_grey, cmap='gray')
  ax[1].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
  
  fourier(verticalBars)
  fourier(verticalBars15)
  fourier(verticalBars30)
  fourier(verticalBars45)
  fourier(verticalBars60)
  fourier(verticalBars75)
  fourier(verticalBars90)
