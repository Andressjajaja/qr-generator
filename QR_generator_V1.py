import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import qrcode
from tkinter import messagebox
from PIL import Image, ImageTk


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

#VENTANA PRINCIPAL-----------------------------------------------------------------------
ventana = ctk.CTk()
ventana.title("QRcode Generator (By: Andrés_Mrc)")
ventana.geometry("800x500")
ventana.minsize(500,250)
ventana.resizable(width=False, height=False)

#IMAGENSITA (PARTE SUPERIOR IZQUIERDA) 
#ventana.iconbitmap("D:\Proyecto_interfazQR\img\logoQR.ico")

#FUNCIONES-------------------------------------------------------------------------------
def resize_qr_image(qr_image, container_width, container_height, margin=20):
    max_size = min(container_width, container_height) - margin * 2

    qr_image = qr_image.resize((max_size, max_size), Image.LANCZOS)
    return qr_image

def limpiar_campos():
    entrada.delete(0, tk.END)
    label.configure(image="")
    label.image = None

def generacion():
    global img_qr
    url = entrada.get().strip()

    if not url:
        messagebox.showwarning("Error", "Por favor ingrese una URL")
        limpiar_campos()
        return

    qr = qrcode.QRCode(version=1, box_size=15, border=2)
    qr.add_data(url)
    qr.make(fit=True)

    img_qr = qr.make_image(fill='black', back_color='white')
    

    container_width = 250
    container_height = 250
    
    img_qr_resized = resize_qr_image(img_qr, container_width, container_height)
    img_qr_tk = ImageTk.PhotoImage(img_qr_resized)

    #ACTUALIZACIÓN DE LABEL
    label.configure(image=img_qr_tk)
    label.image = img_qr_tk

def guardar():
    if 'img_qr' not in globals():
        messagebox.showwarning("Error", "Primero debe generar un código QR")
        limpiar_campos()
        return
        
    guardar_qr = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("All files", "*.*")],
        title="Guardar código QR"
    )
    if guardar_qr:
        img_qr.save(guardar_qr)
        messagebox.showinfo("Éxito", "Código QR guardado correctamente")
        limpiar_campos()

def cambiar_tema():
    if switch_tema.get() == 1:
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

#FRAME (CUADRADO DENTRO DE LA VENTANA)---------------------------------------------------
fondo = ctk.CTkFrame(master=ventana, fg_color="#451e84", width=400, height=600)
fondo.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
#fondo.pack(side=TOP, fill="both", expand=True)

#DONDE SE MUESTRA EL QR
fondo2 = ctk.CTkFrame(master=ventana, fg_color="#451e84", width=250, height=250)
fondo2.place(relx=0.75, rely=0.5, anchor=tk.CENTER)
fondo2.grid_propagate(False)  # Mantener tamaño fijo


#DEGRADADO DE FRAMES---------------------------------------------------------------------
frame_principal = ctk.CTkFrame(master=fondo, fg_color="#451e84", width=500, height=65)
frame_principal.place(relx=0.5, rely=0.86, anchor=tk.CENTER)

frame1 = ctk.CTkFrame(master=frame_principal, fg_color="#9858ff", width=500, height=30)
frame1.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

frame2 = ctk.CTkFrame(master=frame_principal, fg_color="#7443c4", width=500, height=20)
frame2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

frame3 = ctk.CTkFrame(master=frame_principal, fg_color="#55318f", width=500, height=20)
frame3.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


#TEXTO QUE SALE EN LA VENTANA------------------------------------------------------------
texto = ctk.CTkLabel(master=fondo, text="Ingrese URL", text_color="#FFFFFF", font=("Verdana",20))
texto.place(relx=0.5, rely=0.4, anchor="center")


#CAJA DE TEXTO (DONDE INGRESAN EL TEXTO)-------------------------------------------------
entrada = ctk.CTkEntry(fondo, placeholder_text="URL", width=250, height=35, corner_radius=15, border_color="#9858ff")
#entrada.grid(columnspan=2, row=1, padx=4, pady=4)
entrada.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


#BOTON (GENERAR)-------------------------------------------------------------------------
btn = ctk.CTkButton(master=fondo, text="Generar", corner_radius=15, width=100, height=35,
                    fg_color="#9858ff", hover_color="#55318f", command=generacion)
btn.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

#BOTON (GUARDAR)
btn_guardar = ctk.CTkButton(master=ventana, text="Guardar", corner_radius=15, width=100, height=35,
                    fg_color="#9858ff", hover_color="#55318f", command=guardar)
btn_guardar.place(relx=0.87, rely=0.9, anchor=tk.CENTER)

#SWITCH CAMBIO DE TEMA
switch_tema = ctk.CTkSwitch(master=ventana, text="Tema",command=cambiar_tema,
                           fg_color="#383838", button_color="#9858ff", button_hover_color="#55318f")
switch_tema.place(relx=0.95, rely=0.05, anchor=tk.CENTER)

#PARA COLOCAR EL QR CREADO EN EL LABEL---------------------------------------------------
label = ctk.CTkLabel(master=fondo2, text=" ")
label.place(relx=0.5, rely=0.5, anchor="center")
label.configure(fg_color="#451e84")



ventana.mainloop()