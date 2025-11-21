package org.example.bookclubb.models;



import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import org.springframework.format.annotation.DateTimeFormat;

import java.util.List;

@Entity
@Table(name="users")
public class User {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank
    @Size(min = 3, message = "Username must be at least 3 characters")
    private String username;

    @NotBlank
    @Email
    private String email;

    @NotBlank
    @Size(min = 8, message = "Password must be 8 characters or longer")
    private String password;

    @Transient
    private String confirmPassword;

    // Relationship
    @OneToMany(mappedBy = "user", cascade = CascadeType.ALL, fetch = FetchType.LAZY)
    private List<Book> books;

    public User() {}
    public User(String username, String email, String password) {
        this.username = username;
        this.email = email;
        this.password = password;

    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getConfirmPassword() {
        return confirmPassword;
    }

    public void setConfirmPassword(String confirmPassword) {
        this.confirmPassword = confirmPassword;
    }

    public List<Book> getBooks() {
        return books;
    }

    public void setBooks(List<Book> books) {
        this.books = books;
    }
    // Getters/Setters
}
