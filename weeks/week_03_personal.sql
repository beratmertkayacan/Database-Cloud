SELECT *
FROM departments;

SELECT *
FROM employees;

SELECT DEPARTMENT_ID, DEPARTMENT_NAME, LOCATION_ID + 300
FROM departments


SELECT last_name, salary, salary + 300
FROM   employees
LIMIT 5;

SELECT last_name "ax", salary AS yy
FROM employees;

SELECT DEPARTMENT_NAME "Dept"
FROM departments;


-- 20 SONRASI

SELECT CONCAT(last_name, job_id) AS employee -- birleştirmek için
FROM employees;

SELECT CONCAT(last_name, 'nin meslek idsi ', job_id) AS "Employee Details"
FROM employees;

SELECT COUNT(DISTINCT DEPARTMENT_ID)
FROM departments;

DESCRIBE departments;

SELECT first_name, last_name, job_id, salary*12 "Yearly Sal"
FROM employees;

-- 26 SONRASI

SELECT employee_id, last_name, job_id, department_id
FROM   employees
WHERE  department_id = 90;

select last_name,job_id,hire_date from employees where hire_date = "1987-08-12";

select last_name,job_id,hire_date from employees where last_name = "King";

select salary,last_name,job_id FROM employees where salary <= 3000;

select salary,last_name,job_id FROM employees where salary != 24000;

SELECT last_name, salary
FROM   employees
WHERE  salary BETWEEN 2500 AND 3500;

SELECT COUNT(*) FROM employees WHERE salary BETWEEN 3500 AND 2500;   -- 0
-- sınırları ters yazarsan hata değil, 0 satır döner

SELECT last_name, salary, employee_id, manager_id
FROM employees
WHERE salary IN (2400, 2500, 2600);

SELECT last_name, salary, manager_id, employee_id
FROM employees
WHERE last_name LIKE '____';

SELECT last_name
FROM   employees
WHERE  last_name LIKE '_o%';

SELECT last_name, manager_id
FROM employees
WHERE manager_id IS NULL;


SELECT employee_id, last_name, job_id, salary
FROM   employees
WHERE  salary >= 10000
AND    job_id LIKE '%MAN%';


SELECT employee_id, last_name, job_id, salary
FROM employees
WHERE salary >= 1000
OR job_id LIKE '%MAN%';

SELECT last_name, job_id
FROM   employees
WHERE  job_id NOT IN ('IT_PROG', 'ST_CLERK', 'SA_REP');


SELECT last_name, salary, department_id
FROM employees
WHERE salary >= 8000 AND department_id IN (50,80);

-- DERS 20.10.2026

SELECT department_id, department_name, location_id, city
FROM departments
NATURAL JOIN locations;

-- USING  ve WHERE aynı anda kullanılmaz

SELECT worker.last_name emp, manager.last_name mgr
FROM employees worker JOIN employees manager
ON (worker.manager_id = manager.employee_id);

SELECT e.last_name, e.salary, j.grade_level
FROM employees e JOIN job_grades j
ON e.salary BETWEEN j.lowest_sal AND j.highest_sal;

SELECT e.last_name, e.department_id, d.department_name
FROM employees e LEFT OUTER JOIN departments d
ON (e.department_id = d.department_id);

SELECT e.last_name, d.department_id, d.department_name
FROM employees e RIGHT OUTER JOIN departments d
ON (e.department_id = d.department_id);



SELECT last_name, department_name FROM employees CROSS JOIN departments;


SELECT last_name, salary
FROM employees
WHERE salary > (SELECT salary FROM employees WHERE last_name = 'Abel');


SELECT last_name, job_id, salary
FROM   employees
WHERE  job_id = (SELECT job_id FROM employees WHERE employee_id = 176)
AND    salary > (SELECT salary FROM employees WHERE employee_id = 176);


-- single row = multiple row subquery hata verir
SELECT employee_id, last_name
FROM   employees
WHERE  salary = (SELECT MIN(salary)
                 FROM   employees
                 GROUP BY department_id);


SELECT employee_id, last_name, job_id, salary
FROM   employees
WHERE  salary < ANY (SELECT salary FROM employees WHERE job_id = 'IT_PROG')
AND    job_id <> 'IT_PROG';

SELECT employee_id, last_name, job_id, salary
FROM   employees
WHERE salary < ALL (SELECT salary FROM employees WHERE job_id = 'IT_PROG')
AND   job_id <> 'IT_PROG';


SELECT * FROM departments
WHERE NOT EXISTS (SELECT * FROM employees
                  WHERE employees.department_id = departments.department_id);


SELECT emp.last_name
FROM   employees emp
WHERE  emp.employee_id NOT IN (SELECT mgr.manager_id FROM employees mgr);

SELECT salary, last_name
FROM employees
WHERE salary > (select avg(salary) from employees);


