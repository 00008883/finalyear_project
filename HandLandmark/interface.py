import sys

import customtkinter as ctk
import main
import FaceIdentification

class DMSApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{1280}x{720}")
        self.title("BeHealth DMS")

        self.frame_side = ctk.CTkFrame(master=self, width=140, corner_radius=0)
        self.frame_side.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.frame_side.grid_rowconfigure(4, weight=1)
        self.frame_main = ctk.CTkFrame(master=self)
        self.frame_main.grid(row=0, column=1, padx=(20, 20), pady=20)
        self.frame_buttons = ctk.CTkFrame(master=self)
        self.frame_buttons.grid(row=1, column=1, padx=(20, 20), pady=(20, 0))


        self.faceID_state = "normal"
        self.switch_faceId = ctk.StringVar(value="on")
        self.driver_name = "Guest"

        # SIDE INTERFACE GRID
        self.switch = ctk.CTkSwitch(master=self.frame_side, text="Enable Face ID", command=self.enableFaceSwitch, variable=self.switch_faceId,
                                    onvalue="on", offvalue="off")
        self.switch.grid(row=1, column=0, padx=10, pady=(100, 10))
        self.logo_label = ctk.CTkLabel(self.frame_side, text="BeHealth",
                                                 font=ctk.CTkFont(size=20, weight="bold"), width= 200)
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button = ctk.CTkButton(self.frame_side, text="EXIT", height=40, command=self.sidebar_button_event)
        self.sidebar_button.grid(row=2, column=0, padx=20, pady=(500, 100))

        # MAIN INTERFACE GRID
        # Main label
        self.title_label = ctk.CTkLabel(self.frame_main, text="BeHealth Driver Monitoring System",
                                        font=ctk.CTkFont(size=30, weight="bold"))
        self.title_label.grid(padx=350, pady=100)

        # Welcome Label
        self.welcome_label = ctk.CTkLabel(self.frame_main, text="Welcome, {}".format(self.driver_name),
                                        font=ctk.CTkFont(size=20))
        self.welcome_label.grid(padx=350, pady=100)

        # Face ID button
        self.faceID_button = ctk.CTkButton(self.frame_buttons, text="Face ID", width=200, height=50, state=self.faceID_state, command=self.faceID)
        self.faceID_button.grid(row=1, column=0, padx=50, pady=10)

        # Monitoring Button
        self.main_button = ctk.CTkButton(self.frame_buttons, text="Monitoring System", width=200, height=50,  command=self.monitoringSystem)
        self.main_button.grid(row=1, column=1, padx=50, pady=10)

    def faceID(self):
        try:
            self.faceId = FaceIdentification
            self.driver_fname = self.faceId.main()
            self.driver_name = self.driver_fname.replace("_", " ")
            self.welcome_label.configure(text="Welcome, {}".format(self.driver_name))
            print(self.driver_name)

        except:
            print("Something went wrong with Identification Module")

    # Monitor button functionality
    def monitoringSystem(self):
        try:
            main.main()
        except:
            print("Something went wrong with Monitoring Module")

    def enableFaceSwitch(self):
        try:
            self.check = self.switch_faceId.get()
            if self.check == "on":
                self.faceID_state = "normal"
                print("switch toggled, current value:", self.switch_faceId.get())
            elif self.check == "off":
                self.faceID_state = "disabled"
                print("switch toggled, current value:", self.switch_faceId.get())
            self.faceID_button.configure(state=self.faceID_state)
        except:
            print("Something went wrong with switch")

    # Exit button function
    def sidebar_button_event(self):
        sys.exit()

if __name__ == "__main__":
    application = DMSApp()
    application.mainloop()