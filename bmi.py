import tkinter
import customtkinter


class bmi:
    def __init__(self):
        self.__init_ui()
        self.__app.mainloop()

    def __init_ui(self):
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

        self.__app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        self.__app.geometry("400x400")

        self.__init_input_grid()
        self.__init_confirm_button()
        self.__init_output_field()

    def __init_input_grid(self):
        self.__app.grid_columnconfigure(0, weight = 0)
        self.__app.grid_columnconfigure((0, 1), weight = 0)  

        self.__init_labels()
        self.__init_input_fields()

    def __init_labels(self):
        weight_label = customtkinter.CTkLabel(self.__app, text="Gewicht", font=customtkinter.CTkFont(family = "Hack", size=20))
        weight_label.grid(column = 0, row = 0, padx = 20, pady = 20)

        height_label = customtkinter.CTkLabel(self.__app, text="Höhe", font=customtkinter.CTkFont(family = "Hack", size=20))
        height_label.grid(column = 0, row = 1, padx = 20, pady = 20)

    def __init_input_fields(self):
        self.weight_input_field = customtkinter.CTkEntry(master = self.__app, placeholder_text="in kg")
        self.weight_input_field.grid(column = 1, row = 0, padx = 20, pady = 20)

        self.height_input_field = customtkinter.CTkEntry(master = self.__app, placeholder_text="in m")
        self.height_input_field.grid(column = 1, row = 1, padx = 20, pady = 20)

    def __init_confirm_button(self):
        # Use CTkButton instead of tkinter Button
        button = customtkinter.CTkButton(master=self.__app, text="Berechnen", width=350, command=self.__berechne_bmi)
        button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    
    def __init_output_field(self):
        self.__bmi_label = customtkinter.CTkLabel(self.__app, fg_color = "#a6d189", width=350, text_color = "black", text = "BMI-Wert: 0", 
                                           font = customtkinter.CTkFont(family = "Hack", size = 20))
        self.__bmi_label.grid(column = 0, row = 5, columnspan = 2, padx = 25, pady = 100)

    def __berechne_bmi(self):
        bmi = float(self.weight_input_field.get()) / pow(float(self.height_input_field.get()), 2)
        self.__bmi_label.configure(text = "BMI-Wert: " + str(round(bmi, 2)))
        self.set_bmi_coloring(round(bmi, 2))

def set_bmi_coloring(self, bmi):
        if bmi <= 17:
            self.__bmi_label.configure(fg_color = "#e78284", text_color = "black")
        elif bmi <= 18.5 and bmi > 17:
            self.__bmi_label.configure(fg_color = "#e5c890", text_color = "black")
        elif bmi <= 25 and bmi > 18.5:
            self.__bmi_label.configure(fg_color = "#a6d189", text_color = "black")
        elif bmi <= 30 and bmi > 25:
            self.__bmi_label.configure(fg_color = "#e5c890", text_color = "black")
        elif bmi <= 35 and bmi > 30:
            self.__bmi_label.configure(fg_color = "#ef9f76", text_color = "black")
        elif bmi > 35:
            self.bmi_label.configure(fg_color = "#e78284", text_color = "black")

bmi = bmi()