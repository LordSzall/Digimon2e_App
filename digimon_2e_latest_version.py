import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import math
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class DigimonDNDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digimon Digital Adventures Digimon Sheet")
        self.root.geometry("1080x2400")
        
        # Initialize variables
        self.current_theme = "Agumon"
        self.open_sheets = []
        self.notebook = None
        self.current_file = None
        self.tab_counter = 0
        
        # Theme colors
        self.themes = {
            "Agumon": {
                "bg": "#333333",  # Dark gray
                "fg": "#f1ba63",  # Agumon orange/gold
                "accent": "#f1ba63",
                "text": "white",
                "highlight": "#f1ba63",
                "secondary_bg": "#444444"
            },
            "Gabumon": {
                "bg": "#443c70",  # Navy blue
                "fg": "#d0d0d0",  # Light gray
                "accent": "#443c70",
                "text": "white",
                "highlight": "#5b5294",
                "secondary_bg": "#383361"
            },
            "Guilmon": {
                "bg": "#4d1f1f",  # Dark red
                "fg": "#d0d0d0",  # Light gray
                "accent": "#4d1f1f",
                "text": "white",
                "highlight": "#5b3a3a",
                "secondary_bg": "#3b2a2a"
            },
            "Terriermon": {
                "bg": "#3d5b1f",  # Forest green
                "fg": "#d0d0d0",  # Light gray
                "accent": "#3d5b1f",
                "text": "white",
                "highlight": "#5b5b3a",
                "secondary_bg": "#3b3b2a"
            },
            "Tsukaimon": {
                "bg": "#5e219c",  # Dark Purple
                "fg": "#cccccc",  # Lighter Gray
                "accent": "#5e219c",
                "text": "black",
                "highlight": "#5b5b3a",
                "secondary_bg": "#cccccc"
            },
            "Sunarizamon": {
                "bg": "#d3db3d",  # Olive green
                "fg": "#cccccc",  # Lighter gray
                "accent": "#3d5b1f",
                "text": "black",
                "highlight": "#5b5b3a",
                "secondary_bg": "#cccccc"
            }
        }
        
        # Create UI
        self.setup_ui()
        
    def setup_ui(self):
        # Configure style based on current theme
        self.configure_style()
        
        # Create main menu
        self.create_menu()
        
        # Create notebook for character sheets
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Welcome tab
        welcome_frame = ttk.Frame(self.notebook)
        self.notebook.add(welcome_frame, text="Welcome")
        
        # Welcome content
        welcome_label = ttk.Label(
            welcome_frame, 
            text="Welcome to Digimon Digital Adventures Digimon Sheet", 
            font=("Arial", 18, "bold")
        )
        welcome_label.pack(pady=50)
        
        info_text = (
            "Create a new character sheet from the File menu or open an existing one.\n\n"
            "Current Theme: " + self.current_theme
        )
        info_label = ttk.Label(welcome_frame, text=info_text, font=("Arial", 12))
        info_label.pack(pady=20)
        
        # Add theme image
        img_frame = ttk.Frame(welcome_frame)
        img_frame.pack(pady=30)
        
        if self.current_theme == "Agumon":
            agumon_img = tk.PhotoImage(file=resource_path("agumon.png"))
            agumon_label = ttk.Label(img_frame, image=agumon_img)
            agumon_label.image = agumon_img
            agumon_label.grid(row=0, column=0, padx=10)
        elif self.current_theme == "Gabumon":
            gabumon_img = tk.PhotoImage(file=resource_path("gabumon.png"))
            gabumon_label = ttk.Label(img_frame, image=gabumon_img)
            gabumon_label.image = gabumon_img
            gabumon_label.grid(row=0, column=0, padx=10)
        elif self.current_theme == "Guilmon":
            guilmon_img = tk.PhotoImage(file=resource_path("guilmon.png"))
            guilmon_label = ttk.Label(img_frame, image=guilmon_img)
            guilmon_label.image = guilmon_img
            guilmon_label.grid(row=0, column=0, padx=10)
        elif self.current_theme == "Terriermon":
            terriermon_img = tk.PhotoImage(file=resource_path("terriermon.png"))
            terriermon_label = ttk.Label(img_frame, image=terriermon_img)
            terriermon_label.image = terriermon_img
            terriermon_label.grid(row=0, column=0, padx=10)
        elif self.current_theme == "Tsukaimon":
            tsukaimon_img = tk.PhotoImage(file=resource_path("tsukaimon.png"))
            tsukaimon_label = ttk.Label(img_frame, image=tsukaimon_img)
            tsukaimon_label.image = tsukaimon_img
            tsukaimon_label.grid(row=0, column=0, padx=10)
        elif self.current_theme == "Sunarizamon":
            sunarizamon_img = tk.PhotoImage(file=resource_path("sunarizamon.png"))
            sunarizamon_label = ttk.Label(img_frame, image=sunarizamon_img)
            sunarizamon_label.image = sunarizamon_img
            sunarizamon_label.grid(row=0, column=0, padx=10)
        
        # Buttons
        button_frame = ttk.Frame(welcome_frame)
        button_frame.pack(pady=30)
        
        new_button = ttk.Button(button_frame, text="New Character Sheet", command=self.new_sheet)
        new_button.grid(row=0, column=0, padx=10)
        
        open_button = ttk.Button(button_frame, text="Open Character Sheet", command=self.open_sheet)
        open_button.grid(row=0, column=1, padx=10)

    def configure_style(self):
        style = ttk.Style()
        style.theme_use('default')
        theme = self.themes[self.current_theme]
        
        # Configure TFrame
        style.configure("TFrame", background=theme["bg"])
        
        # Configure TLabel
        style.configure("TLabel", background=theme["bg"], foreground=theme["text"])
        
        # Configure TButton
        style.configure("TButton", 
                        background=theme["accent"],
                        foreground=theme["text"],
                        borderwidth=1)
        style.map("TButton",
                 background=[('active', theme["highlight"])],
                 foreground=[('active', theme["text"])])
        
        # Configure TEntry
        style.configure("TEntry", 
                        fieldbackground=theme["secondary_bg"],
                        foreground=theme["text"])
        
        # Configure TCombobox
        style.configure("TCombobox",
                       fieldbackground=theme["secondary_bg"],
                       background=theme["accent"],
                       foreground=theme["text"])
        
        # Configure TNotebook
        style.configure("TNotebook", background=theme["bg"])
        style.configure("TNotebook.Tab", 
                       background=theme["secondary_bg"],
                       foreground=theme["text"],
                       padding=[10, 2])
        style.map("TNotebook.Tab",
                 background=[('selected', theme["accent"])],
                 foreground=[('selected', theme["text"])])
        
        # Configure the root window
        self.root.configure(bg=theme["bg"])

    def create_menu(self):
        menubar = tk.Menu(self.root)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New Character Sheet", command=self.new_sheet)
        file_menu.add_command(label="Open Character Sheet", command=self.open_sheet)
        file_menu.add_command(label="Save", command=self.save_sheet)
        file_menu.add_command(label="Save As", command=self.save_as)
        file_menu.add_command(label="Close Character Sheet", command=self.close_sheet)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        # Theme menu
        theme_menu = tk.Menu(menubar, tearoff=0)
        theme_menu.add_command(label="Agumon Theme", command=lambda: self.change_theme("Agumon"))
        theme_menu.add_command(label="Gabumon Theme", command=lambda: self.change_theme("Gabumon"))
        theme_menu.add_command(label="Guilmon Theme", command=lambda: self.change_theme("Guilmon")) 
        theme_menu.add_command(label="Terriermon Theme", command=lambda: self.change_theme("Terriermon"))
        theme_menu.add_command(label="Tsukaimon Theme", command=lambda: self.change_theme("Tsukaimon"))
        theme_menu.add_command(label="Sunarizamon Theme", command=lambda: self.change_theme("Sunarizamon"))
        menubar.add_cascade(label="Themes", menu=theme_menu)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)
        
        self.root.config(menu=menubar)
    
    def change_theme(self, theme_name):
        self.current_theme = theme_name
        self.configure_style()
        messagebox.showinfo("Theme Changed", f"Theme changed to {theme_name}")
        
        # Rebuild current tabs with new theme
        active_tab = self.notebook.select()
        if active_tab:
            index = self.notebook.index(active_tab)
            
            # Check if the active tab is the welcome tab
            if index == 0:
                # Recreate the welcome tab
                self.notebook.forget(active_tab)
                welcome_frame = ttk.Frame(self.notebook)
                
                # Recreate the welcome content
                self.notebook.add(welcome_frame, text="Welcome")
                welcome_label = ttk.Label(
                    welcome_frame, 
                    text="Welcome to Digimon Digital Adventures Digimon Sheet", 
                    font=("Arial", 18, "bold")
                )
                welcome_label.pack(pady=50)
                info_text = (
                    "Create a new character sheet from the File menu or open an existing one.\n\n"
                    "Current Theme: " + self.current_theme
                )
                info_label = ttk.Label(welcome_frame, text=info_text, font=("Arial", 12))
                info_label.pack(pady=20)
                
                # Recreate the image
                img_frame = ttk.Frame(welcome_frame)
                img_frame.pack(pady=30)
                
                if self.current_theme == "Agumon":
                    agumon_img = tk.PhotoImage(file=resource_path("agumon.png"))
                    agumon_label = ttk.Label(img_frame, image=agumon_img)
                    agumon_label.image = agumon_img
                    agumon_label.grid(row=0, column=0, padx=10)
                elif self.current_theme == "Gabumon":
                    gabumon_img = tk.PhotoImage(file=resource_path("gabumon.png"))
                    gabumon_label = ttk.Label(img_frame, image=gabumon_img)
                    gabumon_label.image = gabumon_img
                    gabumon_label.grid(row=0, column=0, padx=10)
                elif self.current_theme == "Guilmon":
                    guilmon_img = tk.PhotoImage(file=resource_path("guilmon.png"))
                    guilmon_label = ttk.Label(img_frame, image=guilmon_img)
                    guilmon_label.image = guilmon_img
                    guilmon_label.grid(row=0, column=0, padx=10)
                elif self.current_theme == "Terriermon":
                    terriermon_img = tk.PhotoImage(file=resource_path("terriermon.png"))
                    terriermon_label = ttk.Label(img_frame, image=terriermon_img)
                    terriermon_label.image = terriermon_img
                    terriermon_label.grid(row=0, column=0, padx=10)
                elif self.current_theme == "Tsukaimon":
                    tsukaimon_img = tk.PhotoImage(file=resource_path("tsukaimon.png"))
                    tsukaimon_label = ttk.Label(img_frame, image=tsukaimon_img)
                    tsukaimon_label.image = tsukaimon_img
                    tsukaimon_label.grid(row=0, column=0, padx=10)
                elif self.current_theme == "Sunarizamon":
                    sunarizamon_img = tk.PhotoImage(file=resource_path("sunarizamon.png"))
                    sunarizamon_label = ttk.Label(img_frame, image=sunarizamon_img)
                    sunarizamon_label.image = sunarizamon_img
                    sunarizamon_label.grid(row=0, column=0, padx=10)
                
                # Recreate buttons
                button_frame = ttk.Frame(welcome_frame)
                button_frame.pack(pady=30)
                new_button = ttk.Button(button_frame, text="New Character Sheet", command=self.new_sheet)
                new_button.grid(row=0, column=0, padx=10)
                open_button = ttk.Button(button_frame, text="Open Character Sheet", command=self.open_sheet)
                open_button.grid(row=0, column=1, padx=10)
            
            # If the active tab is not the welcome tab, recreate it
            else:
                # Find the Welcome tab
                welcome_tab = self.notebook.nametowidget(self.notebook.tabs()[0])

                # Recreate the welcome tab
                self.notebook.forget(welcome_tab)
                welcome_frame = ttk.Frame(self.notebook)
                
                # Recreate the welcome content
                self.notebook.add(welcome_frame, text="Welcome")
                welcome_label = ttk.Label(
                    welcome_frame, 
                    text="Welcome to Digimon Digital Adventures Digimon Sheet", 
                    font=("Arial", 18, "bold")
                )
                welcome_label.pack(pady=50)
                info_text = (
                    "Create a new character sheet from the File menu or open an existing one.\n\n"
                    "Current Theme: " + self.current_theme
                )
                info_label = ttk.Label(welcome_frame, text=info_text, font=("Arial", 12))
                info_label.pack(pady=20)
                
                # Recreate the image
                img_frame = ttk.Frame(welcome_frame)
                img_frame.pack(pady=30)
                if self.current_theme == "Agumon":
                    agumon_img = tk.PhotoImage(file="agumon.png")
                    agumon_label = ttk.Label(img_frame, image=agumon_img)
                    agumon_label.image = agumon_img
                    agumon_label.grid(row=0, column=0, padx=10)
                elif self.current_theme == "Gabumon":
                    gabumon_img = tk.PhotoImage(file="gabumon.png")
                    gabumon_label = ttk.Label(img_frame, image=gabumon_img)
                    gabumon_label.image = gabumon_img
                    gabumon_label.grid(row=0, column=0, padx=10)
                elif self.current_theme == "Guilmon":
                    guilmon_img = tk.PhotoImage(file="guilmon.png")
                    guilmon_label = ttk.Label(img_frame, image=guilmon_img)
                    guilmon_label.image = guilmon_img
                    guilmon_label.grid(row=0, column=0, padx=10)
                elif self.current_theme == "Terriermon":
                    terriermon_img = tk.PhotoImage(file="terriermon.png")
                    terriermon_label = ttk.Label(img_frame, image=terriermon_img)
                    terriermon_label.image = terriermon_img
                    terriermon_label.grid(row=0, column=0, padx=10) 
                elif self.current_theme == "Tsukaimon":
                    tsukaimon_img = tk.PhotoImage(file="tsukaimon.png")
                    tsukaimon_label = ttk.Label(img_frame, image=tsukaimon_img)
                    tsukaimon_label.image = tsukaimon_img
                    tsukaimon_label.grid(row=0, column=0, padx=10)
                
                # Recreate buttons
                button_frame = ttk.Frame(welcome_frame)
                button_frame.pack(pady=30)
                new_button = ttk.Button(button_frame, text="New Character Sheet", command=self.new_sheet)
                new_button.grid(row=0, column=0, padx=10)
                open_button = ttk.Button(button_frame, text="Open Character Sheet", command=self.open_sheet)

            # Recreate all character sheets with new theme
            for sheet in self.open_sheets:
                sheet["frame"].destroy()
                new_frame = ttk.Frame(self.notebook)
                self.notebook.add(new_frame, text=sheet["name"])
                sheet["frame"] = new_frame
                self.create_character_form(new_frame, sheet["data"])
            
            # Select the same tab that was active
            if index < len(self.open_sheets):
                self.notebook.select(index)
    
    def new_sheet(self):
        self.tab_counter += 1
        tab_name = f"New Sheet {self.tab_counter}"
        
        # Create new frame
        sheet_frame = ttk.Frame(self.notebook)
        self.notebook.add(sheet_frame, text=tab_name)
        self.notebook.select(sheet_frame)
        
        # Create empty character data
        character_data = {
            "name": "",
            "digimon": "",
            "stage": "Child",
            "size": "Medium",
            "attribute": "Vaccine",
            "type": "",
            "wound_boxes": 0,
            "temp_boxes": 0,
            "battery": 0,
            "effects": [
                {
                    "eff_name": "",
                    "potency": 0,
                    "duration": 0,
                }
            ],
            "stats": {
                "acc_dp": 0,
                "acc_bonus": 0,
                "dam_dp": 0,
                "dam_bonus": 0,
                "dod_dp": 0,
                "dod_bonus": 0,
                "arm_dp": 0,
                "arm_bonus": 0,
                "hp_dp": 0,
                "hp_bonus": 0
            },
            "derived_stats": {
                "bit_bonus": 0,
                "dos_bonus": 0,
                "ram_bonus": 0,
                "cpu_bonus": 0
            },
            "misc_stats": {
                "move_bonus": 0,
                "init_bonus": 0,
                "range_bonus": 0,
                "max_range_bonus": 0
            },
            "attacks": [
                {
                    "name": "Signature Move",
                    "accuracy": 0,
                    "type": "Melee",
                    "damage": 0,
                    "tags": ["", "", ""]
                }
            ],
            "bonus_dp_var": 0,
            "dp_allocated_var": 10,
        }
        
        # Store sheet data
        sheet_info = {
            "name": tab_name,
            "frame": sheet_frame,
            "data": character_data,
            "file_path": None
        }
        self.open_sheets.append(sheet_info)
        
        # Create form
        self.create_character_form(sheet_frame, character_data)
    
    def open_sheet(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    character_data = json.load(file)
                
                # Create new tab for opened file
                file_name = os.path.basename(file_path)
                sheet_frame = ttk.Frame(self.notebook)
                self.notebook.add(sheet_frame, text=file_name)
                self.notebook.select(sheet_frame)
                
                # Store sheet data
                sheet_info = {
                    "name": file_name,
                    "frame": sheet_frame,
                    "data": character_data,
                    "file_path": file_path
                }
                self.open_sheets.append(sheet_info)
                
                # Create form
                self.create_character_form(sheet_frame, character_data)
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {str(e)}")
    
    def save_sheet(self):
        current_tab = self.notebook.select()
        if not current_tab:
            messagebox.showinfo("Info", "No character sheet is open")
            return
        
        # Find the sheet info based on the current tab
        sheet_info = None
        for sheet in self.open_sheets:
            if sheet["frame"] == self.notebook.nametowidget(current_tab):
                sheet_info = sheet
                break
        
        if not sheet_info:
            messagebox.showinfo("Info", "No character sheet is open")
            return
        
        if sheet_info["file_path"]:            
            # Save to existing file
            self.save_data_to_file(sheet_info["file_path"], sheet_info)
        else:
            # Prompt for save as
            self.save_as()
    
    def save_as(self):
        current_tab = self.notebook.select()
        if not current_tab:
            messagebox.showinfo("Info", "No character sheet is open")
            return
        
        # Find the sheet info based on the current tab
        sheet_info = None
        for sheet in self.open_sheets:
            if sheet["frame"] == self.notebook.nametowidget(current_tab):
                sheet_info = sheet
                break
        
        if not sheet_info:
            messagebox.showinfo("Info", "No character sheet is open")
            return
        
        # Prompt for file path
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json"), ("All Files", "*.*")]
        )

        if file_path:
            # Save to file
            self.save_data_to_file(file_path, sheet_info)
            
            # Update the file path in the sheet info
            sheet_info["file_path"] = file_path
            
            # Update the tab name to the file name
            file_name = os.path.basename(file_path)
            self.notebook.tab(sheet_info["frame"], text=file_name)
            sheet_info["name"] = file_name

    def save_data_to_file(self, file_path, sheet_info):
        try:
            # Get a clean copy of the character data
            clean_data = self.get_updated_character_data(sheet_info)

            # Save the clean copy to the file
            with open(file_path, 'w') as file:
                json.dump(clean_data, file, indent=4)
            
            messagebox.showinfo("Success", "Character sheet saved successfully!")    
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file: {str(e)}")
    
    def get_updated_character_data(self, sheet_info):
        # Creates a clean copy of the character data based on current form data
        # Returns a new dictionary with the updated data

        # Make a deep copy of the original data
        updated_data = {}
        form_refs = sheet_info["data"].get("_form_refs", {})

        # Basic info
        updated_data["name"] = form_refs["name_entry"].get() if "name_entry" in form_refs else ""
        updated_data["digimon"] = form_refs["digimon_entry"].get() if "digimon_entry" in form_refs else ""
        updated_data["stage"] = form_refs["stage_combo"].get() if "stage_combo" in form_refs else "Child"
        updated_data["size"] = form_refs["size_combo"].get() if "size_combo" in form_refs else "Medium"
        updated_data["attribute"] = form_refs["attr_combo"].get() if "attr_combo" in form_refs else "Vaccine"
        updated_data["type"] = form_refs["type_entry"].get() if "type_entry" in form_refs else ""

        # Wound and Temp boxes
        updated_data["wound_boxes"] = int(form_refs["wound_var"].get()) if "wound_var" in form_refs else 0
        updated_data["temp_boxes"] = int(form_refs["temp_var"].get()) if "temp_var" in form_refs else 0
        updated_data["battery"] = int(form_refs["batt_var"].get()) if "batt_var" in form_refs else 0

        # Base Stats
        updated_data["stats"] = {}
        for stat in ["acc", "dam", "dod", "arm", "hp"]:
            dp_var = form_refs["dp_vars"].get(f"{stat}_dp")
            bonus_var = form_refs["bonus_vars"].get(f"{stat}_bonus")

            updated_data["stats"][f"{stat}_dp"] = int(dp_var.get() or 0) if dp_var else 0
            updated_data["stats"][f"{stat}_bonus"] = int(bonus_var.get() or 0) if bonus_var else 0
        
        # Derived Stats
        updated_data["derived_stats"] = {}
        for stat in ["bit", "dos", "ram", "cpu"]:
            bonus_var = form_refs["derived_bonus_vars"].get(f"{stat}_bonus")
            updated_data["derived_stats"][f"{stat}_bonus"] = int(bonus_var.get() or 0) if bonus_var else 0
        
        # Misc Stats
        updated_data["misc_stats"] = {}
        for stat in ["move", "init", "range", "max_range"]:
            bonus_var = form_refs["misc_bonus_vars"].get(f"{stat}_bonus")
            updated_data["misc_stats"][f"{stat}_bonus"] = int(bonus_var.get() or 0) if bonus_var else 0
        
        # Qualities
        updated_data["qualities"] = form_refs["qualities_text"].get("1.0", tk.END).strip() if "qualities_text" in form_refs else ""

        # Attacks (collect from form refs) in each attack data)
        updated_data["attacks"] = []
        for attack in sheet_info["data"].get("attacks", []):
            attack_refs = attack.get("_form_refs", {})
            if attack_refs:
                updated_attack = {
                    "name": attack_refs["name"].get(),
                    "accuracy": int(attack_refs["accuracy"].get() or 0),
                    "type": attack_refs["type"].get(),
                    "damage": int(attack_refs["damage"].get() or 0),
                    "tags": [tag.get() for tag in attack_refs["tags"]]
                }
                updated_data["attacks"].append(updated_attack)
        
        # Effects (collect from form refs) in each effect data)
        updated_data["effects"] = []
        for effect in sheet_info["data"].get("effects", []):
            effect_refs = effect.get("_form_refs", {})
            if effect_refs:
                updated_effect = {
                    "eff_name": effect_refs["eff_name"].get(),
                    "potency": int(effect_refs["potency"].get() or 0),
                    "duration": int(effect_refs["duration"].get() or 0),
                }
                updated_data["effects"].append(updated_effect)

        # Get all Allocated DP info
        updated_data["bonus_dp_var"] = int(form_refs["bonus_dp_var"].get()) if "bonus_dp_var" in form_refs else 0
        updated_data["quality_spent_var"] = int(form_refs["quality_spent_var"].get()) if "quality_spent_var" in form_refs else 0
        updated_data["stat_spent_var"] = int(form_refs["stat_spent_var"].get()) if "stat_spent_var" in form_refs else 0
        updated_data["dp_spent_var"] = int(form_refs["dp_spent_var"].get()) if "dp_spent_var" in form_refs else 0
        updated_data["dp_allocated_var"] = int(form_refs["dp_allocated_var"].get()) if "dp_allocated_var" in form_refs else 0
        
        return updated_data
    
    def update_character_data(self, sheet_info):
        # Update the character data based on the current form data
        updated_data = self.get_updated_character_data(sheet_info)
        # Preserve any metadata that might be in the original data
        for key, value in updated_data.items():
            if key not in sheet_info["data"]:
                sheet_info["data"][key] = value
            else:
                sheet_info["data"][key].update(value)
        
        # Keep the form references in the original data
        if "_form_refs" in sheet_info["data"]:
            updated_data["_form_refs"] = sheet_info["data"]["_form_refs"]

    #Helper function to safely convert string to int
    def safe_int(self, value):
        try:
            return int(value)
        except ValueError:
            return 0


    # Close the current character sheet
    def close_sheet(self):
        # Check if the current tab is not the welcome tab
        current_tab = self.notebook.select()
        if current_tab and current_tab != self.notebook.tabs()[0]:
            # Find the sheet info based on the current tab
            sheet_info = None
            for sheet in self.open_sheets:
                if sheet["frame"] == self.notebook.nametowidget(current_tab):
                    sheet_info = sheet
                    break
            
            if sheet_info:
                # Remove the tab and its data
                self.notebook.forget(sheet_info["frame"])
                self.open_sheets.remove(sheet_info)
                
                # Destroy the frame to free up resources
                sheet_info["frame"].destroy()
                
                messagebox.showinfo("Info", "Character sheet closed successfully!")
    
    def show_about(self):
        about_text = (
            "Digimon 2e Digimon Sheet\n\n"
            "A character sheet application for Digimon 2E Adventures.\n"
            "Credit goes to Dr. Digitama.\n\n"
            "Created with Python and Tkinter."
        )
        messagebox.showinfo("About", about_text)
    
    def create_character_form(self, parent_frame, character_data):
        theme = self.themes[self.current_theme]
        
        # Create main container with scrollbar
        canvas = tk.Canvas(parent_frame, bg=theme["bg"])
        scrollbar = ttk.Scrollbar(parent_frame, orient="vertical", command=canvas.yview)
        
        # Scrollable Frame
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        
        # Add mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        # Add Mobile support for scrolling
        def _on_touch_start(event):
            canvas.scan_mark(event.x, event.y)
        
        def _on_touch_move(event):
            canvas.scan_dragto(event.x, event.y, gain=1)
        
        #Bind all events to the canvas
        canvas.bind("<Button-1>", _on_touch_start)
        canvas.bind("<B1-Motion>", _on_touch_move)
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
        # Start creating the character sheet
        # Top Line
        top_frame = ttk.Frame(scrollable_frame)
        top_frame.pack(fill="x", padx=20, pady=10)
        
        # Character basic info (Name, Digimon, Stage, Size, Attribute, Type)
        ttk.Label(top_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        name_entry = ttk.Entry(top_frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)
        name_entry.insert(0, character_data.get("name", ""))
        
        ttk.Label(top_frame, text="Digimon:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        digimon_entry = ttk.Entry(top_frame)
        digimon_entry.grid(row=0, column=3, padx=5, pady=5)
        digimon_entry.insert(0, character_data.get("digimon", ""))
        
        ttk.Label(top_frame, text="Stage:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        stage_combo = ttk.Combobox(top_frame, values=["Baby", "Child", "Adult", "Perfect", "Ultimate"])
        stage_combo.grid(row=0, column=5, padx=5, pady=5)
        stage_combo.set(character_data.get("stage", "Child"))
        
        ttk.Label(top_frame, text="Size:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        size_combo = ttk.Combobox(top_frame, values=["Small", "Medium", "Large", "Huge", "Gigantic", "Colossal"])
        size_combo.grid(row=1, column=1, padx=5, pady=5)
        size_combo.set(character_data.get("size", "Medium"))
        
        ttk.Label(top_frame, text="Attribute:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        attr_combo = ttk.Combobox(top_frame, values=["Vaccine", "Data", "Virus"])
        attr_combo.grid(row=1, column=3, padx=5, pady=5)
        attr_combo.set(character_data.get("attribute", "Vaccine"))
        
        ttk.Label(top_frame, text="Type:").grid(row=1, column=4, padx=5, pady=5, sticky="e")
        type_entry = ttk.Entry(top_frame)
        type_entry.grid(row=1, column=5, padx=5, pady=5)
        type_entry.insert(0, character_data.get("type", ""))
        
        # DP Allocation - Creating Variables before any Calculations
        bonus_dp_var = tk.StringVar(value=str(character_data.get("bonus_dp_var", 0)))
        stat_spent_var = tk.StringVar(value="0")
        quality_spent_var = tk.StringVar(value=str(character_data.get("quality_spent_var", 0)))
        dp_spent_var = tk.StringVar(value="0")
        dp_allocated_var = tk.StringVar(value="0")
        
        # Store references immediately
        character_data.setdefault("_form_refs", {}).update({
            "bonus_dp_var": bonus_dp_var,
            "quality_spent_var": quality_spent_var,
            "stat_spent_var": stat_spent_var,
            "dp_spent_var": dp_spent_var,
            "dp_allocated_var": dp_allocated_var
        })
        
        # Combat tracker
        combat_frame = ttk.Frame(scrollable_frame)
        combat_frame.pack(fill="x", padx=20, pady=10)
        
        ttk.Label(combat_frame, text="Wound Boxes:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        
        wound_var = tk.StringVar()
        wound_entry = ttk.Entry(combat_frame, width=5, textvariable=wound_var)
        wound_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        wound_var.set(str(character_data.get("wound_boxes", 0)))
        
        ttk.Label(combat_frame, text="/").grid(row=0, column=2)
        
        max_health_var = tk.StringVar(value="0")  # Will be calculated
        ttk.Label(combat_frame, textvariable=max_health_var).grid(row=0, column=3, padx=5, pady=5, sticky="w")
        
        ttk.Label(combat_frame, text="Temp. Boxes:").grid(row=0, column=4, padx=20, pady=5, sticky="e")

        temp_var = tk.StringVar()
        temp_entry = ttk.Entry(combat_frame, width=5, textvariable=temp_var)
        temp_entry.grid(row=0, column=5, padx=5, pady=5, sticky="w")
        temp_var.set(str(character_data.get("temp_boxes", 0)))

        ttk.Label(combat_frame, text="Battery").grid(row=0, column=6, padx=20, pady=5, sticky="e")

        batt_var = tk.StringVar()
        batt_entry = ttk.Entry(combat_frame, width=5, textvariable=temp_var)
        batt_entry.grid(row=0, column=7, padx=5, pady=5, sticky="w")
        batt_var.set(str(character_data.get("battery", 0)))

        ttk.Label(combat_frame, text="/").grid(row=0, column=8)

        max_batt_var = tk.StringVar(value="0") # Will be calulated
        ttk.Label(combat_frame, textvariable=max_batt_var).grid(row=0, column=9, padx=5, pady=5, sticky="w")

        # Effects section
        effects_frame = ttk.Frame(scrollable_frame)
        effects_frame.pack(fill="x", padx=20, pady=10)
        
        ttk.Label(effects_frame, text="Effects & Conditions", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=7, padx=5, pady=5, sticky="w"
        )
        
        # Column headers
        ttk.Label(effects_frame, text="Effect").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(effects_frame, text="Potency").grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(effects_frame, text="Duration").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        
        # Container for dynamic effects
        effects_container = ttk.Frame(effects_frame)
        effects_container.grid(row=2, column=0, columnspan=9, padx=5, pady=5, sticky="w")
        
        # Add button for new effects
        add_effect_btn = ttk.Button(
            effects_frame, 
            text="Add Effect", 
            command=lambda: self.add_effect_row(effects_container, character_data)
        )
        add_effect_btn.grid(row=3, column=0, padx=5, pady=10, sticky="w")
        
        # Add existing effects
        for effect in character_data.get("effects", []):
            self.add_effect_row(effects_container, character_data, effect)

        # Stats (with both display and DP entry)
        stats_frame = ttk.Frame(scrollable_frame)
        stats_frame.pack(fill="x", padx=20, pady=10)
        
        # Create dictionaries to store variables
        stat_vars = {}
        dp_vars = {}
        bonus_vars = {}
        derived_vars = {}
        derived_bonus_vars = {}
        misc_vars = {}
        misc_bonus_vars = {}
        
        # Stats setup
        stat_names = ["ACC", "DAM", "DOD", "ARM", "HP"]
        for i, stat in enumerate(stat_names):
            # Create frame for each stat
            stat_frame = ttk.Frame(stats_frame)
            stat_frame.grid(row=0, column=i, padx=20, pady=5)
            
            # Stat value display
            stat_vars[stat.lower()] = tk.StringVar(value="0")
            ttk.Label(stat_frame, textvariable=stat_vars[stat.lower()], 
                     font=("Arial", 24, "bold")).pack(pady=5)
            
            # Stat name
            ttk.Label(stat_frame, text=stat).pack(pady=2)
            
            # DP input
            ttk.Label(stat_frame, text="DP:").pack(pady=2)
            dp_vars[f"{stat.lower()}_dp"] = tk.StringVar()
            dp_vars[f"{stat.lower()}_dp"].set(str(character_data["stats"].get(f"{stat.lower()}_dp", 0)))
            dp_entry = ttk.Entry(stat_frame, width=5, textvariable=dp_vars[f"{stat.lower()}_dp"])
            dp_entry.pack(pady=2)
            
            # Bonus input
            ttk.Label(stat_frame, text="Qualities:").pack(pady=2)
            bonus_vars[f"{stat.lower()}_bonus"] = tk.StringVar()
            bonus_vars[f"{stat.lower()}_bonus"].set(str(character_data["stats"].get(f"{stat.lower()}_bonus", 0)))
            bonus_entry = ttk.Entry(stat_frame, width=5, textvariable=bonus_vars[f"{stat.lower()}_bonus"])
            bonus_entry.pack(pady=2)

            # Bind calculation to DP and Bonus change
            dp_vars[f"{stat.lower()}_dp"].trace_add("write", 
                                                    lambda *args, s=stat.lower(): self.calculate_stats(
                                                        stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, 
                                                        derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, 
                                                        max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, 
                                                        stat_spent_var, dp_spent_var, dp_allocated_var
                                                    ))
            bonus_vars[f"{stat.lower()}_bonus"].trace_add("write", 
                                                    lambda *args, s=stat.lower(): self.calculate_stats(
                                                        stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, 
                                                        derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, 
                                                        max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, 
                                                        stat_spent_var, dp_spent_var, dp_allocated_var
                                                    ))
            
        # Derived Stats
        derived_frame = ttk.Frame(scrollable_frame)
        derived_frame.pack(fill="x", padx=28, pady=10)
        
        derived_names = ["BIT", "DOS", "RAM", "CPU"]
        for i, stat in enumerate(derived_names):
            # Create frame for each derived stat
            derived_stat_frame = ttk.Frame(derived_frame)
            derived_stat_frame.grid(row=0, column=i, padx=20, pady=5)
            
            # Derived stat value display
            derived_vars[stat.lower()] = tk.StringVar(value="0")
            ttk.Label(derived_stat_frame, textvariable=derived_vars[stat.lower()], 
                     font=("Arial", 24, "bold")).pack(pady=5)
            
            # Derived stat name
            ttk.Label(derived_stat_frame, text=stat).pack(pady=2)

            # Derived stat bonus input
            ttk.Label(derived_stat_frame, text="Qualities:").pack(pady=2)
            derived_bonus_vars[f"{stat.lower()}_bonus"] = tk.StringVar()
            derived_bonus_vars[f"{stat.lower()}_bonus"].set(
                str(character_data["derived_stats"].get(f"{stat.lower()}_bonus", 0)
                    ))
            derived_bonus_entry = ttk.Entry(derived_stat_frame, width=5,
                textvariable=derived_bonus_vars[f"{stat.lower()}_bonus"]
                )
            derived_bonus_entry.pack(pady=2)
            
            # Bind calculation to derived stat bonus change
            derived_bonus_vars[f"{stat.lower()}_bonus"].trace_add("write",
                lambda *args, s=stat.lower(): self.calculate_stats(
                    stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, 
                    derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, 
                    max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, 
                    stat_spent_var, dp_spent_var, dp_allocated_var
                ))
            
        # Misc Stats
        misc_frame = ttk.Frame(scrollable_frame)
        misc_frame.pack(fill="x", padx=20, pady=10)

        misc_names = ["Movement", "Initiative", "Range", "Eff. Limit"]
        misc_keys = ["move", "init", "range", "max_range"]

        for i, stat in enumerate(misc_names):
            # Create frame for each misc stat
            misc_stat_frame = ttk.Frame(misc_frame)
            misc_stat_frame.grid(row=0, column=i, padx=20, pady=5)
            
            # Misc stat value display
            misc_vars[misc_keys[i]] = tk.StringVar(value="0")
            ttk.Label(misc_stat_frame, textvariable=misc_vars[misc_keys[i]], 
                     font=("Arial", 24, "bold")).pack(pady=5)
            
            # Misc stat name
            ttk.Label(misc_stat_frame, text=stat).pack(pady=2)

            # Misc stat bonus input
            ttk.Label(misc_stat_frame, text="Qualities:").pack(pady=2)
            misc_bonus_vars[f"{misc_keys[i]}_bonus"] = tk.StringVar()
            misc_bonus_vars[f"{misc_keys[i]}_bonus"].set(
                str(character_data["misc_stats"].get(f"{misc_keys[i]}_bonus", 0))
                )
            misc_bonus_entry = ttk.Entry(
                misc_stat_frame, width=5, textvariable=misc_bonus_vars[f"{misc_keys[i]}_bonus"]
                )
            misc_bonus_entry.pack(pady=2)
            
            # Bind calculation to misc stat bonus change
            misc_bonus_vars[f"{misc_keys[i]}_bonus"].trace_add("write",
                lambda *args, s=stat.lower(): self.calculate_stats(
                    stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, 
                    derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, 
                    max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, 
                    stat_spent_var, dp_spent_var, dp_allocated_var
                ))
        
        # Bind stage change to stat recalculation
        stage_combo.bind("<<ComboboxSelected>>", 
                        lambda event: self.calculate_stats(
                            stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, 
                            derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, 
                            max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, 
                            stat_spent_var, dp_spent_var, dp_allocated_var
                        ))
        
        # Bind size change to stat recalculation
        size_combo.bind("<<ComboboxSelected>>", 
                lambda event: self.calculate_stats(
                    stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, 
                    derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, 
                    max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, 
                    stat_spent_var, dp_spent_var, dp_allocated_var
                ))
        
        # Initial calculation
        self.calculate_stats(
            stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, 
            derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, 
            max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, 
            stat_spent_var, dp_spent_var, dp_allocated_var
        )
        
        # Attacks section
        attacks_frame = ttk.Frame(scrollable_frame)
        attacks_frame.pack(fill="x", padx=20, pady=10)
        
        ttk.Label(attacks_frame, text="Attacks", font=("Arial", 14, "bold")).grid(
            row=0, column=0, columnspan=9, padx=5, pady=5, sticky="w"
        )
        
        # Column headers
        ttk.Label(attacks_frame, text="Attack").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(attacks_frame, text="Accuracy").grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Label(attacks_frame, text="Type").grid(row=1, column=2, padx=5, pady=5, sticky="w")
        ttk.Label(attacks_frame, text="Damage").grid(row=1, column=3, padx=5, pady=5, sticky="w")
        ttk.Label(attacks_frame, text="Tags").grid(row=1, column=4, padx=5, pady=5, sticky="w")
        
        # Container for dynamic attacks
        attacks_container = ttk.Frame(attacks_frame)
        attacks_container.grid(row=2, column=0, columnspan=9, padx=5, pady=5, sticky="w")
        
        # Add button for new attacks
        add_attack_btn = ttk.Button(
            attacks_frame, 
            text="Add Attack", 
            command=lambda: self.add_attack_row(attacks_container, character_data)
        )
        add_attack_btn.grid(row=3, column=0, padx=5, pady=10, sticky="w")
        
        # Add existing attacks
        for attack in character_data.get("attacks", []):
            self.add_attack_row(attacks_container, character_data, attack)
        
        # Allocated DP Tracker
        allocated_frame = ttk.Frame(scrollable_frame)
        allocated_frame.pack(fill="x", padx=20, pady=10)
        
        ttk.Label(allocated_frame, text="Allocated DP", font=("Arial", 14, "bold")).grid(
            row=0, column=0, padx=5, pady=5, sticky="w"
        )
        
        # Make sure these variables are included in your form_refs dictionary
        character_data["_form_refs"].update({
            "bonus_dp_var": bonus_dp_var,
            "quality_spent_var": quality_spent_var,
            "stat_spent_var": stat_spent_var,
            "dp_spent_var": dp_spent_var,
            "dp_allocated_var": dp_allocated_var
        })
        
        # Bonus DP Allocated
        ttk.Label(allocated_frame, text="Bonus DP:").grid(
            row=1, column=0, padx=5, pady=5, sticky="w"
        )
        bonus_dp_entry = ttk.Entry(allocated_frame, width=8, textvariable=bonus_dp_var)
        bonus_dp_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        bonus_dp_var.trace_add("write", lambda *args: self.calculate_stats(
            stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, 
            derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, 
            max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, 
            stat_spent_var, dp_spent_var, dp_allocated_var
        ))
        
        # Total DP Display
        ttk.Label(allocated_frame, text="Total DP Spent:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        ttk.Label(allocated_frame, textvariable=dp_spent_var).grid(row=1, column=3, padx=5, pady=5, sticky="w")

        ttk.Label(allocated_frame, text="/").grid(row=1, column=4)
        
        ttk.Label(allocated_frame, textvariable=dp_allocated_var).grid(row=1, column=5, padx=5, pady=5, sticky="w")

        # DP Spent in Qualities
        ttk.Label(allocated_frame, text="Quality DP:").grid(
            row=2, column=0, padx=5, pady=5, sticky="w"
        )
        quality_spent_entry = ttk.Entry(allocated_frame, width=8, textvariable=quality_spent_var)
        quality_spent_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        quality_spent_var.trace_add("write", lambda *args: self.calculate_stats(
            stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, 
            derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, 
            max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, 
            stat_spent_var, dp_spent_var, dp_allocated_var
        ))
        
        # Stats Spent in Qualities
        ttk.Label(allocated_frame, text="Stat DP:").grid(
            row=2, column=2, padx=5, pady=5, sticky="w"
        )
        ttk.Label(allocated_frame, textvariable=stat_spent_var).grid(row=2, column=3, padx=5, pady=5, sticky="w")

        # Qualities section
        qualities_frame = ttk.Frame(scrollable_frame)
        qualities_frame.pack(fill="x", padx=20, pady=10)
        qualities_frame.pack_propagate(False)
        qualities_frame.config(height=500)
        
        ttk.Label(qualities_frame, text="Qualities", font=("Arial", 14, "bold")).pack(anchor="w", pady=5)
        
        qualities_text = tk.Text(qualities_frame, height=10, width=80, wrap="word", 
                              bg=theme["secondary_bg"], fg=theme["text"])
        qualities_text.pack(fill="both", expand=True, pady=5)
        qualities_text.insert("1.0", character_data.get("qualities", ""))
        
        # Scrollbar for qualities text
        qualities_scroll = ttk.Scrollbar(qualities_text, command=qualities_text.yview)
        qualities_text.configure(yscrollcommand=qualities_scroll.set)
        qualities_scroll.pack(side="right", fill="y")
        
        # Store references to form elements for later data collection
        character_data["_form_refs"] = {
            "name_entry": name_entry,
            "digimon_entry": digimon_entry,
            "stage_combo": stage_combo,
            "size_combo": size_combo,
            "attr_combo": attr_combo,
            "type_entry": type_entry,
            "wound_var": wound_var,
            "temp_var": temp_var,
            "batt_var": batt_var,
            "dp_vars": dp_vars,
            "bonus_vars": bonus_vars,
            "derived_vars": derived_vars,
            "derived_bonus_vars": derived_bonus_vars,
            "misc_vars": misc_vars,
            "misc_bonus_vars": misc_bonus_vars,
            "qualities_text": qualities_text,
            "bonus_dp_var": bonus_dp_var,
            "quality_spent_var": quality_spent_var,
            "stat_spent_var": stat_spent_var,
            "dp_spent_var": dp_spent_var,
            "dp_allocated_var": dp_allocated_var
            # Attacks will be collected separately
            # Effects will be collected separately
        }
    
    def calculate_stats(self, stage_combo, size_combo, dp_vars, bonus_vars, stat_vars, derived_vars, derived_bonus_vars, misc_vars, misc_bonus_vars, max_health_var, max_batt_var, bonus_dp_var, quality_spent_var, stat_spent_var, dp_spent_var, dp_allocated_var):
        try:
            # Get stage value (1-5)
            stage_values = {"Baby": 1, "Child": 2, "Adult": 3, "Perfect": 4, "Ultimate": 5}
            stage_value = stage_values.get(stage_combo.get(), 1)  # Default to Child if invalid
            
            # Get size value (1-6)
            size_values = {"Small": 1, "Medium": 2, "Large": 3, "Huge": 4, "Gigantic": 5, "Colossal": 6}
            size_value = size_values.get(size_combo.get(), 2) #Default to Medium if invalid 

            # Calculate which size bonus to inherit
            if size_value == 1:
                size_bit = 1
                size_dos = 0
                size_ram = 2
                size_cpu = 0
            if size_value == 2:
                size_bit = 1
                size_dos = 0
                size_ram = 1
                size_cpu = 0

            if size_value == 3:
                size_bit = 1
                size_dos = 0
                size_ram = 0
                size_cpu = 1
            
            if size_value == 4:
                size_bit = 0
                size_dos = 1
                size_ram = 0
                size_cpu = 1
            
            if size_value > 5:
                size_bit = 0
                size_dos = 1
                size_ram = 0
                size_cpu = 2

            # Calculate primary stats
            for stat in ["acc", "dam", "dod", "arm", "hp"]:
                dp = int(dp_vars.get(f"{stat}_dp").get() or 0)
                bonus = int(bonus_vars.get(f"{stat}_bonus").get() or 0)
                stat_value = stage_value + dp + bonus
                stat_vars[stat].set(str(stat_value))
            
            # Calculate Derived stats
            # for stat in ["acc"]
            
            acc_stat = int(stat_vars["acc"].get())
            dam_stat = int(stat_vars["dam"].get())
            dod_stat = int(stat_vars["dod"].get())
            arm_stat = int(stat_vars["arm"].get())
            hp_stat = int(stat_vars["hp"].get())

            acc_bonus = int(bonus_vars.get("acc_bonus").get() or 0)
            dam_bonus = int(bonus_vars.get("dam_bonus").get() or 0)
            dod_bonus = int(bonus_vars.get("dod_bonus").get() or 0)
            arm_bonus = int(bonus_vars.get("arm_bonus").get() or 0)
            hp_bonus = int(bonus_vars.get("hp_bonus").get() or 0)

            # Calulate derived stat bonuses
            bit_bonus = int(derived_bonus_vars.get("bit_bonus").get() or 0)
            dos_bonus = int(derived_bonus_vars.get("dos_bonus").get() or 0)
            ram_bonus = int(derived_bonus_vars.get("ram_bonus").get() or 0)
            cpu_bonus = int(derived_bonus_vars.get("cpu_bonus").get() or 0)

            bit_value = max(1, math.floor(((acc_stat - acc_bonus) + 3) / 3)) + bit_bonus + size_bit
            dos_value = max(1, math.floor(((dam_stat - dam_bonus) + 3) / 3)) + dos_bonus + size_dos
            ram_value = max(1, math.floor(((dod_stat - dod_bonus) + 3) / 3)) + ram_bonus + size_ram
            cpu_value = max(1, math.floor(((arm_stat - arm_bonus) + 3) / 3)) + cpu_bonus + size_cpu

            derived_vars["bit"].set(str(bit_value))
            derived_vars["dos"].set(str(dos_value))
            derived_vars["ram"].set(str(ram_value))
            derived_vars["cpu"].set(str(cpu_value))
            
            print((derived_vars["bit"]).get());
            print((derived_vars["dos"]).get());
            print((derived_vars["ram"]).get());
            print((derived_vars["cpu"]).get());
            
            # Calculate max health
            max_health = (hp_stat * 2) + (stage_value - 1) - hp_bonus
            max_health_var.set(str(max_health))

            # Calculate max battery
            max_batt = stage_value - 1
            max_batt_var.set(str(max_batt))

            # Calculate misc stats
            bit_stat = int(derived_vars["bit"].get())
            ram_stat = int(derived_vars["ram"].get())

            move_bonus = int(misc_bonus_vars["move_bonus"].get() or 0)
            init_bonus = int(misc_bonus_vars["init_bonus"].get() or 0)
            range_bonus = int(misc_bonus_vars["range_bonus"].get() or 0)
            max_range_bonus = int(misc_bonus_vars["max_range_bonus"].get() or 0)

            move_stat = stage_value + 1 + move_bonus
            init_stat = ram_stat + init_bonus
            range_stat = bit_stat + 3 + range_bonus
            max_range_stat = range_stat + (stage_value - 1) + max_range_bonus

            misc_vars["move"].set(str(move_stat))
            misc_vars["init"].set(str(init_stat))
            misc_vars["range"].set(str(range_stat))
            misc_vars["max_range"].set(str(max_range_stat))
            
            # Calculate DP spent in stats
            stats_spent = 0
            for stat in ["acc", "dam", "dod", "arm", "hp"]:
                dp_value = int(dp_vars.get(f"{stat}_dp").get() or 0)
                stats_spent += dp_value
            stat_spent_var.set(str(stats_spent))

            # Get DP spent in Qualities
            quality_spent = int(quality_spent_var.get() or 0)

            # Calculate total DP spent
            total_dp_spent = stats_spent + quality_spent
            dp_spent_var.set(str(total_dp_spent))

            # Get bonus DP allocated from entry
            bonus_dp_allocated = int(bonus_dp_var.get() or 0)

            # Calculate max DP allocated (10 per stage level plus bonus)
            stage_values = {"Baby": 1, "Child": 2, "Adult": 3, "Perfect": 4, "Ultimate": 5}
            stage_value = stage_values.get(stage_combo.get(), 2)  # Default to Child if invalid
            max_dp_allocated = ((stage_value - 1) * 10) + bonus_dp_allocated
            dp_allocated_var.set(str(max_dp_allocated))

        except Exception as e:
            print(f"Error calculating stats: {str(e)}")
            # Keep values as-is in case of error
    
    def add_effect_row(self, parent, character_data, effect_data=None):
        print("Adding Effect...")
        if "effects" not in character_data:
            character_data["effects"] = []
        elif not isinstance(character_data["effects"], list):
            character_data["effects"] = [character_data["effects"]] if character_data["effects"] else []
        
        if effect_data is None:
            effect_data = {
                "eff_name": "",
                "potency": 0,
                "duration": 0,
            }
            character_data["effects"].append(effect_data)
        
        # Create row frame
        effect_index = len(parent.winfo_children())
        row_frame2 = ttk.Frame(parent)
        row_frame2.pack(fill="x", pady=5)
        
        # Effect name
        effect_name = ttk.Entry(row_frame2, width=10)
        effect_name.grid(row=0, column=0, padx=5)
        effect_name.insert(0, effect_data.get("eff_name", ""))
        
        # Potency
        potency = ttk.Entry(row_frame2, width=8)
        potency.grid(row=0, column=1, padx=5)
        potency.insert(0, effect_data.get("potency", ""))
        
        # Type dropdown
        duration = ttk.Entry(row_frame2, width=8)
        duration.grid(row=0, column=2, padx=5)
        duration.insert(0,effect_data.get("duration", ""))
        
        # Remove button
        if effect_index >= 0: 
            remove_btn = ttk.Button(
                row_frame2, 
                text="-", 
                width=2,
                command=lambda: self.remove_effect(row_frame2, character_data, effect_index)
            )
            remove_btn.grid(row=0, column=5, padx=5)
        
        # Store references for data collection
        effect_data["_form_refs"] = {
            "eff_name": effect_name,
            "potency": potency,
            "duration": duration,
            "row_frame2": row_frame2
        }

    def remove_effect(self, row_frame2, character_data, index):
        # Remove from UI
        row_frame2.destroy()
        
        # Remove from data structure
        if index < len(character_data["effects"]):
            character_data["effects"].pop(index)
        
        # Reindex remaining effects
        # This is important for proper saving later
        for i, effect in enumerate(character_data["effects"]):
            if "_form_refs" in effect and "row_frame2" in effect["_form_refs"]:
                effect["_form_refs"]["row_frame2"].update_idletasks()

    def add_attack_row(self, parent, character_data, attack_data=None):
        print("Adding Attack...")
        if attack_data is None:
            attack_data = {
                "name": "",
                "accuracy": 0,
                "type": "Melee",
                "damage": 0,
                "tags": ["", "", ""]
            }
            character_data["attacks"].append(attack_data)
        
        # Create row frame
        attack_index = len(parent.winfo_children())
        row_frame = ttk.Frame(parent)
        row_frame.pack(fill="x", pady=5)
        
        # Attack name
        attack_name = ttk.Entry(row_frame, width=20)
        attack_name.grid(row=0, column=0, padx=5)
        attack_name.insert(0, attack_data.get("name", ""))
        
        # Accuracy
        accuracy = ttk.Entry(row_frame, width=8)
        accuracy.grid(row=0, column=1, padx=5)
        accuracy.insert(0, attack_data.get("accuracy", ""))
        
        # Type dropdown
        attack_type = ttk.Combobox(row_frame, values=["Melee", "Ranged", "Support"], width=10)
        attack_type.grid(row=0, column=2, padx=5)
        attack_type.set(attack_data.get("type", "Melee"))
        
        # Damage
        damage = ttk.Entry(row_frame, width=8)
        damage.grid(row=0, column=3, padx=5)  
        damage.insert(0, attack_data.get("damage", ""))
        
        # Tags (3 fields)
        tags_frame = ttk.Frame(row_frame)
        tags_frame.grid(row=0, column=4, padx=5)
        
        tag_entries = []
        for i in range(3):
            tag = ttk.Entry(tags_frame, width=10)
            tag.pack(side="left", padx=2)
            tag.insert(0, attack_data.get("tags", ["", "", ""])[i] if i < len(attack_data.get("tags", [])) else "")
            tag_entries.append(tag)
        
        # Remove button (except for first attack)
        if attack_index > 0:
            remove_btn = ttk.Button(
                row_frame, 
                text="-", 
                width=2,
                command=lambda: self.remove_attack(row_frame, character_data, attack_index)
            )
            remove_btn.grid(row=0, column=5, padx=5)
        
        # Store references for data collection
        attack_data["_form_refs"] = {
            "name": attack_name,
            "accuracy": accuracy,
            "type": attack_type,
            "damage": damage,
            "tags": tag_entries,
            "row_frame": row_frame
        }
    
    def remove_attack(self, row_frame, character_data, index):
        # Remove from UI
        row_frame.destroy()
        
        # Remove from data structure
        if index < len(character_data["attacks"]):
            character_data["attacks"].pop(index)
        
        # Reindex remaining attacks
        # This is important for proper saving later
        for i, attack in enumerate(character_data["attacks"]):
            if "_form_refs" in attack and "row_frame" in attack["_form_refs"]:
                attack["_form_refs"]["row_frame"].update_idletasks()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DigimonDNDApp(root)
    root.mainloop()
