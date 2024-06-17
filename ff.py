import tkinter as tk
from tkinter import ttk
from Utility import find_spirit_recipe,spirit_recipies

class KHDDD_Spirit_Search_GUI():

    def __init__(self):
        self.setup_root()
        self.setup_frames()
        self.setup_data()
        self.setup_widgets()
        self.setup_layout()
        self.root.mainloop()

    def setup_root(self):
        
        print("setup_root: before tk.Tk()")
        self.root = tk.Tk()
        print("setup_root: after tk.Tk()")
        
        self.root.title('KHDDD Utility')
        print("setup_root: after root.title()")
        
        self.root.geometry('500x275')
        print("setup_root: after root.geometry()")

    def setup_frames(self):
        print("setup_frames: before creating frame_search")
        self.frame_search = tk.Frame(self.root)
        print("setup_frames: after creating frame_search")
        
        print("setup_frames: before creating frame_table")
        self.frame_table = tk.Frame(self.root)
        print("setup_frames: after creating frame_table")

    def setup_data(self):
        print("setup_data: before sorting options")
        self.options = list(set([recipe['Spirit'] for recipe in spirit_recipies]))
        print("setup_data: after sorting options")
        
        self.options.sort()
        print(f"setup_data: options: {self.options}")
        
        print("setup_data: before getting column names")
        self.columns = list(spirit_recipies[0].keys())
        print(f"setup_data: columns: {self.columns}")
    
    def setup_widgets(self):
        print("setup_widgets: before creating label")
        self.label = tk.Label(self.frame_search, text='Select a spirit:')
        print("setup_widgets: after creating label")
        
        print("setup_widgets: before creating dropdown")
        self.dropdown = ttk.Combobox(self.frame_search, values=self.options)
        print("setup_widgets: after creating dropdown")
        
        print("setup_widgets: before binding dropdown")
        self.dropdown.bind('<<ComboboxSelected>>', self.on_option_selected)
        print("setup_widgets: after binding dropdown")
        
        print("setup_widgets: before creating table")
        self.table = ttk.Treeview(self.frame_table,columns=self.columns, show='headings')
        print("setup_widgets: after creating table")
        
        for col in self.columns:
            print(f"setup_widgets: before configuring table column {col}")
            self.table.heading(col,text=col)
            self.table.column(col,width=100)
            print(f"setup_widgets: after configuring table column {col}")
        
        # print("setup_widgets: before creating button")
        # self.button = tk.Button(self.frame_search, text='Search', command=self.on_click)
        # print("setup_widgets: after creating button")
        
        data:list[dict] = []
        for row in data:
            print("setup_widgets: before inserting into table")
            data_handle:tuple = tuple(row.values())
            self.table.insert("",tk.END, values=data_handle)
            print("setup_widgets: after inserting into table")


    # def on_click(self):
    #     print("on_click: before getting spirit from dropdown")
    #     self.spirit = self.dropdown.get()
    #     print(f"on_click: got spirit: {self.spirit}")
        
    #     print("on_click: before calling find_spirit_recipe")
    #     recipe = find_spirit_recipe(self.spirit)
    #     print(f"on_click: got recipe: {recipe}")
        
    #     print("on_click: before calling update_data")
    #     self.update_data(recipe)
    #     print("on_click: after calling update_data")
    
    def on_option_selected(self,event):
        print("on_option_selected: before getting spirit from dropdown")
        self.spirit = self.dropdown.get()
        print(f"on_option_selected: got spirit: {self.spirit}")
        
        print("on_option_selected: before calling find_spirit_recipe")
        recipe = find_spirit_recipe(self.spirit)
        print(f"on_option_selected: got recipe: {recipe}")
        
        print("on_option_selected: before calling update_data")
        self.update_data(recipe)
        print("on_option_selected: after calling update_data")
    
    def update_data(self,new_data:list[dict]):
        print("update_data: before deleting table children")
        self.table.delete(*self.table.get_children())
        print("update_data: after deleting table children")
        
        print("update_data: before iterating over new_data")
        for row in new_data:
            print("update_data: before creating data_handle")
            data_handle:tuple = tuple(row.values())
            print("update_data: after creating data_handle")
            
            print("update_data: before inserting into table")
            self.table.insert("",tk.END, values=data_handle)
            print("update_data: after inserting into table")

    def setup_layout(self):
        print("setup_layout: before packing frame_search")
        self.frame_search.pack(side=tk.TOP)
        print("setup_layout: after packing frame_search")
        
        print("setup_layout: before packing frame_table")
        self.frame_table.pack(side=tk.TOP)
        print("setup_layout: after packing frame_table")
        
        print("setup_layout: before packing label")
        self.label.pack(side=tk.LEFT)
        print("setup_layout: after packing label")
        
        print("setup_layout: before packing dropdown")
        self.dropdown.pack(side=tk.LEFT)
        print("setup_layout: after packing dropdown")
        
        # print("setup_layout: before packing button")
        # self.button.pack(side=tk.RIGHT)
        # print("setup_layout: after packing button")
        
        print("setup_layout: before packing table")
        self.table.pack(expand=True, fill=tk.BOTH)
        print("setup_layout: after packing table")
