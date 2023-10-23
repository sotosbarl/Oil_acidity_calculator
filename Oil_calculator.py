import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk  # Import the necessary modules
import json

# # Sample data
# data = {
#     "1": {"mass": 0, "acidity": 0},
#     "2": {"mass": 0, "acidity": 0},
#     "3": {"mass": 0, "acidity": 0},
#     "4": {"mass": 0, "acidity": 0},
#     "5": {"mass": 0, "acidity": 0},
#     "6": {"mass": 0, "acidity": 0},
# }
#
# # Save data to a JSON file
# with open("data.json", "w") as json_file:
#     json.dump(data, json_file)


class AcidityCalculatorApp:


    def __init__(self, root):
        self.root = root
        self.root.title("Acidity Calculator")

        self.root.geometry("1200x1000")  # Adjust the dimensions as needed
        self.bold_font = ("Helvetica", 12, "bold")
        self.bold_font_big = ("Helvetica", 16, "bold")

        with open("data.json", "r") as json_file:
            self.loaded_data = json.load(json_file)





        # background_image = Image.open("olive.webp")  # Replace with your image file
        # self.background_photo = ImageTk.PhotoImage(background_image)
        # self.background_label = tk.Label(self.root, image=self.background_photo)
        # self.background_label.place(relwidth=1, relheight=1)

        tank1_image = Image.open("background.png")  # Replace with your image file
        self.tank1_image = ImageTk.PhotoImage(tank1_image)
        self.background_label3 = tk.Label(self.root, image=self.tank1_image)
        self.background_label3.pack()

        # elsap_image = Image.open("elsap.jpg")  # Replace with your image file
        # self.elsap_image = ImageTk.PhotoImage(elsap_image)
        # self.background_label2 = tk.Label(self.root, image=self.elsap_image)
        # self.background_label2.place(relwidth=0.15, relheight=0.09, relx=0.85, rely=0.85, anchor="center")
        self.total_mass_list = []
        self.initial_acidity_list = []
        self.supplier_variables = []


        for i in range(1,7):
            self.tank_name = str(i)

            # Access specific tank data
            tank_name = f"{self.tank_name}"
            tank_info = self.loaded_data.get(tank_name)
            if tank_info:
                mass = tank_info.get("mass")
                acidity = tank_info.get("acidity")
                self.total_mass_list.append(mass)
                self.initial_acidity_list.append(acidity)

            else:
                print(f"{tank_name} not found in the loaded data.")



        self.content_frame = tk.Frame(self.root)
        self.content_frame.place(relx=0.5, rely=0.3, anchor="center")


        # Custom button style
        style = ttk.Style()
        style.configure("TButton", padding=5, relief="flat", background="#4CAF50", foreground="white")

        self.pages = [self.create_initial_page(), None, None]
        self.current_page = 0

        self.show_page(self.current_page)





    def create_initial_page(self):
        initial_page = tk.Frame(self.content_frame)

        self.tank1 = tk.Frame(self.root)
        self.tank1.place(relx=0.08, rely=0.35, anchor="center")

        self.tank2 = tk.Frame(self.root)
        self.tank2.place(relx=0.38, rely=0.35, anchor="center")

        self.tank3 = tk.Frame(self.root)
        self.tank3.place(relx=0.66, rely=0.35, anchor="center")

        self.tank4 = tk.Frame(self.root)
        self.tank4.place(relx=0.08, rely=0.67, anchor="center")

        self.tank5 = tk.Frame(self.root)
        self.tank5.place(relx=0.38, rely=0.67, anchor="center")

        self.tank6 = tk.Frame(self.root)
        self.tank6.place(relx=0.66, rely=0.67, anchor="center")


        self.initial_mass_label = tk.Label(self.tank1, text="Tank 1",font= self.bold_font)
        self.initial_mass_label.pack()
        self.initial_next_button = tk.Button(self.tank1, text="Select", command=lambda: self.go_to_added_page1(1), bg='green',
                                             font=self.bold_font)
        self.initial_next_button.pack()


        self.initial_mass_label = tk.Label(self.tank2, text="Tank 2", font=self.bold_font)
        # self.initial_mass_label.place(relx=0.8, rely=0.8, anchor="center")
        self.initial_mass_label.pack()
        self.initial_next_button = tk.Button(self.tank2, text="Select", command=lambda: self.go_to_added_page1(2), bg='green',
                                             font=self.bold_font)

        self.initial_next_button.pack()

        self.initial_mass_label = tk.Label(self.tank3, text="Tank 3", font=self.bold_font)
        self.initial_mass_label.pack()
        self.initial_next_button = tk.Button(self.tank3, text="Select", command=lambda: self.go_to_added_page1(3),bg='green',font=self.bold_font)
        self.initial_next_button.pack()

        self.initial_mass_label = tk.Label(self.tank4, text="Tank 4", font=self.bold_font)
        self.initial_mass_label.pack()
        self.initial_next_button = tk.Button(self.tank4, text="Select", command=lambda: self.go_to_added_page1(4),
                                             bg='green', font=self.bold_font)
        self.initial_next_button.pack()

        self.initial_mass_label = tk.Label(self.tank5, text="Tank 5", font=self.bold_font)
        self.initial_mass_label.pack()
        self.initial_next_button = tk.Button(self.tank5, text="Select", command=lambda: self.go_to_added_page1(5),
                                             bg='green', font=self.bold_font)
        self.initial_next_button.pack()

        self.initial_mass_label = tk.Label(self.tank6, text="Tank 6", font=self.bold_font)
        self.initial_mass_label.pack()
        self.initial_next_button = tk.Button(self.tank6, text="Select", command=lambda: self.go_to_added_page1(6),
                                             bg='green', font=self.bold_font)
        self.initial_next_button.pack()

        # self.num_suppliers_entry = tk.Entry(initial_page)
        # self.num_suppliers_entry.pack()


        self.result_label11 = tk.Label(self.tank1, text="Acidity:", font=self.bold_font)
        self.result_label12 = tk.Label(self.tank2, text="Acidity:", font=self.bold_font)
        self.result_label13 = tk.Label(self.tank3, text="Acidity:", font=self.bold_font)
        self.result_label14 = tk.Label(self.tank4, text="Acidity:", font=self.bold_font)
        self.result_label15 = tk.Label(self.tank5, text="Acidity:", font=self.bold_font)
        self.result_label16 = tk.Label(self.tank6, text="Acidity:", font=self.bold_font)
        self.result_label21 = tk.Label(self.tank1, text="Mass:", font=self.bold_font)
        self.result_label22 = tk.Label(self.tank2, text="Mass:", font=self.bold_font)
        self.result_label23 = tk.Label(self.tank3, text="Mass:", font=self.bold_font)
        self.result_label24 = tk.Label(self.tank4, text="Mass:", font=self.bold_font)
        self.result_label25 = tk.Label(self.tank5, text="Mass:", font=self.bold_font)
        self.result_label26 = tk.Label(self.tank6, text="Mass:", font=self.bold_font)


        self.result_label21.pack()
        self.result_label22.pack()
        self.result_label23.pack()
        self.result_label24.pack()
        self.result_label25.pack()
        self.result_label26.pack()
        self.result_label11.pack()
        self.result_label12.pack()
        self.result_label13.pack()
        self.result_label14.pack()
        self.result_label15.pack()
        self.result_label16.pack()

        labels1 = [self.result_label11,self.result_label12,self.result_label13,self.result_label14,self.result_label15,self.result_label16]
        labels2 = [self.result_label21, self.result_label22, self.result_label23, self.result_label24,
                  self.result_label25, self.result_label26]

        for i in range(1,7):
            tank_name = str(i)
            tank_info = self.loaded_data.get(tank_name)

            if tank_info:
                mass = tank_info.get("mass")
                acidity = tank_info.get("acidity")

            labels1[i-1].config(text=f"Acidity: {self.initial_acidity_list[i-1]:.2f}", font=self.bold_font)
            labels2[i-1].config(text=f"Mass: {self.total_mass_list[i-1]:.2f}", font=self.bold_font)

        # self.initial_mass_label.place(relx=0.8, rely=0.8, anchor="center")


        return initial_page

    def create_added_page1(self,tank_id):
        self.hide_page(0)

        self.tank1.place_forget()
        self.tank2.place_forget()
        self.tank3.place_forget()
        self.tank4.place_forget()
        self.tank5.place_forget()
        self.tank6.place_forget()

        tank1_image2 = Image.open("background2.png")  # Replace with your image file
        self.tank1_image2 = ImageTk.PhotoImage(tank1_image2)
        self.background_label4 = tk.Label(self.root, image=self.tank1_image2)
        self.background_label4.pack()
        #
        self.background_label3.pack_forget()

        self.content_frame = tk.Frame(self.root)
        self.content_frame.place(relx=0.5, rely=0.3, anchor="center")
        #
        #
        #
        # elsap_image = Image.open("elsap.jpg")  # Replace with your image file
        # self.elsap_image = ImageTk.PhotoImage(elsap_image)
        # self.background_label2 = tk.Label(self.root, image=self.elsap_image)
        # self.background_label2.place(relwidth=0.15, relheight=0.09, relx=0.85, rely=0.85, anchor="center")
        #
        initial_page = tk.Frame(self.content_frame)
        initial_page.place(relx=0.9, rely=0.4, anchor="center")



        #
        self.hide_page(1)

        self.tank_name = tank_id

        # Access specific tank data
        # tank_name = f"{self.tank_name}"
        # tank_info = self.loaded_data.get(tank_name)

        self.initial_mass_label = tk.Label(self.root, text=f"Tank {self.tank_name}", font=self.bold_font_big)

        self.initial_mass_label.place(relx=0.31, rely=0.08, anchor="center")

        # if tank_info:
        #     mass = tank_info.get("mass")
        #     acidity = tank_info.get("acidity")
        # else:
        #     print(f"{tank_name} not found in the loaded data.")

        mass = self.total_mass_list[tank_id-1]
        acidity = self.initial_acidity_list[tank_id-1]

        self.initial_mass_label = tk.Label(self.root, text=f"Mass: {mass:.2f}", font=self.bold_font)
        self.initial_mass_label.place(relx=0.235, rely=0.33, anchor="center")

        self.initial_mass_label2 = tk.Label(self.root, text=f"Acidity: {acidity:.2f}", font=self.bold_font)
        self.initial_mass_label2.place(relx=0.235, rely=0.42, anchor="center")

        self.initial_mass_label3 = tk.Label(self.root, text="Suppliers:", font=self.bold_font)
        self.initial_mass_label3.place(relx=0.61, rely=0.38, anchor="center")

        self.num_suppliers_entry = tk.Entry(self.root)
        self.num_suppliers_entry.place(relx=0.61, rely=0.42, anchor="center")

        self.initial_next_button = tk.Button(self.root, text="Next", command=self.go_to_added_page2, bg='green',
                                             font=self.bold_font)
        self.initial_next_button.place(relx=0.61, rely=0.47, anchor="center")

        self.menu_button = tk.Button(self.root, text="Back to initial page", command=self.return_to_menu, bg='green',
                                             font=self.bold_font)
        self.menu_button.place(relx=0.81, rely=0.1, anchor="center")

        self.empty_button = tk.Button(self.root, text="Empty tank", command=self.empty_tank, bg='red',
                                             font=self.bold_font)
        self.empty_button.place(relx=0.61, rely=0.77, anchor="center")

        return initial_page



    def create_added_page2(self):
        added_page = tk.Frame(self.content_frame)
        self.hide_page(1)
        self.initial_next_button.place_forget()
        self.initial_mass_label3.place_forget()
        self.initial_mass_label.place_forget()
        self.initial_mass_label2.place_forget()
        self.num_suppliers_entry.place_forget()
        # self.result_label.place_forget()
        # self.result_label2.place_forget()


        num_suppliers_entry = self.num_suppliers_entry.get()
        self.num_of_suppliers = int(num_suppliers_entry)
        self.supplier_variables = [{"mass": tk.StringVar(), "acidity": tk.StringVar()} for _ in range(self.num_of_suppliers)]

        for i in range(self.num_of_suppliers):
            self.added_mass_label = tk.Label(added_page, text=f"Added Mass (Supplier {i + 1}):",font= self.bold_font)
            self.added_mass_label.pack()

            self.added_mass_entry = tk.Entry(added_page, textvariable=self.supplier_variables[i]["mass"])
            self.added_mass_entry.pack()

            self.added_acidity_label = tk.Label(added_page, text=f"Added Acidity (Supplier {i + 1}):",font= self.bold_font)
            self.added_acidity_label.pack()

            self.added_acidity_entry = tk.Entry(added_page, textvariable=self.supplier_variables[i]["acidity"])
            self.added_acidity_entry.pack()



        self.calculate_button = tk.Button(added_page, text="Calculate",font= self.bold_font ,bg='green',command=self.calculate_initial_acidity)
        self.calculate_button.pack()

        # self.correction = tk.Button(added_page, text="Νέα Μέτρηση",bg='green', command=self.recreate_initial_page,font= self.bold_font)
        # self.correction.pack()

        self.result_label = tk.Label(self.root, text="Acidity:",font= self.bold_font)
        self.result_label.place(relx=0.235, rely=0.42, anchor="center")


        self.result_label2 = tk.Label(self.root, text="Mass:",font= self.bold_font)
        self.result_label2.place(relx=0.235, rely=0.33, anchor="center")

        self.next_button = tk.Button(added_page, text="Next",bg='green', command=self.go_to_third_page,font= self.bold_font)
        self.next_button.pack()

        return added_page

    # def create_added_page(self):
    #     added_page = tk.Frame(self.content_frame)
    #
    #     self.added_mass_label = tk.Label(added_page, text="Added Mass:",font= self.bold_font)
    #     self.added_mass_label.pack()
    #
    #     self.added_mass_entry = tk.Entry(added_page)
    #     self.added_mass_entry.pack()
    #
    #     self.added_acidity_label = tk.Label(added_page, text="Added Acidity:",font= self.bold_font)
    #     self.added_acidity_label.pack()
    #
    #     self.added_acidity_entry = tk.Entry(added_page)
    #     self.added_acidity_entry.pack()
    #
    #     self.calculate_button = tk.Button(added_page, text="Calculate",bg='green', command=self.go_to_added_page2,font= self.bold_font)
    #     self.calculate_button.pack()
    #
    #     self.correction = tk.Button(added_page, text="Νέα Μέτρηση",bg='green', command=self.recreate_initial_page,font= self.bold_font)
    #     self.correction.pack()
    #
    #     self.result_label = tk.Label(self.root, text="Acidity:", font=self.bold_font)
    #     self.result_label.place(relx=0.235, rely=0.42, anchor="center")
    #
    #     self.result_label2 = tk.Label(self.root, text="Mass:", font=self.bold_font)
    #     self.result_label2.place(relx=0.235, rely=0.33, anchor="center")
    #
    #     self.result_label.config(text=f"Acidity: {self.initial_acidity_list[self.tank_name - 1]:.2f}",
    #                              font=self.bold_font)
    #     self.result_label2.config(text=f"Mass: {self.total_mass_list[self.tank_name - 1]:.2f}", font=self.bold_font)
    #
    #     return added_page

    def show_page(self, page_num):
        page = self.pages[page_num]
        if page is not None:
            page.pack()


    def empty_tank(self):
        self.total_mass_list[self.tank_name-1] = 0
        self.initial_acidity_list[self.tank_name-1] = 0

        self.initial_mass_label = tk.Label(self.root, text="Mass: 0.00", font=self.bold_font)
        self.initial_mass_label.place(relx=0.235, rely=0.33, anchor="center")

        self.initial_mass_label2 = tk.Label(self.root, text="Acidity: 0.00", font=self.bold_font)
        self.initial_mass_label2.place(relx=0.235, rely=0.42, anchor="center")



    def hide_page(self, page_num):
        page = self.pages[page_num]
        if page is not None:
            page.pack_forget()

    def go_to_added_page(self):
        initial_acidity = self.initial_acidity_entry.get()
        initial_mass = self.initial_mass_entry.get()

        if initial_acidity and initial_mass:
            self.pages[1] = self.create_added_page()
            self.initial_acidity = float(initial_acidity)
            self.total_mass = float(initial_mass)

            self.hide_page(self.current_page)
            self.current_page = 1
            self.show_page(self.current_page)
            self.result_label.config(text=f"Acidity: {self.initial_acidity:.2f}",font= self.bold_font)
            self.result_label2.config(text=f"Mass: {self.total_mass:.2f}",font= self.bold_font)

        else:
            messagebox.showwarning("Input Error", "Please enter both initial acidity and mass.")

    def go_to_added_page1(self,tank_id):
        self.tank_id = tank_id
        self.pages[1] = self.create_added_page1(tank_id)
        self.hide_page(self.current_page)
        self.current_page = 1
        self.show_page(self.current_page)
        self.result_label.config(text=f"Acidity: {self.initial_acidity_list[self.tank_name-1]:.2f}",font= self.bold_font)
        self.result_label2.config(text=f"Mass: {self.total_mass_list[self.tank_name-1]:.2f}",font= self.bold_font)

    def go_to_added_page2(self):
        self.pages[1] = self.create_added_page2()
        self.hide_page(self.current_page)
        self.current_page = 1
        self.show_page(self.current_page)
        self.result_label.config(text=f"Acidity: {self.initial_acidity_list[self.tank_name-1]:.2f}",font= self.bold_font)
        self.result_label2.config(text=f"Mass: {self.total_mass_list[self.tank_name-1]:.2f}",font= self.bold_font)

    def return_to_menu(self):


        for widget in root.winfo_children():
            widget.destroy()



        # self.pages = [self.create_initial_page(), None, None]
        # self.current_page = 0

        # self.hide_page(self.current_page)
        # self.current_page = 1
        # self.show_page(current_page)

        tank1_image = Image.open("background.png")  # Replace with your image file
        self.tank1_image = ImageTk.PhotoImage(tank1_image)
        self.background_label3 = tk.Label(self.root, image=self.tank1_image)
        self.background_label3.pack()


        # elsap_image = Image.open("elsap.jpg")  # Replace with your image file
        # self.elsap_image = ImageTk.PhotoImage(elsap_image)
        # self.background_label2 = tk.Label(self.root, image=self.elsap_image)
        # self.background_label2.place(relwidth=0.15, relheight=0.09, relx=0.85, rely=0.85, anchor="center")

        self.content_frame = tk.Frame(self.root)
        self.content_frame.place(relx=0.5, rely=0.3, anchor="center")

        self.create_initial_page()


        self.result_label.config(text=f"Acidity: {self.initial_acidity_list[self.tank_name-1]:.2f}",font= self.bold_font)
        self.result_label2.config(text=f"Mass: {self.total_mass_list[self.tank_name-1]:.2f}",font= self.bold_font)

    def recreate_initial_page(self):
        self.hide_page(self.current_page)
        self.pages[0] = self.create_initial_page()
        self.current_page = 0
        self.show_page(self.current_page)

    def calculate_initial_acidity(self):
        # self.total_mass = 0
        # self.initial_acidity = 0
        nominator = self.total_mass_list[self.tank_name-1]*self.initial_acidity_list[self.tank_name-1]

        for i in range(self.num_of_suppliers):
            added_mass = float(self.supplier_variables[i]["mass"].get())
            added_acidity = float(self.supplier_variables[i]["acidity"].get())

            self.total_mass_list[self.tank_name-1] += added_mass
            nominator += added_mass * added_acidity

        # self.total_mass += self.total_mass
        self.initial_acidity_list[self.tank_name-1] = nominator / self.total_mass_list[self.tank_name-1]
        self.acidity_list = self.initial_acidity_list
        self.result_label = tk.Label(self.root, text="Acidity:", font=self.bold_font)
        self.result_label.place(relx=0.235, rely=0.42, anchor="center")

        self.result_label2 = tk.Label(self.root, text="Mass:", font=self.bold_font)
        self.result_label2.place(relx=0.235, rely=0.33, anchor="center")
        self.result_label.config(text=f"Acidity: {self.initial_acidity_list[self.tank_name-1]:.2f}",font= self.bold_font)
        self.result_label2.config(text=f"Mass: {self.total_mass_list[self.tank_name-1]:.2f}",font= self.bold_font)

        # Load data from the JSON file
        with open("data.json", "r") as json_file:
            existing_data = json.load(json_file)

        # Specify the tank you want to modify
        target_tank = str(self.tank_name)

        # Check if the target tank exists in the data
        if target_tank in existing_data:
            # Update the data for the target tank
            new_mass = self.total_mass_list[self.tank_name-1]  # New mass value
            new_acidity = self.initial_acidity_list[self.tank_name-1]  # New acidity value
            existing_data[target_tank]["mass"] = new_mass
            existing_data[target_tank]["acidity"] = new_acidity

            # Save the updated data back to the JSON file
            with open("data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            print(f"Data for {target_tank} has been updated.")
        else:
            print(f"{target_tank} not found in the loaded data.")

    def calculate_resulting_acidity(self):
        added_mass = float(self.added_mass_entry.get())
        added_acidity = float(self.added_acidity_entry.get())


        initial_mass = self.total_mass_list[self.tank_name-1]
        initial_acidity = self.initial_acidity_list[self.tank_name-1]
        self.total_mass_list[self.tank_name-1] += added_mass

        if  added_mass>0:
            resulting_acidity = (initial_acidity * initial_mass + added_mass * added_acidity) / self.total_mass_list[self.tank_name-1]
        else:
            resulting_acidity = initial_acidity


        self.acidity_list[self.tank_name-1] = resulting_acidity
        self.result_label.config(text=f"Acidity: {self.acidity_list[self.tank_name-1]:.2f}")
        self.result_label2.config(text=f"Mass: {self.total_mass_list[self.tank_name-1]:.2f}")

        with open("data.json", "r") as json_file:
            existing_data = json.load(json_file)

        # Specify the tank you want to modify
        target_tank = str(self.tank_name)

        # Check if the target tank exists in the data
        if target_tank in existing_data:
            # Update the data for the target tank
            new_mass = self.total_mass_list[self.tank_name-1]  # New mass value
            new_acidity = self.acidity_list[self.tank_name-1]  # New acidity value
            existing_data[target_tank]["mass"] = new_mass
            existing_data[target_tank]["acidity"] = new_acidity

            # Save the updated data back to the JSON file
            with open("data.json", "w") as json_file:
                json.dump(existing_data, json_file, indent=4)

            print(f"Data for {target_tank} has been updated.")
        else:
            print(f"{target_tank} not found in the loaded data.")

# ... (previous code)

    def create_third_page(self):
        third_page = tk.Frame(self.content_frame)

        self.added_mass_label = tk.Label(third_page, text="Added Mass:",font= self.bold_font)
        self.added_mass_label.pack()

        self.added_mass_entry = tk.Entry(third_page)
        self.added_mass_entry.pack()

        self.added_acidity_label = tk.Label(third_page, text="Added Acidity:",font= self.bold_font)
        self.added_acidity_label.pack()

        self.added_acidity_entry = tk.Entry(third_page)
        self.added_acidity_entry.pack()

        self.calculate_button = tk.Button(third_page, text="Calculate",bg='green', command=self.calculate_resulting_acidity,font= self.bold_font)
        self.calculate_button.pack()

        self.result_label = tk.Label(self.root, text="Acidity:", font=self.bold_font)
        self.result_label.place(relx=0.235, rely=0.42, anchor="center")

        self.result_label2 = tk.Label(self.root, text="Mass:", font=self.bold_font)
        self.result_label2.place(relx=0.235, rely=0.33, anchor="center")

        self.result_label.config(text=f"Acidity: {self.initial_acidity_list[self.tank_name - 1]:.2f}",
                                 font=self.bold_font)
        self.result_label2.config(text=f"Mass: {self.total_mass_list[self.tank_name - 1]:.2f}", font=self.bold_font)

        return third_page

    def go_to_third_page(self):

        self.pages[2] = self.create_third_page()
        self.hide_page(self.current_page)
        self.current_page = 2
        self.show_page(self.current_page)
        self.result_label.config(text=f"Acidity: {self.initial_acidity_list[self.tank_name-1]:.2f}")
        self.result_label2.config(text=f"Mass: {self.total_mass_list[self.tank_name-1]:.2f}")

    # ... (previous code)

if __name__ == "__main__":
    root = tk.Tk()
    app = AcidityCalculatorApp(root)
    root.mainloop()

