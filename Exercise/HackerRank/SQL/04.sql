-- https://www.hackerrank.com/challenges/the-company/problem?isFullScreen=true

SELECT
    c.company_code,
    c.founder,
    COUNT(DISTINCT lead_manager_code),
    COUNT(DISTINCT senior_manager_code),
    COUNT(DISTINCT manager_code),
    COUNT(DISTINCT employee_code)
FROM company c
JOIN employee e
ON c.company_code = e.company_code
GROUP BY c.company_code, c.founder
ORDER BY 1
;
