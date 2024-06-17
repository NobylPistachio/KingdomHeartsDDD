import tkinter as tk
from tkinter import ttk
from Utility import find_spirit_recipe,spirit_recipies



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
        """
        Handles the event when the button is clicked.

        Retrieves the selected option from the dropdown combobox and updates the data by calling the `update_data` function with the result of `find_spirit_recipe` function.

        Parameters:
            None

        Returns:
            None
        """
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
        """
        Updates the data displayed in the table.

        Parameters:
            new_data (list[dict]): A list of dictionaries containing the new data to be displayed.

        Returns:
            None
        """
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
    KHDDD_Spirit_Search()