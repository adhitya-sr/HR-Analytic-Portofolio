-------------- EDA SECTION
----- JUMLAH KARYAWAN -----
SELECT COUNT(DISTINCT employee_id) AS total_employee
FROM "sukma ramadhan".hrd

----- JUMLAH KARYAWAN AKTIF -----
SELECT COUNT(DISTINCT employee_id) AS total_active_employee
FROM "sukma ramadhan".hrd
WHERE employment_status = 'Active'

----- JUMLAH KARYAWAN RESIGNED -----
SELECT COUNT(DISTINCT employee_id) AS total_resigned_employee
FROM "sukma ramadhan".hrd
WHERE employment_status = 'Resigned'

----- ATTRITION RATE -----
SELECT 
ROUND((COUNT(CASE
	WHEN employment_status = 'Resigned'
	THEN 1
END)*100.0)/COUNT(*),2)
AS attrition_rate
FROM "sukma ramadhan".hrd

----- GAJI KESELURUHAN KARYAWAN AKTIF-----
SELECT SUM(monthly_salary) AS total_salary
FROM "sukma ramadhan".hrd
WHERE employment_status = 'Active'

----- DISTRIBUSI KARYAWAN PER GENDER ------
SELECT gender, 
ROUND(COUNT(*)*100.0/SUM(COUNT(*)) OVER(),2) AS percentage
FROM "sukma ramadhan".hrd
GROUP BY gender

----- DISTRIBUSI KARYAWAN PER REGIONAL -----
SELECT region, COUNT(*) AS total_employee
FROM "sukma ramadhan".hrd
GROUP BY region
ORDER BY total_employee DESC

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

----- RATA-RATA KEHADIRAN KARYAWAN -----
SELECT AVG(attendance_rate) AS average_attendance
FROM "sukma ramadhan".hrd
WHERE employment_status = 'Active'

----- RATA-RATA TINGKAT PERFORMA -----
SELECT AVG(performance_score) AS average_performance
FROM "sukma ramadhan".hrd
WHERE performance_score IS NOT NULL

----- TOTAL KARYAWAN PER DEPARTMENT -----
SELECT department, COUNT(*) AS total_employee
FROM "sukma ramadhan".hrd
WHERE employment_status = 'Active'
GROUP BY department
ORDER BY total_employee DESC

----- ATTRITION RATE PER DEPARTMENT-----
SELECT EXTRACT (YEAR FROM resignation_date) AS tahun,
COUNT(employee_id) AS total_resigned
FROM "sukma ramadhan".hrd
WHERE resignation_date < current_date AND resignation_date IS NOT NULL
GROUP BY tahun
ORDER BY tahun

----- TENURE KARYAWAN ------
SELECT department, ROUND(AVG(years_at_company),2) AS tenure
FROM "sukma ramadhan".hrd
GROUP BY department

----- TINGKAT KEHADIRAN KARYAWAN -----
SELECT department, ROUND(AVG(attendance_rate),2) AS average_attendance
FROM "sukma ramadhan".hrd
WHERE employment_status = 'Active'
GROUP BY department
ORDER BY average_attendance ASC

----- RATA-RATA JOB SATISFACTION -----
SELECT department, ROUND(AVG(job_satisfaction),2) AS average_satisfaction
FROM "sukma ramadhan".hrd
WHERE job_satisfaction IS NOT NULL
GROUP BY department
