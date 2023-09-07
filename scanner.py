import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from pyzbar.pyzbar import decode

# Create a function to handle the scan button click event
def scan_qr_code():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Could not capture video frame.")
            break
        
        decoded_objects = decode(frame)
        if decoded_objects:
            for obj in decoded_objects:
                qr_data = obj.data.decode('utf-8')
                qr_code_label.config(text=f"QR Code Content: {qr_data}")
        
        # Display the video feed in the UI
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
        video_label.config(image=photo)
        video_label.photo = photo
        
        root.update()

    cap.release()

# Create the main application window
root = tk.Tk()
root.title("QR Code Scanner")

# Create a label for displaying the video feed
video_label = ttk.Label(root)
video_label.pack()

# Create a label for displaying the QR code content
qr_code_label = ttk.Label(root, text="QR Code Content: ")
qr_code_label.pack()

# Create a scan button
scan_button = ttk.Button(root, text="Scan QR Code", command=scan_qr_code)
scan_button.pack()

# Start the GUI main loop
root.mainloop()
