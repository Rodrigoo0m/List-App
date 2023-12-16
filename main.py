import tkinter as tk
from tkinter import simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        root.title("Lista de Tarefas | Rodrigoo0m")

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.listbox = tk.Listbox(self.frame, width=50, height=10)
        self.listbox.pack(side="left", fill="y")

        self.scrollbar = tk.Scrollbar(self.frame, orient="vertical")
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.addButton = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.addButton.pack(fill='x')

        self.editButton = tk.Button(root, text="Editar Tarefa Selecionada", command=self.edit_task)
        self.editButton.pack(fill='x')

        self.deleteButton = tk.Button(root, text="Excluir Tarefa", command=self.delete_task)
        self.deleteButton.pack(fill='x')

    def add_task(self):
        task = simpledialog.askstring("Adicionar Tarefa", "Descrição da Tarefa:")
        if task:
            self.listbox.insert(tk.END, task)

    def edit_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            task = self.listbox.get(selected_index)
            new_task = simpledialog.askstring("Editar Tarefa", "Editar Tarefa:", initialvalue=task)
            if new_task:
                self.listbox.delete(selected_index)
                self.listbox.insert(selected_index, new_task)
        except IndexError:
            pass

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_index)
        except IndexError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
