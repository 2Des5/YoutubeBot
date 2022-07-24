from ast import While
from asyncore import write
from random import random
from re import sub
from turtle import pos
import urllib.request
from urllib.request import install_opener, urlretrieve
from numpy import clip
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import unittest
import time
import requests
import instaloader
from User import USER, PASSWORD
import random
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx, AudioFileClip, afx , CompositeAudioClip
import subprocess


#instaloader --post-filter="not is_video" epicfunnypage   #Descarga imagenes
#Profile = instaloader.Hashtag.from_name(L.context, 'cat')
#post = instaloader.Post.from_shortcode(L.context, 'CKZ7j49FZB')








Memes_Descargados = 0 #solo para printear
cantidad_De_memes_que_agarrar = [1,2,3]  #por pagina
Cuentas_De_memes = ["daquan","epicfunnypage", "fuckjerry","funnymemes","memezar","memes","funnyvideos","cyph6n","repostrandy","succc.exe","startup.mp4","startup.repost","meme.ig"] #de las que agarrar memes
cantidad_de_veces_que_hacer_for_principal = [10,11,12,13,14,15,16,17,18,19,20] #repetir proceso
videos = [] #solo videos para luego ser compilados

Path_De_carpetas_De_memes = [r"C:\Users\Jodidos\VSCode\Youtube_API\cyph6n",r"C:\Users\Jodidos\VSCode\Youtube_API\daquan", r'C:\Users\Jodidos\VSCode\Youtube_API\epicfunnypage', r"C:\Users\Jodidos\VSCode\Youtube_API\fuckjerry",  r"C:\Users\Jodidos\VSCode\Youtube_API\funnymemes", r"C:\Users\Jodidos\VSCode\Youtube_API\funnyvideos",r"C:\Users\Jodidos\VSCode\Youtube_API\meme.ig", r"C:\Users\Jodidos\VSCode\Youtube_API\memes" , r"C:\Users\Jodidos\VSCode\Youtube_API\memezar", r"C:\Users\Jodidos\VSCode\Youtube_API\repostrandy",r"C:\Users\Jodidos\VSCode\Youtube_API\startup.mp4",r"C:\Users\Jodidos\VSCode\Youtube_API\startup.repost",    r"C:\Users\Jodidos\VSCode\Youtube_API\succc.exe"]

meme_ig = False

while True:


    for i in range(random.choice(cantidad_de_veces_que_hacer_for_principal)): #cantidad de veces que realizar esto
        target = random.choice(Cuentas_De_memes)

        if target == "meme.ig": #esto es para que cuando esta en la cuenta meme.ig entonces agarre mas memes que de lo normal
            meme_ig = True
        


        # Get instance
        L = instaloader.Instaloader()

        profile = instaloader.Profile.from_username(L.context, target)    #peril al que targetear

        i = 0

        for post in profile.get_posts():    #descargar post de perfiles

            if meme_ig:
                if i >= 3: # para que agarre 5 memes ya que esta pagina es buena
                    break

            
            elif i  >= random.choice(cantidad_De_memes_que_agarrar): #cantidad de memes que descargar
                break
        
            L.download_post(post,target=profile.username)
            i += 1
            
            print(i)
        Memes_Descargados += i
        meme_ig = False



    for path in Path_De_carpetas_De_memes: #por cada path en la carpeta de path
        folder = os.listdir(path) #la folder es el path del folder
        cwd = os.getcwd()

        for file in folder: #por cada archivo dentro de la folder
            print(file)
            if file.endswith('.mp4'):       #FILTRO DE SOLO VIDEOS
                videos.append( f"{path}\{file}") 
                print(f"VIDEOS: {videos}")
        
        print("\n \n \n")


    print(f"Se descargaron {Memes_Descargados} Memes")

    time.sleep(5)



    #------------------------------------------------------- PASO 1 HECHO



    clip0 = VideoFileClip(r"C:\Users\Jodidos\VSCode\Youtube_API\Bot_De_youtube\Intro_De_YoutubeBot.mp4")
    clip1 = VideoFileClip(f"{videos[0]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)
    clip2 = VideoFileClip(f"{videos[1]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)
    clip3 = VideoFileClip(f"{videos[2]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)
    clip4 = VideoFileClip(f"{videos[3]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)
    clip5 = VideoFileClip(f"{videos[4]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)
    clip6 = VideoFileClip(f"{videos[5]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)      
    clip7 = VideoFileClip(f"{videos[6]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)
    clip8 = VideoFileClip(f"{videos[7]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)
    clip9 = VideoFileClip(f"{videos[8]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)      
    clip10 = VideoFileClip(f"{videos[9]}")#.fx(vfx.fadein, 0.5).fx(vfx.fadeout,0.5)
    clip11 = VideoFileClip(f"{videos[10]}")
    clip12 = VideoFileClip(f"{videos[11]}")
    clip13 = VideoFileClip(f"{videos[12]}")



    Combined = concatenate_videoclips([clip0,clip1, clip2,clip3,clip4,clip5,clip6,clip7,clip8,clip9,clip10], method='compose')

    #combined.audio = CompositeAudioClip([audio])


    Combined.write_videofile("Video.mp4")


    subprocess.run('python C:/Users/Jodidos/VSCode/Youtube_API/Testeando/upload_video.py') #publica video en yt

    time.sleep(86400)







"""   #img = driver.find_element(By.CLASS_NAME,'mm-img').get_attribute("src") #https://imgflip.com/ai-meme
# MAS MEMES EN INGLES    #https://imgflip.com/

# MAS MEMES EN ESPAÑOL      https://es.memedroid.com/memes/random

#urllib.request.urlretrieve(img, "Meme.png") 


class UnitTEst(unittest.TestCase):
    numero_de_meme = 0



    def setUp(self): 
        self.driver = uc.Chrome() 


    def test_Descargar_Memes(self):

        driver = self.driver
        driver.get('https://imgflip.com/')
        print("Abriendo pagina")
        time.sleep(6)

        for i in range(10):
            time.sleep(2)

            driver.find_element(By.ID, "panel-flip").click() #Cambia a meme random
            print("Clickeando al boton randomizador")

            time.sleep(6)

            # get the image source
            imagen = driver.find_element(By.ID, "im").get_attribute('src')
            
            
            print("Encontrando Meme")
            time.sleep(3)
            
            data = requests.get(imagen).content
            
            time.sleep(0.01)
            local_filename = f'Meme{self.numero_de_meme}.png'
            time.sleep(0.001)
            
            with open (local_filename, 'wb') as file: #el wb significa write binary 
                file.write(data)
                

            print(f"Descargando meme  numero: {self.numero_de_meme}")

           # driver.find_element(By.ID, "aim-random-btn").click() #da click al randomizador de memes

            self.numero_de_meme += 1

            

        





if __name__ == '__main__':
    unittest.main()"""