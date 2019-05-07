library( ANTsR )

# Read in the image

dataDirectory <- './Input/'

inputImage <- antsImageRead(
   paste0( dataDirectory, 't1_slice.nii.gz' ), dimension = 2 )

outputImage <- denoiseImage( inputImage, verbose = TRUE )

outputDirectory <- './OutputANTsR/'
if( ! dir.exists( outputDirectory ) )
  {
  dir.create( outputDirectory )
  }
antsImageWrite( outputImage, paste0( outputDirectory, "t1_slice_denoised.nii.gz" ) )

