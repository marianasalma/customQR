# customQR
Custom QR code generator built with Python's GUI Library, Tkinter, and qrcode from Pillow (Python imaging library)

## 📌 Before running
This program utilizes the Python imaging library Pillow and QRcode package
Download by using the following command on the terminal
```
pip install pillow
pip install qrcode
```

## Why?
Why did I code this program when I can generate a QR code of any page with a right-click? Sure, it's easier. But it's also less fun. And the QR codes generated are usually black. Black == boring.
This program lets you pick the color that best represents the url you want it to be linked to!! Cyan? Hot pink? Salmon? Deep pink? You can even customize the color using hexadecimal code. 
Beyond that, this program saves the QR code to a filename (and type) of your choosing.

### To use
1. Run program, tkinter master window will appear
2. Input file name for the QR code to be saved as
3. Input fill color
4. Paste the url you want your QR code to be linked to
5. Click generate qr button, your QR code will be saved to a file in the current path and another frame containing the qr will appear (ready to use!)

### Colors
My personal favorite is DeepPink, but Python supports [the following colors](https://stackoverflow.com/questions/4969543/colour-chart-for-tkinter-and-tix) too.
Color chart [here](https://i0.wp.com/www.wikipython.com/wp-content/uploads/Color-chart-capture-082321.jpg?resize=1000%2C566&ssl=1).

