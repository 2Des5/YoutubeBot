
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.common.keys
import unittest
import time
from selenium.webdriver.common.by import By
import pynput
import random
import pyautogui
import cv2
from Bot_De_youtube.User import USER, PASSWORD



Teclado = pynput.keyboard.Controller()


Mouse = pynput.mouse.Controller()


class Unittest(unittest.TestCase):

  
  def setUp(self):
    self.driver = uc.Chrome()
#class = g-c-R  webstore-test-button-label


  
  def test_Publicar_Video(self):
    driver = self.driver
    driver.get("https://studio.youtube.com/channel/UCG04Ew2RuhqbcOm_wnMFulQ")
    time.sleep(10)
    
    if pyautogui.locateOnScreen(r"C:\Users\Jodidos\VSCode\Youtube_API\Captcha.png", confidence=0.85) != None:
      driver.tab_new('https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl?hl=es-419')
      print("se abrio una nueva pestaña")
      time.sleep(random.uniform(3,4))
      driver.switch_to.window(driver.window_handles[1])
      print("se cambio a la pestaña")
      time.sleep(random.uniform(4,6))
      Mouse.position = pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\AgregarAChrome.png', confidence=0.6)  #pyautogui.click(pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\AgregarAChrome.png'))
      time.sleep(random.uniform(0.2,1))
      Mouse.click(pynput.mouse.Button.left)
      
      print("se dio click al boton de descargar extencion")
      time.sleep(random.uniform(4,5))
      Mouse.position = (pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\AgregarExtencion.png'))  #pyautogui.click(pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\AgregarExtencion.png'))
      time.sleep(random.uniform(0.2,1))
      Mouse.click(pynput.mouse.Button.left)

      print("Se dio click a 'AGREGAR EXTENCION'  para terminar de descargarla")
      time.sleep(random.uniform(6,7))
      driver.switch_to.window(driver.window_handles[0])
      print("se volvio a la pestaña del captcha")
      time.sleep(random.uniform(7,8))

      Mouse.position = (pyautogui.locateOnScreen(r"C:\Users\Jodidos\VSCode\Youtube_API\Captcha.png", confidence=0.6))  #pyautogui.click(pyautogui.locateOnScreen(r"C:\Users\Jodidos\VSCode\Youtube_API\Captcha.png"))
      time.sleep(0.1)
      Mouse.click(pynput.mouse.Button.left)
      print("se dio click al captcha")
      time.sleep(random.uniform(4,6))

      Mouse.position = (pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\Extencion.png', confidence=0.7))  #pyautogui.click(pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\Extencion.png'))
      time.sleep(random.uniform(0.2,1))
      Mouse.click(pynput.mouse.Button.left)
      print("se clickeo la extencion")
      time.sleep(35)
    if pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\Could_Not_Be_resolved.png', confidence=0.8) != None:
      Mouse.position = pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\NuevoDesafio.png', confidence=0.7)
      time.sleep(random.uniform(0.1,1))
      Mouse.click(pynput.mouse.Button.left)
      
      time.sleep(3)

      Mouse.position = (pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\Extencion.png', confidence=0.7))  #pyautogui.click(pyautogui.locateOnScreen(r'C:\Users\Jodidos\VSCode\Youtube_API\Extencion.png'))
      time.sleep(0.1)
      Mouse.click(pynput.mouse.Button.left)
      print("se clickeo la extencion")
      time.sleep(35)
      
    #time.sleep(1000)
    time.sleep(10)

    time.sleep(random.uniform(15,25) )
    
    #----------------------------SE LOGGEA

    loggearse = driver.find_element(By.NAME, "identifier")
    loggearse.click()
    time.sleep(random.uniform(0.1,1))
    loggearse.send_keys("") # ACA PONER EL USER
    print("Pone user")
    time.sleep(random.uniform(1.0,2))
    loggearse.send_keys(Keys.ENTER)
    time.sleep(random.uniform(6,7))
    loggearse = driver.find_element(By.NAME, "password")
    time.sleep(random.uniform(0.1,1))
    loggearse.click()
    time.sleep(random.uniform(0.1,1)) 
    loggearse.send_keys('') #ACA VA LA PASSWORD
    print("Pone contra")
    time.sleep(random.uniform(0.1,1))
    loggearse.send_keys(Keys.ENTER)
    time.sleep(random.uniform(10,15))

    #----------------------------CLiCKEA BOTON PARA SUBIR VIDEO

    publicar = driver.find_element(By.ID, "upload-icon").click()
    print("Clickea para subir video")
    time.sleep(random.uniform(4,5))
    #---------------------------- CLICKEA PARA SELECCIONAR ARCHIVO
    publicar = driver.find_element(By.ID, "select-files-button").click()
    print("Clickea para elegir video ")
    time.sleep(random.uniform(4,7))
    
    #---------------------------- BUSCA ARCHIVO
    Teclado.type(r"C:\Users\Jodidos\VSCode\Youtube_API\Video.mp4")
    time.sleep(random.uniform(0.1,1))
    Teclado.press(pynput.keyboard.Key.enter)
    time.sleep(random.uniform(5,6))

    #---------------AHORA VA A PONER EL TITULO ETC

    titulo = driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div") 
    time.sleep(random.uniform(0.1,1))
    titulo.click()
    print("Clickeo para POner titulo")
    time.sleep(random.uniform(0.1,1))
    titulo.send_keys(Keys.DELETE)
    time.sleep(random.uniform(0.1,1))
    titulo.send_keys("MEMES")
    print("Escribio titulo") 
    time.sleep(random.uniform(1,2))
    #----------------------------- Pone descripcion

    descripcion = driver.find_element(By.XPATH, '/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div')
    time.sleep(random.uniform(0.1,1))
    descripcion.click()
    print("Clickeo para poner descripcion")
    time.sleep(random.uniform(0.1,1))
    descripcion.send_keys("BEST MEMES")
    print("EScribio descripcion")
    time.sleep(random.uniform(2,3))
    #-----------------------  NO ES PARA NIÑOS

    para_niños = driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]/div[1]/div[1]").click()
    print("Clickea 'no es para niños'")
    time.sleep(random.uniform(1,2))
    #---------------------------- SIGUIENTE

    siguiente = driver.find_element(By.ID, "next-button").click()

    print("Clickea 'siguiente'")
    time.sleep(random.uniform(5,6))

    #---------------------------- Vuelve a dar al siguiente
    siguiente = driver.find_element(By.ID, "next-button").click()
    print("Clickea 'siguiente'")

    time.sleep(random.uniform(5,6))
    
    #---------------------------- Vuelve a dar al siguienteX2
    siguiente = driver.find_element(By.ID, "next-button").click()
    print("Clickea 'siguiente'")

    time.sleep(random.uniform(5,6))

    #------------- Darle al publico

    publico = driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]/div[1]/div[1]").click()
    print("CLickea boton para hacer publico el video")
    time.sleep(random.uniform(0.5,1.5))

    #---------------------------- Vuelve a dar al siguienteX2
    siguiente = driver.find_element(By.ID, "done-button").click()
    print("Clickea 'siguiente'")

    time.sleep(random.uniform(5,6))




    







    








