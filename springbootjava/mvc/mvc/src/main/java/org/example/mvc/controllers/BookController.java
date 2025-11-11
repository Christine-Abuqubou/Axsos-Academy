package org.example.mvc.controllers;

import jakarta.servlet.http.HttpSession;

import org.example.mvc.models.Book;
import org.example.mvc.services.BookService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;


@Controller
public class BookController {
    private static final Logger log = LoggerFactory.getLogger(BookController.class);
    @Autowired
    private BookService bookService;

    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("books", bookService.allBooks());
        return "index.jsp";
    }
    @PostMapping("/books")
    public String createBook(
            HttpSession session,
            @RequestParam("title") String title,
            @RequestParam("numberOfPages") int numberOfPages,
            @RequestParam("description") String description,
            @RequestParam("language") String language) {

        session.setAttribute("title", title);
        session.setAttribute("numberOfPages", numberOfPages);
        session.setAttribute("description", description);
        session.setAttribute("language", language);

        Book newBook = new Book(title, description, language, numberOfPages);
        bookService.createBook(newBook);
        return "redirect:/books/" + newBook.getId();



    }

    @GetMapping("/books/{id}")
    public String showBook(@PathVariable("id") Long id, Model model) {
        Book book = bookService.findBook(id);
        if (book == null) {
            model.addAttribute("message", "Book not found with id " + id);
            return "index.jsp";
        }
        model.addAttribute("book", book);
        return "show.jsp";
    }




}
