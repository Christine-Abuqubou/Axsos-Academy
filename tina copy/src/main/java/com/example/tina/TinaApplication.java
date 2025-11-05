package com.example.tina;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import static org.springframework.boot.SpringApplication.*;

@SpringBootApplication
@RestController
public class TinaApplication {

    public static void main(String[] args) {
        run(TinaApplication.class, args);
    }
        @RequestMapping("/")
    public String index() {
        return "Hello World!";
        }

}
