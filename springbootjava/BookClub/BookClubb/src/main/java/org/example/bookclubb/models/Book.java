package org.example.bookclubb.models;



import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

import java.util.Date;

@Entity
@Table(name="books")
public class Book {

    @Id @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotBlank
    @Size(min = 2, message = "Title must be at least 2 characters")
    private String title;

    @NotBlank
    @Size(min = 5, message = "Description must be at least 5 characters")
    private String description;

    // User who added the book
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name="user_id")
    private User user;
    private Date createdAt;
    private Date updatedAt;


    @PrePersist
    protected void onCreate() {
        this.createdAt = new Date();
    }

    @PreUpdate
    protected void onUpdate() {
        this.updatedAt = new Date();
    }
    public Book(){

    }
    public Book(String title, String description, User user) {
        this.title = title;
        this.description = description;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    public Date getCreatedAt() {
        return createdAt;
    }



    public Date getUpdatedAt() {
        return updatedAt;
    }



// Getters/Setters
}
