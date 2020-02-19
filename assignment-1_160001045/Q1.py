import os
import cv2

u = 100000000
d = -100000000
l = 100000000
r = -100000000

def bfs(vis,p,q):
  
  queue = [[p,q]]
  while queue:
    [p,q]=queue.pop(0)
    if p >= 0 and p < vis.shape[0] and q>=0 and q< vis.shape[1] and vis[p,q] == 255:
      queue.append([p+1,q])
      queue.append([p,q+1])
      queue.append([p-1,q])
      queue.append([p,q-1])
      queue.append([p+1,q+1])
      queue.append([p+1,q-1])
      queue.append([p-1,q+1])
      queue.append([p-1,q-1])
      global u,d,l,r
      u=min(u,p)
      d=max(d,p)
      l=min(l,q)
      r=max(r,q)
      vis[p,q]=0

def draw_rectangle(img):

  try:
    row = img.shape[0]
    col = img.shape[1]
    vis = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)      
    for i in range(0,row):
      for j in range(0,col):
        global u,d,l,r
        u = row+1
        d = -row-1
        l = col+1
        r = -col-1
        p = i
        q = j
        if vis[p,q]== 255:
          bfs(vis,p,q)
          cv2.rectangle(gray,(l,u),(r,d),(50,10,150),2)
  except TypeError as error:
      print(error)

  return gray


def main():

  result_dir = "result_connected_component"
  try:
    os.mkdir(result_dir)
  except OSError as error:
      print (error)
  else:
      print ("Successfully created the directory %s " % result_dir)

  dataset = os.listdir("connected_component")
  
  for i in range(0,len(dataset)):
    img = cv2.imread("connected_component/" + dataset[i], cv2.IMREAD_GRAYSCALE)
    if isinstance(img,type(None)):
      break
    else:
      result = draw_rectangle(img)
      cv2.imwrite(result_dir +'/' + dataset[i],result)

main()
