# Agendador de Tarefas – ETL com Python

Este script realiza o **agendamento automático de uma carga de dados (ETL)** utilizando Python.  
A cada intervalo definido, ele lê um arquivo Excel e insere os dados em uma tabela do **SQL Server**.

## 🚀 Funcionalidades
- Agendamento de tarefas com a biblioteca `schedule`
- Leitura de dados a partir de arquivo **Excel**
- Inserção de dados em banco **SQL Server**
- Execução contínua em loop
- Finalização manual via terminal (`Ctrl + C`)

## 🛠️ Tecnologias Utilizadas
- Python
- Pandas
- PyODBC
- Schedule
- SQL Server
- Excel

## ⚙️ Como funciona
1. Conecta ao banco de dados SQL Server  
2. Lê o arquivo `Categoria.xlsx`  
3. Percorre as linhas do arquivo  
4. Insere os dados na tabela `Categoria`  
5. Executa o processo automaticamente a cada **10 segundos**

## ⏱️ Agendamento
```python
schedule.every(10).seconds.do(job)
