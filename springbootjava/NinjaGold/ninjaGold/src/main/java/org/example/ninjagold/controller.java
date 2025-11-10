package org.example.ninjagold;

import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.ArrayList;


@Controller
public class controller {

    @RequestMapping("/")
    public String index(HttpSession session) {
        if (session.getAttribute("gold") == null) {
            session.setAttribute("gold", 0);
        }
        if (session.getAttribute("log") == null) {
            session.setAttribute("log", "");
        }
        return "index.jsp";
    }

    @PostMapping("/process")
    public String process(@RequestParam("place") String place, HttpSession session) {
        // Initialize if missing
        if (session.getAttribute("gold") == null) session.setAttribute("gold", 0);
        if (session.getAttribute("log") == null) session.setAttribute("log", "");

        int gold = (int) session.getAttribute("gold");
        int goldChange = 0;

        if ("farm".equals(place)) {
            goldChange = (int)(Math.random() * 11) + 10;  // +10–20
        } else if ("cave".equals(place)) {
            goldChange = (int)(Math.random() * 6) + 5;    // +5–10
        } else if ("house".equals(place)) {
            goldChange = (int)(Math.random() * 4) + 2;    // +2–5
        } else if ("quest".equals(place)) {
            goldChange = (int)(Math.random() * 101) - 50; // -50–50
        }

        gold += goldChange;
        session.setAttribute("gold", gold);

        String message;
        if (goldChange >= 0) {
            message = "You earned " + goldChange + " gold from the " + place + "!";
        } else {
            message = "You lost " + Math.abs(goldChange) + " gold on a quest!";
        }

        String log = (String) session.getAttribute("log");
        log = message + "\n" + log;
        session.setAttribute("log", log);

        return "redirect:/";
    }
}


