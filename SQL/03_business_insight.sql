-------------- BUSINESS INSIGHT SECTION
----- TREN PEREKRUTAN KARYAWAN -----
SELECT EXTRACT (YEAR FROM hire_date) AS tahun,
	COUNT(*) AS total_hire, 
	LAG(COUNT(*)) OVER (
	ORDER BY EXTRACT (YEAR FROM hire_date)) AS prev_hire,
	COUNT(*) - LAG(COUNT(*)) OVER (
	ORDER BY EXTRACT (YEAR FROM hire_date)) AS hire_growth
	FROM "sukma ramadhan".hrd
	GROUP BY tahun
	ORDER BY tahun

/*selama periode 2018-2025, terjadi terjadi kenaikan dan
penurunan yang cukup signifikan dari tahun sebelumnya
*/

----- TINGKAT TURNOVER PER DEPARTMENT -----
WITH resigned AS (
	SELECT department, COUNT(employee_id) AS total_resigned
	FROM "sukma ramadhan".hrd
	WHERE employment_status = 'Resigned'
	GROUP by department),
	total AS (
	SELECT department, COUNT(*) AS total_employee
	FROM "sukma ramadhan".hrd
	GROUP BY department)
SELECT t.department,
ROUND(COALESCE(r.total_resigned,0)*100.00/t.total_employee, 2) AS turnover_rate
FROM total t LEFT JOIN resigned r
ON t.department = r.department
ORDER BY turnover_rate DESC

/*Turnover tertinggi terjadi di Department Finance
*/

----- DISTRIBUSI GAJI KARYAWAN -----
WITH salary AS(
SELECT department,
	CASE 
		WHEN monthly_salary <= 5000000 THEN 'Low'
		WHEN monthly_salary <= 10000000 THEN 'Mid Low'
		WHEN monthly_salary <= 15000000 THEN 'Medium'
		WHEN monthly_salary <= 25000000 THEN 'Mid High'
		ELSE 'High'
	END AS salary_class
FROM "sukma ramadhan".hrd)
SELECT salary_class, COUNT(salary_class) AS total_employee
FROM salary
GROUP BY salary_class
ORDER BY total_employee

/* Persebaran salary didominasi oleh karyawan bergaji
tinggi*/

----- OVERTIME HOURS VS PERFORMANCE SCORE -----
WITH category AS(
SELECT employee_id, overtime_hours,
	CASE
		WHEN performance_score <= 3.0 THEN 'Low Perform'
		WHEN performance_score <= 4.0 THEN 'Medium Perform'
		ELSE 'High Perform'
	END AS performance
FROM "sukma ramadhan".hrd
WHERE performance_score IS NOT NULL)
SELECT performance, ROUND(AVG(overtime_hours),2) AS avg_overtime
FROM category
GROUP BY performance

SELECT ROUND(CORR(overtime_hours, performance_score)::NUMERIC,2) AS korelasi
FROM "sukma ramadhan".hrd
WHERE performance_score IS NOT NULL 

/*Korelasi yang terhubung antara overtime hours dan performance score
cenderung tidak ada*/

----- HIRE VS RESIGN -----
WITH resign AS (
	SELECT EXTRACT (YEAR FROM resignation_date) AS tahun,
	COUNT(resignation_date) AS resignation
	FROM "sukma ramadhan".hrd
	WHERE resignation_date < current_date
	GROUP BY tahun),
	hire AS (
	SELECT EXTRACT (YEAR FROM hire_date) AS tahun,
	COUNT(hire_date) AS hire
	FROM "sukma ramadhan".hrd
	GROUP BY tahun)
SELECT h.tahun, h.hire, r.resignation
FROM resign r FULL JOIN hire h
ON h.tahun = r.tahun
ORDER BY tahun 

----- SALARY VS SATISFACTION -----
WITH salary AS(
SELECT monthly_salary, ROUND(job_satisfaction,2) AS job_satisfaction,
	CASE 
		WHEN monthly_salary <= 5000000 THEN 'Low'
		WHEN monthly_salary <= 10000000 THEN 'Mid Low'
		WHEN monthly_salary <= 15000000 THEN 'Medium'
		WHEN monthly_salary <= 25000000 THEN 'Mid High'
		ELSE 'High'
	END AS salary_class
FROM "sukma ramadhan".hrd)
SELECT salary_class, ROUND(AVG(job_satisfaction),2)
FROM salary
GROUP BY salary_class

SELECT ROUND(CORR(job_satisfaction, monthly_salary)::NUMERIC,2) AS korelasi
FROM "sukma ramadhan".hrd

/*Korelasi antara gaji dengan job satisfaction cenderung 
sangat lemah
*/

----- TOP 5 EMPLOYEE PER DEPARTMENT-----
WITH top5 AS 
(SELECT department, employee_name, monthly_salary, performance_score, attendance_rate,
	RANK() OVER (
	PARTITION BY department
	ORDER BY performance_score DESC, attendance_rate DESC) AS ranking
FROM "sukma ramadhan".hrd
WHERE performance_score IS NOT NULL AND attendance_rate IS NOT NULL)
SELECT * FROM top5
WHERE ranking <= 5
