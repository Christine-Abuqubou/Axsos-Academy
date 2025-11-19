<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 19/11/2025
  Time: 3:20 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Product Details</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-10">

<h1 class="text-3xl font-bold mb-4 text-blue-700">${product.name}</h1>

<div class="grid grid-cols-2 gap-10">

    <!-- Assign Category -->
    <div class="bg-white p-6 shadow rounded-lg">
        <h2 class="text-xl font-semibold mb-4">Add Category</h2>

        <form action="/products/${product.id}/addCategory" method="post" class="space-y-4">

            <select name="categoryId" class="border p-2 rounded w-full">
                <c:forEach var="c" items="${categories}">
                    <option value="${c.id}">${c.name}</option>
                </c:forEach>
            </select>

            <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
                Add Category
            </button>
        </form>
    </div>

    <!-- Current Categories -->
    <div class="bg-white p-6 shadow rounded-lg">
        <h2 class="text-xl font-semibold mb-4">Assigned Categories</h2>

        <ul class="space-y-2">
            <c:forEach var="c" items="${assignedCategories}">
                <li class="p-3 bg-gray-50 rounded border">${c.name}</li>
            </c:forEach>
        </ul>
    </div>

</div>

</body>
</html>
