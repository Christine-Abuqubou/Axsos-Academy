package org.example.dormsstudent.controllers;

import org.example.dormsstudent.models.Dorm;
import org.example.dormsstudent.models.Student;
import org.example.dormsstudent.services.DormService;
import org.example.dormsstudent.services.StudentService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller
public class StudentController {
    private final StudentService studentService;
    private final DormService dormService;

    public StudentController(StudentService studentService, DormService dormService) {
        this.studentService = studentService;
        this.dormService = dormService;
    }

    @GetMapping("/students/new")
    public String newStudent(@ModelAttribute Student student, Model model){
        List<Dorm> dorms=dormService.allDorm();
        model.addAttribute("dorms",dorms);
        return "NewStudent.jsp";

    }
    @PostMapping("/students")
    public String createStudent(@ModelAttribute Student student){
        studentService.createStudent(student);
        return "redirect:/students/new";
    }




}
