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
    <title>${dorm.name} Details</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-6">
<h1 class="text-3xl font-bold mb-4">Dorm: ${dorm.name}</h1>

<a href="/dorms" class="text-blue-500 hover:underline mb-4 inline-block">Back to Dorms</a>

<h2 class="text-2xl font-semibold mt-4 mb-2">Students</h2>
<table class="min-w-full border border-gray-300">
    <thead class="bg-gray-200">
    <tr>
        <th class="px-4 py-2 border">First Name</th>
        <th class="px-4 py-2 border">Last Name</th>
        <th class="px-4 py-2 border">Age</th>
    </tr>
    </thead>
    <tbody>
    <c:forEach items="${dorm.students}" var="student">
        <tr class="hover:bg-gray-100">
            <td class="px-4 py-2 border">${student.firstName}</td>
            <td class="px-4 py-2 border">${student.lastName}</td>
            <td class="px-4 py-2 border">${student.age}</td>
        </tr>
    </c:forEach>
    </tbody>
</table>
</body>
</html>
