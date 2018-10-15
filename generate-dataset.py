import cv2
import openfieldreaderwrapper
import subprocess
import os
import json
import uuid

images_path = "dataset1\\"

files = os.listdir(images_path)
nb_files = len(files)
pos = 0

for filename in files:
    pos += 1
    print(str(pos) + ' of ' + str(nb_files))

    if not filename.endswith('.jpg'):
        continue

    path = images_path + filename
    filename_noext = filename.replace('.jpg', '')
    img = cv2.imread(path)
    results = openfieldreaderwrapper.find_fields(img)
    return_code = results[0]
    fields = results[1]
    if fields is not None:
        for field in fields:
            for cell_img in field:
                cv2.imwrite(os.path.join('dataset', filename_noext + '_' + uuid.uuid4().hex + '.jpg'), cell_img)
    else:
        print('return_code: '+ str(return_code))

