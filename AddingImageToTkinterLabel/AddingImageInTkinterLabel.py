from tkinter import *

window = Tk()
window.title("Tkinter Shorts")
window.geometry("400x760")

# adding Image in
# Tkinter Window

header_label = Label(
    text="Adding Image In Tkinter Label"
)
header_label.pack()

main_frame = Frame(
    master=window,
    bg="#fff",
)

main_frame.pack(
    expand=1,
    fill=BOTH,
    pady=2,
    padx=3
)

# image_1
image_1 = PhotoImage(
    name="SampleImage",
    file="./sample.png"
)

label_1 = Label(
    master=main_frame,
    image=image_1
)
label_1.pack()

# image_2
image_2 = PhotoImage(
    name="PythonLogo",
    file="./python.png"
)

label_2 = Label(
    master=main_frame,
    image=image_2
)
label_2.pack()

window.mainloop()
