package org.example.bookclubb.controllers;

import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import org.example.bookclubb.models.LoginUser;
import org.example.bookclubb.models.User;
import org.example.bookclubb.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("newUser", new User());
        model.addAttribute("newLogin", new LoginUser());
        return "index";
    }

    @PostMapping("/register")
    public String register(
            @Valid @ModelAttribute("newUser") User newUser,
            BindingResult result,
            HttpSession session,
            Model model) {

        User registeredUser = userService.register(newUser, result);

        if (result.hasErrors()) {
            model.addAttribute("newLogin", new LoginUser());
            return "index";
        }

        session.setAttribute("userId", registeredUser.getId());
        return "redirect:/books";
    }

    @PostMapping("/login")
    public String login(
            @Valid @ModelAttribute("newLogin") LoginUser newLogin,
            BindingResult result,
            HttpSession session,
            Model model) {

        User loggedInUser = userService.login(newLogin, result);

        if (result.hasErrors()) {
            model.addAttribute("newUser", new User());
            return "index";
        }

        session.setAttribute("userId", loggedInUser.getId());
        return "redirect:/books";
    }

    @GetMapping("/logout")
    public String logout(HttpSession session) {
        session.invalidate();
        return "redirect:/";
    }
}
