-- https://school.programmers.co.kr/learn/courses/30/lessons/62284
WITH
tmp AS(
    SELECT id, cart_id, name
    FROM cart_products
    WHERE name IN ('Yogurt', 'Milk')
    GROUP BY cart_id, name
)
SELECT cart_id
FROM tmp
GROUP BY cart_id
HAVING count(cart_id) > 1
