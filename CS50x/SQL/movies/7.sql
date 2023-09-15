write a SQL query to list all movies released in 2010 and their ratings, in descending order by rating. For movies with the same rating, order them alphabetically

SELECT title, rating FROM movies
JOIN ratings ON ratings.movie_id = movies.id
JOIN movies ON movies.id = ratings.movies_id
WHERE year = 2012
ORDER BY rating DESC, title ASC;