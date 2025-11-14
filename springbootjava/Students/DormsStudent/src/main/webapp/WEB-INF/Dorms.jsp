<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 14/11/2025
  Time: 2:22 pm
  To change this template use File | Settings | File Templates.
--%>

<%@ taglib uri="jakarta.tags.core" prefix="c" %>
<%@ taglib uri="jakarta.tags.functions" prefix="fn" %>

<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<html>
<head>
    <title>Dorms</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-6">
<h1 class="text-3xl font-bold mb-4">All Dorms</h1>

<a href="/dorms/new" class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">Add New Dorm</a>

<table class="mt-4 min-w-full border border-gray-300">
    <thead class="bg-gray-200">
    <tr>
        <th class="px-4 py-2 border">ID</th>
        <th class="px-4 py-2 border">Dorm Name</th>
        <th class="px-4 py-2 border">Action</th>
    </tr>
    </thead>
    <tbody>
    <c:forEach var="dorm" items="${dorms}">
        <tr class="hover:bg-gray-100">
            <td class="px-4 py-2 border">${dorm.id}</td>
            <td class="px-4 py-2 border">${dorm.name}</td>
            <td class="px-4 py-2 border">
                <a href="/dorms/${dorm.id}" class="text-blue-500 hover:underline">View</a>
            </td>
        </tr>
    </c:forEach>
    </tbody>
</table>
</body>
</html>
