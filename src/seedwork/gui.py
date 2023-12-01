import customtkinter
from src.objects.simulation import Simulation


class Window:
    app: customtkinter.CTk
    size: tuple[int, int]
    init_arsons: int
    p: float

    def __init__(self):
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
        self.app = customtkinter.CTk()  # create CTk window like you do with the Tk window
        self.app.geometry("400x500")

        frame_1 = customtkinter.CTkFrame(master=self.app)
        frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT,
                                         text="Chance to burn from neighbor:")
        label_1.pack(pady=0, padx=10)

        slider_1 = customtkinter.CTkSlider(master=frame_1, command=self._button_run_function(), from_=0, to=1)
        slider_1.pack(pady=10, padx=10)
        slider_1.set(0.5)

        label_2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Initial arsons")
        label_2.pack(pady=0, padx=10)

        entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="for example 3")
        entry_1.pack(pady=10, padx=10)

        label_3 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Visualize")
        label_3.pack(pady=0, padx=10)

        switch_1 = customtkinter.CTkSwitch(master=frame_1)
        switch_1.pack(pady=10, padx=10)

        label_4 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="Forest size")
        label_4.pack(pady=0, padx=10)

        entry_2 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Width")
        entry_2.pack(pady=10, padx=10)

        entry_3 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Height")
        entry_3.pack(pady=10, padx=10)

        button_1 = customtkinter.CTkButton(master=frame_1, command=self._button_run_function)
        button_1.pack(pady=10, padx=10)

    def _button_run_function(self):
        print('test')
        # simulation = Simulation(size=self.size, init_arsons=self.init_arsons, p=self.p)
        # simulation.simulate(visualize=True)

    def __call__(self):
        self.app.mainloop()

window = Window()
window()