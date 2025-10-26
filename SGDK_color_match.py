import tkinter as tk
from tkinter import messagebox

# ========== PALETA DE REFERÊNCIA (512 cores 3-3-3 bits) ==========
palette_hex = [
    "000000", "002400", "004800", "006c00", "009000", "00b400", "00d800", "00ff00",
    "240000", "242400", "244800", "246c00", "249000", "24b400", "24d800", "24ff00",
    "480000", "482400", "484800", "486c00", "489000", "48b400", "48d800", "48ff00",
    "6c0000", "6c2400", "6c4800", "6c6c00", "6c9000", "6cb400", "6cd800", "6cff00",
    "900000", "902400", "904800", "906c00", "909000", "90b400", "90d800", "90ff00",
    "b40000", "b42400", "b44800", "b46c00", "b49000", "b4b400", "b4d800", "b4ff00",
    "d80000", "d82400", "d84800", "d86c00", "d89000", "d8b400", "d8d800", "d8ff00",
    "ff0000", "ff2400", "ff4800", "ff6c00", "ff9000", "ffb400", "ffd800", "ffff00",
    "000024", "002424", "004824", "006c24", "009024", "00b424", "00d824", "00ff24",
    "240024", "242424", "244824", "246c24", "249024", "24b424", "24d824", "24ff24",
    "480024", "482424", "484824", "486c24", "489024", "48b424", "48d824", "48ff24",
    "6c0024", "6c2424", "6c4824", "6c6c24", "6c9024", "6cb424", "6cd824", "6cff24",
    "900024", "902424", "904824", "906c24", "909024", "90b424", "90d824", "90ff24",
    "b40024", "b42424", "b44824", "b46c24", "b49024", "b4b424", "b4d824", "b4ff24",
    "d80024", "d82424", "d84824", "d86c24", "d89024", "d8b424", "d8d824", "d8ff24",
    "ff0024", "ff2424", "ff4824", "ff6c24", "ff9024", "ffb424", "ffd824", "ffff24",
    "000048", "002448", "004848", "006c48", "009048", "00b448", "00d848", "00ff48",
    "240048", "242448", "244848", "246c48", "249048", "24b448", "24d848", "24ff48",
    "480048", "482448", "484848", "486c48", "489048", "48b448", "48d848", "48ff48",
    "6c0048", "6c2448", "6c4848", "6c6c48", "6c9048", "6cb448", "6cd848", "6cff48",
    "900048", "902448", "904848", "906c48", "909048", "90b448", "90d848", "90ff48",
    "b40048", "b42448", "b44848", "b46c48", "b49048", "b4b448", "b4d848", "b4ff48",
    "d80048", "d82448", "d84848", "d86c48", "d89048", "d8b448", "d8d848", "d8ff48",
    "ff0048", "ff2448", "ff4848", "ff6c48", "ff9048", "ffb448", "ffd848", "ffff48",
    "00006c", "00246c", "00486c", "006c6c", "00906c", "00b46c", "00d86c", "00ff6c",
    "24006c", "24246c", "24486c", "246c6c", "24906c", "24b46c", "24d86c", "24ff6c",
    "48006c", "48246c", "48486c", "486c6c", "48906c", "48b46c", "48d86c", "48ff6c",
    "6c006c", "6c246c", "6c486c", "6c6c6c", "6c906c", "6cb46c", "6cd86c", "6cff6c",
    "90006c", "90246c", "90486c", "906c6c", "90906c", "90b46c", "90d86c", "90ff6c",
    "b4006c", "b4246c", "b4486c", "b46c6c", "b4906c", "b4b46c", "b4d86c", "b4ff6c",
    "d8006c", "d8246c", "d8486c", "d86c6c", "d8906c", "d8b46c", "d8d86c", "d8ff6c",
    "ff006c", "ff246c", "ff486c", "ff6c6c", "ff906c", "ffb46c", "ffd86c", "ffff6c",
    "000090", "002490", "004890", "006c90", "009090", "00b490", "00d890", "00ff90",
    "240090", "242490", "244890", "246c90", "249090", "24b490", "24d890", "24ff90",
    "480090", "482490", "484890", "486c90", "489090", "48b490", "48d890", "48ff90",
    "6c0090", "6c2490", "6c4890", "6c6c90", "6c9090", "6cb490", "6cd890", "6cff90",
    "900090", "902490", "904890", "906c90", "909090", "90b490", "90d890", "90ff90",
    "b40090", "b42490", "b44890", "b46c90", "b49090", "b4b490", "b4d890", "b4ff90",
    "d80090", "d82490", "d84890", "d86c90", "d89090", "d8b490", "d8d890", "d8ff90",
    "ff0090", "ff2490", "ff4890", "ff6c90", "ff9090", "ffb490", "ffd890", "ffff90",
    "0000b4", "0024b4", "0048b4", "006cb4", "0090b4", "00b4b4", "00d8b4", "00ffb4",
    "2400b4", "2424b4", "2448b4", "246cb4", "2490b4", "24b4b4", "24d8b4", "24ffb4",
    "4800b4", "4824b4", "4848b4", "486cb4", "4890b4", "48b4b4", "48d8b4", "48ffb4",
    "6c00b4", "6c24b4", "6c48b4", "6c6cb4", "6c90b4", "6cb4b4", "6cd8b4", "6cffb4",
    "9000b4", "9024b4", "9048b4", "906cb4", "9090b4", "90b4b4", "90d8b4", "90ffb4",
    "b400b4", "b424b4", "b448b4", "b46cb4", "b490b4", "b4b4b4", "b4d8b4", "b4ffb4",
    "d800b4", "d824b4", "d848b4", "d86cb4", "d890b4", "d8b4b4", "d8d8b4", "d8ffb4",
    "ff00b4", "ff24b4", "ff48b4", "ff6cb4", "ff90b4", "ffb4b4", "ffd8b4", "ffffb4",
    "0000d8", "0024d8", "0048d8", "006cd8", "0090d8", "00b4d8", "00d8d8", "00ffd8",
    "2400d8", "2424d8", "2448d8", "246cd8", "2490d8", "24b4d8", "24d8d8", "24ffd8",
    "4800d8", "4824d8", "4848d8", "486cd8", "4890d8", "48b4d8", "48d8d8", "48ffd8",
    "6c00d8", "6c24d8", "6c48d8", "6c6cd8", "6c90d8", "6cb4d8", "6cd8d8", "6cffd8",
    "9000d8", "9024d8", "9048d8", "906cd8", "9090d8", "90b4d8", "90d8d8", "90ffd8",
    "b400d8", "b424d8", "b448d8", "b46cd8", "b490d8", "b4b4d8", "b4d8d8", "b4ffd8",
    "d800d8", "d824d8", "d848d8", "d86cd8", "d890d8", "d8b4d8", "d8d8d8", "d8ffd8",
    "ff00d8", "ff24d8", "ff48d8", "ff6cd8", "ff90d8", "ffb4d8", "ffd8d8", "ffffd8",
    "0000ff", "0024ff", "0048ff", "006cff", "0090ff", "00b4ff", "00d8ff", "00ffff",
    "2400ff", "2424ff", "2448ff", "246cff", "2490ff", "24b4ff", "24d8ff", "24ffff",
    "4800ff", "4824ff", "4848ff", "486cff", "4890ff", "48b4ff", "48d8ff", "48ffff",
    "6c00ff", "6c24ff", "6c48ff", "6c6cff", "6c90ff", "6cb4ff", "6cd8ff", "6cffff",
    "9000ff", "9024ff", "9048ff", "906cff", "9090ff", "90b4ff", "90d8ff", "90ffff",
    "b400ff", "b424ff", "b448ff", "b46cff", "b490ff", "b4b4ff", "b4d8ff", "b4ffff",
    "d800ff", "d824ff", "d848ff", "d86cff", "d890ff", "d8b4ff", "d8d8ff", "d8ffff",
    "ff00ff", "ff24ff", "ff48ff", "ff6cff", "ff90ff", "ffb4ff", "ffd8ff", "ffffff"
]

