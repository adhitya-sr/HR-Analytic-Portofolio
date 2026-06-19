--------- CLEANING SECTION
----- CEK NULL -----
SELECT *
FROM "sukma ramadhan".hrd
WHERE performance_score IS NULL

/*Pada kolom performace score, ada beberapa employee yang
memiliki nilai NULL, kemungkinan manajemen belum memasukkan 
nilai pada database*/

/*Pada kolom attendance rate, ada beberapa employee juga yang
memilii nilai NULL, kemungkinan manajemen juga belum memasukkan
nilai pada databse*/

----- CEK DUPLIKAT -----
SELECT employee_id, COUNT(employee_id) AS data_employee
FROM "sukma ramadhan".hrd
GROUP BY employee_id
HAVING COUNT(employee_id) > 1

WITH duplicate AS (SELECT ctid, employee_id, ROW_NUMBER() OVER(
	PARTITION BY employee_id
	ORDER BY ctid) AS rn
FROM "sukma ramadhan".hrd)
DELETE FROM "sukma ramadhan".hrd
WHERE ctid IN(
	SELECT ctid
	FROM duplicate
	WHERE RN > 1)

/* Ada 47 data yang terduplikat, hingga menyisakan
5873 data unik */

----- UBAH PK -----
ALTER TABLE "sukma ramadhan".hrd
ADD PRIMARY KEY (employee_id)

----- VALIDASI DATA TANGGAL ----
SELECT *
FROM "sukma ramadhan".hrd
WHERE hire_date > resignation_date 

SELECT *
FROM "sukma ramadhan".hrd
WHERE resignation_date > current_date

SELECT *
FROM "sukma ramadhan".hrd
WHERE employment_status = 'Resigned' AND resignation_date > current_date

/* Sebanyak 341 data menunjukkan employment status 'Resigned',
namun resignation date terjadi di masa depan. Data perlu di 
crosscheck, apakah ada kesalahan database atau keputusan perusahaan */

----- CEK MISSTYPE DATA -----
SELECT DISTINCT region
FROM "sukma ramadhan".hrd

UPDATE "sukma ramadhan".hrd SET region = 'Jakarta'
WHERE region = 'Jakrta'

----- CEK CLEANED DATA -----
SELECT * FROM "sukma ramadhan".hrd