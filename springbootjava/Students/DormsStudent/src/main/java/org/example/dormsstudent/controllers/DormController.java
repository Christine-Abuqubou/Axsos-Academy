package org.example.dormsstudent.controllers;

import org.example.dormsstudent.models.Dorm;
import org.example.dormsstudent.services.DormService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class DormController {
    private final DormService dormService;
    public DormController(DormService dormService){
        this.dormService = dormService;
    }
    @GetMapping("/dorms")
    public String dormList(Model model){
        model.addAttribute("dorms",dormService.allDorm());
        return "Dorms.jsp";

    }

    @GetMapping("/dorms/new")
    public String newDorm(@ModelAttribute Dorm dorm){
        return "NewDorms.jsp";
    }

    @PostMapping("/dorms")
    public String createDorm(@ModelAttribute Dorm dorm){
        dormService.createDorm(dorm);
        return "redirect:/dorms";
    }
    @GetMapping("/dorms/{id}")
    public String showDorm(@PathVariable Integer id, Model model){
        Dorm dorm=dormService.findDorm(id);
        model.addAttribute("dorm",dorm);
        return "WestWing.jsp";
    }

}
