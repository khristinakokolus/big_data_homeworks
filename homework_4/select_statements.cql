

-- 1 select
SELECT review_body
FROM product_statistics
WHERE product_id = 'B002G54DAA'
ALLOW FILTERING;

-- 2 select
SELECT review_body
FROM product_statistics
WHERE product_id = 'B002G54DAA'
AND star_rating = 5
ALLOW FILTERING;

-- 3 select
SELECT review_body
FROM customer_statistics
WHERE customer_id = 43173394
ALLOW FILTERING;

-- 4 select
SELECT COUNT(product_id) AS products_reviews_count, product_id, product_title
FROM product_statistics
WHERE review_date <= '2015-08-31'
AND review_date >= '2014-08-31'
GROUP BY product_id
ALLOW FILTERING;

-- 5 select
SELECT COUNT(customer_id) AS customer_reviews_count, customer_id, verified_purchase
FROM customer_statistics
WHERE verified_purchase = 'Y'
AND review_date <= '2015-08-31'
AND review_date >= '2014-08-31'
GROUP BY customer_id
ALLOW FILTERING;


-- 6 select
SELECT COUNT(customer_id) AS hate_comments, customer_id
FROM haters_backers
WHERE review_date <= '2015-08-31'
AND review_date >= '2014-08-31'
AND star_rating <= 2
GROUP BY customer_id
ALLOW FILTERING;


-- 7 select
SELECT COUNT(customer_id) AS great_comments, customer_id
FROM haters_backers
WHERE review_date <= '2015-08-31'
AND review_date >= '2014-08-31'
AND star_rating >= 4
GROUP BY customer_id
ALLOW FILTERING;

