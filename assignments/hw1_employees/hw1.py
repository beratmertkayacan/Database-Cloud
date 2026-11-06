from mysql import connector

# 1) Veritabanına bağlan
my_connection = connector.connect(
    host="localhost", user="root", password="YOUR_PASSWORD", database="employees"
)

# 2) Sorgu göndermek için cursor aç
my_cursor = my_connection.cursor()


"""
1. Find the city of the employees in the IT department.
"""
# 3) Sorgu SQL'lerini MySQL'e gönder
my_cursor.execute("""
SELECT e.last_name, d.department_name, l.city
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE d.department_name = 'IT';
""")

# 4) Sonuçları ekrana yazdırma
print("{:10} {:10} {:10}".format("Last Name", "Department", "city"))
for row in my_cursor:
    print(f"{row[0]:40} {row[1]:40} {row[2]:<4}")


"""
2. Find the number of employees in each city and order in descending order.
"""
my_cursor.execute("""
SELECT l.city, COUNT(*) AS number_of_employees
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
GROUP BY l.city
ORDER BY number_of_employees DESC, l.city;
""")

print("{:24} {:16}".format("City ", "Number of Employees"))
for row in my_cursor:
    print(f"{row[0]:24} {row[1]:<16}")


"""
3. Find the number of employees in each job title and order in descending order.
"""
my_cursor.execute("""
SELECT j.job_title, COUNT(*) AS number_of_employees
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title
ORDER BY number_of_employees DESC, j.job_title;
""")

print("{:24} {:16} ".format("Job Title", "Number employees"))
for row in my_cursor:
    print(f"{row[0]:24} {row[1]:<16} ")


"""
4. Find the employees in UK and CANADA only.
"""
my_cursor.execute("""
SELECT CONCAT(e.first_name, ' ', e.last_name) AS full_name, l.city, c.country_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
JOIN countries c ON l.country_id = c.country_id
WHERE c.country_name IN ('United Kingdom', 'Canada');
""")

print("{:32} {:4} {:100}".format("first name + Last Name", "City", "country"))
for row in my_cursor:
    print(f"{row[0]:32} {row[1]:4} {row[2]:<100}")


"""
5. Find the average salary in every City.
"""
my_cursor.execute("""
SELECT l.city, ROUND(AVG(e.salary), 2) AS average_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
GROUP BY l.city
ORDER BY l.city;
""")

print("{:32} {:4}".format("City", "Average Salary"))
for row in my_cursor:
    print(f"{row[0]:32} {row[1]:<4}")
