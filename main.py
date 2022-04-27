import mysql.connector

def SQLCommandPrint(command):
    myCur = mydb.cursor()
    myCur.execute(command)

    for x in myCur:
        print(x)

def SQLCommand(command):
    myCur = mydb.cursor(buffered=True)
    myCur.execute(command)

    myCur.close()
    mydb.commit()
    return myCur

def viewTable(table, select):
    SQLCommandPrint("select " + select + " from " + table)

def count(table):
    myCur = SQLCommand("SELECT COUNT(*) FROM " + table + ";")
    rows = myCur.fetchall()

    s = str(rows[0])

    return int(s[1:len(s) - 2])

def getInfo(table, ID):
    myCur = SQLCommand("desc " + table)
    rows = myCur.fetchall()
    key = rows[0][0]

    myCur = SQLCommand("SELECT * FROM " + table + " where " + str(key) + " = " + str(ID))
    rows = myCur.fetchall()

    return rows[0]

#this gets all the columsn
def getCols(table):
    myCur = SQLCommand("desc " + table)
    rows = myCur.fetchall()
    cols = []
    for row in rows:
        cols.append(row[0])

    return cols

#this takes in table name and list of parameters as input, every column should be filled on signing up anyone, except IDs (Primary Keys)
#just start array from whatever is first (fname) or (lname) you can get a list of columns by running getCols(table)
#all items in vals should be string, the function automatically converts it to appropriate type
def insert(table, keys, vals):
    myCur = SQLCommand("desc " + table)
    rows = myCur.fetchall()
    key = rows[0][0]
    keys[key] += 1
    ID = keys[key]

    vals.insert(0, ID)

    rows.remove(rows[0])


    x = "" + str(ID)
    cols = "" + key


    for i in range(0, len(vals) - 1):

        if(str(rows[i][1]) != "b'int'"):
            x += ", \"" + str(vals[i + 1]) + "\""
        else:
            x += ", " + str(vals[i + 1])
        cols += ", " + rows[i][0]

    com = "insert into " + table + " (" + cols + ") values (" + x + ")"

    # print(com)
    SQLCommand(com)

def update(table, key, columnID, value):
    Pkey = getCols(table)[0]
    column = getCols(table)[columnID + 1]
    com = "update " + table + " set " + column + " = \"" + value + "\" where " + Pkey + " = " + str(key)

    # print(com)
    SQLCommand(com)

def delete(table, key):
    Pkey = getCols(table)[0]
    com = "delete from " + table + " where " + Pkey + " = " + str(key)

    # print(com)
    SQLCommand(com)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="gymmanagement"
)
