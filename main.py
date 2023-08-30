import tkinter.messagebox as messagebox
import os
import tkinter as tk
from tkinter import filedialog
import random


class DirectoryBuilder(tk.Tk):
    def __init__(self):
        super().__init__()
        self.titles = [
            "DirCreator",
            "FolderTreeMaker",
            "DirectoryMaker",
            "FolderStructureBuilder",
            "DirTreeCreator",
            "DirectoryArchitect",
            "FolderHierarchyBuilder",
            "DirNestBuilder",
            "DirectoryAssembler",
            "FolderNetworkMaker",
            "DirOrganizer",
            "DirectoryConstructor",
            "FolderFrameworkBuilder",
            "DirHierarchyCreator",
            "DirectoryDesigner",
            "FolderSystemMaker",
            "DirWebBuilder",
            "DirectoryNetworkCreator",
            "FolderArchitectureBuilder",
            "DirLatticeConstructor"
        ]
        self.title(random.choice(self.titles))
        self.geometry('400x400')

        # Create widgets
        self.dir_label = tk.Label(self, text='Select Root Directory')
        self.dir_entry = tk.Entry(self)
        self.dir_button = tk.Button(self, text='Browse', command=self.browse_directory)
        self.text_frame = tk.Frame(self)
        self.text_field = tk.Text(self.text_frame, wrap='none', height=10)
        self.text_scrollbar = tk.Scrollbar(self.text_frame, orient='vertical', command=self.text_field.yview)
        self.text_field['yscrollcommand'] = self.text_scrollbar.set
        self.build_button = tk.Button(self, text='Build Dir', command=self.build_directories)

        # Place widgets
        self.dir_label.pack(padx=10, pady=5)
        self.dir_entry.pack(padx=10, pady=5, fill=tk.X)
        self.dir_button.pack(padx=10, pady=5)
        self.text_frame.pack(padx=10, pady=5, expand=True, fill=tk.BOTH)
        self.text_field.pack(side='left', expand=True, fill=tk.BOTH)
        self.text_scrollbar.pack(side='right', fill='y')
        self.build_button.pack(padx=10, pady=5)

    def browse_directory(self):
        self.dir_entry.delete(0, tk.END)
        directory = filedialog.askdirectory()
        self.dir_entry.insert(0, directory)

    def build_directories(self):
        root_dir = self.dir_entry.get()
        dir_structure = self.text_field.get('1.0', tk.END).strip()

        if not root_dir or not dir_structure:
            return

        lines = dir_structure.split('\n')
        parent_dirs = [root_dir]
        for line in lines:
            depth = line.count('\t')
            dir_name = line.strip()
            current_dir = os.path.join(*parent_dirs[:depth + 1], dir_name)
            parent_dirs = parent_dirs[:depth + 1] + [current_dir]
            os.makedirs(current_dir, exist_ok=True)

        self.text_field.delete('1.0', tk.END)
        messagebox.showinfo("Success", "Directories created successfully!")


if __name__ == '__main__':
    app = DirectoryBuilder()
    app.mainloop()
