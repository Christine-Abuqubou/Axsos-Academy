<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 11/11/2025
  Time: 1:26 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Books</title>
    <!-- Tailwind CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen flex flex-col items-center p-6">

<h1 class="text-4xl font-bold mb-6 text-indigo-600">Book Collection</h1>

<!-- Display message if exists -->
<c:if test="${not empty message}">
    <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
            ${message}
    </div>
</c:if>

<!-- List of books -->
<div class="w-full max-w-xl mb-8">
    <h2 class="text-2xl font-semibold mb-4 text-gray-700">All Books</h2>
    <c:if test="${not empty books}">
        <ul class="space-y-3">
            <c:forEach var="book" items="${books}">
                <li class="bg-white shadow-md rounded p-4 flex justify-between items-center hover:bg-indigo-50 transition">
                    <div>
                        <a href="/books/${book.id}" class="font-semibold text-indigo-600 hover:underline">
                                ${book.title}
                        </a>
                        <p class="text-gray-500 text-sm">${book.language} - ${book.numberOfPages} pages</p>
                    </div>
                    <span class="text-gray-400">→</span>
                </li>
            </c:forEach>
        </ul>
    </c:if>
    <c:if test="${empty books}">
        <p class="text-gray-500">No books added yet.</p>
    </c:if>
</div>

<!-- Add a book form -->
<div class="w-full max-w-xl bg-white p-6 rounded shadow-md">
    <h2 class="text-2xl font-semibold mb-4 text-gray-700">Add a Book</h2>
    <form action="/books" method="post" class="space-y-4">
        <div>
            <label class="block text-gray-700 font-medium mb-1">Title</label>
            <input type="text" name="title" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>
        <div>
            <label class="block text-gray-700 font-medium mb-1">Description</label>
            <input type="text" name="description" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>
        <div>
            <label class="block text-gray-700 font-medium mb-1">Language</label>
            <input type="text" name="language" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>
        <div>
            <label class="block text-gray-700 font-medium mb-1">Number of Pages</label>
            <input type="number" name="numberOfPages" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"/>
        </div>
        <button type="submit" class="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700 transition">
            Add Book
        </button>
    </form>
</div>

</body>
</html>
