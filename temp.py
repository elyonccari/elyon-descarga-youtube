import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage, Label, Entry, Button

def descargar_video():
    enlace = video_entry.get()
    if enlace:
        try:
           
            directorio_script = os.path.dirname(os.path.abspath(__file__))
            
           
            ydl_opts = {
                'outtmpl': os.path.join(directorio_script, '%(title)s.%(ext)s'),
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([enlace])
                
            messagebox.showinfo("¡Genial!", "¡El video ha sido capturado con éxito! 🎉")
        except Exception as e:
            
            messagebox.showerror("¡Oh no!", f"¡Algo salió mal! Error: {str(e)}")
    else:
        
        messagebox.showwarning("¡Atención!", "¡Parece que olvidaste poner un enlace! 🤔")

def pegar_enlace():
    try:
        
        enlace = root.clipboard_get()
        video_entry.delete(0, tk.END) 
        video_entry.insert(0, enlace) 
    except tk.TclError:
        
        messagebox.showwarning("¡Oops!", "¡No hay enlace en el portapapeles! 🕵️")

root = tk.Tk()
root.title("¡Descargador de Videos Super Secreto!")
root.config(bd=15)


try:
    imagen = PhotoImage(file="images.png")
    foto = Label(root, image=imagen, bd=0)
    foto.grid(row=0, column=1, columnspan=3) 
except Exception as e:
    print(f"No se pudo cargar la imagen. ¡El misterio de la imagen no resuelto! Error: {e}")


instrucciones = Label(root, text="¡El programa más épico de Elyon, ahora con superpoderes!")
instrucciones.grid(row=1, column=1, columnspan=3) 


video_entry = Entry(root, width=50)
video_entry.grid(row=2, column=1, columnspan=2)  


boton_descargar = Button(root, text="¡Descarga y a gozar!", command=descargar_video)
boton_descargar.grid(row=3, column=1)

boton_pegar = Button(root, text="¡Pega el enlace!", command=pegar_enlace)
boton_pegar.grid(row=3, column=2)

root.mainloop()
