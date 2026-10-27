.headers on
.mode column

.print 'DEFECT 1: Orphan maintenance jobs'
SELECT m.job_id, m.machine_name
FROM maint_job m
LEFT JOIN machine x ON m.machine_name = x.machine_name
WHERE x.machine_name IS NULL;

.print 'DEFECT 2: Duplicate part numbers'
SELECT part_no, COUNT(*) AS copies
FROM part
GROUP BY part_no
HAVING COUNT(*) > 1;

.print 'DEFECT 3: Text-based price comparison'
SELECT part_no, unit_price
FROM part
WHERE unit_price < '15';

.print 'DEFECT 4: Invalid installation date formats'
SELECT machine_name, installed
FROM machine
WHERE installed NOT GLOB
'[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]';

.print 'DEFECT 5: Joining jobs to comma-separated part lists'
SELECT j.job_id, p.description
FROM maint_job j
JOIN part p ON p.part_no = j.parts_used;