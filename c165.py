from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
root=Tk()
root.title("Image Rotation")
root.geometry("600x700")
root.configure(background="lightblue")
label_image=Label(root,bg="lightblue")


img_path=""
def openImage():
    global img_path
    img_path=filedialog.askopenfilename(title="Open Image File",filetypes=[("Image Files","*.jpg *.gif *.jpeg *.png")])
    print(img_path)
    im=Image.open(img_path)
    img=ImageTk.PhotoImage(im)
    label_image['image']=img
    img.close()

def rotateImage():
    global img_path
    im=Image.open(img_path)
    img=ImageTk.PhotoImage(im.rotate(180))
    label_image['image']=img
    img.close()

btn_rotate=Button(root,text="Rotate Image",bg="black",fg="white",command=rotateImage)
btn_rotate.place(relx=0.5,rely=0.7,anchor=CENTER)
btn_open_img=Button(root,text="Open Image",bg="black",fg="white",command=openImage)
btn_open_img.place(relx=0.5,rely=0.2,anchor=CENTER)


label_image.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()