if __name__ == "__main__":
    unittest.main()




  


















#from Google import Create_Service
#from googleapiclient.http import MediaFileUpload
#import datetime

#CLIENT_SECRET_FILE = r"C:\Users\Jodidos\VSCode\Youtube_API\Testeando\client_secrets.json"
#API_NAME = 'youtube'
#API_VERSION = "v3"
#SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

#service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
#SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

#service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#upload_date_time = datetime.datetime(2022, 7, 20, 15, 21, 1).isoformat() + '.000Z'

#request_body = {
#    'snippet': {
#        'categoryI': 19,
#        'title': f'MEMES',
#        'description': 'BEST MEMES',
#        'tags': ['Memes', 'Funny', 'Laugh', 'Best memes', 'actually funny memes']
#    },
#    'status': {
#        'privacyStatus': 'public',
#        'selfDeclaredMadeForKids': False, 
#    },
#    'notifySubscribers': False
#}

#mediaFile = MediaFileUpload('Video.mp4')

#response_upload = service.videos().insert(
#    part='snippet,status',
#    body=request_body,
#    media_body=mediaFile
#).execute()







"""


#!/usr/bin/python

import httplib2
import os
import random
import sys
import time

#from apiclient.base import build

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


# Explicitly tell the underlying HTTP transport library not to retry, since
# we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError)

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret. You can acquire an OAuth 2.0 client ID and client secret from
# the Google API Console at
# https://console.developers.google.com/.
# Please ensure that you have enabled the YouTube Data API for your project.
# For more information about using OAuth2 to access the YouTube Data API, see:
#   https://developers.google.com/youtube/v3/guides/authentication
# For more information about the client_secrets.json file format, see:
#   https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows an application to upload files to the
# authenticated user's YouTube channel, but doesn't allow other types of access.
YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.
MISSING_CLIENT_SECRETS_MESSAGE = """"""
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the API Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets"""
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

