<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 11/11/2025
  Time: 6:44 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>${book.title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen flex flex-col items-center p-6">

<div class="w-full max-w-xl bg-white p-6 rounded shadow-md">
    <h1 class="text-3xl font-bold mb-4 text-indigo-600">${book.title}</h1>
    <p class="text-gray-700 mb-2"><strong>Description:</strong> ${book.description}</p>
    <p class="text-gray-700 mb-2"><strong>Language:</strong> ${book.language}</p>
    <p class="text-gray-700 mb-4"><strong>Number of Pages:</strong> ${book.numberOfPages}</p>
    <a href="/" class="inline-block bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700 transition">
        Back to all books
    </a>
</div>

</body>
</html>

