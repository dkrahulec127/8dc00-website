import SimpleITK as sitk
import os 

#for root, fld, file in os.walk(os.path.join())
# the_files = []
# for file in os.listdir('./'):
#     if not file.endswith('.py') and not file.endswith('.txt'):
#         the_files.append(file)

# for item in the_files:

im = sitk.ReadImage('cameraman.tif')
sitk.WriteImage(im, 'cameraman.tif')




