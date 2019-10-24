from pony import orm
import ipdb
import psycopg2

# Instantiate the database
db = orm.Database()


db.bind(provider='postgres', database='pony', user='postgres')

# Define Enities
# (Note that these classes inherit from db.Entity)
class Author(db.Entity):
    # Required fields (may not be null)
    # Note the argument is the data type
    first_name = orm.Required(str)
    last_name = orm.Required(str)

    # This line establishes a relationship between entities
    books = orm.Set('Book')



class Book(db.Entity):
    # Required field
    title = orm.Required(str)

    # Optional field (NULL is OK)
    num_pages = orm.Optional(int)

    # This defines the other half of the relationship between entities
    # (Note that the argument (data type) is the name of the other class)
    author = orm.Required(Author)


# AFTER all entities are defined, then generate mapping
# which creates tables for you
db.generate_mapping(create_tables=True)

# See this '@' symbol? This is a DECORATED function.
# That means it has some behind-the-scennes functionality
@orm.db_session
def load_data():

    jenny = Author(first_name='Jenny',
                   last_name='McIntosh')

    hope = Book(title='Hope Rises',
                author=jenny,
                num_pages=193)

    falcon = Book(title="Bud's Guide to Falconry",
                author=jenny,
                num_pages=47)


@orm.db_session
def inspect():

    # Pause for introspection
    ipdb.set_trace()
    1

    # Some code to run in the REPL
    #
    #   db.select('select * from author')
    #   (what is the data type retured?)
    #
    #
    #   books = orm.select(bb for bb in Book)
    #   (what is the data type returned?)
    #   (convert it to a list if you want to subscript it)
    #
    #
    #   books2 = orm.select(bb for bb in Book if 'Falcon' in bb.title)
    #   (how many objects returned?)


    # More things to try:
    #  1. Create a new author
    #
    #  2. Create a book by the new author

    #  3. call db.commit() to save your changes to the database


if __name__ == '__main__':
    load_data()
    inspect()



