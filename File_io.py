from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
import requests
from PyInstaller.loader.pyiboot01_bootstrap import entry
from Scripts.Cripta import window
from bottle import response, request
from setuptools.command.upload import upload


def upload():
    filepath = fd.askopenfilename()
    if filepath:
        files = {"file": open(filepath, "rb")}
        response = requests.post("hhtps://file.io", files=file)
        if response.status_code == 200:
            link = response.json()["link"]
            entry.insert(0, link)







window = Tk()
window.title("Сохранение файлов в облаке")
window.geometry("400x200")

button = ttk.Button(text="Загрузить файл", command=upload)
button.pack()

entry = ttk.Entry()
entry.pack()

window.mainloop()

