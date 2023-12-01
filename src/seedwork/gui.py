import customtkinter

from src.objects.simulation import Simulation

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    size: tuple[int, int]
    init_arsons: int
    p: float

    def __init__(self):
        super().__init__()
        self.title("Forest Fire Simulation")
        self.geometry("400x380")

        self.p = 0.3
        self.init_arsons = 3
        self.size = (5, 5)

        self.frame_1 = customtkinter.CTkFrame(master=self)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_1, justify=customtkinter.LEFT,
                                              text="Chance to being set on fire by a neighbor")
        self.label_1.pack(pady=0, padx=10)

        self.slider_1 = customtkinter.CTkSlider(master=self.frame_1, command=self._setup_p,
                                                from_=0, to=1, number_of_steps=100)
        self.slider_1.pack(pady=10, padx=10)
        self.slider_1.set(0.3)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_1, justify=customtkinter.LEFT, text="Initial arsons")
        self.label_2.pack(pady=0, padx=10)

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Number of arsons")
        self.entry_1.pack(pady=10, padx=10)

        self.label_4 = customtkinter.CTkLabel(master=self.frame_1, justify=customtkinter.LEFT, text="Forest size")
        self.label_4.pack(pady=0, padx=10)

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Width")
        self.entry_2.pack(pady=10, padx=10)

        self.entry_3 = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="Height")
        self.entry_3.pack(pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_1, command=self._button_run_function,
                                                text="Run Simulation")
        self.button_1.pack(pady=10, padx=10)

    def _setup_p(self, value):
        self.p = float(value)

    def _button_run_function(self):
        if self.entry_1.get() != '' and self.entry_2.get() != '' and self.entry_3.get() != '':
            self.size = (int(self.entry_2.get()), int(self.entry_3.get()))
            self.init_arsons = int(self.entry_1.get())
            simulation = Simulation(size=self.size, init_arsons=self.init_arsons, p=self.p)
            simulation.simulate(visualize=True)
