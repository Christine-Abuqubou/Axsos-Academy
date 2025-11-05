package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
    @RequestMapping("/kaiashok")
    public String index() {
        String s = "Hello World welcome!";
        return s;
    }
    @RequestMapping("/travel/{city}")
    public String travel(@PathVariable("city") String city, Model model) {
        String message = "Congratulations! You will soon travel to " + city + "!";


        model.addAttribute("message", message);


        return "result";
    }


    @RequestMapping("/ticket/{number}")
    public String ticket(@PathVariable("number") int number, Model model) {
        model.addAttribute("number", number);

        return "result";
    }



}

