from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        total_f = float(total.get())

        if total_f <= 0: raise ValueError
    except ValueError:
        status_lbl.config(foreground="dark red")
        status_text.set('Total must be a number value greater than 0')
        return

    deductions_p1_f = sum_deductions(deductions_p1.get())
    deductions_p2_f = sum_deductions(deductions_p2.get())

    if deductions_p1_f < 0 or deductions_p2_f < 0:
        status_lbl.config(foreground="dark red")
        status_text.set('Deductions are number values separated by a space')
        return
    
    total_deductions = deductions_p1_f + deductions_p2_f
    total_minus_deductions = total_f - total_deductions
    split_cost = total_minus_deductions / 2

    if total_deductions > total_f:
        status_lbl.config(foreground="dark red")
        status_text.set('Total deductions cannot be greater than total cost')
        return

    results_p1.set(f'${split_cost + deductions_p1_f:.2f}')
    results_p2.set(f'${split_cost + deductions_p2_f:.2f}')
    status_lbl.config(foreground="dark green")
    status_text.set(f'Formula (P1): (({total_f:.2f} - {total_deductions:.2f}) / 2) '
                    f'+ {deductions_p1_f:.2f} = {split_cost + deductions_p1_f:.2f}')


def sum_deductions(deductions: str):
    value = 0
    for d in deductions.split(' '):
        try:
            value += 0 if (d == '') else float(d)
        except ValueError:
            return -1
        
    return value


def reset():
    var_list = [total, deductions_p1, deductions_p2, results_p1, results_p2]
    for v in var_list: v.set('')
    status_text.set('')
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

# Font styles
font_h1 = ("Arial", 14, "bold")
font_h2 = ("Arial", 10, "bold")
font_p = ("Arial", 10, "normal")
font_sm = ("Arial", 8, "normal")

ttk.Label(mainframe, text="Total: $", font=font_h1).grid(column=1, row=1, sticky=E)

total = StringVar()
total_entry = ttk.Entry(mainframe, width=8, textvariable=total, font=font_h1)
total_entry.grid(column=2, row=1, sticky=W)

# Deductions frame
deductions_frame = ttk.Labelframe(mainframe, text="Deductions")
deductions_frame.grid(column=1, row=2, columnspan=2, sticky=(W, E))
deductions_frame.columnconfigure(2, weight=1)

ttk.Label(deductions_frame, text="Person 1: $", font=font_p).grid(column=1, row=2, sticky=E)

deductions_p1 = StringVar()
deductions_p1_entry = ttk.Entry(deductions_frame, width=24, textvariable=deductions_p1, font=font_p)
deductions_p1_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(deductions_frame, text="Person 2: $", font=font_p).grid(column=1, row=3, sticky=E)

deductions_p2 = StringVar()
deductions_p2_entry = ttk.Entry(deductions_frame, width=24, textvariable=deductions_p2, font=font_p)
deductions_p2_entry.grid(column=2, row=3, sticky=(W, E))

# Calculate button
calculate_btn = ttk.Button(mainframe, text="Calculate", command=calculate)
calculate_btn.grid(column=1, row=3, columnspan=2, sticky=(W, E))

# Results frame
results_frame = ttk.Labelframe(mainframe, text="Results")
results_frame.grid(column=1, row=4, columnspan=2, sticky=(W, E))
results_frame.columnconfigure(2, weight=1)

results_p1 = StringVar()
ttk.Label(results_frame, text="Person 1 Owes:", font=font_p).grid(column=1, row=1, sticky=E)
ttk.Label(results_frame, textvariable=results_p1, font=font_h2).grid(column=2, row=1, sticky=E)

results_p2 = StringVar()
ttk.Label(results_frame, text="Person 2 Owes:", font=font_p).grid(column=1, row=2, sticky=E)
ttk.Label(results_frame, textvariable=results_p2, font=font_h2).grid(column=2, row=2, sticky=E)

# Reset button
reset_btn = ttk.Button(mainframe, text="Reset", command=reset)
reset_btn.grid(column=1, row=5, columnspan=2)

# Status bar
status_text = StringVar()
ttk.Separator(statusbar).grid(column=1, row=1, sticky=(W, E))
status_lbl = ttk.Label(statusbar, textvariable=status_text, font=font_sm, background="#ddd")
status_lbl.grid(column=1, row=2, sticky=W)

# Add padding to frames
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in deductions_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

for child in results_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

total_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
