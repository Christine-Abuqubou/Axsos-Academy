package org.example.dormsstudent.services;

import org.example.dormsstudent.models.Student;
import org.example.dormsstudent.repositories.DormRepository;
import org.example.dormsstudent.repositories.StudentRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class StudentService {
    private final StudentRepository studentRepo;
    public StudentService(StudentRepository studentRepo) {
        this.studentRepo = studentRepo;
    }
    public List<Student> allStudents(){
        return studentRepo.findAll();

    }
    public Student createStudent(Student student){
        return studentRepo.save(student);
    }
    public Student updateStudent(Student student){
        return studentRepo.save(student);
    }
    public void deleteStudentById(Integer id){
        studentRepo.deleteById(id);
    }
    public Student findStudent(Integer id){
        return studentRepo.findById(id).orElse(null);
    }
}
