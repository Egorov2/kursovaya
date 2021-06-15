import rasterio
from rasterio import plot
import numpy as np

def get_ndvi(red,nir):
  band_red = rasterio.open('LE07_L1TP_197031_20000810_20170210_01_T1_B3.tif')
  band_nir = rasterio.open('LE07_L1TP_197031_20000810_20170210_01_T1_B4.tif')

  red = band_red.read(1).astype('float64')
  nir = band_nir.read(1).astype('float64')

  ndvi=np.where((nir+red)==0.,0,(nir-red)/(nir+red))

  ndviImage = rasterio.open('output.jpg','w',driver='Gtiff',width=band_red.width,height = band_red.height,count=1, crs=band_red.crs,transform=band_red.transform,dtype='float64')
  
  return ndviImage
