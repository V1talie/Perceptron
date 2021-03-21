from tkinter import *
from perceptron import *
from PIL import ImageTk,Image
root = Tk()
root.title("Perceptron Mind")
root.geometry("1280x720")
root['background'] = '#856ff8'

myvar = StringVar()
myvar.set("Introduceti greutatea")
myvar_2 = StringVar()
myvar_2.set("Introduceti inaltimea")
photo = ImageTk.PhotoImage(Image.open("comp_brain.png"))
photo_green = ImageTk.PhotoImage(Image.open("green_2.png"))
photo_red = ImageTk.PhotoImage(Image.open("red_2.png"))

canvass = Canvas(bg="#856ff8", width=1280, height=720)
canvass.pack()


def on_click(event):
    event.widget.delete(0, END)


net = neuralNetwork(2, 3, 1, 0.2)


def perceptron_think():
    global result_string
    for i in range(len(data)):
        data[i][0] = (data[i][0]) / 1000
        data[i][1] = (data[i][1]) / 100
    EPOCHS = 10000
    for epoch in range(EPOCHS):
        random.shuffle(data)
        for point in data:
            training_data = [point[0], point[1]]
            target = point[2]
            net.train(training_data, target)


perceptron_think()


def perceptron_say():
    mystery_human[0] = (mystery_human[0]) / 1000
    mystery_human[1] = (mystery_human[1]) / 100
    if net.query(mystery_human) >= 0.5:
        result_string = "Sanatos"
        canvass.delete("all")
        canvass.create_image(800, 350, image=photo_green)
    elif net.query(mystery_human) < 0.5:
        result_string = "Nesanatos"
        canvass.delete("all")
        canvass.create_image(800, 350, image=photo_red)
    print(net.query(mystery_human))
    return result_string


def perceptron_result():
    num = int(e.get())
    num_1 = int(e_1.get())
    mystery_human[0] = num
    mystery_human[1] = num_1
    perceptron_say()


titlu = Label(root, justify='center', font="Elephant 50", text="Perceptron Mind", bg="#856ff8")
titlu.pack()
titlu.place(height=100, width=600, relx=0.5, rely=0.1, anchor='n')
e = Entry(root, width=50, justify='center', font="Calibri 18", textvariable=myvar, bg="#9781cf", borderwidth=0)
e.bind("<Button-1>", on_click)
e.pack()
e.place(height=50, width=300, relx=0.2, rely=0.4, anchor='s')
e_1 = Entry(root, width=50, justify='center', font="Calibri 18", textvariable=myvar_2, bg="#9781cf", borderwidth=0)
e_1.bind("<Button-1>", on_click)
e_1.pack()
e_1.place(height=50, width=300, relx=0.2, rely=0.5, anchor='s')
btn = Button(root, image=photo, font="Calibri 17", command=perceptron_result, bg="#856ff8", borderwidth=0,
             activebackground="#856ff8")
btn.place(height=125, width=125, relx=0.2, rely=0.7, anchor='s')
root.mainloop()
