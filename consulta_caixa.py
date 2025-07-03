'''Descrição do programa
1 o pragrama deve verificar se o o caixa esta  fantando dinheiro 
2 o Programa deve retornar ao usuario quanto falta 
3 esse programa tem que esta em uma pagina na internet para ser usado online'''

'''Erros que tenho que reparar
1 fazer o pragrama calcular independente de usar . ou ,'''

import customtkinter as ctk

def consultar_caixa():
    try:
        valor_abastecimentos = float(campo_abastecimentos.get())
        valor_dinheiro_relatorio = float(campo_dinheiro_relatorio.get())
        valor_sangrias = float(campo_sangrias.get())
        valor_dinheiro = float(campo_dinheiro.get())

        total_caixa = valor_abastecimentos + valor_dinheiro_relatorio
        total_din_sang = valor_sangrias + valor_dinheiro
        resultado_caixa = total_caixa - total_din_sang

        if total_caixa > total_din_sang:
            resultado.configure(text=f"Caixa está FALTANDO R$ {abs(resultado_caixa):.2f}")
        elif total_caixa < total_din_sang:
            resultado.configure(text=f"Caixa está SOBRANDO R$ {abs(resultado_caixa):.2f}")
        else:
            resultado.configure(text="Caixa está CERTINHO!")

    except ValueError:
        resultado.configure(text="Erro: digite apenas números válidos com ponto.")

# Aparência da interface
ctk.set_appearance_mode('dark')

# Criar a janela
janela = ctk.CTk()
janela.title('Consulta Meu Caixa')
janela.geometry('350x400')

# Campo: Abastecimentos
ctk.CTkLabel(janela, text='Valor total dos abastecimentos').pack(pady=5)
campo_abastecimentos = ctk.CTkEntry(janela, placeholder_text='Ex: 1000.50')
campo_abastecimentos.pack(pady=5)

# Campo: Dinheiro no relatório
ctk.CTkLabel(janela, text='Dinheiro no relatório').pack(pady=5)
campo_dinheiro_relatorio = ctk.CTkEntry(janela, placeholder_text='Ex: 300.00')
campo_dinheiro_relatorio.pack(pady=5)

# Campo: Sangrias
ctk.CTkLabel(janela, text='Valor das sangrias').pack(pady=5)
campo_sangrias = ctk.CTkEntry(janela, placeholder_text='Ex: 200.00')
campo_sangrias.pack(pady=5)

# Campo: Dinheiro físico
ctk.CTkLabel(janela, text='Dinheiro que você tem').pack(pady=5)
campo_dinheiro = ctk.CTkEntry(janela, placeholder_text='Ex: 1100.00')
campo_dinheiro.pack(pady=5)

# Botão de consulta
ctk.CTkButton(janela, text='Consultar', command=consultar_caixa).pack(pady=15)

# Resultado
resultado = ctk.CTkLabel(janela, text='')
resultado.pack(pady=10)

# Iniciar a aplicação
janela.mainloop()






#janela = ctk()
#janela.title('Consulta Caixa')

#texto_orientacao = (janela,text='Digite as informações abaixo')
#texto_orientacao.grid(column=0, row=1)



#botao = Button(janela, text='consultar caixa',command=consulta_caixa)
#botao.grid(column=0, row=2)




#janela.mainloop()