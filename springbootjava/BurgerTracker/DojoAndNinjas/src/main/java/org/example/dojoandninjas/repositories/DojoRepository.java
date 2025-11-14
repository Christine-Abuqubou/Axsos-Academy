package org.example.dojoandninjas.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface Dojo extends CrudRepository<Dojo, Long>  {
    List<Dojo> findAll();
}
