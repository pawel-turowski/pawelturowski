from tkinter import *
from tkinter import messagebox


class Converter(object):
    def display(self):
        root = Tk()

        cent_label = Label(root, text="Celsjusza")
        cent_label.grid(row=0, column=0, padx=5, pady=5, stick=E)

        fah_label = Label(root, text="Fahrenheit")
        fah_label.grid(row=2, column=0, padx=5, pady=5, stick=E)

        cel_label = Label(root, text="Kelwin")
        cel_label.grid(row=3, column=0, padx=5, pady=5, stick=E)

        cent_entry = Entry(root, width=5)
        cent_entry.grid(row=0, column=1, padx=5, pady=5)

        fah_entry = Entry(root, width=5,)
        fah_entry.grid(row=2, column=1, padx=5, pady=5)

        cel_entry = Entry(root, width=5,)
        cel_entry.grid(row=3, column=1, padx=5, pady=5)

        def fah_to_cent():
            fah_string = fah_entry.get()
            fah_float = float(fah_string)
            result = (fah_float - 32)/1.89
            cent_entry.delete(0)
            cent_entry.insert(0, str(result))


        def cent_to_fah():
            cent_string = cent_entry.get()
            cent_float = float(cent_string)
            result = cent_float * 1.8 + 32
            fah_entry.delete(0)
            fah_entry.insert(0, str(result))

        def cent_to_cel():
            cent_string = cent_entry.get()
            cent_float = float(cent_string)
            result = cent_float - 273.15
            cel_entry.delete(0)
            cel_entry.insert(0, str(result))

        def cel_to_cent():
            cel_string = cel_entry.get()
            cel_float = float(cel_string)
            result = cel_float + 273.15
            fah_entry.delete(0)
            fah_entry.insert(0, str(result))



        fah_to_cent_button = Button(root, text="Fahrenheit -> Celsjusz", command=fah_to_cent)
        fah_to_cent_button.grid(row=1, column=0, padx=5, pady=5)

        cent_to_fah_button = Button(root, text="Celsjusz -> Fahrenheit", command=cent_to_fah)
        cent_to_fah_button.grid(row=1, column=1, padx=5, pady=5)

        cent_to_cel_button = Button(root, text="Celsjusz -> Kelwin", command=cent_to_cel)
        cent_to_cel_button.grid(row=1, column=2, padx=5, pady=5)

        cel_to_cent_button = Button(root, text="Kelwin -> Celsjusz", command=cel_to_cent)
        cel_to_cent_button.grid(row=1, column=3, padx=5, pady=5)


        root.mainloop()

if __name__ == '__main__':
    app=Converter()
    app.display()


