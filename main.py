import customtkinter as ctk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import pickle

class SistemaGerenciamentoTarefas:
    def __init__(self, root):
        """ Inicializa o sistema de gerenciamento de tarefas """
        self.root = root
        self.root.title("Sistema de Gerenciamento de Tarefas")
        self.root.geometry("1050x610")

        # Adiciona o ícone da janela
        self.root.iconbitmap("assets/Icon.png")  # Certifique-se de que o caminho esteja correto

        # Senha padrão
        self.senha = "12345"

        # Carregar as tarefas do arquivo
        self.tarefas = self.carregar_tarefas()
        self.tarefa_selecionada = None
        self.tarefa_selecionada_indice = None  # Armazena o índice da tarefa selecionada

        # Carregar imagem de fundo
        self.background_image = ctk.CTkImage(Image.open("assets/inicial.png"), size=(505, 610))

        # Exibe a tela inicial
        self.tela_inicial()

    def carregar_fundo(self):
        """ Configura a imagem de fundo em todas as telas """
        label_background = ctk.CTkLabel(self.root, image=self.background_image)
        label_background.place(relwidth=1, relheight=1)

    def salvar_tarefas(self):
        """ Salva as tarefas no arquivo """
        with open('tarefas.pkl', 'wb') as file:
            pickle.dump(self.tarefas, file)

    def carregar_tarefas(self):
        """ Carrega as tarefas do arquivo """
        try:
            with open('tarefas.pkl', 'rb') as file:
                return pickle.load(file)
        except FileNotFoundError:
            return []

    def adicionar_botao_voltar(self, comando):
        """ Adiciona um botão 'Voltar' no canto superior esquerdo """
        btn_voltar = ctk.CTkButton(self.root, text="Voltar", font=("Arial", 12), command=comando, fg_color="#3A5357", hover_color="#2B4145")
        btn_voltar.place(x=10, y=10)

    def tela_inicial(self):
        """ Cria a tela inicial """
        for widget in self.root.winfo_children():
            widget.destroy()

        # Divisão da tela em dois frames
        frame_esquerda = ctk.CTkFrame(self.root, width=526, height=610, fg_color="white")
        frame_esquerda.grid(row=0, column=0, sticky="ns")
        frame_esquerda.place(x=0, y=0)

        # Ajuste para expandir o frame_direita
        frame_direita = ctk.CTkFrame(self.root, width=525, height=610, fg_color="#A0C4FF")
        frame_direita.grid(row=0, column=1, sticky="nsew")  # Expandir para ocupar o espaço restante
        frame_direita.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

        # Adicionando a imagem de fundo à esquerda
        label_imagem = ctk.CTkLabel(frame_esquerda, image=self.background_image)
        label_imagem.place(relx=0.5, rely=0.5, anchor="center")

        # Conteúdo à direita
        label_titulo = ctk.CTkLabel(frame_direita, text="Tasks To Do", font=("Roboto", 45, "normal"), padx=10, pady=10, text_color="#312D6F")
        label_titulo.pack(pady=(80, 50))


        # Botões de ação na coluna da direita
        btn_add_tarefa = ctk.CTkButton(frame_direita, text="Adicionar Tarefa", font=("Arial", 12), width=245, height=44, command=self.tela_adicionar_tarefa, fg_color="#5856D6", hover_color="#4644ab")
        btn_add_tarefa.pack(pady=10)

        btn_ver_tarefas = ctk.CTkButton(frame_direita, text="Ver Todas as Tarefas", font=("Arial", 12), width=245, height=44, command=self.tela_lista_tarefas, fg_color="#5856D6", hover_color="#4644ab")
        btn_ver_tarefas.pack(pady=10)

        btn_redefinir_senha = ctk.CTkButton(frame_direita, text="Redefinir Senha", font=("Arial", 12), width=245, height=44, command=self.tela_solicitar_senha_redefinir, fg_color="#5856D6", hover_color="#4644ab")
        btn_redefinir_senha.pack(pady=10)

        # Expande o frame principal em toda a janela
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)


    def tela_adicionar_tarefa(self):
       """ Exibe a tela de adicionar tarefa """
       # Define a cor de fundo da janela principal para cobrir toda a tela
       self.root.configure(bg="#8497F633")
    
       # Remove todos os widgets da tela
       for widget in self.root.winfo_children():
           widget.destroy()
    
       # Cria o frame principal com as dimensões e posicionamento corretos
       frame_principal = ctk.CTkFrame(self.root, fg_color="#D6D6F5", corner_radius=10, width=1050, height=610)
       frame_principal.place(relx=0.5, rely=0.5, anchor="center")
    
       # Título da tela
       ctk.CTkLabel(frame_principal, text="Tarefas", font=("Arial", 20, "bold"), text_color="#312D6F").pack(pady=(10, 20))
    
       # Campo Nome
       ctk.CTkLabel(frame_principal, text="Nome", font=("Arial", 12), text_color="black", anchor="w").pack(fill="x", padx=20)
       nome_entry = ctk.CTkEntry(frame_principal, placeholder_text="Nome da tarefa", font=("Arial", 12), fg_color="#FFF", text_color="black", border_color="#555")
       nome_entry.pack(fill="x", padx=20, pady=(0, 10))
    
       # Campo Tipo
       ctk.CTkLabel(frame_principal, text="Tipo", font=("Arial", 12), text_color="black", anchor="w").pack(fill="x", padx=20)
       tipo_var = ctk.StringVar()
       tipo_menu = ctk.CTkComboBox(frame_principal, variable=tipo_var, values=["Pessoal", "Empresarial", "Acadêmico"], font=("Arial", 12), fg_color="#FFF", text_color="black")
       tipo_menu.pack(fill="x", padx=20, pady=(0, 10))
    
       # Campo Descrição
       ctk.CTkLabel(frame_principal, text="Descrição", font=("Arial", 12), text_color="black", anchor="w").pack(fill="x", padx=20)
       descricao_entry = ctk.CTkTextbox(frame_principal, font=("Arial", 12), height=60, fg_color="#FFF", text_color="black")
       descricao_entry.pack(fill="x", padx=20, pady=(0, 10))
    
       # Linha para Prazo e Status
       linha_inferior = ctk.CTkFrame(frame_principal, fg_color="#D6D6F5")
       linha_inferior.pack(fill="x", padx=20, pady=(0, 10))
    
       # Campo Prazo
       ctk.CTkLabel(linha_inferior, text="Prazo", font=("Arial", 12), text_color="black", anchor="w").grid(row=0, column=0, sticky="w", padx=(0, 10))
       prazo_entry = ctk.CTkEntry(linha_inferior, placeholder_text="dd/mm/yyyy", font=("Arial", 12), fg_color="#FFF", text_color="black")
       prazo_entry.grid(row=1, column=0, sticky="we")
    
       # Campo Status
       ctk.CTkLabel(linha_inferior, text="Status", font=("Arial", 12), text_color="black", anchor="w").grid(row=0, column=1, sticky="w", padx=(10, 0))
       status_var = ctk.StringVar(value="Em processo")
       status_menu = ctk.CTkComboBox(linha_inferior, variable=status_var, values=["Em processo", "Concluída", "Pendente"], font=("Arial", 12), fg_color="#FFF", text_color="black")
       status_menu.grid(row=1, column=1, sticky="we")
    
       # Botão Salvar
       btn_salvar = ctk.CTkButton(frame_principal, text="Salvar", font=("Arial", 12), width=200, fg_color="#4A3CB1", hover_color="#3A2B8C", command=lambda: self.salvar_tarefa(
           nome_entry.get(),
           tipo_var.get(),
           prazo_entry.get(),
           status_var.get(),
           descricao_entry.get("1.0", "end-1c")
       ))
       btn_salvar.pack(pady=(20, 10))






    def salvar_tarefa(self, nome, tipo, prazo, prioridade, status, descricao):
        """ Salva a tarefa na lista e no arquivo """
        if not nome or not tipo or not prazo or not prioridade or not status or not descricao.strip():
            messagebox.showerror("Erro", "Preencha todos os campos.")
        else:
            self.tarefas.append({"nome": nome, "tipo": tipo, "prazo": prazo, "prioridade": prioridade, "status": status, "descricao": descricao})
            self.salvar_tarefas()
            messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
            self.tela_inicial()

    def tela_lista_tarefas(self):
        """ Exibe a lista de tarefas """
        for widget in self.root.winfo_children():
            widget.destroy()

        self.carregar_fundo()

        self.adicionar_botao_voltar(self.tela_inicial)

        label = ctk.CTkLabel(self.root, text="Lista de Tarefas", font=("Arial", 16), padx=10, pady=10)
        label.pack(pady=20)

        frame_lista = ctk.CTkFrame(self.root)
        frame_lista.pack(pady=10)

        colunas = ("Nome", "Tipo", "Prazo", "Prioridade", "Status")
        self.lista_tarefas = ttk.Treeview(frame_lista, columns=colunas, show='headings')
        self.lista_tarefas.column("Nome", width=150)
        self.lista_tarefas.column("Tipo", width=100)
        self.lista_tarefas.column("Prazo", width=100)
        self.lista_tarefas.column("Prioridade", width=100)
        self.lista_tarefas.column("Status", width=150)

        for col in colunas:
            self.lista_tarefas.heading(col, text=col)

        self.lista_tarefas.pack()

        for tarefa in self.tarefas:
            self.lista_tarefas.insert("", "end", values=(tarefa["nome"], tarefa["tipo"], tarefa["prazo"], tarefa["prioridade"], tarefa["status"]))

        btn_editar_tarefa = ctk.CTkButton(self.root, text="Editar Tarefa", font=("Arial", 12), width=200, command=self.ver_descricao_tarefa, fg_color="black")
        btn_editar_tarefa.pack(pady=10)

        btn_ver_detalhes = ctk.CTkButton(self.root, text="Ver Detalhes da Tarefa", font=("Arial", 12), width=200, command=self.tela_detalhes_tarefa, fg_color="black")
        btn_ver_detalhes.pack(pady=10)

        btn_marcar_concluida = ctk.CTkButton(self.root, text="Marcar como Concluída", font=("Arial", 12), width=200, command=self.marcar_concluida, fg_color="black")
        btn_marcar_concluida.pack(pady=10)
        
        btn_remover = ctk.CTkButton(self.root, text="Remover", font=("Arial", 12), width=200, command=self.tela_solicitar_senha_para_remover, fg_color="black")
        btn_remover.pack(pady=10)

    def ver_descricao_tarefa(self):
        """ Exibe a tela para editar a tarefa selecionada """
        self.selecionar_tarefa()
        if self.tarefa_selecionada is None:
            messagebox.showerror("Erro", "Selecione uma tarefa para editar.")
            return
        self.tela_descricao_tarefa()

    def tela_detalhes_tarefa(self):
        """ Exibe uma tela com o nome e a descrição da tarefa selecionada """
        self.selecionar_tarefa()
        if self.tarefa_selecionada is None:
            messagebox.showerror("Erro", "Selecione uma tarefa para ver os detalhes.")
            return
        
        tarefa = self.tarefas[self.tarefa_selecionada]

        for widget in self.root.winfo_children():
            widget.destroy()

        self.carregar_fundo()
        self.adicionar_botao_voltar(self.tela_lista_tarefas)

        ctk.CTkLabel(self.root, text="Detalhes da Tarefa", font=("Arial", 16), padx=5).pack(pady=10)
        ctk.CTkLabel(self.root, text=f"Nome: {tarefa['nome']}", font=("Arial", 14), width=50,height=50, padx=5, fg_color="#AAA3A3", text_color="black").pack(pady=5)
        ctk.CTkLabel(self.root, text="Descrição:", font=("Arial", 16), padx=5).pack(pady=5)

        # Substitui o rótulo da descrição por um campo branco como na tela de adicionar tarefa
        descricao_entry = ctk.CTkTextbox(self.root, font=("Arial", 12), height=100, width=400, fg_color="#AAA3A3", text_color="black")
        descricao_entry.insert("1.0", tarefa["descricao"])
        descricao_entry.configure(state="disabled")  # Impede edição, já que é uma visualização
        descricao_entry.pack(pady=10)

    def tela_descricao_tarefa(self):
        """ Exibe a tela para editar os detalhes da tarefa selecionada """
        for widget in self.root.winfo_children():
            widget.destroy()

        self.carregar_fundo()
        self.adicionar_botao_voltar(self.tela_lista_tarefas)

        tarefa = self.tarefas[self.tarefa_selecionada]

        ctk.CTkLabel(self.root, text="Nome da Tarefa", font=("Arial", 12), padx=5, pady=2).pack(pady=5)
        nome_entry = ctk.CTkEntry(self.root, font=("Arial", 12), fg_color="#AAA3A3", text_color="black")
        nome_entry.insert(0, tarefa["nome"])
        nome_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Tipo da Tarefa", font=("Arial", 12), padx=35, pady=2).pack(pady=5)
        tipo_var = ctk.StringVar()
        tipo_menu = ctk.CTkComboBox(self.root, variable=tipo_var, values=["Pessoal", "Empresarial", "Acadêmico"], font=("Arial", 12), fg_color="#AAA3A3", text_color="black")
        tipo_menu.pack(pady=5)

        ctk.CTkLabel(self.root, text="Prazo", font=("Arial", 12), padx=50, pady=2).pack(pady=5)
        prazo_entry = ctk.CTkEntry(self.root, font=("Arial", 12), fg_color="#AAA3A3", text_color="black")
        prazo_entry.insert(0, tarefa["prazo"])
        prazo_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Prioridade", font=("Arial", 12), padx=45, pady=2).pack(pady=5)
        prioridade_var = ctk.StringVar()
        prioridade_menu = ctk.CTkComboBox(self.root, variable=prioridade_var, values=["Baixa", "Média", "Alta"], font=("Arial", 12), fg_color="#AAA3A3", text_color="black")
        prioridade_menu.pack(pady=5)

        ctk.CTkLabel(self.root, text="Status", font=("Arial", 12), padx=57, pady=2).pack(pady=5)
        status_var = ctk.StringVar(value="Pendente")
        status_menu = ctk.CTkComboBox(self.root, variable=status_var, values=["Pendente", "Concluída", "Parcialmente Concluída"], font=("Arial", 12), fg_color="#AAA3A3", text_color="black")
        status_menu.pack(pady=5)

        ctk.CTkLabel(self.root, text="Descrição", font=("Arial", 12), padx=47, pady=2).pack(pady=5)
        descricao_entry = ctk.CTkTextbox(self.root, font=("Arial", 12), height=100, width=400, fg_color="#AAA3A3", text_color="black")
        descricao_entry.insert("1.0", tarefa["descricao"])
        descricao_entry.pack(pady=5)

        btn_salvar = ctk.CTkButton(self.root, text="Salvar Alterações", font=("Arial", 12), width=20, command=lambda: self.salvar_edicao_tarefa(nome_entry.get(), tipo_var.get(), prazo_entry.get(), prioridade_var.get(), status_var.get(), descricao_entry.get("1.0", "end-1c")), fg_color="black")
        btn_salvar.pack(pady=20)

    def salvar_edicao_tarefa(self, nome, tipo, prazo, prioridade, status, descricao):
        """ Salva as edições feitas na tarefa """
        if not nome or not tipo or not prazo or not prioridade or not status or not descricao.strip():
            messagebox.showerror("Erro", "Preencha todos os campos.")
        else:
            self.tarefas[self.tarefa_selecionada] = {"nome": nome, "tipo": tipo, "prazo": prazo, "prioridade": prioridade, "status": status, "descricao": descricao}
            self.salvar_tarefas()
            messagebox.showinfo("Sucesso", "Tarefa editada com sucesso!")
            self.tela_lista_tarefas()

    def tela_solicitar_senha_para_remover(self):
        """ Exibe uma tela para solicitar a senha antes de remover a tarefa """
        senha_popup = ctk.CTkToplevel(self.root)
        senha_popup.title("Autenticação de Senha")
        senha_popup.geometry("300x150")

        ctk.CTkLabel(senha_popup, text="Digite a senha para remover a tarefa:", font=("Arial", 12)).pack(pady=10)
        senha_entry = ctk.CTkEntry(senha_popup, show="*", font=("Arial", 12))
        senha_entry.pack(pady=5)

        btn_confirmar = ctk.CTkButton(senha_popup, text="Confirmar", font=("Arial", 12), command=lambda: self.verificar_senha(senha_entry.get(), senha_popup, self.remover_tarefa))
        btn_confirmar.pack(pady=10)

    def verificar_senha(self, senha_digitada, popup, acao_sucesso):
        """ Verifica se a senha digitada está correta e executa uma ação se estiver correta """
        if senha_digitada == self.senha:
            popup.destroy()
            acao_sucesso()
        else:
            messagebox.showerror("Erro", "Senha incorreta!")

    def remover_tarefa(self):
        """ Remove a tarefa selecionada """
        self.selecionar_tarefa()
        if self.tarefa_selecionada is None:
            messagebox.showerror("Erro", "Selecione uma tarefa para remover.")
            return
        self.tarefas.pop(self.tarefa_selecionada)
        self.salvar_tarefas()
        messagebox.showinfo("Sucesso", "Tarefa removida com sucesso.")
        self.tela_lista_tarefas()

    def tela_solicitar_senha_redefinir(self):
        """ Solicita a senha antes de redirecionar para a tela de redefinir senha """
        senha_popup = ctk.CTkToplevel(self.root)
        senha_popup.title("Autenticação de Senha")
        senha_popup.geometry("300x150")

        ctk.CTkLabel(senha_popup, text="Digite a senha para redefinir:", font=("Arial", 12)).pack(pady=10)
        senha_entry = ctk.CTkEntry(senha_popup, show="*", font=("Arial", 12))
        senha_entry.pack(pady=5)

        btn_confirmar = ctk.CTkButton(senha_popup, text="Confirmar", font=("Arial", 12), command=lambda: self.verificar_senha(senha_entry.get(), senha_popup, self.tela_redefinir_senha))
        btn_confirmar.pack(pady=10)

    def tela_redefinir_senha(self):
        """ Exibe a tela de redefinição de senha """
        for widget in self.root.winfo_children():
            widget.destroy()

        self.carregar_fundo()
        self.adicionar_botao_voltar(self.tela_inicial)

        ctk.CTkLabel(self.root, text="Redefinição de Senha", font=("Arial", 16), padx=10, pady=10).pack(pady=(10, 40))

        ctk.CTkLabel(self.root, text="Senha atual:", font=("Arial", 12), padx=5, pady=2).pack(pady=5)
        senha_atual_entry = ctk.CTkEntry(self.root, show="*", font=("Arial", 12), fg_color="#AAA3A3", text_color="black")
        senha_atual_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Nova senha:", font=("Arial", 12), padx=5, pady=2).pack(pady=5)
        nova_senha_entry = ctk.CTkEntry(self.root, show="*", font=("Arial", 12), fg_color="#AAA3A3", text_color="black")
        nova_senha_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Confirmar nova senha:", font=("Arial", 12), padx=5, pady=2).pack(pady=5)
        confirmar_nova_senha_entry = ctk.CTkEntry(self.root, show="*", font=("Arial", 12), fg_color="#AAA3A3", text_color="black")
        confirmar_nova_senha_entry.pack(pady=5)

        btn_salvar_senha = ctk.CTkButton(self.root, text="Redefinir Senha", font=("Arial", 12), command=lambda: self.redefinir_senha(senha_atual_entry.get(), nova_senha_entry.get(), confirmar_nova_senha_entry.get()), fg_color="black")
        btn_salvar_senha.pack(pady=20)

    def redefinir_senha(self, senha_atual, nova_senha, confirmar_nova_senha):
        """ Redefine a senha se a senha atual estiver correta e as novas senhas coincidirem """
        if senha_atual == self.senha:
            if nova_senha == confirmar_nova_senha and nova_senha.strip():
                self.senha = nova_senha
                messagebox.showinfo("Sucesso", "Senha redefinida com sucesso!")
                self.tela_inicial()
            else:
                messagebox.showerror("Erro", "As novas senhas não coincidem ou estão em branco!")
        else:
            messagebox.showerror("Erro", "Senha atual incorreta!")

    def marcar_concluida(self):
        """ Alterna o status da tarefa entre 'Pendente', 'Parcialmente Concluída', e 'Concluída' """
        self.selecionar_tarefa()
        if self.tarefa_selecionada is None:
            messagebox.showerror("Erro", "Selecione uma tarefa para alterar o status.")
            return

        status_atual = self.tarefas[self.tarefa_selecionada]['status']
        if status_atual == "Pendente":
            self.tarefas[self.tarefa_selecionada]['status'] = "Parcialmente Concluída"
        elif status_atual == "Parcialmente Concluída":
            self.tarefas[self.tarefa_selecionada]['status'] = "Concluída"
        else:
            self.tarefas[self.tarefa_selecionada]['status'] = "Pendente"

        self.salvar_tarefas()
        messagebox.showinfo("Sucesso", f"Status alterado para {self.tarefas[self.tarefa_selecionada]['status']}.")
        self.tela_lista_tarefas()

    def selecionar_tarefa(self):
        """ Seleciona uma tarefa na lista de tarefas """
        try:
            selected_item = self.lista_tarefas.selection()[0]
            self.tarefa_selecionada = self.lista_tarefas.index(selected_item)
            self.tarefa_selecionada_indice = selected_item  # Armazena o identificador da tarefa
        except IndexError:
            self.tarefa_selecionada = None
            self.tarefa_selecionada_indice = None

# Inicializa o app
root = ctk.CTk()
app = SistemaGerenciamentoTarefas(root)
root.mainloop()
