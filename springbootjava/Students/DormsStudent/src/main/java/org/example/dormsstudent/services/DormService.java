package org.example.dormsstudent.services;

import org.example.dormsstudent.models.Dorm;
import org.example.dormsstudent.repositories.DormRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DormService {
    private final DormRepository dormRepo;
    public DormService(DormRepository repository) {
        this.dormRepo = repository;
    }

    public List<Dorm> allDorm(){
        return dormRepo.findAll();
    }

    public Dorm findDorm(Integer id){
        return dormRepo.findById(id).orElse(null);
    }

    public Dorm createDorm(Dorm dorm){
        return dormRepo.save(dorm);
    }


}
