

select title,category.name,release_year from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id;

select title,category.name,release_year from film
join film_category on film.film_id = film_category.film_id
join category on film_category.category_id = category.category_id
where category.name in ('Action','Comedy','Family');