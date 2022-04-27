import main as m
import bcrypt as bc
import tkinter as tk

keys =	{
  'Mid': m.count('members'),
  'Did': m.count('dietplan'),
  'machine_id': m.count('equipments'),
  'tid': m.count('trainer'),
  'ManagerID': m.count('managers'),
  'wid': m.count('workout'),
  'wpid': m.count('workoutPlan')
}

def clear_frame():
   for widgets in page.winfo_children():
      widgets.destroy()

#                              the passwords
passwords = ["123", "123", "123"]
hashed = []

for password in passwords:
    password = password.encode('utf-8')
    temp = bc.hashpw(password, bc.gensalt(10))
    hashed.append(temp)

#checks password
def checkPass(password, i):
    t = bc.checkpw(password.encode('utf-8'), hashed[i])
    return t

#                               main menu
def menu():
    clear_frame()
    tk.Label(page, text = 'Main Menu', font = ("Arial", 25)).grid(row = 0)
    tk.Button(page, text = 'Manage Users', font = ("Arial", 18), command = checkPassUser).grid(row = 1)
    tk.Button(page, text = 'Manage Trainers', font = ("Arial", 18), command = checkPassTrainer).grid(row = 2)
    tk.Button(page, text = 'Manage Equipment', font = ("Arial", 18), command = checkPassEquip).grid(row = 3)

#                           basic view function
def enterIDtoView(i):
    clear_frame()
    target = ['Member', 'Trainer', 'Equipment']

    tk.Label(page, text = 'View ' + target[i] + ' with ID : ', font = ("Arial", 25)).grid(row = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: viewThem(i, temp.get())).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = menu).grid(columnspan = 2)

def viewThem(i, ID):
    clear_frame()
    target = ['Member', 'Trainer', 'Equipment']
    targetTable = ['members', 'trainer', 'equipments']

    attributes = []
    attributes.append(['First name', 'Last name', 'gender', 'Diet', 'Joining date', 'Address', 'Height', 'Weight', 'Age', 'Membership Type', 'Emergency Contact', 'Contact', 'Trainer', 'Workout Plan', 'Manager ID'])
    attributes.append(['First name', 'Last name', 'Contact', 'Manager ID'])
    attributes.append(['Workout Plan ID', 'Quantity', 'Machine', 'Date Of Purchase', 'Condition', 'Worker in charge'])

    tk.Label(page, text = 'View ' + target[i] + " with ID " + str(ID), font = ("Arial", 25)).grid(row = 0, columnspan = 2)

    atts = m.getInfo(targetTable[i], ID)

    for j in range(len(attributes[i])):
        tk.Label(page, text = attributes[i][j] + " : ", font = ("Arial", 18)).grid(row = j + 1, column = 0)
        tk.Label(page, text = atts[j + 1], font = ("Arial", 18)).grid(row = j + 1, column = 1)

    tk.Button(page, text = 'Back', font = ("Arial", 18), command = menu).grid(columnspan = 2)

#                             all member options
def checkPassUser():
    clear_frame()
    tk.Label(page, text = 'Manage Users', font = ("Arial", 25)).grid(row = 0)

    tk.Label(page, text = 'Enter Password', font = ("Arial", 18)).grid(row =1, column = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1, column = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: submitPassUser(temp.get())).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = menu).grid(columnspan = 2)

def submitPassUser(password):
    if(checkPass(password, 0)):
        manageUsers()
    else:
        checkPassUser()

def manageUsers():
    clear_frame()
    tk.Label(page, text = 'Manage Members', font = ("Arial", 25)).grid(row = 0)
    tk.Button(page, text = 'Add Member', font = ("Arial", 18), command = addUser).grid(row = 1)
    tk.Button(page, text = 'Modify Member', font = ("Arial", 18), command = modifyUser).grid(row = 2)
    tk.Button(page, text = 'Delete Member', font = ("Arial", 18), command = deleteUser).grid(row = 3)
    tk.Button(page, text = 'View Member info', font = ("Arial", 18), command = lambda : enterIDtoView(0)).grid(row = 4)


    tk.Label(page, text = '', font = ("Arial", 18)).grid(row = 4)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = menu).grid(row = 5)

