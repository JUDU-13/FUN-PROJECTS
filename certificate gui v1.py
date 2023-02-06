import tkinter as tk

def print_certificate():
    # Get the values from the GUI
    name = name_entry.get()
    course = course_entry.get()

    # Print the certificate
    print(f"Certificate of Completion\n\nThis is to certify that {name}\nhas successfully completed the course\n{course}")

# Create the main window
root = tk.Tk()
root.title("Certificate Printer")

# Create the name label and entry
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

# Create the course label and entry
course_label = tk.Label(root, text="Course:")
course_entry = tk.Entry(root)

# Create the print button
print_button = tk.Button(root, text="Print", command=print_certificate)

# Pack the GUI elements
name_label.pack()
name_entry.pack()
course_label.pack()
course_entry.pack()
print_button.pack()

# Start the main event loop
root.mainloop()
#over