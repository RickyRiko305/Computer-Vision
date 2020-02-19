# -*- coding: utf-8 -*-
import os
import cv2


def dist(a,b):
  return abs(a[0]-b[0])+abs(a[1]-b[1])
  
def classify(pbg):

  img = pbg.copy()
  proper_label = [47329,54047]
  white_label = [39679,61697]
  label_missing = [50942,50434]
  bottle_missing = [32491,68885]
  threshold = 127
  row = img.shape[0]
  col = img.shape[1]
  b = 0
  w = 0

  for x in range(0,row):
    for y in range(0,col):
      if img[x,y] <= threshold :
        b+=1
        img[x,y]=0
      else :
        w+=1
        img[x,y]=255

  prop = dist(proper_label,[b,w])

  white = dist(white_label,[b,w])

  label = dist(label_missing,[b,w])

  bottle = dist(bottle_missing,[b,w])

  if( prop < white and prop < label and prop < bottle):
    return 'Proper Bottle'
  elif( white < prop and white < label and white < bottle):
    return 'White Label'
  elif( label < white and label < prop and label < bottle):
    return 'Label Missing'
  else:
    return 'Bottle Missing'


def main():
  try:
    os.mkdir('Proper Bottle')
  except OSError as error:
    print(error)

  try:
    os.mkdir('White Label')
  except OSError as error:
    print(error)

  try:
    os.mkdir('Label Missing')
  except OSError as error:
    print(error)

  try:
    os.mkdir('Bottle Missing')
  except OSError as error:
    print(error)

  dataset_name = "coke_bottle_images"

  dataset = os.listdir(dataset_name)
  for i in range(0,len(dataset)):
    image_path = dataset_name + "/" + dataset[i]
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if isinstance(img,type(None)):
      continue
    else:
      result = classify(img)
      tmp = cv2.imread(image_path)
      cv2.imwrite(result+ '/' + dataset[i], tmp)

main()
