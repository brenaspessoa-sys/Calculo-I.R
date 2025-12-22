import tkinter as tk
from tkinter import messagebox

def calcular_imposto():
    try:
        renda = float(entrada_renda.get())
        if renda < 0:
            messagebox.showerror("Erro", "Por favor insira um valor positivo")
            return
            
        # Calculando imposto de renda com a dedução
        if renda <= 2259.20:
            imposto = 0
        elif renda <= 2826.65:
            imposto = (renda*0.075) - 169.44
        elif renda <= 3751.05:
            imposto = (renda*0.15) - 381.44
        elif renda <= 4664.68:
            imposto = (renda*0.225) - 662.77
        else:
            imposto = (renda*0.275) - 896

        # Mostrando resultado
        if imposto == 0:
            resultado = 'Você está isento do imposto de renda!'
        else:
            resultado = f'O valor do seu imposto de renda é R$ {imposto:.2f}'
            
        if messagebox.askyesno("Carga Efetiva", "Deseja saber a carga efetiva do seu IR?"):
            carga = (imposto/renda)*100
            resultado += f'\nA carga efetiva do IR para sua renda é {carga:.2f}%'
            
        messagebox.showinfo("RESULTADO", resultado)
            
    except ValueError:
        messagebox.showerror("Erro", "Por favor insira um valor numérico válido")

# Criando janela principal
janela = tk.Tk()
janela.title("Calculadora de Imposto de Renda")
janela.geometry("400x200")

# Criando widgets
tk.Label(janela, text="=== Calculadora de Imposto de Renda ===", font=('Arial', 12, 'bold')).pack(pady=10)
tk.Label(janela, text="Esta calculadora irá ajudar você a calcular seu imposto de renda mensal").pack()

tk.Label(janela, text="Por favor, insira sua renda mensal (R$):").pack(pady=10)
entrada_renda = tk.Entry(janela)
entrada_renda.pack()

tk.Button(janela, text="Calcular Imposto", command=calcular_imposto).pack(pady=20)

janela.mainloop()
