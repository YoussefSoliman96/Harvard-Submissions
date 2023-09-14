write a SQL query to determine the average rating of all movies released in 2012.
SELECT AVG(rating) FROM movies JOIN ratings ON movies.id = (SELECT id FROM movies WHERE year = 2012);