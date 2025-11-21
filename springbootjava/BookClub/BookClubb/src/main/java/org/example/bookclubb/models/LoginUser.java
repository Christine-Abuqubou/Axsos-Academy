package org.example.bookclubb.models;


import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public class LoginUser {

    @NotBlank
    @Email
    private String email;

    @NotBlank
    @Size(min = 8, message = "Password must be 8 characters")
    private String password;

    public LoginUser() {}
    public LoginUser(String email, String password) {
        this.email = email;
        this.password = password;
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
    // Getters/Setters
}
