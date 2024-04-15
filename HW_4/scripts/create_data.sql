
CREATE TABLE employee (
    id INTEGER,
    name VARCHAR,
    department VARCHAR,
    position VARCHAR,
    salary INTEGER
);
-- Вставка данных о сотрудниках
INSERT INTO employee (id, name, department, position, salary) VALUES
(1, 'John Doe', 'Sales', 'Manager', 60000),
(2, 'Jane Smith', 'Sales', 'Associate', 45000),
(3, 'Bob Johnson', 'Marketing', 'Director', 75000),
(4, 'Emily Brown', 'Marketing', 'Associate', 50000),
(5, 'Michael Lee', 'IT', 'Manager', 65000),
(6, 'Sarah Clark', 'IT', 'Developer', 55000),
(7, 'David Wang', 'IT', 'Developer', 55000),
(8, 'Lisa Kim', 'HR', 'Manager', 62000),
(9, 'Alex Chen', 'HR', 'Associate', 48000);

CREATE TABLE departments (
    id INTEGER,
    name VARCHAR,
    manager VARCHAR
);

INSERT INTO departments (id, name, manager) VALUES
(1, 'Sales', 1),
(2, 'Marketing', 3),
(3, 'IT', 5),
(4, 'HR', 8);

SELECT * FROM employee;

SELECT * FROM departments;