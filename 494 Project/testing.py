from tkinter import *
from sunau import AUDIO_UNKNOWN_SIZE
import speech_recognition as sr 
import dearpygui.dearpygui as dpg

listOfReminders=[]
reminders=dict({})
reminderToAdd=""
reminderToRemove=""
reminder=""
# Record Audio
rstr = ""
newStr = ""

def edit_helper(reminderToEdit,reminders):
  r = sr.Recognizer()
  with(dpg.window(label='EDIT', pos=(0,150), width = 1440)):
    dpg.add_text('What should I change the time to?')
  with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio=r.listen(source)
    rstr = r.recognize_google(audio)
    #print("You said: " + rstr)
    return rstr

def substring_after(s, delim):
    return s.partition(delim)[2]

def speak_callback():
  with sr.Microphone() as source:
      r = sr.Recognizer()
      # print("Say something!")
      feedbackList.insert(0, "Say something!")
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
      rstr = r.recognize_google(audio)
      # reminder = parse(rstr)
      
      if("add reminder" in rstr or 'new reminder' in rstr):
        if('at' not in rstr):
          reminderToAdd=substring_after(rstr,'reminder')
          reminderToAdd=reminderToAdd.strip()
          #listOfReminders.append(reminderToAdd)
          reminders[reminderToAdd]='NO TIME GIVEN'
        else:
          reminderToAdd=substring_after(rstr,'reminder')
          reminderToAdd=reminderToAdd.split('at',1)[0]
          timeToAdd = substring_after(rstr,'at')
          reminderToAdd=reminderToAdd.strip()
          #listOfReminders.append(reminderToAdd)
          reminders[reminderToAdd]= timeToAdd
      if("remove reminder" in rstr):
        reminderToRemove=substring_after(rstr,'reminder')
        reminderToRemove=reminderToRemove.strip()
        #listOfReminders.remove(reminderToRemove)
        if(reminderToRemove in reminders):
          reminders.pop(reminderToRemove)
      if("edit reminder" in rstr):
        reminderToEdit=substring_after(rstr,'reminder')
        reminderToEdit=reminderToEdit.strip()
        if(reminderToEdit in reminders):
          newTime=edit_helper(reminderToEdit,reminders)
          
          print("NEW TIME IS: " + newTime)
        reminders[reminderToEdit]=newTime
        

    # dpg.add_text("Add - Add reminder x at y")
    # dpg.add_text("Remove - Remove reminder x")
    # dpg.add_text("Edit - Edit reminder x, new x")
    #dpg.add_text(r.recognize_google(audio))
      # print("You said: " + rstr)
      #------------------------
      feedbackList.insert(0, 'You said: ' + rstr)

      global newStr
      newStr = "ABC"
      print("TESTING: ")
      print(*listOfReminders,sep=', ')
      #with dpg.window(label="reminder"):
      #  for i in listOfReminders:
      #    dpg.add_text(i)

      # with reminderWindow:
      #   for i in reminders:
      #     mStr=i+" " + reminders[i]
      #     dpg.add_text(mStr)
      # size = len(reminders)
      # reminderList.insert(END, mStr)
      reminderList.delete(0,END)
      for i in reminders:
          mStr=i+" " + reminders[i]
          reminderList.insert(END, mStr)
          
      print(reminders)

      
  except sr.UnknownValueError:
    feedbackList.insert(0, "Google Speech Recognition could not understand audio")
    print("Google Speech Recognition could not understand audio")
  except sr.RequestError as e:
    feedbackList.insert(0, "Could not request results from Google Speech Recognition service; {0}")
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = Tk()
r.geometry("1000x800")
r.title('Counting Seconds')
button = Button(r, text='Stop', width=25, command=r.destroy)
button.grid(row=0,column=0,columnspan=1)
# button.pack()
bSpeak = Button(r, text='Speak', width=25, command=speak_callback)
bSpeak.grid(row=0,column=1,columnspan=1)
# bSpeak.pack()

scrollbar = Scrollbar(r)
# scrollbar.pack( side = LEFT, fill = Y)
scrollbar2 = Scrollbar(r)
# scrollbar2.pack( side = RIGHT, fill = Y)
reminderList = Listbox(r, yscrollcommand = scrollbar.set , width = 100)
feedbackList = Listbox(r, yscrollcommand = scrollbar2.set , width = 100)
for line in range(20):
   feedbackList.insert(0, 'This is line number       ' + str(line))
for line in range(20):
   reminderList.insert(END, 'This is line number            ' + str(line))
# reminderList.pack( side = TOP, fill = BOTH )
# feedbackList.pack( side = BOTTOM, fill = BOTH )
# scrollbar.config( command = reminderList.yview )
# scrollbar2.config( command = feedbackList.yview )



reminderList.grid(row=3,column=0,columnspan=3)
# scrollbar.grid(row=3,column=4,rowspan=1)
feedbackList.grid(row=4,column=0,columnspan=2)
# scrollbar2.grid(row=4,column=4,rowspan=1)
r.mainloop()

# root = Tk()
# root.grid_rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)

# frame_main = Frame(root, bg="gray")
# frame_main.grid(sticky='news')

# label1 = Label(frame_main, text="Label 1", fg="green")
# label1.grid(row=0, column=0, pady=(5, 0), sticky='nw')

# label2 = Label(frame_main, text="Label 2", fg="blue")
# label2.grid(row=1, column=0, pady=(5, 0), sticky='nw')

# label3 = Label(frame_main, text="Label 3", fg="red")
# label3.grid(row=3, column=0, pady=5, sticky='nw')

# # Create a frame for the canvas with non-zero row&column weights
# frame_canvas = Frame(frame_main)
# frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
# frame_canvas.grid_rowconfigure(0, weight=1)
# frame_canvas.grid_columnconfigure(0, weight=1)
# # Set grid_propagate to False to allow 5-by-5 buttons resizing later
# frame_canvas.grid_propagate(False)

# # Add a canvas in that frame
# canvas = Canvas(frame_canvas, bg="yellow")
# canvas.grid(row=0, column=0, sticky="news")

# # Link a scrollbar to the canvas
# vsb = Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
# vsb.grid(row=0, column=1, sticky='ns')
# canvas.configure(yscrollcommand=vsb.set)

# # Create a frame to contain the buttons
# frame_buttons = Frame(canvas, bg="blue")
# canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

# # Add 9-by-5 buttons to the frame
# rows = 9
# columns = 5
# buttons = [[Button() for j in range(columns)] for i in range(rows)]
# for i in range(0, rows):
#     for j in range(0, columns):
#         buttons[i][j] = Button(frame_buttons, text=("%d,%d" % (i+1, j+1)))
#         buttons[i][j].grid(row=i, column=j, sticky='news')

# # Update buttons frames idle tasks to let tkinter calculate buttons sizes
# frame_buttons.update_idletasks()

# # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
# first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, 5)])
# first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 5)])
# frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
#                     height=first5rows_height)

# # Set the canvas scrolling region
# canvas.config(scrollregion=canvas.bbox("all"))

# # Launch the GUI
# root.mainloop()