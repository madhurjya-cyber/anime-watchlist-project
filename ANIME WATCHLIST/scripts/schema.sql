create database Anime_Database;
use  Anime_Database;

Create table genre(
genre_id int auto_increment primary key,
genre_name varchar(100) unique not null
);

Create table user(
user_id int auto_increment primary key,
username varchar(50) not null unique,
email varchar(100) not null unique
);

create table Anime(
anime_id int auto_increment primary key,
title varchar(100) not null,
episodes int not null,
release_year year,
genre_id int,
foreign key(genre_id) references genre(genre_id)
);

select * from watchlist;

create table watchlist(
watch_id int auto_increment primary key,
user_id int not null,
anime_id int not null,
status ENUM(
    'Watching',
    'Completed',
    'Dropped',
    'On Hold',
    'Plan to Watch'
) NOT NULL,
rating decimal(3,1),
foreign key(user_id) references user(user_id),
foreign key(anime_id) references Anime(anime_id)
);
drop table watchlist;
describe genre;
describe Anime;

insert into genre(genre_name) values
("Action"),
("Adventure"),
("Mystery"),
("Sports"),
("Fantasy");

insert into user(username,email) values
("Micheal","michealstark76@gmail.com"),
("Jason","jasonstark43@gmail.com00");

insert into Anime(title,episodes,release_year,genre_id) values
("One Piece","1165",1999,2),
("Fullmetal Alchemist","64",2009,1),
("Monster","74",2004,3),
("Haikyuu","85",2014,4),
("Naruto","720",2002,2);

insert into watchlist(user_id,anime_id,status,rating) values
(1,3,"completed",9.5),
(1,5,"watching",9.5),
(1,1,"Plan to watch",null),
(2,2,"completed",10),
(2,4,"completed",9.5),
(2,3,"completed",9.5);

select * from watchlist;

select u.username,A.title,w.status,w.rating	
from watchlist w
join user u on w.user_id=u.user_id
join Anime A on w.anime_id=A.anime_id;








