package org.example.product.services;

import org.example.product.models.Product;
import org.example.product.repositories.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProductService {
    @Autowired
    private ProductRepository productRepo;

    public Product saveProduct(Product product) {
        return productRepo.save(product);
    }

    public Product getProduct(Long id) {
        return productRepo.findById(id).orElse(null);
    }
    public List<Product> getAllProducts() {
        return productRepo.findAll();
    }


}
