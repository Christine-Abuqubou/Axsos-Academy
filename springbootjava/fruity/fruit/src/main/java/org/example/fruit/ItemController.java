package org.example.fruit;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.ArrayList;

@Controller
public class ItemController {



        @RequestMapping("/")
        public String index(Model model) {

            ArrayList<Item> fruits = new ArrayList<Item>();
            fruits.add(new Item("Kiwi", 1.50));
            fruits.add(new Item("Mango", 2.00));
            fruits.add(new Item("Goji Berries", 4.00));
            fruits.add(new Item("Guava", 0.75));

            // Add fruits to the model
            model.addAttribute("fruits", fruits);

            return "index.jsp";
        }
    }



