-- Quiz session

-- 1.Display employee_id, first_name, last_name and the yearly salary as “Annual Salary” for the first five employees.

SELECT employee_id,first_name,last_name,salary*12 AS "Annual Salary"
FROM employees
ORDER BY first_name
LIMIT 5;

-- 2.Show each employee’s name as “Last, First” under the heading “Full Name”.

SELECT CONCAT(last_name, ',', first_name) AS "Full Name"
FROM employees
ORDER BY employee_id;

-- 3.Which different job ids exist in department 80, and how many different job ids exist in the whole table?

SELECT DISTINCT job_id
FROM employees
WHERE department_id = 80;
SELECT COUNT(DISTINCT job_id) FROM employees;

-- 4.List the employees of department 50 earning between 3000 and 5000 (inclusive), highest salary first.

SELECT last_name, salary, employee_id
FROM employees
WHERE department_id = 50 AND salary BETWEEN 3000 AND 5000
ORDER BY salary DESC, last_name;

-- 5.Find last names that start with ‘K’ or end with ’n’.

SELECT last_name
FROM employees
WHERE last_name LIKE 'k%' OR last_name LIKE '%n';

-- 6.Show employees whose job is neither SA_REP nor ST_CLERK and who earn more than 12000.

SELECT job_id, last_name
FROM employees
WHERE job_id NOT IN ('SA_REP', 'ST_CLERK') AND salary > 12000;

