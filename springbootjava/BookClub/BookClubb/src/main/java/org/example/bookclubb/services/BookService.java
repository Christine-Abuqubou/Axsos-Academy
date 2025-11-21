package org.example.bookclubb.services;





import org.example.bookclubb.models.Book;
import org.example.bookclubb.repositories.BookRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class BookService {
    @Autowired
    private BookRepository bookRepo;

    public Book create(Book book) {
        return bookRepo.save(book);
    }

    public List<Book> all() {
        return bookRepo.findAll();
    }

    public Book find(Long id) {
        return bookRepo.findById(id).orElse(null);
    }

    public Book update(Book book) {
        return bookRepo.save(book);
    }

    public void delete(Long id) {
        bookRepo.deleteById(id);
    }
}

