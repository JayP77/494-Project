import speech_recognition as sr
import dearpygui.dearpygui as dpg

def parse(str):
  create = "create "
  add = "add "
  lstr = str.lower()
  print(f"string:{lstr}")
  idxCreate = lstr.find("create")
  idxAdd = lstr.find("add")
  # print(f"create {idxCreate}")
  # print(f"add {idxAdd}")

  # get lower command and add everything after
  # create exists but add doesnt or create lower index
  if idxCreate != -1 and (idxAdd == -1 or idxCreate < idxAdd):
    idx = idxCreate
    size = len(create)
  # create doesnt exist but add does or add lower index
  elif idxAdd != -1 and (idxCreate == -1 or idxCreate > idxAdd):
    idx = idxAdd
    size = len(add)
  else:
    return ""
  # print(f"idx {idx}")
  # print(f"size {size}")
  # print(f"string from idx:{str[(idx+size):]}")
  return str[(idx+size):]

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    print (r.recognize_google(audio))
    #print("You said: " + r.recognize_google(audio))
# print("a")
# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    str = r.recognize_google(audio)
    reminder = parse(str)
    print("You said: " + str)

    
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

def save_callback():
    print("Save Clicked")

with dpg.window(label="Example Window"):
    dpg.add_text("Hello world")
    dpg.add_text(r.recognize_google(audio))
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

# make sure we got a command
if reminder != "":
  with dpg.window(label="reminder"):
    dpg.add_text(reminder)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
