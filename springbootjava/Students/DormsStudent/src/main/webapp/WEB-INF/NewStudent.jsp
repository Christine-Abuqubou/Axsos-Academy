<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 14/11/2025
  Time: 2:23 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Add New Student</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-6">
<h1 class="text-3xl font-bold mb-4">Add a New Student</h1>

<form action="/students" method="post" class="bg-white p-6 rounded shadow-md max-w-md">
    <label class="block mb-2">First Name:</label>
    <input type="text" name="firstName" class="border px-3 py-2 w-full mb-4 rounded" required>

    <label class="block mb-2">Last Name:</label>
    <input type="text" name="lastName" class="border px-3 py-2 w-full mb-4 rounded" required>

    <label class="block mb-2">Age:</label>
    <input type="number" name="age" class="border px-3 py-2 w-full mb-4 rounded">

    <label class="block mb-2">Dorm:</label>
    <select name="dorm.id" class="border px-3 py-2 w-full mb-4 rounded" required>
        <option value="">--Select Dorm--</option>
        <c:forEach var="dorm" items="${dorms}">
            <option value="${dorm.id}">${dorm.name}</option>
        </c:forEach>
    </select>

    <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Create Student</button>
</form>

<a href="/students/new" class="block mt-4 text-blue-500 hover:underline">Back to Students</a>
</body>
</html>
