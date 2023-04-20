-- https://school.programmers.co.kr/learn/courses/30/lessons/131534

SELECT
    YEAR(sales_date) AS year,
    MONTH(sales_date) AS month,
    COUNT(DISTINCT(os.user_id)) AS purchased_users,
    ROUND(COUNT(DISTINCT(os.user_id)) / (SELECT COUNT(user_id) FROM user_info WHERE YEAR(joined) = 2021), 1) AS purchased_ratio
FROM online_sale os
INNER JOIN user_info ui
ON os.user_id = ui.user_id
WHERE YEAR(joined) = 2021
GROUP BY year, month
ORDER BY 1, 2
;
