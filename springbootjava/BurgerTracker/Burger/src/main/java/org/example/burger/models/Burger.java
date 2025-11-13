package org.example.burger.models;



import jakarta.persistence.*;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;
import java.util.Date;

@Entity
@Table(name="burger")  // this will create a table called "burgers"
public class Burger {

    // ---------- Primary Key ----------
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    // ---------- Fields ----------
    @NotBlank(message="Burger name is required!")
    @Size(min=3, message="Name must be at least 3 characters")
    private String name;

    @NotBlank(message="Restaurant name is required!")
    private String restaurant;

    @NotBlank(message="Notes are required!")
    private String notes;

    private Integer rating;

    // ---------- Timestamps ----------
    @Column(updatable=false)
    private Date createdAt;
    private Date updatedAt;

    // ---------- Lifecycle Methods ----------
    @PrePersist
    protected void onCreate() {
        this.createdAt = new Date();
    }

    @PreUpdate
    protected void onUpdate() {
        this.updatedAt = new Date();
    }

    // ---------- Constructors ----------
    public Burger() {}

    // ---------- Getters & Setters ----------
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getRestaurant() { return restaurant; }
    public void setRestaurant(String restaurant) { this.restaurant = restaurant; }

    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }

    public Integer getRating() { return rating; }
    public void setRating(Integer rating) { this.rating = rating; }

    public Date getCreatedAt() { return createdAt; }
    public Date getUpdatedAt() { return updatedAt; }
}

