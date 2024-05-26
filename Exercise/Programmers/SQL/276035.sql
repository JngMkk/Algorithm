WITH TMP AS (
    SELECT
        BIT_OR(CODE) AS CODE
    FROM
        SKILLCODES
    WHERE
        CATEGORY = 'Front End'
)

SELECT
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS
WHERE
    SKILL_CODE & (SELECT CODE FROM TMP) > 0
ORDER BY
    1
;

-- -------------------------------------------------------------------

SELECT DISTINCT
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS
JOIN
    SKILLCODES
ON
    SKILL_CODE & CODE != 0
WHERE
    CATEGORY = 'Front End'
ORDER BY
    1
;
