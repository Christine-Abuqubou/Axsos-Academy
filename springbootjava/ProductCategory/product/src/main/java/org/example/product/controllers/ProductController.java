package org.example.product.controllers;

import org.example.product.models.Category;
import org.example.product.models.Product;
import org.example.product.services.CategoryService;
import org.example.product.services.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class ProductController {

    @Autowired
    private ProductService productService;

    @Autowired
    private CategoryService categoryService;


    // ================== HOME PAGE (LIST ALL) ==================
    @GetMapping("/")
    public String homePage(Model model){
        model.addAttribute("products", productService.getAllProducts());
        model.addAttribute("categories", categoryService.findAll());
        return "index";
    }



    // ================== CREATE PRODUCT ==================
    @GetMapping("/products/new")
    public String newProduct(@ModelAttribute("product") Product product) {
        return "newProduct";
    }

    @PostMapping("/products/new")
    public String createProduct(@ModelAttribute("product") Product product) {
        productService.saveProduct(product);
        return "redirect:/";
    }



    // ================== CREATE CATEGORY ==================
    @GetMapping("/categories/new")
    public String newCategory(@ModelAttribute("category") Category category) {
        return "newCategory";
    }

    @PostMapping("/categories/new")
    public String createCategory(@ModelAttribute("category") Category category) {
        categoryService.saveCategory(category);
        return "redirect:/";
    }



    // ================== SHOW PRODUCT & ADD CATEGORY ==================
    @GetMapping("/products/{id}")
    public String showProduct(@PathVariable("id") Long id, Model model) {

        Product product = productService.getProduct(id);

        model.addAttribute("product", product);
        model.addAttribute("categories", categoryService.findAll());
        model.addAttribute("assignedCategories", product.getCategories());

        return "productShow";
    }

    @PostMapping("/products/{productId}/addCategory")
    public String addCategoryToProduct(
            @PathVariable Long productId,
            @RequestParam Long categoryId
    ) {
        Product product = productService.getProduct(productId);
        Category category = categoryService.getCategory(categoryId);

        product.getCategories().add(category);
        productService.saveProduct(product);

        return "redirect:/products/" + productId;
    }



    // ================== SHOW CATEGORY & ADD PRODUCT ==================
    @GetMapping("/categories/{id}")
    public String showCategory(@PathVariable("id") Long id, Model model) {

        Category category = categoryService.getCategory(id);

        model.addAttribute("category", category);
        model.addAttribute("products", productService.getAllProducts());
        model.addAttribute("assignedProducts", category.getProducts());

        return "categoryShow";
    }

    @PostMapping("/categories/{categoryId}/addProduct")
    public String addProductToCategory(
            @PathVariable Long categoryId,
            @RequestParam Long productId
    ) {
        Category category = categoryService.getCategory(categoryId);
        Product product = productService.getProduct(productId);

        category.getProducts().add(product);
        categoryService.saveCategory(category);

        return "redirect:/categories/" + categoryId;
    }
}
