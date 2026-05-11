import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import os
from datetime import datetime

# Nome do arquivo para salvar os dados
DATA_FILE = "copa_bets_data.json"

class BettingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Apostas - Copa dos Bares")
        self.root.geometry("900x600")
        
        self.current_user = None
        self.data = self.load_data()
        
        # Tela inicial
        self.show_login_screen()

    def load_data(self):
        if not os.path.exists(DATA_FILE):
            # Dados iniciais de exemplo
            default_data = {
                "users": {"admin": "1234"}, # Usuário admin padrão (senha: 1234)
                "games": [
                    {"id": 1, "team_a": "Brasil", "team_b": "Argentina", "odd_a": 2.10, "odd_draw": 3.00, "odd_b": 3.50, "status": "Aberto"},
                    {"id": 2, "team_a": "França", "team_b": "Alemanha", "odd_a": 2.50, "odd_draw": 2.80, "odd_b": 2.90, "status": "Aberto"}
                ],
                "bets": []
            }
            return default_data
        else:
            try:
                with open(DATA_FILE, "r") as f:
                    return json.load(f)
            except:
                return {"users": {"admin": "1234"}, "games": [], "bets": []}

    def save_data(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # --- TELA DE LOGIN ---
    def show_login_screen(self):
        self.clear_window()
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(pady=100)

        tk.Label(frame, text="Login - Copa dos Bares", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(frame, text="Usuário:").pack(anchor="w")
        self.entry_user = tk.Entry(frame, width=30)
        self.entry_user.pack(pady=5)

        tk.Label(frame, text="Senha:").pack(anchor="w")
        self.entry_pass = tk.Entry(frame, show="*", width=30)
        self.entry_pass.pack(pady=5)

        tk.Button(frame, text="Entrar", command=self.login, bg="#4CAF50", fg="white", width=15).pack(pady=20)
        tk.Label(frame, text="Dica Admin: user='admin', pass='1234'", fg="gray").pack()

    def login(self):
        user = self.entry_user.get()
        password = self.entry_pass.get()

        if user in self.data["users"] and self.data["users"][user] == password:
            self.current_user = user
            if user == "admin":
                self.show_admin_dashboard()
            else:
                self.show_user_dashboard()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    # --- PAINEL DO ADMINISTRADOR ---
    def show_admin_dashboard(self):
        self.clear_window()
        
        # Header
        header = tk.Frame(self.root, bg="#333", height=50)
        header.pack(fill="x")
        tk.Label(header, text=f"Painel Administrativo (Logado: {self.current_user})", bg="#333", fg="white", font=("Arial", 12)).pack(side="left", padx=20, pady=10)
        tk.Button(header, text="Sair", command=self.show_login_screen).pack(side="right", padx=20, pady=10)

        # Notebook (Abas)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Aba 1: Gerenciar Jogos
        tab_games = tk.Frame(notebook)
        notebook.add(tab_games, text="Gerenciar Jogos")
        self.build_admin_games_tab(tab_games)

        # Aba 2: Ver Apostas
        tab_bets = tk.Frame(notebook)
        notebook.add(tab_bets, text="Ver Todas as Apostas")
        self.build_admin_bets_tab(tab_bets)
        
        # Aba 3: Gerenciar Usuários
        tab_users = tk.Frame(notebook)
        notebook.add(tab_users, text="Gerenciar Usuários")
        self.build_admin_users_tab(tab_users)

    def build_admin_games_tab(self, parent):
        frame_form = tk.LabelFrame(parent, text="Cadastrar Novo Jogo", padx=10, pady=10)
        frame_form.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_form, text="Time A:").grid(row=0, column=0, sticky="e")
        entry_a = tk.Entry(frame_form)
        entry_a.grid(row=0, column=1, padx=5)

        tk.Label(frame_form, text="Odd Time A:").grid(row=0, column=2, sticky="e")
        entry_odd_a = tk.Entry(frame_form, width=8)
        entry_odd_a.grid(row=0, column=3, padx=5)

        tk.Label(frame_form, text="Empate Odd:").grid(row=1, column=0, sticky="e")
        entry_draw = tk.Entry(frame_form, width=8)
        entry_draw.grid(row=1, column=1, padx=5)

        tk.Label(frame_form, text="Time B:").grid(row=1, column=2, sticky="e")
        entry_b = tk.Entry(frame_form)
        entry_b.grid(row=1, column=3, padx=5)

        tk.Label(frame_form, text="Odd Time B:").grid(row=2, column=0, sticky="e")
        entry_odd_b = tk.Entry(frame_form, width=8)
        entry_odd_b.grid(row=2, column=1, padx=5)

        def add_game():
            try:
                new_id = len(self.data["games"]) + 1
                game = {
                    "id": new_id,
                    "team_a": entry_a.get(),
                    "team_b": entry_b.get(),
                    "odd_a": float(entry_odd_a.get()),
                    "odd_draw": float(entry_draw.get()),
                    "odd_b": float(entry_odd_b.get()),
                    "status": "Aberto"
                }
                self.data["games"].append(game)
                self.save_data()
                messagebox.showinfo("Sucesso", "Jogo cadastrado!")
                refresh_list()
                # Limpar campos
                entry_a.delete(0, tk.END)
                entry_b.delete(0, tk.END)
                entry_odd_a.delete(0, tk.END)
                entry_draw.delete(0, tk.END)
                entry_odd_b.delete(0, tk.END)
            except ValueError:
                messagebox.showerror("Erro", "Preencha todos os campos corretamente (odds devem ser números).")

        tk.Button(frame_form, text="Adicionar Jogo", command=add_game, bg="#2196F3", fg="white").grid(row=3, column=1, columnspan=2, pady=10)

        # Lista de Jogos
        tk.Label(parent, text="Jogos Ativos:").pack(anchor="w", padx=10)
        columns = ("ID", "Time A", "Odd A", "Empate", "Odd Emp", "Time B", "Odd B", "Status")
        tree = ttk.Treeview(parent, columns=columns, show="headings", height=10)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        def refresh_list():
            for item in tree.get_children():
                tree.delete(item)
            for g in self.data["games"]:
                tree.insert("", "end", values=(g["id"], g["team_a"], g["odd_a"], "-", g["odd_draw"], g["team_b"], g["odd_b"], g["status"]))
        
        refresh_list()

    def build_admin_bets_tab(self, parent):
        columns = ("ID", "Usuário", "Jogo", "Aposta Em", "Valor", "Retorno Potencial", "Data")
        tree = ttk.Treeview(parent, columns=columns, show="headings", height=15)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.pack(fill="both", expand=True, padx=10, pady=10)

        def refresh_bets():
            for item in tree.get_children():
                tree.delete(item)
            for bet in self.data["bets"]:
                tree.insert("", "end", values=(
                    bet["id"], bet["user"], f"{bet['team_a']} x {bet['team_b']}", 
                    bet["selection"], f"R$ {bet['amount']:.2f}", f"R$ {bet['potential_return']:.2f}", bet["date"]
                ))
        
        refresh_bets()
        tk.Button(parent, text="Atualizar Lista", command=refresh_bets).pack(pady=5)

    def build_admin_users_tab(self, parent):
        frame = tk.Frame(parent, padx=20, pady=20)
        frame.pack()
        
        tk.Label(frame, text="Criar Novo Usuário (Bar/Apostador)").pack()
        
        tk.Label(frame, text="Nome de Usuário:").pack(pady=5)
        new_user_entry = tk.Entry(frame)
        new_user_entry.pack()
        
        tk.Label(frame, text="Senha:").pack(pady=5)
        new_pass_entry = tk.Entry(frame)
        new_pass_entry.pack()
        
        def create_user():
            u = new_user_entry.get()
            p = new_pass_entry.get()
            if u and p:
                if u in self.data["users"]:
                    messagebox.showwarning("Aviso", "Usuário já existe!")
                else:
                    self.data["users"][u] = p
                    self.save_data()
                    messagebox.showinfo("Sucesso", f"Usuário {u} criado!")
                    new_user_entry.delete(0, tk.END)
                    new_pass_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Erro", "Preencha todos os campos")

        tk.Button(frame, text="Criar Usuário", command=create_user, bg="#4CAF50", fg="white").pack(pady=20)
        
        tk.Label(frame, text="Usuários Existentes:").pack()
        users_list = tk.Listbox(frame)
        users_list.pack()
        for u in self.data["users"].keys():
            users_list.insert(tk.END, u)

    # --- PAINEL DO USUÁRIO COMUM ---
    def show_user_dashboard(self):
        self.clear_window()
        
        header = tk.Frame(self.root, bg="#009688", height=50)
        header.pack(fill="x")
        tk.Label(header, text=f"Bem-vindo, {self.current_user}!", bg="#009688", fg="white", font=("Arial", 12)).pack(side="left", padx=20, pady=10)
        tk.Button(header, text="Sair", command=self.show_login_screen).pack(side="right", padx=20, pady=10)

        tk.Label(self.root, text="Jogos Disponíveis para Aposta", font=("Arial", 14, "bold")).pack(pady=20)

        # Lista de jogos para apostar
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True, padx=20)

        def render_games():
            for widget in container.winfo_children():
                widget.destroy()
            
            if not self.data["games"]:
                tk.Label(container, text="Nenhum jogo disponível no momento.").pack()
                return

            for game in self.data["games"]:
                if game["status"] == "Aberto":
                    frame_game = tk.LabelFrame(container, text=f"{game['team_a']} vs {game['team_b']}", padx=10, pady=10)
                    frame_game.pack(fill="x", pady=5)

                    tk.Label(frame_game, text=f"Vitória {game['team_a']} (Odd: {game['odd_a']})").pack(side="left", padx=10)
                    btn_a = tk.Button(frame_game, text="Apostar", command=lambda g=game, sel=game['team_a']: self.place_bet(g, sel))
                    btn_a.pack(side="left", padx=5)

                    tk.Label(frame_game, text="Empate (Odd: {})".format(game['odd_draw'])).pack(side="left", padx=10)
                    btn_draw = tk.Button(frame_game, text="Apostar", command=lambda g=game, sel="Empate": self.place_bet(g, sel))
                    btn_draw.pack(side="left", padx=5)

                    tk.Label(frame_game, text=f"Vitória {game['team_b']} (Odd: {game['odd_b']})").pack(side="left", padx=10)
                    btn_b = tk.Button(frame_game, text="Apostar", command=lambda g=game, sel=game['team_b']: self.place_bet(g, sel))
                    btn_b.pack(side="left", padx=5)

        render_games()
        
        tk.Button(self.root, text="Atualizar Jogos", command=render_games).pack(pady=10)
        
        # Histórico do usuário
        tk.Label(self.root, text="Minhas Apostas Recentes", font=("Arial", 12, "bold")).pack(pady=10)
        cols = ("Jogo", "Seleção", "Valor", "Retorno")
        tree = ttk.Treeview(self.root, columns=cols, show="headings", height=5)
        for c in cols: tree.heading(c, text=c)
        tree.pack(fill="x", padx=20)
        
        my_bets = [b for b in self.data["bets"] if b["user"] == self.current_user]
        for b in reversed(my_bets[-5:]): # Últimas 5
            tree.insert("", "end", values=(f"{b['team_a']}x{b['team_b']}", b["selection"], f"R$ {b['amount']}", f"R$ {b['potential_return']}"))

    def place_bet(self, game, selection):
        amount_str = simpledialog.askstring("Confirmar Aposta", f"Apostar em {selection}?\nOdd: {game.get('odd_a') if selection == game['team_a'] else (game.get('odd_b') if selection == game['team_b'] else game.get('odd_draw'))}\nDigite o valor da aposta (R$):")
        
        if amount_str:
            try:
                amount = float(amount_str)
                if amount <= 0:
                    raise ValueError
                odd = 0
                if selection == game["team_a"]: odd = game["odd_a"]
                elif selection == game["team_b"]: odd = game["odd_b"]
                else: odd = game["odd_draw"]
                
                potential = amount * odd
                
                new_bet = {
                    "id": len(self.data["bets"]) + 1,
                    "user": self.current_user,
                    "game_id": game["id"],
                    "team_a": game["team_a"],
                    "team_b": game["team_b"],
                    "selection": selection,
                    "amount": amount,
                    "potential_return": potential,
                    "date": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                self.data["bets"].append(new_bet)
                self.save_data()
                messagebox.showinfo("Sucesso", f"Aposta realizada!\nPotencial retorno: R$ {potential:.2f}")
                self.show_user_dashboard() # Refresh
            except ValueError:
                messagebox.showerror("Erro", "Valor inválido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BettingSystem(root)
    root.mainloop()
