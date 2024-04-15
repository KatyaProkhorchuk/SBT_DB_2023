-- Создание таблицы
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name VARCHAR,
    department VARCHAR,
    salary DECIMAL
);

-- Вставка данных
INSERT INTO employees (id, name, department, salary)
VALUES (1, 'Иван', 'Engineering', 60000),
       (2, 'Александр', 'Marketing', 55000),
       (3, 'Василиса', 'Engineering', 62000);

-- Выборка данных
SELECT * FROM employees;


