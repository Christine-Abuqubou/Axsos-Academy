package org.example.dormsstudent.repositories;

import org.example.dormsstudent.models.Dorm;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface DormRepository extends JpaRepository<Dorm,Integer> {
}
