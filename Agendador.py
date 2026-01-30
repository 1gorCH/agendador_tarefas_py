import schedule  
import time  
import pandas as pd
import pyodbc 


def job():  
    server = 'DESKTOP-QTTENIF' 
    database = 'Python' 
    conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                        f'SERVER={server};'
                        f'DATABASE={database};'
                        'Trusted_Connection=yes;')

    cursor = conexaoDB.cursor()   # criando cursor de comando 

    dados = pd.read_excel(r"C:\Users\Gamer\OneDrive\Desktop\dio-git-e-github\Python Banco de Dados, ETL Avançado e Automação Web\Origem\Origem\arquivos_excel\Categoria.xlsx")
    str(dados.columns).replace("'","") 

    # faz carga no banco de dados
    for index, linha in dados.iterrows():
        
        cursor.execute("Insert into [Categoria](ID,Categoria)values(?,?)",linha['ID'],linha['Nome']) 
        
    conexaoDB.commit()   
    cursor.close() 
    conexaoDB.close() 
    
schedule.every(10).seconds.do(job) # escolher a frequencia 
while True: # loop contínuo
    schedule.run_pending()  # Executa tarefas agendadas que estão prontas para serem executadas
    time.sleep(1)  # Pausa por 1 segundo antes de verificar novamente as tarefas agendadas   


#para parar é só dar ctrl + c no terminal ou cmd


