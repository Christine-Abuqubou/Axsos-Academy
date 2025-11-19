package org.example.product.services;

import org.example.product.models.Category;
import org.example.product.repositories.CategoryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CategoryService {
    @Autowired
    private CategoryRepository categoryRepo;


    public Category saveCategory(Category category){
        return categoryRepo.save(category);
    }
    public Category findById(Long id){
        return categoryRepo.findById(id).orElse(null);
    }
    public List<Category> findAll(){
        return categoryRepo.findAll();
    }


    public Category getCategory(Long categoryId) {
        return categoryRepo.findById(categoryId).orElse(null);
    }
}
