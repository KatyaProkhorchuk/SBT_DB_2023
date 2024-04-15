-- Выборка с агрегацией и группировкой
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;

-- Подзапрос
SELECT name, department
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

