import ants
import os

# os.chdir( "/Users/ntustison/Data/antsExamples/DenoiseImageExample/" )

# Read in the image

dataDirectory = './Input/'

inputImageFile = dataDirectory + 't1_slice.nii.gz'
inputImage = ants.image_read( inputImageFile )

outputImage = ants.denoise_image( inputImage, v = 1 )

outputDirectory = './OutputANTsPy/'
if not os.path.isdir( outputDirectory ):
  os.mkdir( outputDirectory )

outputImageFile = outputDirectory + "t1_slice_denoised.nii.gz"
ants.image_write( outputImage, outputImageFile )

