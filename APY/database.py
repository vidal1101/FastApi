from peewee  import *

Database = MySQLDatabase('peliculas',
                        user='root',
                        password='Runo1101',
                        host='localhost')


class User(Model):
    username = CharField(max_length=50)
    email = CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        database =Database
        table_name='Usuarios'