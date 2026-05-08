SELECT *FROM job_postings
LIMIT 10;

SELECT fraudulent,
       COUNT(*) AS total_jobs
FROM job_postings
GROUP BY fraudulent;

SELECT fraudulent,
       COUNT(*) AS total_jobs,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM job_postings),2) AS percentage
FROM job_postings
GROUP BY fraudulent;

SELECT employment_type,
       COUNT(*) AS total_jobs,
       SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) AS fake_jobs
FROM job_postings
GROUP BY employment_type
ORDER BY fake_jobs DESC;

SELECT employment_type,
       COUNT(*) AS total_jobs,
       SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) AS fake_jobs,
       ROUND(
           SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS fraud_percentage
FROM job_postings
GROUP BY employment_type
ORDER BY fraud_percentage DESC;

SELECT industry,
       COUNT(*) AS total_jobs,
       SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) AS fake_jobs,
       ROUND(
           SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS fraud_percentage
FROM job_postings
GROUP BY industry
HAVING total_jobs >= 20
ORDER BY fraud_percentage DESC
LIMIT 15;

SELECT job_function,
       COUNT(*) AS total_jobs,
       SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) AS fake_jobs,
       ROUND(
           SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS fraud_percentage
FROM job_postings
GROUP BY job_function
HAVING total_jobs >= 20
ORDER BY fraud_percentage DESC;

SELECT title,
       COUNT(*) AS occurrences
FROM job_postings
WHERE fraudulent = 1
GROUP BY title
ORDER BY occurrences DESC
LIMIT 15;

SELECT 
    SUM(CASE WHEN title LIKE '%Work From Home%' THEN 1 ELSE 0 END) AS work_from_home,
    SUM(CASE WHEN title LIKE '%Data Entry%' THEN 1 ELSE 0 END) AS data_entry,
    SUM(CASE WHEN title LIKE '%Urgent%' THEN 1 ELSE 0 END) AS urgent,
    SUM(CASE WHEN title LIKE '%Payroll%' THEN 1 ELSE 0 END) AS payroll
FROM job_postings
WHERE fraudulent = 1;

SELECT fraudulent,
       SUM(CASE WHEN title LIKE '%Data Entry%' THEN 1 ELSE 0 END) AS data_entry_jobs
FROM job_postings
GROUP BY fraudulent;

SELECT location,
       COUNT(*) AS total_jobs,
       SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) AS fake_jobs,
       ROUND(
           SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS fraud_percentage
FROM job_postings
GROUP BY location
HAVING total_jobs >= 20
ORDER BY fraud_percentage DESC
LIMIT 15;

CREATE VIEW vw_fraud_summary AS
SELECT fraudulent,
       COUNT(*) AS total_jobs,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM job_postings),2) AS percentage
FROM job_postings
GROUP BY fraudulent;

SELECT *
FROM vw_fraud_summary;

CREATE VIEW vw_employment_fraud AS
SELECT employment_type,
       COUNT(*) AS total_jobs,
       SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) AS fake_jobs,
       ROUND(
           SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS fraud_percentage
FROM job_postings
GROUP BY employment_type;

CREATE VIEW vw_industry_fraud AS
SELECT industry,
       COUNT(*) AS total_jobs,
       SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) AS fake_jobs,
       ROUND(
           SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS fraud_percentage
FROM job_postings
GROUP BY industry;

CREATE VIEW vw_function_fraud AS
SELECT job_function,
       COUNT(*) AS total_jobs,
       SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) AS fake_jobs,
       ROUND(
           SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS fraud_percentage
FROM job_postings
GROUP BY job_function;

CREATE VIEW vw_location_fraud AS
    SELECT 
        location,
        COUNT(*) AS total_jobs,
        SUM(CASE
            WHEN fraudulent = 1 THEN 1
            ELSE 0
        END) AS fake_jobs,
        ROUND(SUM(CASE
                    WHEN fraudulent = 1 THEN 1
                    ELSE 0
                END) * 100.0 / COUNT(*),
                2) AS fraud_percentage
    FROM
        job_postings
    GROUP BY location;
    
    CREATE VIEW vw_fake_title_patterns AS
SELECT title,
       COUNT(*) AS occurrences
FROM job_postings
WHERE fraudulent = 1
GROUP BY title;

CREATE VIEW vw_suspicious_keywords AS
SELECT 
    fraudulent,
    SUM(CASE WHEN title LIKE '%Data Entry%' THEN 1 ELSE 0 END) AS data_entry_jobs,
    SUM(CASE WHEN title LIKE '%Work From Home%' THEN 1 ELSE 0 END) AS work_from_home_jobs,
    SUM(CASE WHEN title LIKE '%Urgent%' THEN 1 ELSE 0 END) AS urgent_jobs,
    SUM(CASE WHEN title LIKE '%Payroll%' THEN 1 ELSE 0 END) AS payroll_jobs
FROM job_postings
GROUP BY fraudulent;


CREATE VIEW vw_executive_summary AS
SELECT 
    COUNT(*) AS total_jobs,
    SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) AS total_fake_jobs,
    SUM(CASE WHEN fraudulent = 0 THEN 1 ELSE 0 END) AS total_real_jobs,
    ROUND(SUM(CASE WHEN fraudulent = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS fake_percentage,
    COUNT(DISTINCT industry) AS total_industries,
    COUNT(DISTINCT job_function) AS total_functions,
    COUNT(DISTINCT employment_type) AS total_employment_types
FROM job_postings;


