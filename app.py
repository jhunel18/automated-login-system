import qrcode
from PIL import Image, ImageTk
import os
import tkinter as tk
from tkinter import Entry, Button, Label, filedialog

def generate_and_show_qr_code():
    library_id = library_id_entry.get()
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(library_id)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the PIL image to a PhotoImage
    img_tk = ImageTk.PhotoImage(img)
    
    # Display the QR code image in a Label widget
    qr_label.config(image=img_tk)
    qr_label.img = img_tk  # Store a reference to the image to prevent garbage collection
    
    result_label.config(text=f"QR code for Library ID {library_id}")

def generate_and_save_qr_code():
    library_id = library_id_entry.get()
    output_folder = output_folder_entry.get()

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(library_id)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code with a filename based on the Library ID
    file_name = f"{library_id}_qr_code.png"
    file_path = os.path.join(output_folder, file_name)
    img.save(file_path)

    result_label.config(text=f"QR code saved to {file_path}")

def browse_folder():
    folder_path = filedialog.askdirectory()
    output_folder_entry.delete(0, tk.END)
    output_folder_entry.insert(0, folder_path)

# Create a Tkinter window
window = tk.Tk()
window.title("QR Code Generator")

# Library ID Entry
library_id_label = Label(window, text="Library ID:")
library_id_label.pack()
library_id_entry = Entry(window)
library_id_entry.pack()

# Generate and Show QR Code Button
generate_show_button = Button(window, text="Generate & Show QR Code", command=generate_and_show_qr_code)
generate_show_button.pack()

# Output Folder Entry and Browse Button
output_folder_label = Label(window, text="Output Folder:")
output_folder_label.pack()
output_folder_entry = Entry(window)
output_folder_entry.pack()
browse_button = Button(window, text="Browse", command=browse_folder)
browse_button.pack()

# QR Code Label
qr_label = Label(window)
qr_label.pack()

# Generate QR Code and Save Button
generate_save_button = Button(window, text="Generate & Save QR Code", command=generate_and_save_qr_code)
generate_save_button.pack()

# Result Label
result_label = Label(window, text="")
result_label.pack()

window.mainloop()
