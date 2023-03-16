import tkinter as tk
from tkinter import filedialog
import time

def select_log_file():
    log_file_path = filedialog.askopenfilename(
        title="Selecione o arquivo de log",
        filetypes=(("Log files", "*.log"), ("All files", "*.*"))
    )
    log_file_path_var.set(log_file_path)

def filter_log():
    keyword = keyword_entry.get()
    log_file_path = log_file_path_var.get()
    filtered_log = ""
    count = 0
    with open(log_file_path, "r") as f:
        for line in f:
            if keyword in line:
                filtered_log += line
                count += 1
    filtered_log_var.set(filtered_log)
    count_var.set(f"Erro encontrado {count} vezes")
    if count >= int(count_limit_entry.get()):
        auto_filter_button.config(state="disabled")
        root.bell()

def auto_filter_log():
    interval = int(interval_entry.get()) * 3600
    count_limit = int(count_limit_entry.get())
    count = 0
    while True:
        filter_log()
        if int(count_var.get().split()[2]) >= count_limit:
            auto_filter_button.config(state="disabled")
            root.bell()
            break
        time.sleep(interval)

root = tk.Tk()
root.configure(bg="black")  # definindo a cor de fundo da janela principal

log_file_path_var = tk.StringVar()
log_file_path_label = tk.Label(root, textvariable=log_file_path_var, bg="black", fg="white")
log_file_path_label.pack()

select_log_file_button = tk.Button(root, text="Selecionar arquivo de log", command=select_log_file, bg="green", fg="white")
select_log_file_button.pack()

keyword_entry = tk.Entry(root, bg="white")
keyword_entry.pack()

filter_button = tk.Button(root, text="Filtrar erros", command=filter_log, bg="green", fg="white")
filter_button.pack()

filtered_log_var = tk.StringVar()
filtered_log_label = tk.Label(root, textvariable=filtered_log_var, bg="black", fg="white")
filtered_log_label.pack()

count_var = tk.StringVar()
count_label = tk.Label(root, textvariable=count_var, bg="black", fg="white")
count_label.pack()

count_limit_label = tk.Label(root, text="Limite de vezes:", bg="black", fg="white")
count_limit_label.pack()

count_limit_entry = tk.Entry(root, bg="white")
count_limit_entry.pack()

interval_label = tk.Label(root, text="Intervalo em horas:", bg="black", fg="white")
interval_label.pack()

interval_entry = tk.Entry(root, bg="white")
interval_entry.pack()

auto_filter_button = tk.Button(root, text="Iniciar filtragem automática", command=auto_filter_log, bg="green", fg="white", state="disabled")
auto_filter_button.pack()

root.mainloop()
