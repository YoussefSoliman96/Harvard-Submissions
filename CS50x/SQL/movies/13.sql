write a SQL query to list the names of all people who starred in a movie in which Kevin Bacon also starred.

SELECT name FROM people
JOIN stars ON stars.movie_id = movies.id
JOIN movies ON movies.id = stars.movie_id
WHERE movies.id in
(SELECT movies.id FROM movies
JOIN stars ON stars.movie_id = movies.id
JOIN people ON people.id = stars.person_id
WHERE people.name = "Kevin Bacon")