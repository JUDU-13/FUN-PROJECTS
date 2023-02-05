import tkinter as tk

def calculate_bmi():
    # Get the values from the GUI
    height = float(height_entry.get())
    weight = float(weight_entry.get())

    # Calculate the BMI
    bmi = weight / (height * height)

    # Update the BMI label
    bmi_label.config(text=f"BMI: {bmi:.2f}")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create the height label and entry
height_label = tk.Label(root, text="Height (m):")
height_entry = tk.Entry(root)

# Create the weight label and entry
weight_label = tk.Label(root, text="Weight (kg):")
weight_entry = tk.Entry(root)

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi)

# Create the BMI label
bmi_label = tk.Label(root, text="")

# Pack the GUI elements
height_label.pack()
height_entry.pack()
weight_label.pack()
weight_entry.pack()
calculate_button.pack()
bmi_label.pack()

# Start the main event loop
root.mainloop()
