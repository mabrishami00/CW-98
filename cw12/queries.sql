

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

select customer.first_name,customer.last_name,film.title,(return_date - rental_date) as rental_duration
from customer
join rental on customer.customer_id = rental.customer_id
join inventory on rental.inventory_id = inventory.inventory_id
join film on inventory.film_id = film.film_id;

select title, length from film
where length > (select avg(length) from film);

select film.film_id, title, return_date from rental
join inventory on rental.inventory_id = inventory.inventory_id
join film on inventory.film_id = film.film_id
where return_date between '2005-05-29' and '2005-05-30';