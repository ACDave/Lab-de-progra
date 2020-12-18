# -*- coding: cp1252 -*-
from ftplib import FTP
import os

ftp_connect= FTP("ftp.us.debian.org")
ftp_connect.login()

def files():
   
   archivos= []
   if os.path.isdir("pract_ftp"):
      pass
   else:
      os.mkdir("pract_ftp")

   ftp_connect.dir("*.msg", archivos.append)
   count= len(archivos)
   if count != 0:
      for i in range(count):
         arch=archivos[i][56:90]
         arch=arch.strip()
         with open("pract_ftp/"+str(arch), "wb") as connection_file:
            ftp_connect.retrbinary("RETR " + str(arch), connection_file.write)
   else:
      pass

   ftp_connect.cwd("debian")
   ftp_connect.cwd("doc")
   archivos= []
   ftp_connect.dir("*.txt", archivos.append)
   count= len(archivos)
   if count != 0:
      for i in range(count):
         arch=archivos[i][56:90]
         arch=arch.strip()
         with open("pract_ftp/"+str(arch), "wb") as connection_file:
            ftp_connect.retrbinary("RETR " + str(arch), connection_file.write)
   else:
      pass
   ftp_connect.cwd("..")
   archivos=[]
   ftp_connect.dir("README*", archivos.append)
   count= len(archivos)
   if count != 0:
      for i in range(count):
         arch=archivos[i][56:90]
         arch=arch.strip()
         with open("pract_ftp/"+str(arch), "wb") as connection_file:
            ftp_connect.retrbinary("RETR " + str(arch), connection_file.write)
   else:
      pass
   
   archivos=[]
   count= len(archivos)
   ftp_connect.dir("*html", archivos.append)
   if count != 0:
      for i in range(count): 
         arch= archivos[i][56:90]
         arch= arch.strip()
         with open("pract_ftp/"+str(arch), "wb") as connection_file:
            ftp_connect.retrbinary("RETR " + str(archivo), connection_fie.write)
   else:
      pass

   return 0

def directories():
   
  try:
    lst=[]
    lst_dir=[]
    dics=[]
    rm=[]
    i= 0
    j= 0
    
    ftp_connect.retrlines("LIST",lst.append)
    lst_dir.append([line for line in ls if line.startswith("dr")])
    lst_dir.append([line for line in ls if line.startswith("dr")])
    for k in range(len(lst_dir)):       
      lng= len(lst_dir[k])
      direct= ftp_connect.pwd()   
      if lng > 0:
         for j in range(lng):
            fil= lst_dir[k][j][56:95]
            numb= dic.find("->")
            print("total directories: " + str(lng))
            if numb > 0:
               fil= dic[0:numb]
               fil= dic.strip()
               if fil in rm:
                  pass
               else:
                  print(dic)
                  dics.append(dic)
            else:
               if fil in rm:
                  pass
               else:
                  print(fil)
                  dics.append(fil)

      elif lng == 1:
         for j in range(lng):
            fil= lst_dir[k][j][56:95]
            numb= fil.find("->")
            print("total directories: " + str(lng))
            if numb > 0:
               fil= fil[0:numb]
               fil= fil.strip()
               if fil in rm:
                  pass
               else:
                  print(fil)
                  dics.append(fil)
            else:
               if fil in rm:
                  pass
               else:
                  print(fil)
                  dics.append(fil)    
         remove.append(fil)
         fpt_connect.cwd("..")
         ftp_connect.cwd("..")

    print(fil)
    ftp_connect.cwd(str(dics[0]))
    directories()
  except:
   print("Ohh no! there was an error")
   rm.append(fiñ)
   ftp_connect.cwd("..")
   ftp_connect.cwd("..")
   directories() 
 
 
files()
ftp_connect.quit()
