import tkinter
import socket
ventana = tkinter.Tk()
#       nos ayuda a darles medidas especificas a la cventana (anchoxalto
ventana.geometry("600x200")
#       a una variable le asignamos el import tkinter , ocupamos.label(etiqueta)
#      le enviamos(vetana_nom, y lo que le pondremos
#etiqueta = tkinter.Label(ventana, text = "helouder")
#       tambien le podemos asignar color con , bg(background) = "color"
p= "hola "
Nombre_usu = socket.gethostname()
etiqueta = tkinter.Label(ventana, text = p + Nombre_usu, bg ="red")


#       para darle una acomodadita y ponerla en la ventana le asignaremos .pack a la etiqueta
#etiqueta.pack()

#       pero ahora si queremos posicionarla en algun punto usaremos
#nombre etiqueta.pack(side(lado).LADO(en MAYUSCULAS) must be top, bottom, left, or right
etiqueta.pack(side= tkinter.TOP)


        #mainloop hace que siga constante
ventana.mainloop()
#metodos que admiten bind button canvas checkout, entry frame, entrym label
#list box Menu, menubutton, message, scale, scrollbar, text topleve,