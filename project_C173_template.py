from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
root = Tk()
root.geometry("900x500")

label_selected_doctor=Label(root)
label_selected_doctor.place(relx=0.01, rely=0.3,anchor=W)

label_selected_IT=Label(root)
label_selected_IT.place(relx=0.01, rely=0.6,anchor=W)

label_selected_chemical=Label(root)
label_selected_chemical.place(relx=0.01, rely=0.9,anchor=W)

class parent():
    def __init__(self):
        print("This is parent class")
    def doctor(doctor_name):
        #create a list, add the hospital names inside it
        hospital_list = ["advocate condel","Lutheran","northshore"]
        #create variable for random number generation random.randint(0,3)
        random_hospital = random.randint(0,2)
        label_selected_doctor['text'] = doctor_name+" has been alloted to "+hospital_list[random_hospital]
        
        
    def softwareEngineer(it_professional_name):
        #add IT company names inside the list
        IT_company_list = ["cognizant","Capgemini","tcs"]
        #generate random number for number of IT companies listed
        random_IT_company = random.randint(0,2)
        
        #generate the text on the label_selected_IT, as it_professional_name has been allotted to the IT_company_list[random_IT_company]
        label_selected_IT['text'] = it_professional_name+" Has been alloted to "+IT_company_list[random_IT_company]
        
        
    def chemicalEngineer(chemical_engineer_name):
        #add chemical engineering company names like "Air Liquide", "BASF", "Albemarle Corporation", "DuPont"
        company_list = ["Air liquide","BASF", "Albemarle Corporation"]
        random_company = random.randint(0,2)
        label_selected_chemical['text'] = chemical_engineer_name+" has been alloted to "+company_list[random_company]



class child1(parent):
    def __init__(self):
        print("This is child1 class")
        
    def getDoctor(self):
        #pass a name, example "Yusuf"
        name = "Yusuf"
        #call the function doctor of the class parent, pass the variable name to it
        parent.doctor(name)
        
class child2(parent):
    def __init__(self):
        print("This is child2 class")
        
        
    def getIT(self):
        #pass a name, example "Yusuf"
        name = "Michael"
        #call the function softwareEngineer of the class parent, pass the variable name to it
        parent.softwareEngineer(name)
        
        
        
class child3(parent):
    def __init__(self):
        print("This is child3 class")
    def getChemical(self):
        #pass a name, example "Yusuf"
        name = "Noah"
        #call the function chemicalEngineer of the class parent, pass the variable name to it
        parent.chemicalEngineer(name)
        
        
        
#create object for child2 and 3        
obj1 = child1()
obj2 = child2()
obj3 = child3()


btn_doctor = Button(root, text="Show the hospital alloted", command=obj1.getDoctor)
btn_doctor.place(relx=0.1, rely=0.23,anchor=CENTER)

btn_it = Button(root, text="Show the IT company alloted", command=obj2.getIT)
btn_it.place(relx=0.11, rely=0.53,anchor=CENTER)

btn_chemical = Button(root, text="Show the chemical company alloted", command=obj3.getChemical)
btn_chemical.place(relx=0.13, rely=0.83,anchor=CENTER)

root.mainloop()