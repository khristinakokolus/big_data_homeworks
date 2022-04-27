USE reviews;

-- used ids from sample dataset
-- 1 select statement
SELECT review_body
FROM product_rating
WHERE product_id = 'B00EDBY7X8';

-- 2 select statement
SELECT review_body
FROM product_rating
WHERE product_id = 'B00EDBY7X8'
AND star_rating = 5;

-- 3 select statement
SELECT review_body
FROM customer_rating
WHERE customer_id = 18778586;

-- 4 select statement
SELECT customer_id
FROM customer_statistics
WHERE total_reviews_amount > N
AND product_ids CONTAINS 'B00EDBY7X8';

-- 5 select statement
SELECT COUNT(*)
FROM customer_rating
WHERE customer_id = 18778586
AND star_rating = 4
AND star_rating = 5;