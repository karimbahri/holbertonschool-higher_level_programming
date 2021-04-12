--  a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT tv_genres.name FROM tv_show
JOIN tv_show_genres ON tv_genres.show_id = tv_shows.id
JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;