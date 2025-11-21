package org.example.bookclubb.controllers;


import jakarta.servlet.http.HttpSession;
import jakarta.validation.Valid;
import org.example.bookclubb.models.Book;
import org.example.bookclubb.models.User;
import org.example.bookclubb.repositories.UserRepository;
import org.example.bookclubb.services.BookService;
import org.example.bookclubb.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/books")
public class BookController {

    @Autowired
    private BookService bookService;
    @Autowired
    private UserService userService;
    @Autowired
    private UserRepository userRepo;

    @GetMapping("")
    public String books(HttpSession session, Model model) {
        Long uid = (Long) session.getAttribute("userId");
        if (uid == null) return "redirect:/";
        User user = userService.findById(uid);
        model.addAttribute("user", user);
        model.addAttribute("books", bookService.all());
        return "books";
    }

    @GetMapping("/new")
    public String newBookForm(HttpSession session, Model model) {
        Long uid = (Long) session.getAttribute("userId");
        if (uid == null) return "redirect:/";
        model.addAttribute("book", new Book());
        return "addBook";
    }

    @PostMapping("/new")
    public String create(@Valid @ModelAttribute("book") Book book,
                         BindingResult result, HttpSession session) {

        Long uid = (Long) session.getAttribute("userId");
        if (uid == null) return "redirect:/";

        if (result.hasErrors()) return "addBook";

        User user = userService.findById(uid);
        book.setUser(user);
        bookService.create(book);
        return "redirect:/books";
    }

    @GetMapping("/{id}")
    public String show(@PathVariable Long id, Model model, HttpSession session) {
        Long uid = (Long) session.getAttribute("userId");
        if (uid == null) return "redirect:/";
        Book b = bookService.find(id);
        if (b == null) return "redirect:/books";
        model.addAttribute("book", b);
        return "showBook";
    }

    // Edit - only owner
    @GetMapping("/{id}/edit")
    public String editForm(@PathVariable Long id, Model model, HttpSession session) {
        Long uid = (Long) session.getAttribute("userId");
        if (uid == null) return "redirect:/";
        Book b = bookService.find(id);
        if (b == null) return "redirect:/books";
        if (!b.getUser().getId().equals(uid)) return "redirect:/books";
        model.addAttribute("book", b);
        return "addBook"; // reuse addBook.jsp for edit (it binds to book)
    }

    @PostMapping("/{id}/edit")
    public String edit(@PathVariable Long id, @Valid @ModelAttribute("book") Book book,
                       BindingResult result, HttpSession session) {
        Long uid = (Long) session.getAttribute("userId");
        if (uid == null) return "redirect:/";
        Book existing = bookService.find(id);
        if (existing == null) return "redirect:/books";
        if (!existing.getUser().getId().equals(uid)) return "redirect:/books";
        if (result.hasErrors()) return "addBook";
        existing.setTitle(book.getTitle());
        existing.setDescription(book.getDescription());
        bookService.update(existing);
        return "redirect:/books/" + id;
    }

    // Delete - only owner
    @PostMapping("/{id}/delete")
    public String delete(@PathVariable Long id, HttpSession session) {
        Long uid = (Long) session.getAttribute("userId");
        if (uid == null) return "redirect:/";
        Book b = bookService.find(id);
        if (b == null) return "redirect:/books";
        if (!b.getUser().getId().equals(uid)) return "redirect:/books";
        bookService.delete(id);
        return "redirect:/books";
    }
}
