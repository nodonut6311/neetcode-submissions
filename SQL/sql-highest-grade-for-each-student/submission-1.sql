SELECT student_id, exam_id, score
FROM exam_results e1
WHERE NOT EXISTS (
    SELECT 1
    FROM exam_results e2
    WHERE e2.student_id = e1.student_id
      AND e2.score > e1.score
)
AND NOT EXISTS (
    SELECT 1
    FROM exam_results e3
    WHERE e3.student_id = e1.student_id
      AND e3.score = e1.score
      AND e3.exam_id < e1.exam_id
)
ORDER BY student_id ASC;