import tkinter as tk
import qrcode


def generate_qr_code():
    # Get the text from the text entry
    text = text_entry.get()

    # Create a QR code object
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add the text to the QR code object
    qr.add_data(text)
    qr.make(fit=True)

    # Get the QR code matrix
    qr_matrix = qr.get_matrix()

    # Create an image from the QR code matrix
    qr_img = qrcode.make_qr_code(qr_matrix)

    # Display the image in the image label
    qr_code_img = tk.PhotoImage(image=qr_img)
    qr_code_label.config(image=qr_code_img)
    qr_code_label.image = qr_code_img


# Create the GUI window
root = tk.Tk()
root.title("QR Code Generator")

# Create the text entry
text_entry = tk.Entry(root)
text_entry.pack()

# Create the generate QR code button
generate_button = tk.Button(
    root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()

# Create the QR code image label
qr_code_label = tk.Label(root)
qr_code_label.pack()

# Start the GUI event loop
root.mainloop()
