import pymysql
from tabulate import tabulate


class EMPLOYEEs:

    def detail(self):



        connection = pymysql.connect(host='localhost', user='root', password='Tiger@123')
        cursor = connection.cursor()


        cursor.execute('CREATE DATABASE IF NOT EXISTS Practice_link')
        cursor.execute('USE Practice_link')
        cursor.execute(
                'CREATE TABLE IF NOT EXISTS EMPLOYEE(ID INT PRIMARY KEY AUTO_INCREMENT , NAME VARCHAR(30), SALARY VARCHAR(30),DESIGNATION VARCHAR(30),JOINING_DATE VARCHAR(30))')

        print('\n'
              '1.Add the EMPLOYEE record\n'
              '2.Update the EMPLOYEE record\n'
              '3.Delete particular row\n'
              '4.Do you want to add column\n'
              '5.Do you want to rename the column\n'
              '6.Do you want to see the EMPLOYEE table\n'
              '7.Do you want to exit\n'
              '8.To delete particular column \n'
              '9.DO you want to perform a query operation\n')


        while True:
            detail=input('Enter the number which you prefer')

            if detail=='1':
                def add():

                    try:
                        name = input('Enter name ')
                        salary = input('Enter salary ')
                        designation = input('Enter designation ')
                        date = input('enter your date ')
                        cursor.execute(
                            'INSERT INTO EMPLOYEE (name, salary, designation, joining_date) VALUES (%s, %s, %s, %s)',
                            (name, salary, designation, date))
                        connection.commit()
                        print('The record is Added \n')
                    except Exception as e:
                        print(f'{e}')
                add()
                while True :
                    detail_s = input('Do you want to add another record (y/n)').lower()
                    if detail_s=='y':
                        add()
                    elif detail_s=='n':
                        obj.detail()
                    else:
                        print('Enter Properly (y/n) \n')
            elif detail=='2':
               def update():

                 try:
                     id_value = input('Enter the id to update particular record ')
                     cursor.execute('SELECT id FROM EMPLOYEE WHERE id=%s', (id_value,))
                     result = cursor.fetchone()

                     if result:
                         up_rec_value = input("Enter the column name : ")
                         if up_rec_value == 'id':
                             print('You cant modify the id')
                             update()
                         change_rec_value = input(f"Enter the new value for to update this {up_rec_value}: ")

                         cursor.execute(f'update EMPLOYEE set {up_rec_value}=%s where id=%s',
                                        (change_rec_value, id_value))
                         connection.commit()
                         print('The record is updated \n')
                     else:

                         print(f'Error, {id_value} is not present in database  \n')
                 except Exception as e:
                     print(f'{e}')

               update()
               while True:
                   detail_s = input('Do you want to update the record (y/n)').lower()
                   if detail_s == 'y':
                       update()
                   elif detail_s== 'n':
                        obj.detail()
                   else:
                    print('Enter Properly (y/n) \n')
            elif detail=='3':
                def delete():
                    try:
                        id_value = input('Enter the id,you want to delete ')
                        cursor.execute('SELECT id FROM EMPLOYEE WHERE id=%s', (id_value,))
                        result = cursor.fetchall()
                        results = cursor.fetchone()

                        if result:
                            cursor.execute('DELETE FROM EMPLOYEE WHERE id=%s', (id_value,))

                            conform = input('Are you sure you want to delete particular row (yes/no) \n').lower()
                            if conform == 'yes':
                                connection.commit()
                                print(f'The id {id_value}  is deleted successfully \n')
                            elif conform == 'no':
                                connection.rollback()
                                print(f'The id {id_value} is not deleted \n')
                            else:
                                print('Plz enter (yes/no) \n')

                        else:
                            print('ID not found in the database')
                    except Exception as e:
                        print(f'{e}')

                delete()
                while True:
                    detail_s = input('Do you want to delete another record (y/n) ').lower()
                    if detail_s == 'y':
                        delete()
                    elif detail_s == 'n':
                        obj.detail()
                    else:
                        print('Enter Properly (y/n) \n')
            elif detail=='4':
                def column_detail():
                   try:
                       colum_name = input('Enter the column name ')

                       column_type = input('Enter the datatype ')
                       cursor.execute(f'ALTER TABLE EMPLOYEE ADD COLUMN {colum_name} {column_type}')
                       connection.commit()

                       print('The record is added successfully \n')
                   except Exception as e:
                       print(f'{e}')
                column_detail()
                while True:
                    detail_s = input('Do you want to add another column (y/n) ').lower()
                    if detail_s == 'y':
                        column_detail()
                    elif detail_s == 'n':
                        obj.detail()
                    else:
                        print('Enter Properly (y/n) \n')
            elif detail=='5':
                def rename():
                    try:
                        colum_name = input('Enter the column name ')
                        new_colum_name = input('Enter the new column name ')
                        cursor.execute(f'ALTER TABLE EMPLOYEE RENAME COLUMN {colum_name} to {new_colum_name} ')
                        connection.commit()
                        print(f'The  {colum_name}  is  renamed \n')
                    except Exception as e:
                        print(f'{e}')
                rename()
                while True:
                    detail_s = input('Do you want to add another column (y/n) ').lower()
                    if detail_s == 'y':
                        rename()
                    elif detail_s == 'n':
                        obj.detail()
                    else:
                        print('Enter Properly (y/n) \n')
            elif detail=='6':

                   cursor.execute('select * from EMPLOYEE')
                   result = cursor.fetchall()
                   print("welcome to employee table")
                   # headers=[ 'ID' ,'NAME' , 'SALARY' , 'DESIGNATION' ,'JOINING_DATE']
                   print(tabulate(result, tablefmt="psql"))

            elif detail=='7':
                print('Your exiting \n')
                exit()
            elif detail == '8':
                def column_drop():
                   try:
                       colum_name = input('Enter the column name ')

                       cursor.execute(f'ALTER TABLE EMPLOYEE DROP COLUMN {colum_name} ')
                       connection.commit()
                       print(f'The id {colum_name}  is deleted successfully \n')
                   except Exception as e:
                       print(f'{e}')

                column_drop()
                while True:
                    detail_s = input('Do you want to add another column (y/n) ').lower()
                    if detail_s == 'y':
                        column_drop()
                    elif detail_s == 'n':
                        obj.detail()
                    else:
                        print('Enter Properly (y/n) \n')


            elif detail == '9':
              try:
                  detail_s = input('Do to perform query on database ')

                  cursor.execute(detail_s)
                  result = cursor.fetchall()

                  print('The accepting query')
                  print(tabulate(result,tablefmt="psql"))

              except Exception as e:
                  print(f'{e}')

            else:
                print('Enter above number properly')


obj=EMPLOYEEs()

def details():
    print('WELCOME TO THE EMPLOYEE TABLE \n ')
    while True:
        y_n=input('Do you want to do any modification in EMPLOYEE table(y/n) \n').lower()
        if y_n=='y':
            obj.detail()

        elif y_n=='n':
            print('Thank you for visiting')
            exit()

        else:
            print('please enter (y/n) properly')

details()