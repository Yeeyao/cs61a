SELECT name FROM records WHERE supervisor = 'Oliver Warbucks';

SELECT * FROM records WHERE name = supervisor;

SELECT name FROM records WHERE salary > 50000 ORDER BY name DESC

SELECT m.day, m.time FROM records AS r, mettings AS m 
WHERE r.division = m.division AND supervisor = 'Oliver Warbucks';

SELECT a.division, b.division FROM records AS a, records AS b
WHERE a.supervisor = b.name AND a.division != b.division;

SELECT a.name, b.name FROM records AS a, records AS b, meemtings AS m1, meetings AS m2
WHERE a.division = m1.division AND b.division = m2.division AND
a.time = b.time AND a.day = b.day AND a.name < b.name;

SELECT supervisor, SUM(salary) FROM records GROUP BY supervisor;

SELECT m.day FROM meetings AS m, SUM(*) AS num FROM records AS r
WHERE m.division = r.division GROUP BY m.day HAVING num < 5;

SELECT a.division FROM records AS a, records AS b
WHERE a.name != b.name and a.division = b.division GROUP BY a.division HAVING
SUM(a.salary + b.salary) < 100000;

CREATE TABLE pnt AS
SELECT professor AS professor, course AS course, COUNT(*) AS times FROM courses GROUP BY processor, course;

SELECT a.professor, b.professor, a.course FROM pnt AS a, pnt AS b
WHERE a.course = b.course AND a.times =  b.times;

--- 注意这里的 group by
SELECT a.professor, b.professor, a.course FROM courese AS a, courese AS b
WHERE a.course = b.course AND a.semestere =  b.semestere AND a.professor < b.professor
GROUP BY a.coures, a.processor, b.processor HAVING COUNT(*) > 1;