VALID_PRIVACY_STATUSES = ("public", "private", "unlisted")


def get_authenticated_service(args):
  flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
    scope=YOUTUBE_UPLOAD_SCOPE,
    message=MISSING_CLIENT_SECRETS_MESSAGE)

  storage = Storage("%s-oauth2.json" % sys.argv[0])
  credentials = storage.get()

  if credentials is None or credentials.invalid:
    credentials = run_flow(flow, storage, args)

  return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    http=credentials.authorize(httplib2.Http()))

def initialize_upload(youtube, options):
  tags = None
  if options.keywords:
    tags = options.keywords.split(",")

  body=dict(
    snippet=dict(
      title=options.title,
      description=options.description,
      tags=tags,
      categoryId=options.category
    ),
    status=dict(
      privacyStatus=options.privacyStatus
    )
  )

  # Call the API's videos.insert method to create and upload the video.
  insert_request = youtube.videos().insert(
    part=",".join(body.keys()),
    body=body,
    # The chunksize parameter specifies the size of each chunk of data, in
    # bytes, that will be uploaded at a time. Set a higher value for
    # reliable connections as fewer chunks lead to faster uploads. Set a lower
    # value for better recovery on less reliable connections.
    #
    # Setting "chunksize" equal to -1 in the code below means that the entire
    # file will be uploaded in a single HTTP request. (If the upload fails,
    # it will still be retried where it left off.) This is usually a best
    # practice, but if you're using Python older than 2.6 or if you're
    # running on App Engine, you should set the chunksize to something like
    # 1024 * 1024 (1 megabyte).
    media_body=MediaFileUpload(options.file, chunksize=-1, resumable=True)
  )

  resumable_upload(insert_request)

# This method implements an exponential backoff strategy to resume a
# failed upload.
def resumable_upload(insert_request):
  response = None
  error = None
  retry = 0
  while response is None:
    try:
      print ("Uploading file...")
      status, response = insert_request.next_chunk()
      if response is not None:
        if 'id' in response:
          print ("Video id '%s' was successfully uploaded." % response['id'])
        else:
          exit("The upload failed with an unexpected response: %s" % response)
    except HttpError as e:
      if e.resp.status in RETRIABLE_STATUS_CODES:
        error = "A retriable HTTP error %d occurred:\n%s" % (e.resp.status,
                                                             e.content)
      else:
        raise
    except RETRIABLE_EXCEPTIONS as e:
      error = "A retriable error occurred: %s" % e

    if error is not None:
      print (error)
      retry += 1
      if retry > MAX_RETRIES:
        exit("No longer attempting to retry.")

      max_sleep = 2 ** retry
      sleep_seconds = random.random() * max_sleep
      print ("Sleeping %f seconds and then retrying..." % sleep_seconds)
      time.sleep(sleep_seconds)

if __name__ == '__main__':
  argparser.add_argument("--file", required=True, help="Video file to upload")
  argparser.add_argument("--title", help="Video title", default="Test Title")
  argparser.add_argument("--description", help="Video description",
    default="Test Description")
  argparser.add_argument("--category", default="22",
    help="Numeric video category. " +
      "See https://developers.google.com/youtube/v3/docs/videoCategories/list")
  argparser.add_argument("--keywords", help="Video keywords, comma separated",
    default="")
  argparser.add_argument("--privacyStatus", choices=VALID_PRIVACY_STATUSES,
    default=VALID_PRIVACY_STATUSES[0], help="Video privacy status.")
  args = argparser.parse_args()

  if not os.path.exists(args.file):
    exit("Please specify a valid file using the --file= parameter.")

  youtube = get_authenticated_service(args)
  try:
    initialize_upload(youtube, args)
  except HttpError as e:
    print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))"""