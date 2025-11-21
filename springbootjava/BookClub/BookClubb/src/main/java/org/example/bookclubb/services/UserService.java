package org.example.bookclubb.services;



import org.example.bookclubb.models.LoginUser;
import org.example.bookclubb.models.User;
import org.example.bookclubb.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;

import java.util.Optional;

@Service
public class UserService {

    private final UserRepository userRepo;
    private final BCryptPasswordEncoder bCrypt;

    @Autowired
    public UserService(UserRepository userRepo) {
        this.userRepo = userRepo;
        this.bCrypt = new BCryptPasswordEncoder();
    }

    public User register(User newUser, BindingResult result) {
        if (userRepo.existsByEmail(newUser.getEmail())) {
            result.rejectValue("email", "Exists", "Email already registered");
        }

        if (newUser.getPassword() == null || !newUser.getPassword().equals(newUser.getConfirmPassword())) {
            result.rejectValue("confirmPassword", "Match", "Passwords must match");
        }

        if (result.hasErrors()) return null;

        // hash and save
        newUser.setPassword(bCrypt.encode(newUser.getPassword()));
        newUser.setConfirmPassword(null);
        return userRepo.save(newUser);
    }

    public User login(LoginUser loginUser, BindingResult result) {
        Optional<User> opt = Optional.ofNullable(userRepo.findByEmail(loginUser.getEmail()));
        if (opt.isEmpty()) {
            result.rejectValue("email", "NotFound", "Email not registered");
            return null;
        }
        User user = opt.get();
        if (!bCrypt.matches(loginUser.getPassword(), user.getPassword())) {
            result.rejectValue("password", "Invalid", "Invalid password");
            return null;
        }
        return user;
    }

    public User findById(Long id) {
        return userRepo.findById(id).orElse(null);
    }
}
