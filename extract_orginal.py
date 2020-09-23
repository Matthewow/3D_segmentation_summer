import SimpleITK as sitk
import sys
import numpy as np
import imageio
from PIL import Image
np.set_printoptions(threshold=sys.maxsize)

# def combine

original = 'D:/CityU/RAproject/Result_Prostate/Label/prostate_00img.nii.gz'
label = 'D:/CityU/RAproject/Result_Prostate/Label/prostate_00label.nii.gz'

# Read the .nii image containing the volume with SimpleITK:
sitk_ori = sitk.ReadImage(original)
sitk_label = sitk.ReadImage(label)

# and access the numpy array:
original_np = sitk.GetArrayFromImage(sitk_ori)
label_np = sitk.GetArrayFromImage(sitk_label)

for i in range(40):
    data_ori_np = np.clip((original_np[0][i] - np.min(original_np[0][i]))*(255.0/(np.max(original_np[0][i]) - np.min(original_np[0][i]))), 0, 255).astype(np.uint8)
    original_3c = np.stack((data_ori_np,) * 3, axis=-1)

    for j in range(320):
        for k in range(320):
            if label_np[i][j][k] == 1:
                original_3c[j][k][2] = round((255 - original_3c[j][k][2]) * 0.4 + original_3c[j][k][1])
            if label_np[i][j][k] == 2:
                original_3c[j][k][1] = round((255 - original_3c[j][k][1]) * 0.3 + original_3c[j][k][1])
                original_3c[j][k][0] = round((255 - original_3c[j][k][0]) * 0.5 + original_3c[j][k][0])
    img = Image.fromarray(original_3c, 'RGB')
    img.save(f'./combine_label/{i}.png')
    print(i)
print("Finished")



#
# data_ori = original_np[1][0]
# data_ori_np = np.clip((data_ori - np.min(data_ori))*(255.0/(np.max(data_ori) - np.min(data_ori))), 0, 255).astype(np.uint8)
