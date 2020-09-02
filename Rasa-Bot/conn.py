import sqlite3

conn = sqlite3.connect('docs.db')

conn.execute("create table if not exists doctors (doctor_name text, email text, city text)")

temp_str = "insert into doctors (doctor_name, email, city) values ('Dr.Parag Mehta', 'abc@xyz.com', 'Mumbai')"
conn.execute(temp_str)

temp_str = "insert into doctors (doctor_name, email, city) values ('Dr.Shyam Sharma', 'cde@xyz.com', 'Delhi')"
conn.execute(temp_str)

temp_str = "insert into doctors (doctor_name, email, city) values ('Dr.Mukesh Dave', 'efg@xyz.com', 'Ahmedabad')"
conn.execute(temp_str)

temp_str = "insert into doctors (doctor_name, email, city) values ('Dr.Rohit Mehra', 'hij@xyz.com', 'Mumbai')"
conn.execute(temp_str)

temp_str = "insert into doctors (doctor_name, email, city) values ('Dr.Krishna Iyer', 'klm@xyz.com', 'Bangalore')"
conn.execute(temp_str)

conn.commit()

content = conn.execute("select * from doctors")
for i in content:
    print(i)
