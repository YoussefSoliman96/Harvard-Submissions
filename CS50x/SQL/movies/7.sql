write a SQL query to list all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically

SELECT title, rating, year FROM movies
JOIN ratings ON movies.id = ratings.movie_id
WHERE year = 2012
ORDER BY rating DESC, title ASC;