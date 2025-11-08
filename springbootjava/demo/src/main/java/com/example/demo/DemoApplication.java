package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@SpringBootApplication
@RestController
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
    @RequestMapping("/")
    public String index() {
        return "Hello World!";
    }
    @RequestMapping("kaiashok")
    public String kaiashok() {
        return "Hello World! welcome Human";
    }
    @RequestMapping("/travel/{city}")
    public String travel(@PathVariable String city) {
        return " Congratulation u will soon travel to " + city+ "!";
    }
    @RequestMapping("/lotto/{number}")
    public String lotto(@PathVariable String number) {
        if  (number.length() % 2 == 0) {
            return "You will take a grand journey in the near future but be wary of tempting offers.";
        } else {
            return "You have enjoyed the fruits of your labor, but now is a great time to spend time with family and friends.";

        }


    }
    @GetMapping("/greeting")
    public String greeting(
            @RequestParam(value = "name", defaultValue = "human") String name,
            @RequestParam(value = "last_name", required = false) String lastName
    ) {
        String greeting = "Hello " + name;
        if (lastName != null && !lastName.isEmpty()) {
            greeting += " " + lastName;
        }
        return greeting;
    }

//    @Controller
//    @RequestMapping("/x")
//    public String index(Model model) {
//
//        String name = "Grace Hopper";
//        String itemName = "Copper wire";
//        double price = 5.25;
//        String description = "Metal strips, also an illustration of nanoseconds.";
//        String vendor = "Little Things Corner Store";
//
//        model.addAttribute("name", name);
//        model.addAttribute("itemName", itemName);
//        model.addAttribute("price", price);
//        model.addAttribute("description", description);
//        model.addAttribute("vendor", vendor);
//
//        // Your code here! Add values to the view model to be rendered
//
//        return "index.jsp";
//    }


}
