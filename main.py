'''
GUI interface for the program
'''
import tkinter as tk
from tkinter.ttk import *
from dotenv import dotenv_values, set_key



# def hello_world():
#     result_label = tk.Label(root, text="")
#     # result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
#     result_label.config(text="Hello World!")
#     result_label.place(x=100, y=100)
#     elements.append(result_label)

#     button = tk.Button(root, text="<- Back", command=lambda: change_screens(startup_screen))
#     button.place(x=10, y=10)
#     elements.append(button)
#     root.update() # force an update?


# def validate_entries(entry_elements):
#     for key, entry in entry_elements:
#         value = entry.get()
#         if not value:
#             print("Please fill out all fields")
#             label = tk.Label(root, text="Please fill out all fields", fg="red")
#             label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
#             errors.append(label)
#             return
#     print("all fields filled out")
#     change_screens(hello_world)

# def startup_screen():

#     env_values = dotenv_values(".env")
#     entry_elements = [] # for saving changes

#     def save_changes():
#         print("saving changes")
#         print(entry_elements)
#         for key, entry in entry_elements:
#             value = entry.get()
#             print("setting key", key, "to", value)
#             set_key(".env", key, value)

#     # buttons before entries for assignemnt ordering purposes
#     ok_button = tk.Button(root, text="OK", command=lambda: validate_entries(entry_elements))
#     ok_button.grid(row=len(env_values), column=0, columnspan=2, padx=10, pady=10)

#     save_button = tk.Button(root, text="Save", command=save_changes, state=tk.DISABLED)
#     save_button.grid(row=len(env_values), column=1, columnspan=2, padx=10, pady=10)

#     def entry_changed(*args):
#         print("entry changed")
#         save_button.config(state=tk.NORMAL)  # Enable the save button
#         for e in errors:
#             e.destroy()

#     for i, (key, value) in enumerate(env_values.items()):
#         label = tk.Label(root, text=key)
#         label.grid(row=i, column=0, padx=10, pady=5)
#         elements.append(label)

#         entry_var = tk.StringVar()
#         entry_var.set(value)

#         entry = tk.Entry(root, width=70, textvariable=entry_var)
#         # entry.insert(0, value)
#         entry.grid(row=i, column=1, padx=10, pady=5)
#         elements.append(entry)
#         entry_elements.append((key, entry))

#         entry_var.trace("w", entry_changed)

    
#      # elements.append(ok_button)
#     ### why dont i need to append these buttons???
    


#     root.update()



class Screen():
    def __init__(self, root, screens) -> None:
        self.root = root
        self.screens = screens
        self.stuff = []
    
    def render(self) -> None:
        pass

    def hide(self) -> None:
        for elem in self.stuff:
            elem.destroy()
        self.stuff.clear()

class StartupScreen(Screen):
    def __init__(self, root, screens) -> None:
        super().__init__(root, screens)
        self.env_values = dotenv_values(".env")
        self.entry_elements = [] # for saving changes
    
    def save_changes(self):
        print("saving changes")
        print(self.entry_elements)
        for key, entry in self.entry_elements:
            value = entry.get()
            print("setting key", key, "to", value)
            set_key(".env", key, value)
    
    def entry_changed(self, *args):
        print("entry changed")
        self.save_button.config(state=tk.NORMAL)
    
    def validate_entries(self):
        for key, entry in self.entry_elements:
            value = entry.get()
            if not value:
                print("Please fill out all fields")
                label = tk.Label(self.root, text="Please fill out all fields", fg="red")
                label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)
                self.screens.errors.append(label)
                return
        print("all fields filled out")
        self.screens.change_screen("hello_world")
    
    def render(self) -> None:
        print("rendering startup screen")
        # buttons before entries for assignemnt ordering purposes
        ok_button = tk.Button(self.root, text="OK", command=self.validate_entries)
        ok_button.grid(row=len(self.env_values), column=0, columnspan=2, padx=10, pady=10)
        self.stuff.append(ok_button)

        save_button = tk.Button(self.root, text="Save", command=self.save_changes, state=tk.DISABLED)
        save_button.grid(row=len(self.env_values), column=1, columnspan=2, padx=10, pady=10)
        self.save_button = save_button

        # for i, (key, value) in enumerate(self.env_values.items()):
        #     label = tk.Label(self.root, text=key)
        #     label.grid(row=i, column=0, padx=10, pady=5)
        #     self.stuff.append(label)

        #     entry_var = tk.StringVar()
        #     entry_var.set(value)

        #     entry = tk.Entry(self.root, width=70, textvariable=entry_var)
        #     # entry.insert(0, value)
        #     entry.grid(row=i, column=1, padx=10, pady=5)
        #     self.stuff.append(entry)
        #     self.entry_elements.append((key, entry))

        #     entry_var.trace("w", self.entry_changed)

# class TestWidget(Screen):
#     def __init__(self, root, screens):
#         super().__init__(root, screens)
#         # self.label = tk.Label(root, text="Hello World 2!")
#         # self.button = tk.Button(root, text="Click Me!", command=lambda: screens.change_screen("test_widget2"))    
    
#     def render(self) -> None:
#         label = tk.Label(self.root, text="Hello World 2!")
#         button = tk.Button(self.root, text="Click Me!", command=lambda: self.screens.change_screen("test_widget2"))
#         label.pack()
#         button.pack()
#         self.stuff.append(label)
#         self.stuff.append(button)

# class TestWidget2(Screen):
#     def __init__(self, root, screens):
#         super().__init__(root, screens)
#         # self.label = tk.Label(root, text="Hello World 3!")
#         # self.button = tk.Button(root, text="Click Me!", command=lambda: screens.change_screen("test_widget"))    
    
#     def render(self) -> None:
#         label = tk.Label(self.root, text="Hello World 3!")
#         button = tk.Button(self.root, text="Click Me!", command=lambda: self.screens.change_screen("test_widget"))
#         label.pack()
#         button.pack()
#         self.stuff.append(label)
#         self.stuff.append(button)



class Screens():
    def __init__(self, root) -> None:
        # self.test_widget = TestWidget(root, self)
        # self.test_widget2 = TestWidget2(root, self)
        self.startup_screen = StartupScreen(root, self)
        self.current_screen = None
    
    def lookup(self, page) -> Screen:
        # if page == "test_widget":
        #     return self.test_widget
        # elif page == "test_widget2":
        #     return self.test_widget2
        if page == "startup_screen":
            return self.startup_screen
        else:
            raise ValueError(f"Page {page} not found")

    def get_current_page(self) -> Screen:
        return self.current_screen

    def set_current_page(self, page) -> None:
        self.current_screen = self.lookup(page)
        # print("page lookup", self.current_page)
        self.current_screen.render()
        
    def change_screen(self, page) -> None:
        # print("changing screen")
        # print("current page", self.current_page)
        # print("new page", page)
        self.current_screen.hide()
        self.set_current_page(page)


class Data():
    def __init__(self, root) -> None:
        ### Setup ###
        self.width = 800
        self.height = 600
        self.timerDelay = 1# milliseconds
        ### Layout ###



        # tbd

        ### Widgets ###
        self.screens = Screens(root)
        

class App():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.data = Data(root=self.root)

    def run(self):
        self.root.title("App")
        self.root.minsize(self.data.width, self.data.height) # Enough to fit the api key?

        self.data.screens.set_current_page("startup_screen")
        
        self.root.mainloop()
        print("App closed")


if __name__ == '__main__':
   app = App()
   app.run()