def KHDDD_Spirit_Search():
    """
    Creates a GUI window for searching spirits in the KHDDD Utility.
    
    This function initializes a Tkinter root window with the title 'KHDDD Utility' and the geometry '500x275'. 
    It creates two frames: `frame_search` and `frame_table`, which are used to organize the widgets in the window.
    
    The function creates a label widget with the text 'Select a spirit:' in the `frame_search` frame.
    
    The `on_option_selected` function is defined to handle the event when an option is selected in the dropdown combobox. 
    It retrieves the selected option and prints it.
    
    The `options` list is created by extracting the unique 'Spirit' values from the `spirit_recipies` list and sorting them.
    The `dropdown` widget is created with the `values` parameter set to the `options` list. It is bound to the '<<ComboboxSelected>>' event and the `on_option_selected` function is called when the event occurs.
    """
    root = tk.Tk()
    root.title('KHDDD Utility')
    root.geometry('500x275')

    tab_search_spirit = ttk.Notebook(root)
    #setup frames
    frame_search = tk.Frame(root)
    frame_table = tk.Frame(root)

    label = tk.Label(frame_search, text='Select a spirit:')

    def on_option_selected(event):
        """
        Handles the event when an option is selected in the dropdown combobox.

        Args:
            event (Event): The event object representing the option selection.

        Returns:
            None

        Prints the selected option to the console.
        """
        selected_option = dropdown.get()
        print(f"Selected option: {selected_option}")

    options = list(set([recipe['Spirit'] for recipe in spirit_recipies]))
    options.sort()
    dropdown = ttk.Combobox(frame_search, values=options)
    dropdown.bind('<<ComboboxSelected>>', on_option_selected)

    def on_click():
        spirit = dropdown.get()
        update_data(find_spirit_recipe(spirit))

    button = tk.Button(frame_search, text='Search', command=on_click)

    columns = list(spirit_recipies[0].keys())

    table = ttk.Treeview(frame_table,columns=columns, show='headings')

    data:list[dict] = []
    for col in columns:
        table.heading(col,text=col,)
        table.column(col,width=100)
    for row in data:
        data_handle:tuple = tuple(row.values())
        table.insert("",tk.END, values=data_handle)

    def update_data(new_data:list[dict]):
        table.delete(*table.get_children())
        for row in new_data:
            data_handle:tuple = tuple(row.values())
            table.insert("",tk.END, values=data_handle)


    #layout
    frame_search.pack(side=tk.TOP)
    frame_table.pack(side=tk.TOP)


    label.pack(side=tk.LEFT)
    dropdown.pack(side=tk.LEFT)
    button.pack(side=tk.RIGHT)
    table.pack(expand=True, fill=tk.BOTH)




    root.mainloop()

if __name__ == '__main__':
    # khddd_spirit_search()
    # KHDDD_Spirit_Search()
    KHDDD_Spirit_Search_GUI()