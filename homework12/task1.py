"""
Using ORM framework of your choice, create models classes created in
Homework 6 (Teachers, Students, Homework and others). Target database
should be sqlite (filename main.db located in current directory). ORM
framework should support migrations.

Utilizing that framework capabilities, create a migration file, creating all
necessary database structures. A migration file (separate) creating at least
one record in each created database table.

(*) optional task: write standalone script (get_report.py) that retrieves
and stores the following information into CSV file report.csv.
For all done (completed) homeworks: Student name (who completed homework),
Creation date, Teacher name who created homework.

Utilize ORM capabilities as much as possible, avoiding executing raw SQL
queries.
"""
from homework12.create_records import fill_tables_with_data
from homework12.create_structures import create_tables

if __name__ == "__main__":
    create_tables()
    fill_tables_with_data()
