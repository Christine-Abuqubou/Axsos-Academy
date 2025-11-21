package org.example.bookclubb.repositories;


import org.example.bookclubb.models.User;
import org.springframework.data.jpa.repository.JpaRepository;


public interface UserRepository extends JpaRepository<User, Long> {
    boolean existsByEmail(String email);
    User findByEmail(String email);
}
