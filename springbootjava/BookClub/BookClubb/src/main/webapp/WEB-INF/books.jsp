<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 21/11/2025
  Time: 2:42 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
    <title>All Books</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100">

<c:if test="${empty sessionScope.userId}">
    <c:redirect url="/" />
</c:if>

<div class="max-w-4xl mx-auto mt-10">

    <div class="flex justify-between items-center mb-6">
        <h1 class="text-3xl font-bold">Welcome, ${user.username}!</h1>
        <a href="/logout" class="text-red-600 underline">Logout</a>
    </div>

    <a href="/books/new" class="bg-blue-600 text-white px-4 py-2 rounded">Add Book</a>

    <div class="mt-6 bg-white p-6 rounded shadow">

        <table class="w-full">
            <thead>
            <tr class="border-b">
                <th class="p-2">Title</th>
                <th class="p-2">Added By</th>
            </tr>
            </thead>

            <tbody>
            <c:forEach items="${books}" var="b">
                <tr class="border-b">
                    <td class="p-2 text-blue-600 underline">
                        <a href="/books/${b.id}">${b.title}</a>
                    </td>
                    <td class="p-2">${b.user.username}</td>
                </tr>
            </c:forEach>
            </tbody>
        </table>

    </div>

</div>
</body>
</html>
