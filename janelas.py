from tkinter import *
class Application:
   def __init__(self, master=None):
         self.container1 = Frame(master)
         self.container1.pack()
         self.msg = Label(self.container1,text="A ps está chegando!")
         self.msg["font"] = ("Verdana", "10", "bold")
         self.msg.pack()
         self.sair = Button(self.container1)
         self.sair["text"] = "Clique aqui para sair"
         self.sair["font"] = ("Verdana", "20")
         self.botao.bind("<Button-1>", self.mudarCurso)
         self.sair.pack()
         
root = Tk()  
Application(root)
root.mainloop()    

