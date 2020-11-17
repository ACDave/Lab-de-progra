import requests
import re
import os
from bs4 import BeautifulSoup
import argparse
from PIL import ExifTags, Image
from PIL.ExifTags import TAGS

Psr = argparse.ArgumentParser() 
Psr.add_argument("-url", type=str, help="url del sitio web", required=True)#parser
Paramts= Psr.parse_args()
URL= Paramts.url 


def obt_lnks(URL):
    lnks = [] 
    Req= requests.get(URL) 
    SP = BeautifulSoup(Req.content, 'html.parser') 
    Etiqs= SP.find_all('a')

    for etiqueta in Etiqs:
        url= etiqueta.get('href')
        try:
            if url.find('https') == 0:
                lnks.append(url)
        except:
            None
    return lnks


def descargar_imgs(URL):  
   expresion_url= re.compile(r'http(s)?://\w*.\w*.\w*') 
   resul= expresion_url.search(URL) 
   respond = requests.get(URL)
   sp = BeautifulSoup(respond.content, "html.parser")
   imgs = sp.find_all("img")
   
   try:
      os.mkdir("Downloaded_Imgs")
      i = 1
   except:
      with open("num_imag.txt","r") as file:
         i = file.read()
         i = int(i)
   for img in imgs:
      lnk = img.get("src")
      img_name = "Downloaded_Imgs" + "/" + "image" + str(i)+ ".jpg"
      with open(img_name, "wb")as file:
         resul_lnk = expresion_url.search(lnk)
         try:
            resul_lnk.group()
         except:
            lnk = str(resul.group()) + lnk
         file.write(requests.get(lnk).content)
      try:
         Image.open(img_name)
         print(f"Descargando imagen{i}...")
         i += 1
      except:
         os.remove(img_name)
         print("Se rechazo una imagen...")
      
   with open("num_imag.txt","w") as file:
      file.write(str(i))



def meta_data(image):
    print("Sacando la metadata de imagenes...")
    img_name = image
    img= Image.open(img_name)
    meta_dat= []
    exf_data = img.getexif()
    for tag_id in exf_data:
        tag = TAGS.get(tag_id, tag_id)
        dat= exf_data.get(tag_id)
        if isinstance(dat, bytes):
            data = dat.decode()
        meta_dat.append(f"{tag}: {data}\n")
    return meta_dat
    
descargar_imgs(URL)
imgs = os.listdir("Downloaded_Imgs")
carpeta = os.mkdir("Metadatos")
for i in range(1, len(imgs)):
    meta = meta_data(f"Downloaded_Imgs/image{i}.jpg")
    with open(f"Metadatos/meta_data{i}.txt","w", encoding= "utf-8") as file:
       for line in meta:
          file.write(line)
