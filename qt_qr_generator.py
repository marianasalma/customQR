from doctest import master
from tkinter import *
from PIL import Image, ImageTk
import qrcode

class CuteQr:
    def __init__(self, master):
        self.master = master
        master.title("❀ custom qr code generator ❀")
        master.geometry("350x160")

        # Label and field to input filename 
        self.labelFilename = Label(master, text="save barcode to png file [eg: my_qr.png]:", font=("Helvetica", 10, "bold"))
        self.labelFilename.pack()
        self.filename = StringVar()
        self.field_name = Entry(master, textvariable=self.filename, width=40)
        self.field_name.pack()

        # Label and field to input qr code color
        self.label_color = Label(master, text="✧ enter qr code color ✧", font=("Helvetica", 10, "bold"))
        self.label_color.pack()
        self.input_color = StringVar()
        self.field_color = Entry(master, textvariable=self.input_color, width=40)
        self.field_color.pack()
        self.color = self.input_color.get()

        # Label and field to input link
        self.label_link = Label(master, text="✧ enter your link ✧", font=("Helvetica", 10, "bold"))
        self.label_link.pack()
        self.input_link = StringVar()
        self.field_link = Entry(master, textvariable=self.input_link, width=40)
        self.field_link.pack()

        # Button to generate qr code
        self.button = Button(master, text="*✧･ﾟ:* generate qr! *✧･ﾟ:*", command=self.create_qr)
        self.button.pack()

    def create_qr(self):
        link = self.input_link.get()
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(link)
        qr.make(fit=True)
        name = self.filename.get()
        color = self.input_color.get()
        img = qr.make_image(fill_color=color, back_color='white')
        img.save(name)

        new = Toplevel(master)
        new.title("QR code of "+name)
        new.geometry("500x500") 
        new.resizable(0, 0)
        img1 = ImageTk.PhotoImage(Image.open(name))
        panel = Label(new, image = img1)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        new.mainloop()

def main():
    root = Tk()
    qrcode_generator = CuteQr(root)
    root.mainloop()

if __name__ == "__main__":
    main()

