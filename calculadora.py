import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

visor = tk.Entry(janela, font=("Arial", 20), justify="right")
visor.pack(fill="both", padx=10, pady=10)

def clicar(valor):
    atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, atual + valor)
def calcular():
    conta = visor.get()
    try:
        resultado = eval(conta)
        visor.delete(0, tk.END)
        visor.insert(0, resultado)
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")
def limpar():
    visor.delete(0, tk.END)

# 🔥 FRAME DOS BOTÕES
frame = tk.Frame(janela)
frame.pack()

tk.Button(frame, text="7", width=5, height=2, command=lambda: clicar("7")).grid(row=0, column=0)
tk.Button(frame, text="8", width=5, height=2, command=lambda: clicar("8")).grid(row=0, column=1)
tk.Button(frame, text="9", width=5, height=2, command=lambda: clicar("9")).grid(row=0, column=2)

tk.Button(frame, text="4", width=5, height=2, command=lambda: clicar("4")).grid(row=1, column=0)
tk.Button(frame, text="5", width=5, height=2, command=lambda: clicar("5")).grid(row=1, column=1)
tk.Button(frame, text="6", width=5, height=2, command=lambda: clicar("6")).grid(row=1, column=2)

tk.Button(frame, text="1", width=5, height=2, command=lambda: clicar("1")).grid(row=2, column=0)
tk.Button(frame, text="2", width=5, height=2, command=lambda: clicar("2")).grid(row=2, column=1)
tk.Button(frame, text="3", width=5, height=2, command=lambda: clicar("3")).grid(row=2, column=2)
tk.Button(frame, text="0", width=5, height=2, command=lambda: clicar("0")).grid(row=3, column=0)

tk.Button(frame, text="+", width=5, height=2, command=lambda: clicar("+")).grid(row=3, column=1)

tk.Button(frame, text="=", width=5, height=2, bg="lightgreen", command=calcular).grid(row=3, column=2)
tk.Button(frame, text="C", width=5, height=2, command=limpar).grid(row=3, column=3)
tk.Button(frame, text="-", width=5, height=2, command=lambda: clicar("-")).grid(row=0, column=3)
tk.Button(frame, text="*", width=5, height=2, command=lambda: clicar("*")).grid(row=1, column=3)
tk.Button(frame, text="/", width=5, height=2, command=lambda: clicar("/")).grid(row=2, column=3)
janela.mainloop()
