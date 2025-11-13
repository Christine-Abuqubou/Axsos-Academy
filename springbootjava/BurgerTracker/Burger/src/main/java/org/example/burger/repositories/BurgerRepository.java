package org.example.burger.repositories;

import org.example.burger.models.Burger;
import org.springframework.data.repository.CrudRepository;



import org.springframework.stereotype.Repository;

@Repository
public interface BurgerRepository extends CrudRepository<Burger, Long> {

}

