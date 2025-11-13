package org.example.burger.controllers;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;
import org.example.burger.models.Burger;
import org.example.burger.services.BurgerService;

import jakarta.validation.Valid;

@Controller
public class BurgerController {

    @Autowired
    private BurgerService burgerService;

    @GetMapping("/")
    public String index(@ModelAttribute("burger") Burger burger, Model model) {
        model.addAttribute("burgers", burgerService.allBurgers());
        return "index.jsp";
    }

    @PostMapping("/burgers")
    public String create(@Valid @ModelAttribute("burger") Burger burger,
                         BindingResult result, Model model) {
        if (result.hasErrors()) {
            model.addAttribute("burgers", burgerService.allBurgers());
            return "index.jsp";
        }
        burgerService.createBurger(burger);
        return "redirect:/";
    }
    @GetMapping("/burgers/edit/{id}")
    public String editForm(@PathVariable("id") Long id, Model model) {
        Burger burger = burgerService.findBurger(id);
        model.addAttribute("burger", burger);
        return "edit.jsp";
    }

    // ---------- Process edit form ----------
    @PutMapping("/burgers/{id}")
    public String update(@Valid @ModelAttribute("burger") Burger burger,
                         BindingResult result) {
        if (result.hasErrors()) {
            return "edit.jsp";
        }
        burgerService.updateBurger(burger);
        return "redirect:/";
    }
}
