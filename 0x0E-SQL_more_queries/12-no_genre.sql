-- This script lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- Can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_shows.title, tsg.genre_id
	FROM tv_shows
	LEFT JOIN tv_show_genres AS tsg
	ON tv_shows.id = tsg.show_id
	WHERE tsg.genre_id IS NULL
	ORDER BY tv_shows.title ASC, tsg.genre_id ASC;
