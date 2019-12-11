from tksheet import Sheet
import tkinter as tk


class demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.sheet_demo = Sheet(self,
                                width = 1000,
                                height = 700,
                                align = "w",
                                header_align = "center",
                                row_index_align = "center",
                                row_index_width = 50,
                                total_rows = 2000,
                                total_columns = 100)
        self.sheet_demo.enable_bindings(("single",
                                         "drag_select",
                                         "column_drag_and_drop",
                                         "row_drag_and_drop",
                                         "column_select",
                                         "row_select",
                                         "column_width_resize",
                                         "double_click_column_resize",
                                         "row_width_resize",
                                         "column_height_resize",
                                         "arrowkeys",
                                         "row_height_resize",
                                         "double_click_row_resize",
                                         "copy",
                                         "cut",
                                         "paste",
                                         "delete",
                                         "undo",
                                         "edit_cell",
                                         "rc_insert_column",
                                         "rc_delete_column",
                                         "rc_insert_row",
                                         "rc_delete_row"))
        self.sheet_demo.grid(row = 0, column = 0, sticky = "nswe")
        

        """_________________________ EXAMPLES _________________________ """
        """_____________________________________________________________"""

        # __________ CHANGING THEME __________

        #self.sheet_demo.change_theme("dark")

        # __________ HIGHLIGHT / DEHIGHLIGHT CELLS __________

        self.sheet_demo.highlight_cells(row = 0, column = 0, bg = "#ed4337", fg = "white")
        self.sheet_demo.highlight_cells(row = 0, bg = "#ed4337", fg = "white", canvas = "row_index")
        self.sheet_demo.highlight_cells(column = 0, bg = "#ed4337", fg = "white", canvas = "header")

        # __________ SETTING OR RESETTING TABLE DATA __________
        
        self.data = [[f"Row {r} Column {c}" for c in range(100)] for r in range(2000)]
        self.sheet_demo.data_reference(self.data)

        # __________ DISPLAY SUBSET OF COLUMNS __________

        #self.sheet_demo.display_subset_of_columns(indexes = [5, 7, 9, 1], enable = True)

        # __________ SETTING HEADERS __________

        #self.headers = [f"Header {c}" for c in range(100)]
        #self.sheet_demo.headers(self.headers)

        # __________ INSERTING A ROW __________

        #self.sheet_demo.insert_row(row = (f"my new row here {c}" for c in range(100)), idx = 0) # a filled row at the start
        #self.sheet_demo.insert_row() # an empty row at the end

        # __________ INSERTING A COLUMN __________

        #self.sheet_demo.insert_column(column = (f"my new col here {r}" for r in range(5000)), idx = 0) # a filled column at the start
        #self.sheet_demo.insert_column() # an empty column at the end

        # __________ HIDING THE ROW INDEX AND HEADERS __________

        #self.sheet_demo.hide("row_index")
        #self.sheet_demo.hide("top_left")
        #self.sheet_demo.hide("header")
        

        
app = demo()
app.mainloop()
