Make sure to keep these two files in the same folder 

CHANGES NEEDED TO MAKE after you fork the repo

    engine = create_engine('postgresql://youruser:yourpassword@localhost:5432/yourdatabase')
    
here , replace these user, password ...with your database information.

user = Your database username	

password = Your password for the DB user	

host = Where your database is hosted	localhost (or IP addr)

port = PostgreSQL default is 5432

database = Name of the database you want to access	