# add user vvvvv
def addUser():
    atts = ['First name', 'Last name', 'gender', 'Diet', 'Joining date', 'Address', 'Height', 'Weight', 'Age', 'Membership Type', 'Emergency Contact', 'Contact', 'Trainer', 'Workout Plan', 'Manager']

    clear_frame()
    tk.Label(page, text = 'Add Member', font = ("Arial", 25)).grid(row = 0, columnspan = 2)

    entries = []

    n = len(atts)
    for i in range(0, n):
        tk.Label(page, text = atts[i], font = ("Arial", 18)).grid(row = i + 1, column = 0)

        temp = tk.StringVar()
        tk.Entry(page, textvariable = temp).grid(row = i + 1, column = 1)
        entries.append(temp)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: submitNewUser(entries)).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageUsers).grid(columnspan = 2)

def submitNewUser(entries):
    clear_frame()
    values = []
    for entry in entries:
        values.append(entry.get())
    m.insert("members", keys, values)

    tk.Label(page, text = 'Member Added', font = ("Arial", 25)).grid(columnspan = 2)
    tk.Button(page, text = 'Main Menu', font = ("Arial", 18), command = manageUsers).grid(columnspan = 2)
# add user ^^^^^

# modify user vvvvv
def modifyUser():
    atts = ['First name', 'Last name', 'gender', 'Diet', 'Joining date', 'Address', 'Height', 'Weight', 'Age', 'Membership Type', 'Emergency Contact', 'Contact', 'Trainer', 'Workout Plan', 'Manager']

    clear_frame()
    tk.Label(page, text = 'Modify Member', font = ("Arial", 25)).grid(row = 0, columnspan = 2)
    tk.Label(page, text = 'Choose Attribute', font = ("Arial", 25)).grid(row = 1, columnspan = 2)
    for i in range(len(atts)):
        tk.Button(page, text = atts[i], font = ("Arial", 14), command = lambda i = i: modifyAttrUser(atts, i)).grid(columnspan = 2)

    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageUsers).grid(columnspan = 2)

def modifyAttrUser(atts, i):
    clear_frame()
    tk.Label(page, text = 'enter new value for ' + atts[i], font = ("Arial", 18)).grid(row = 1, column = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1, column = 1)

    tk.Label(page, text = 'enter member ID', font = ("Arial", 18)).grid(row = 2, column = 0)
    temp2 = tk.StringVar()
    tk.Entry(page, textvariable = temp2).grid(row = 2, column = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: submitNewAttrUser(i, temp, temp2)).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = modifyUser).grid(columnspan = 2)

def submitNewAttrUser(attID, newAtt, ID):
    m.update("members", ID.get(), attID, newAtt.get())
    clear_frame()

    tk.Label(page, text = 'Attribute changed', font = ("Arial", 25)).grid(row = 1, column = 0)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageUsers).grid(columnspan = 2)
# modify user ^^^^^

# delete user vvvvv
def deleteUser():
    clear_frame()
    tk.Label(page, text = 'Delete Member', font = ("Arial", 25)).grid(row = 0, columnspan = 2)

    tk.Label(page, text = "Enter member ID", font = ("Arial", 18)).grid(row =  1, column = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1, column = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: deleteUserWithID(temp.get())).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageUsers).grid(columnspan = 2)

def deleteUserWithID(ID):
    m.delete("members", ID)
    clear_frame()

    tk.Label(page, text = 'Deleted Member with ID : ' + ID, font = ("Arial", 25)).grid(row = 1, column = 0)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageUsers).grid(columnspan = 2)
# delete user ^^^^^

#                              all trainer functions
def checkPassTrainer():
    clear_frame()
    tk.Label(page, text = 'Manage Trainers', font = ("Arial", 25)).grid(row = 0)

    tk.Label(page, text = 'Enter Password', font = ("Arial", 18)).grid(row =1, column = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1, column = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: submitPassTrainer(temp.get())).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = menu).grid(columnspan = 2)

def submitPassTrainer(password):
    if(checkPass(password, 1)):
        manageTrainers()
    else:
        checkPassTrainer()

def manageTrainers():
    clear_frame()
    tk.Label(page, text = 'Manage Trainers', font = ("Arial", 25)).grid(row = 0)
    tk.Button(page, text = 'Add Trainer', font = ("Arial", 18), command = addTrainer).grid(row = 1)
    tk.Button(page, text = 'Modify Trainer', font = ("Arial", 18), command = modifyTrainer).grid(row = 2)
    tk.Button(page, text = 'Delete Trainer', font = ("Arial", 18), command = deleteTrainer).grid(row = 3)
    tk.Button(page, text = 'View Trainer info', font = ("Arial", 18), command = lambda : enterIDtoView(1)).grid(row = 4)

    tk.Label(page, text = '', font = ("Arial", 18)).grid(row = 4)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = menu).grid(row = 5)

