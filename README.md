# Instructions to run login.py are as follows:
1. If you don't already have SQL Server you can download it here: https://go.microsoft.com/fwlink/?linkid=866662

2. Once installed, proceed to restoring the DB. Information on how to do that can be found here: https://docs.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-a-database-backup-using-ssms?view=sql-server-ver15

3. The connection info in the main for both login.py and register.py need to be changed:
   The server needs to be changed to the name of your computer.
  ```mydb = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=NAME_OF_YOUR_COMPUTER_HERE;'
    'Database=Mydb;'
    'Trust_Connection=yes;')
  ```
5. After all of the above steps have been completed proceed to running login.py.
