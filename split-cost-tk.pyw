from tkinter import *
from tkinter import ttk
from idlelib.tooltip import Hovertip

def calculate(*args):
    try:
        total_f = float(total.get())

        if total_f <= 0: raise ValueError
    except ValueError:
        status_lbl.config(foreground="dark red")
        status_text.set('Total must be a number value greater than 0')
        return

    individual_deductions = [0]
    for i in range(1, split_val.get() + 1):
        deductions = sum_deductions(deduction_vars[i].get())
        individual_deductions.append(deductions)
        
        if deductions < 0:
            status_lbl.config(foreground="dark red")
            status_text.set('Deductions are number values separated by a space')
            return
    
    total_deductions = sum(individual_deductions)
    total_minus_deductions = total_f - total_deductions
    split_cost = total_minus_deductions / split_val.get()

    if total_deductions > total_f:
        status_lbl.config(foreground="dark red")
        status_text.set('Total deductions cannot be greater than total cost')
        return
    
    for i in range(1, split_val.get() + 1):
        individual_total = split_cost + individual_deductions[i]
        result_vars[i].set(f'${individual_total:.2f}')

        Hovertip(results_frame.nametowidget(f"results_p{i}_lbl_2"),
            f'Formula (Person {i}): (({total_f:.2f} - {total_deductions:.2f}) / {split_val.get()}) '
            f'+ {individual_deductions[i]:.2f} = {individual_total:.2f}')

    # Display a statusbar message
    status_lbl.config(foreground="dark green")
    status_text.set('Split cost calculated!')


def sum_deductions(deductions: str):
    value = 0
    for d in deductions.split(' '):
        try:
            value += 0 if (d == '') else float(d)
        except ValueError:
            return -1
        
    return value


def update_ui():
    # Remove widgets from frame
    for child in deductions_frame.winfo_children():
        child.destroy()

    for child in results_frame.winfo_children():
        child.destroy()

    reset(reset_all=False)

    for i in range(1, split_val.get() + 1):
        deduction_lbl = ttk.Label(deductions_frame, text=f"Person {i}: $", font=font_p)
        deduction_lbl.grid(column=1, row=i, sticky=E, padx=5, pady=5)
        Hovertip(deduction_lbl, deductions_tooltip_1)

        # deduction = StringVar(root, name=f"deductions_p{i}")
        deduction_entry = ttk.Entry(deductions_frame, width=24, textvariable=deduction_vars[i], font=font_p)
        deduction_entry.grid(column=2, row=i, sticky=(W, E), padx=5, pady=5)
        Hovertip(deduction_entry, deductions_tooltip_2)

        # result = StringVar(root, name=f"results_p{i}")
        result_lbl_1 = ttk.Label(results_frame, text=f"Person {i} Owes:", font=font_p)
        result_lbl_1.grid(column=1, row=i, sticky=E, padx=5, pady=5)
        result_lbl_2 = ttk.Label(results_frame, textvariable=result_vars[i], name=f"results_p{i}_lbl_2", font=font_h2)
        result_lbl_2.grid(column=2, row=i, sticky=E, padx=5, pady=5)


def reset(reset_all=True):
    global deduction_vars, result_vars
    if reset_all:
        total.set('')
        deduction_vars = [StringVar() for i in range(8)]

    status_text.set('')
    result_vars = [StringVar() for i in range(8)]
    total_entry.focus()


# Graphical User Interface
root = Tk()
root.title("Split Cost")
root.iconbitmap("sc-logo.ico")
root.resizable(width=False, height=False)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

mainframe = ttk.Frame(root, padding="5 5 5 5")
mainframe.grid(column=1, row=1, sticky=(N, W, E, S))
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)

ttk.Style().configure("Statusbar.TFrame", background="#ddd")
statusbar = ttk.Frame(root, style="Statusbar.TFrame")
statusbar.grid(column=1, row=2, sticky=(N, W, E, S))
statusbar.columnconfigure(1, weight=1)
statusbar.rowconfigure(1, weight=1)

split_val = IntVar(value=2)
deduction_vars = [StringVar() for i in range(8)]
result_vars = [StringVar() for i in range(8)]

# Font styles
font_h1 = ("Arial", 14, "bold")
font_h2 = ("Arial", 10, "bold")
font_p = ("Arial", 10, "normal")
font_sm = ("Arial", 8, "normal")

ttk.Label(mainframe, text="Total: $", font=font_h1).grid(column=1, row=1, sticky=E)

total = StringVar()
total_entry = ttk.Entry(mainframe, width=8, textvariable=total, font=font_h1)
total_entry.grid(column=2, row=1, sticky=W)
Hovertip(total_entry, 'Total can be an integer or decimal value')

# Split frame
split_frame = ttk.Labelframe(mainframe, text="Split")
split_frame.grid(column=1, row=2, columnspan=2, sticky=(W, E))

ttk.Radiobutton(split_frame, text="2-way", variable=split_val, value=2, command=update_ui)
ttk.Radiobutton(split_frame, text="3-way", variable=split_val, value=3, command=update_ui)
ttk.Radiobutton(split_frame, text="4-way", variable=split_val, value=4, command=update_ui)
ttk.Radiobutton(split_frame, text="5-way", variable=split_val, value=5, command=update_ui)

# Deductions frame
deductions_frame = ttk.Labelframe(mainframe, text="Deductions")
deductions_frame.grid(column=1, row=3, columnspan=2, sticky=(W, E))
deductions_frame.columnconfigure(2, weight=1)

deductions_tooltip_1 = ("Deductions are for items which will not be shared.\n"
                        "For instance, if Person 1 has a deduction for an item\n"
                        "costing $5, Person 2 won't have to pay for any of it.")
deductions_tooltip_2 = "Deductions can be integer or decimal values separated by a space"

# Calculate button
calculate_btn = ttk.Button(mainframe, text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=4, columnspan=2, sticky=(W, E))

# Results frame
results_frame = ttk.Labelframe(mainframe, text="Results")
results_frame.grid(column=1, row=5, columnspan=2, sticky=(W, E))
results_frame.columnconfigure(2, weight=1)

# Reset button
reset_btn = ttk.Button(mainframe, text="Reset", command=reset)
reset_btn.grid(column=1, row=6, columnspan=2)

# Status bar
status_text = StringVar()
ttk.Separator(statusbar).grid(column=1, row=1, sticky=(W, E))
status_lbl = ttk.Label(statusbar, textvariable=status_text, font=font_sm, background="#ddd")
status_lbl.grid(column=1, row=2, sticky=W)

# Add padding to frames
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

for i, child in enumerate(split_frame.winfo_children()):
    child.grid_configure(column=i+1, row=1, padx=5, pady=5, sticky=(W, E))

total_entry.focus()
root.bind("<Return>", calculate)

update_ui()
root.mainloop()
