from converter import Converter
from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter import ttk


class ConverterGUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Конвертер единиц")

        self.label = Label(self.window, text="Выберите опцию:")
        self.label.pack()

        self.option_var = StringVar()
        self.option_combobox = ttk.Combobox(self.window, textvariable=self.option_var)
        self.option_combobox['values'] = ["Конвертация длин", "Конвертация веса", "Конвертация валют"]
        self.option_combobox.pack()

        self.option_var.trace_add("write", self.handle_option_change)

        self.value_label = Label(self.window, text="Введите значение:")
        self.value_label.pack()

        self.value = Entry(self.window)
        self.value.pack()

        self.source_unit_label = Label(self.window, text="Введите исходную единицу измерения:")
        self.source_unit_label.pack()

        self.option_var1 = StringVar()
        self.option_combobox1 = ttk.Combobox(self.window, textvariable=self.option_var1)
        self.option_combobox1['values'] = []
        self.option_combobox1.pack()

        self.target_unit_label = Label(self.window, text="Введите целевую единицу измерения:")
        self.target_unit_label.pack()

        self.option_var2 = StringVar()
        self.option_combobox2 = ttk.Combobox(self.window, textvariable=self.option_var2)
        self.option_combobox2['values'] = []
        self.option_combobox2.pack()

        self.result_label = Label(self.window, text="Результат:")
        self.result_label.pack()

        self.result = Label(self.window, text="")
        self.result.pack()

        self.convert_button = Button(self.window, text="Конвертировать", command=self.convert)
        self.convert_button.pack()

        self.option_var1.trace_add("write", self.option_change)
        self.option_var2.trace_add("write", self.option_change)

        self.window.mainloop()

    def convert(self):
        option = self.option_var.get()
        value = float(self.value.get())
        source_unit = self.option_combobox1.get()
        target_unit = self.option_combobox2.get()

        if option == 'Конвертация длин':
            result = Converter.convert_length(value, source_unit, target_unit)
            self.result.configure(text=result)

        else:
            self.result.configure(text="Неверный выбор. Попробуйте еще раз.")

    def handle_option_change(self, *args):
        if self.option_var.get() == "Конвертация длин":
            self.option_combobox1['values'] = ['in', 'ft', 'yd', 'mi', 'вершок', 'аршин', 'сажень', 'верста', 'mm',
                                               'cm', 'm', 'km']
            self.option_combobox2['values'] = ['in', 'ft', 'yd', 'mi', 'вершок', 'аршин', 'сажень', 'верста', 'mm',
                                               'cm', 'm', 'km']
        elif self.option_var.get() == "Конвертация веса":
            self.option_combobox1['values'] = ['oz', 'lb', 'лот', 'золотник', 'доля', 'фунт', 'g', 'kg', 'tonne']
            self.option_combobox2['values'] = ['oz', 'lb', 'лот', 'золотник', 'доля', 'фунт', 'g', 'kg', 'tonne']
        elif self.option_var.get() == "Конвертация валют":
            self.option_combobox1['values'] = ['USD', 'RUB', 'EUR', 'GBP']
            self.option_combobox2['values'] = ['USD', 'RUB', 'EUR', 'GBP']
        else:
            self.option_combobox1['values'] = []
            self.option_combobox2['values'] = []

        self.option_combobox1.set('')
        self.option_combobox2.set('')
        self.result.config(text="")

    def option_change(self, *args):
        self.result.config(text="")


if __name__ == "__main__":
    converter_gui = ConverterGUI()
