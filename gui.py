from tkinter import*
from PIL import Image , ImageTk
import action 
import spech_to_text 


def User_send():
    send = entry1.get()
    bot = action.Action(send)
    text.insert(END, "Me --> "+send+"\n")
    if bot != None:
        text.insert(END, "Bot <-- "+ str(bot)+"\n")
    if bot == "ok sir":
          root.destroy()  
          

def ask():

    ask_val= spech_to_text.spech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "Me --> "+ask_val+"\n") 
    if bot_val != None:
       text.insert(END, "Bot <-- "+ str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def delete_text():
    text.delete("1.0", "end")


root = Tk()
root.geometry("550x675")
root.title("AI Assistant")
root.resizable(False,False)
root.config(bg="#8AAAE5")

  


# Main Frame
Main_frame = LabelFrame(root , padx=55,  pady=10 , borderwidth=3 ,  relief="raised")
Main_frame.config(bg="white")
Main_frame.grid(row = 1 ,  column= 1 ,  padx= 55 ,  pady =  55)

# Text Lable 
Text_lable = Label(Main_frame, text = " Aditya's AI Assistant" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "#8AAAE5")
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 20)


#Image 
Display_Image = ImageTk.PhotoImage(Image.open("image_as.jpeg"))
Image_Lable = Label(Main_frame, image= Display_Image)
Image_Lable.grid(row = 1 ,  column=0 , pady=20)



# Add a text widget

text=Text(root , font= ('Courier 10 bold') , bg = "#356696")
text.grid(row = 2,  column= 0)
text.place(x= 80, y= 375, width= 375, height= 100) 




# Add a entry widget
entry1 = Entry(root, justify = CENTER)
entry1.place(x=90 , y = 500 , width= 350, height= 30)



# Add a text button1
button1 =  Button(root,  text="ASK" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 50, y= 575)

# Add a text button2
button2 =  Button(root,  text="Send" , bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=User_send)
button2.place(x= 360, y= 575)

# Add a text button3
button3 = Button(root, text="Delete", bg="#356696" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete_text)
button3.place(x= 200, y= 575)
root.mainloop()