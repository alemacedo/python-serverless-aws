import db_connect

def getEmployees (nome):
    if nome == None or nome == '':
        print('Sem nome')
    else:
        
        myResult = db_connect.runQuery("SELECT * FROM employee_data", nome)
               
        for result in myResult:
            print(result)
        

getEmployees("Alexandre")