def hex_to_rgb(hex_str):
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "{:02x}{:02x}{:02x}".format(*rgb)

def closest_colors(rgb_input, palette, num=5):
    r1, g1, b1 = rgb_input
    distances = []
    for hex_color in palette:
        r2, g2, b2 = hex_to_rgb(hex_color)
        dist = (r1 - r2)**2 + (g1 - g2)**2 + (b1 - b2)**2
        distances.append((dist, (r2, g2, b2)))
    distances.sort(key=lambda x: x[0])
    return [c for d, c in distances[:num]]

class ColorMatcherApp:
    def __init__(self, root):
        self.root = root
        root.title("Cores Equivalentes SGDK")
        root.geometry("350x210")       # <-- define tamanho da janela
        root.resizable(False, False)    # impede redimensionamento

        tk.Label(root, text="Digite a cor em HEX sem # (ex: FF8800):").pack(pady=5)
        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        tk.Button(root, text="Encontrar Cores", command=self.match_color).pack(pady=5)

        self.result_frame = tk.Frame(root)
        self.result_frame.pack(pady=10)

        # === ADIÇÃO: cria 5 blocos desativados visíveis ===
        self.bg_color = root.cget("bg")
        self.color_frames = []
        self.color_entries = []

        for i in range(5):
            frame = tk.Frame(self.result_frame, width=60, height=40,
                             bg=self.bg_color, relief="sunken", bd=2)
            frame.grid(row=0, column=i, padx=5)
            entry = tk.Entry(self.result_frame, width=8, font=("Arial", 10),
                             state="disabled", disabledbackground=self.bg_color)
            entry.grid(row=1, column=i, pady=2)
            self.color_frames.append(frame)
            self.color_entries.append(entry)
        # ================================================

    def match_color(self):
        hex_input = self.entry.get().strip()
        if len(hex_input) != 6:
            messagebox.showerror("Erro", "Digite um valor HEX válido (6 caracteres).")
            return
        try:
            rgb_input = hex_to_rgb(hex_input)
        except:
            messagebox.showerror("Erro", "Valor HEX inválido.")
            return

        closest = closest_colors(rgb_input, palette_hex, num=5)

        # === substitui apenas o conteúdo dos blocos ===
        for i, color in enumerate(closest):
            hex_color = rgb_to_hex(color).upper()
            frame = self.color_frames[i]
            entry = self.color_entries[i]
            frame.config(bg="#" + hex_color)
            entry.config(state="normal")
            entry.delete(0, tk.END)
            entry.insert(0, hex_color)
            entry.bind("<Button-1>", lambda e, en=entry: en.select_range(0, tk.END))
            frame.bind("<Button-1>", lambda e, en=entry: en.select_range(0, tk.END))
        # ===============================================

root = tk.Tk()
app = ColorMatcherApp(root)
root.mainloop()