# import tkinter as tk
#
# # importing tkinter module
# from tkinter import *
# from tkinter import ttk
# from tkinter.ttk import *
#
# RegistrationForm = Tk()
#
# RegistrationForm.title("Registration Form")
# RegistrationForm.geometry("500x500")
# heading_font = ("Arial", 18, "bold")
# heading_label = tk.Label(
#     text="Welcome to the App",
#     font=heading_font,
#     bg="lightblue",
#     fg="darkblue",
#     pady=20
# )
# entry_field = tk.Entry(RegistrationForm)
#
#
# #now let create a label widget
# l1 = tk.Label(RegistrationForm, text = "student_id:")
#
#
# # grid method to arrange labels in respective
# # rows and columns as specified
# l1.grid(row = 0, column = 0, sticky = W, pady = 2)
# RegistrationForm.mainloop()
import tkinter as tk

RegistrationForm = tk.Tk()
RegistrationForm.title("Registration Form")
RegistrationForm.geometry("500x450")

heading = tk.Label(RegistrationForm, text="Registration Form", font=("sans serif", 16,  "bold underline"), fg="blue")
heading.grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(RegistrationForm, text="Student_id:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
# creating a fram for generate + entry (student_id)
student_id_frame = tk.Frame(RegistrationForm)
student_id_frame.grid(row=1, column=1, sticky="w")

student_id_entry = tk.Entry(student_id_frame, width=20)
student_id_entry.pack(side="left")

# generate_btn = tk.Button(student_id_frame, text="Generate", font=("sans serif", 8))
# generate_btn.pack(side="left", padx=5)

tk.Label(RegistrationForm, text="F_name:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
f_name_entry = tk.Entry(RegistrationForm)
f_name_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Label(RegistrationForm, text="L_name:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
l_name_entry = tk.Entry(RegistrationForm)
l_name_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

tk.Label(RegistrationForm, text="Age:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
age_entry = tk.Entry(RegistrationForm)
age_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

tk.Label(RegistrationForm, text="Gender:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
gender_variable = tk.StringVar(value="Male")
radio_frame = tk.Frame(RegistrationForm)
radio_frame.grid(row=5, column=1, sticky="w")
# tk.Radiobutton(radio_frame, text="Male", variable=gender_variable, value="Male").pack(side="left")
# tk.Radiobutton(radio_frame, text="Female", variable=gender_variable, value="Female").pack(side="left")

male_btn = tk.Radiobutton(
    radio_frame,
    text="Male",
    variable=gender_variable,
    value="Male",
    indicatoron=0,
    width=10,
)
male_btn.pack(side="left", padx=2)

female_btn = tk.Radiobutton(
    radio_frame,
    text="Female",
    variable=gender_variable,
    value="Female",
    indicatoron=0,
    width=10,
)
female_btn.pack(side="left", padx=2)

tk.Label(RegistrationForm, text="Address:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
address_entry = tk.Entry(RegistrationForm)
address_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

tk.Label(RegistrationForm, text="Tel No:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
tel_entry = tk.Entry(RegistrationForm)
tel_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

button_frame = tk.Frame(RegistrationForm)
button_frame.grid(row=8, column=0, columnspan=2, pady=20)
submit_btn = tk.Button(button_frame, text="Register", width=12, bg="blue", fg="white")
submit_btn.pack(side="left", padx=10)
clear_btn = tk.Button(button_frame, text="Clear", width=12)
clear_btn.pack(side="left", padx=10)
#
import random
def generate_id():
    value = f"YIBS23SE0-{random.randint(1000, 9999)}"
    student_id_entry.delete(0, tk.END)  # Clear current text
    student_id_entry.insert(0, value)  # Insert new valu
gen_btn = tk.Button(student_id_frame, text="Generate", command=generate_id)
gen_btn.pack(side="left", padx=5)
# def clear_form():
#     student_id_entry.delete(0, tk.END)
#     f_name_entry.delete(0, tk.END)
#     l_name_entry.delete(0, tk.END)
#     age_entry.delete(0, tk.END)
#     # for Radiobuttons, you reset the variable instead
#     gender_variable.set("Male")
#
# # then attach it to the button
# clear_btn = tk.Button(button_frame, text="Clear", command=clear_form)

RegistrationForm.mainloop()