package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
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
    @RequestMapping("/")
    public String ixndex(@RequestParam(value="name", required=false) String name,@RequestParam(value = "last_name", required = false) String lastName) {
        return "Hello " + name + " " + lastName;
    }



}

