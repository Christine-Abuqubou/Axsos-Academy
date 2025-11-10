package org.example.omikuji;

import jakarta.servlet.http.HttpSession;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller

public class controller {
    @RequestMapping("/omikuji")
    public String index() {
        return "index.jsp";
    }
   @PostMapping("/omikuji/process")
    public String processForm(HttpSession session,
                              @RequestParam("city") String city,
                              @RequestParam("number") int number,
                              @RequestParam("person") String person,
                              @RequestParam("hobby") String hobby,
                              @RequestParam("living") String living,
                              @RequestParam("compliment" )String compliment){
       session.setAttribute("city", city);
       session.setAttribute("number", number);
       session.setAttribute("person", person);
       session.setAttribute("hobby", hobby);
       session.setAttribute("living", living);
       session.setAttribute("compliment", compliment);
        return  "redirect:/omikuji/show";

   }
    @GetMapping("/omikuji/show")
    public String showResult() {
        return "view.jsp";
    }






   }




