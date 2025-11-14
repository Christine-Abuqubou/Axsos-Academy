<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 14/11/2025
  Time: 2:23 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="jakarta.tags.core" prefix="c" %>
<%@ taglib uri="jakarta.tags.functions" prefix="fn" %>

<html>
<head>
    <title>Add New Dorm</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-6">
<h1 class="text-3xl font-bold mb-4">Add a New Dorm</h1>

<form action="/dorms" method="post" class="bg-white p-6 rounded shadow-md max-w-md">
    <label class="block mb-2">Dorm Name:</label>
    <input type="text" name="name" class="border px-3 py-2 w-full mb-4 rounded" required>

    <button type="submit" class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Create Dorm</button>
</form>

<a href="/dorms" class="block mt-4 text-blue-500 hover:underline">Back to Dorms</a>
</body>
</html>