# add trainer vvvvv
def addTrainer():
    atts = ['First name', 'Last name', 'Contact', 'Manager']

    clear_frame()
    tk.Label(page, text = 'Add Trainer', font = ("Arial", 25)).grid(row = 0, columnspan = 2)

    entries = []

    n = len(atts)
    for i in range(0, n):
        tk.Label(page, text = atts[i], font = ("Arial", 18)).grid(row = i + 1, column = 0)

        temp = tk.StringVar()
        tk.Entry(page, textvariable = temp).grid(row = i + 1, column = 1)
        entries.append(temp)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: submitNewTrainer(entries)).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageTrainers).grid(columnspan = 2)

def submitNewTrainer(entries):
    clear_frame()
    values = []
    for entry in entries:
        values.append(entry.get())
    m.insert("trainer", keys, values)

    tk.Label(page, text = 'Trainer Added', font = ("Arial", 25)).grid(columnspan = 2)
    tk.Button(page, text = 'Main Menu', font = ("Arial", 18), command = manageTrainers).grid(columnspan = 2)
# add trainer ^^^^^

# modify trainer vvvvv
def modifyTrainer():
    atts = ['First name', 'Last name', 'Contact', 'Manager']

    clear_frame()
    tk.Label(page, text = 'Modify Trainer', font = ("Arial", 25)).grid(row = 0, columnspan = 2)
    tk.Label(page, text = 'Choose Attribute', font = ("Arial", 25)).grid(row = 1, columnspan = 2)
    for i in range(len(atts)):
        tk.Button(page, text = atts[i], font = ("Arial", 18), command = lambda i = i: modifyAttrTrainer(atts, i)).grid(columnspan = 2)

    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageTrainers).grid(columnspan = 2)

def modifyAttrTrainer(atts, i):
    clear_frame()
    tk.Label(page, text = 'enter new value for ' + atts[i], font = ("Arial", 18)).grid(row = 1, column = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1, column = 1)

    tk.Label(page, text = 'enter trainer ID', font = ("Arial", 18)).grid(row = 2, column = 0)
    temp2 = tk.StringVar()
    tk.Entry(page, textvariable = temp2).grid(row = 2, column = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: submitNewAttrTrainer(i, temp, temp2)).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = modifyTrainer).grid(columnspan = 2)

def submitNewAttrTrainer(attID, newAtt, ID):
    m.update("trainer", ID.get(), attID, newAtt.get())
    clear_frame()

    tk.Label(page, text = 'Attribute changed', font = ("Arial", 25)).grid(row = 1, column = 0)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageTrainers).grid(columnspan = 2)
# modify trainer ^^^^^

# delete trainer vvvvv
def deleteTrainer():
    clear_frame()
    tk.Label(page, text = 'Delete Trainer', font = ("Arial", 25)).grid(row = 0, columnspan = 2)

    tk.Label(page, text = "Enter Trainer ID", font = ("Arial", 18)).grid(row =  1, column = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1, column = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: deleteTrainerWithID(temp.get())).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageTrainers).grid(columnspan = 2)

def deleteTrainerWithID(ID):
    m.delete("trainer", ID)
    clear_frame()

    tk.Label(page, text = 'Deleted trainer with ID : ' + ID, font = ("Arial", 25)).grid(row = 1, column = 0)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageTrainers).grid(columnspan = 2)
# delete Trainer ^^^^^

#                              all Equipment functions
def checkPassEquip():
    clear_frame()
    tk.Label(page, text = 'Manage Equipment', font = ("Arial", 25)).grid(row = 0)

    tk.Label(page, text = 'Enter Password', font = ("Arial", 18)).grid(row =1, column = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1, column = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: submitPassEquip(temp.get())).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = menu).grid(columnspan = 2)

def submitPassEquip(password):
    if(checkPass(password, 2)):
        manageEquipments()
    else:
        checkPassEquip()

