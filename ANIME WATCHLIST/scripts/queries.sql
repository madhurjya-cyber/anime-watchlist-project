-- lets practice some query before we move onto python

-- Query 1: Show All Anime
select title from Anime;

-- Query 2: Show All Users
select username from user;

-- Query 3: Show Completed Anime
select * from watchlist
where status = "completed";

-- Query 5: Show Top Rated Anime
select anime_id,rating from watchlist
order by rating desc; 

-- join concept 
select u.username,A.title,w.rating
from watchlist w
join user u on w.user_id=u.user_id
join anime a on w.anime_id=A.anime_id;

-- Average Rating
select avg(rating) from watchlist;

-- Number of Anime per Genre
select g.genre_name,
count(*) as total
from anime A
join genre g
on A.genre_id=g.genre_id
group by g.genre_name;

-- Highest Rated Anime
select A.title,w.rating
from watchlist w
inner join anime a on w.anime_id=A.anime_id;
