

select title,category.name,release_year from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id;

select title,category.name,release_year from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where category.name in ('Action','Comedy','Family');

select category.name, count(*) as category_count from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
group by category.name;

select category.name, count(*) as category_count from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
group by category.name
having count(*) >= 60 and count(*) <= 68;

select title, language.name, category.name from film
join language on film.language_id = language.language_id
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id;

