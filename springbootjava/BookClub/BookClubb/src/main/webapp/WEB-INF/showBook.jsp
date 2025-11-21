<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 21/11/2025
  Time: 2:43 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>


<!DOCTYPE html>
<html>
<head>
    <title>Book Details</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100">

<c:if test="${empty sessionScope.userId}">
    <c:redirect url="/" />
</c:if>

<div class="max-w-xl mx-auto mt-10 bg-white p-6 rounded shadow">

    <h1 class="text-3xl font-bold">${book.title}</h1>
    <p class="mt-3">${book.description}</p>
    <p class="text-gray-500 mt-2">Added by: ${book.user.username}</p>

    <a href="/books" class="text-blue-600 underline block mt-4">Back to Books</a>

    <c:if test="${book.user.id == sessionScope.userId}">
        <div class="mt-4 flex gap-4">
            <a href="/books/${book.id}/edit" class="bg-yellow-500 text-white px-4 py-2 rounded">Edit</a>

            <form action="/books/${book.id}/delete" method="post">
                <button class="bg-red-600 text-white px-4 py-2 rounded">Delete</button>
            </form>
        </div>
    </c:if>

</div>
</body>
</html>

