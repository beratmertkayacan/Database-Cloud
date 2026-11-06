USE employees;

-- 1. Find the city of the employees in the IT department.
SELECT e.last_name, d.department_name, l.city
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
WHERE d.department_name = 'IT';

-- 2. Find the number of employees in each city and order in descending order.
SELECT l.city, COUNT(*) AS number_of_employees
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
GROUP BY l.city
ORDER BY number_of_employees DESC, l.city;

-- 3. Find the number of employees in each job title and order in descending order.
SELECT j.job_title, COUNT(*) AS number_of_employees
FROM employees e
JOIN jobs j ON e.job_id = j.job_id
GROUP BY j.job_title
ORDER BY number_of_employees DESC, j.job_title;

-- 4. Find the employees in UK and CANADA only.
SELECT CONCAT(e.first_name, ' ', e.last_name) AS full_name, l.city, c.country_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
JOIN countries c ON l.country_id = c.country_id
WHERE c.country_name IN ('United Kingdom', 'Canada');

-- 5. Find the average salary in every City.
SELECT l.city, ROUND(AVG(e.salary), 2) AS average_salary
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN locations l ON d.location_id = l.location_id
GROUP BY l.city
ORDER BY l.city;
