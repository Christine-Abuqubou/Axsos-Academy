package org.example.burger.services;

import org.springframework.stereotype.Service;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.example.burger.models.Burger;
import org.example.burger.repositories.BurgerRepository;

@Service
public class BurgerService {

    @Autowired
    private BurgerRepository burgerRepo;

    public List<Burger> allBurgers() {
        return (List<Burger>) burgerRepo.findAll();
    }

    public Burger createBurger(Burger b) {
        return burgerRepo.save(b);
    }
}

