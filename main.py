'''
GUI interface for the program
'''
import tkinter as tk
from dotenv import dotenv_values, set_key

# root = tk.Tk()
# root.title("Env Viewer")
# root.minsize(700, 200) # Enough to fit the api key?

# # Create labels and entry fields for each screen so we can destroy them while moving to the next screen
# elements = []
# errors = [] # for displaying errors

# # def change_screens(next_screen):
# #     for entry in elements:
# #         entry.destroy()
# #     next_screen()
# def change_screens(next_screen):
#     clear_elements()
#     next_screen()

# def clear_elements():
#     for element in elements:
#         element.destroy()
#     elements.clear()

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

# startup_screen()
# root.mainloop()


# def run(width=300, height=300):
#     # Set up data and call init
#     class Struct(object): pass
#     data = Struct()
#     data.width = width
#     data.height = height
#     data.timerDelay = 1# milliseconds
#     root = tK()
#     init(data)

#     # and launch the app
#     root.mainloop()  # blocks until window is closed
#     print("bye!")

# def main():
#     run(1280, 800)

# if __name__ == '__main__':
#     main()

class Widget():
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

class TestWidget(Widget):
    def __init__(self, root, screens):
        super().__init__(root, screens)
        # self.label = tk.Label(root, text="Hello World 2!")
        # self.button = tk.Button(root, text="Click Me!", command=lambda: screens.change_screen("test_widget2"))    
    
    def render(self) -> None:
        self.label = tk.Label(self.root, text="Hello World 2!")
        self.button = tk.Button(self.root, text="Click Me!", command=lambda: self.screens.change_screen("test_widget2"))
        self.label.pack()
        self.button.pack()
        self.stuff.append(self.label)
        self.stuff.append(self.button)


class TestWidget2(Widget):
    def __init__(self, root, screens):
        super().__init__(root, screens)
        # self.label = tk.Label(root, text="Hello World 3!")
        # self.button = tk.Button(root, text="Click Me!", command=lambda: screens.change_screen("test_widget"))    
    
    def render(self) -> None:
        self.label = tk.Label(self.root, text="Hello World 3!")
        self.button = tk.Button(self.root, text="Click Me!", command=lambda: self.screens.change_screen("test_widget"))
        self.label.pack()
        self.button.pack()
        self.stuff.append(self.label)
        self.stuff.append(self.button)



class Screens():
    def __init__(self, root) -> None:
        self.test_widget = TestWidget(root, self)
        self.test_widget2 = TestWidget2(root, self)
        self.current_page = None
    
    def lookup(self, page) -> Widget:
        if page == "test_widget":
            return self.test_widget
        elif page == "test_widget2":
            return self.test_widget2
        else:
            raise ValueError(f"Page {page} not found")

    def get_current_page(self) -> Widget:
        return self.current_page

    def set_current_page(self, page) -> None:
        self.current_page = self.lookup(page)
        # print("page lookup", self.current_page)
        self.current_page.render()
        
    def change_screen(self, page) -> None:
        # print("changing screen")
        # print("current page", self.current_page)
        # print("new page", page)
        self.current_page.hide()
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

        self.data.screens.set_current_page("test_widget2")
        
        self.root.mainloop()
        print("App closed")


if __name__ == '__main__':
   app = App()
   app.run()