def manageEquipments():
    clear_frame()
    tk.Label(page, text = 'Manage The Equipment', font = ("Arial", 25)).grid(row = 0)
    tk.Button(page, text = 'Add Equipment', font = ("Arial", 18), command = addEquipment).grid(row = 1)
    tk.Button(page, text = 'Modify Equipment', font = ("Arial", 18), command = modifyEquipment).grid(row = 2)
    tk.Button(page, text = 'Delete Equipment', font = ("Arial", 18), command = deleteEquipment).grid(row = 3)
    tk.Button(page, text = 'View Equipment info', font = ("Arial", 18), command = lambda : enterIDtoView(2)).grid(row = 4)

    tk.Label(page, text = '', font = ("Arial", 18)).grid(row = 4)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = menu).grid(row = 5)

# add Equipment vvvvv
def addEquipment():
    atts = ['Workout Plan ID', 'Quantity', 'Machine', 'Date Of Purchase', 'Condition', 'Worker in charge']

    clear_frame()
    tk.Label(page, text = 'Add Equipment', font = ("Arial", 25)).grid(row = 0, columnspan = 2)

    entries = []

    n = len(atts)
    for i in range(0, n):
        tk.Label(page, text = atts[i], font = ("Arial", 18)).grid(row = i + 1, column = 0)

        temp = tk.StringVar()
        tk.Entry(page, textvariable = temp).grid(row = i + 1, column = 1)
        entries.append(temp)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: submitNewEquipments(entries)).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageEquipments).grid(columnspan = 2)

def submitNewEquipment(entries):
    clear_frame()
    values = []
    for entry in entries:
        values.append(entry.get())
    m.insert("equipments", keys, values)

    tk.Label(page, text = 'Equipment Added', font = ("Arial", 25)).grid(columnspan = 2)
    tk.Button(page, text = 'Main Menu', font = ("Arial", 18), command = manageEquipments).grid(columnspan = 2)
# add Equipment ^^^^^

# modify Equipment vvvvv
def modifyEquipment():
    atts = ['Workout Plan ID', 'Quantity', 'Machine', 'Date Of Purchase', 'Condition', 'Worker in charge']

    clear_frame()
    tk.Label(page, text = 'Modify Equipment', font = ("Arial", 25)).grid(row = 0, columnspan = 2)
    tk.Label(page, text = 'Choose Attribute', font = ("Arial", 25)).grid(row = 1, columnspan = 2)
    for i in range(len(atts)):
        tk.Button(page, text = atts[i], font = ("Arial", 18), command = lambda i = i: modifyAttrEquipments(atts, i)).grid(columnspan = 2)

    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageEquipments).grid(columnspan = 2)

def modifyAttrEquipments(atts, i):
    clear_frame()
    tk.Label(page, text = 'enter new value for ' + atts[i], font = ("Arial", 18)).grid(row = 1, column = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1, column = 1)

    tk.Label(page, text = 'enter equipment ID', font = ("Arial", 18)).grid(row = 2, column = 0)
    temp2 = tk.StringVar()
    tk.Entry(page, textvariable = temp2).grid(row = 2, column = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: submitNewAttrEquipments(i, temp, temp2)).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = modifyEquipment).grid(columnspan = 2)

def submitNewAttrEquipments(attID, newAtt, ID):
    m.update("equipments", ID.get(), attID, newAtt.get())
    clear_frame()

    tk.Label(page, text = 'Attribute changed', font = ("Arial", 25)).grid(row = 1, column = 0)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageEquipments).grid(columnspan = 2)
# modify Equipment ^^^^^

# delete Equipment vvvvv
def deleteEquipment():
    clear_frame()
    tk.Label(page, text = 'Delete Equipment', font = ("Arial", 25)).grid(row = 0, columnspan = 2)

    tk.Label(page, text = "Enter Equipment ID", font = ("Arial", 18)).grid(row =  1, column = 0)
    temp = tk.StringVar()
    tk.Entry(page, textvariable = temp).grid(row = 1, column = 1)

    tk.Button(page, text = 'Submit', font = ("Arial", 18), command = lambda: deleteEquipmentWithID(temp.get())).grid(columnspan = 2)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageEquipments).grid(columnspan = 2)

def deleteEquipmentWithID(ID):
    m.delete("equipments", ID)
    clear_frame()

    tk.Label(page, text = 'Deleted Equipment with ID : ' + ID, font = ("Arial", 25)).grid(row = 1, column = 0)
    tk.Button(page, text = 'Back', font = ("Arial", 18), command = manageEquipments).grid(columnspan = 2)
# delete Equipment ^^^^^

# this runs the final code
root = tk.Tk()
root.minsize(400, 400)
root.title('Gym Management System')

page = tk.Frame(root)
page.grid()

menu()

root.mainloop()
