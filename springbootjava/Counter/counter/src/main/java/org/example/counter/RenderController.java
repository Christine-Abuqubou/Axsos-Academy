package org.example.counter;

import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class RenderController {
    @RequestMapping("/")
    public String index(HttpSession session , Model model) {
        Integer counter = (Integer) session.getAttribute("counter");
        if (counter == null) {
            counter = 0;
        }
        counter++;
        session.setAttribute("counter", counter);


        model.addAttribute("counter", counter);

        return "index.jsp";
    }

    @RequestMapping("/counter")
    public String counter(HttpSession session , Model model) {
        Integer counter = (Integer) session.getAttribute("counter");
        if (counter == null) {
            counter = 0;
            session.setAttribute("counter", counter);
        }

        model.addAttribute("counter", counter);
        return "links.jsp";
    }



}
