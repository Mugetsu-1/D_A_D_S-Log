 SELECT *
 FROM film
WHERE NOT rental_duration = 5


SELECT *
FROM customer
WHERE first_name = 'Erica';


 SELECT email 
 FROM customer 
 WHERE first_name = 'Nancy' AND last_name = 'Thomas';

SELECT customer_id
 FROM payment
WHERE amount > 5
 ORDER BY customer_id DESC
 LIMIT 10;
