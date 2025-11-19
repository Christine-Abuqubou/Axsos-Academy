<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 19/11/2025
  Time: 4:35 pm
  To change this template use File | Settings | File Templates.
--%>

<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <title>Category Details</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-10">

<h1 class="text-3xl font-bold mb-4 text-green-700">${category.name}</h1>

<div class="grid grid-cols-2 gap-10">

    <!-- Add Product -->
    <div class="bg-white p-6 shadow rounded-lg">
        <h2 class="text-xl font-semibold mb-4">Add Product</h2>

        <form action="/categories/${category.id}/addProduct" method="post" class="space-y-4">

            <select name="productId" class="border p-2 rounded w-full">
                <c:forEach var="p" items="${products}">
                    <option value="${p.id}">${p.name}</option>
                </c:forEach>
            </select>

            <button class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
                Add Product
            </button>
        </form>
    </div>

    <!-- Assigned Products -->
    <div class="bg-white p-6 shadow rounded-lg">
        <h2 class="text-xl font-semibold mb-4">Assigned Products</h2>

        <ul class="space-y-2">
            <c:forEach var="p" items="${assignedProducts}">
                <li class="p-3 bg-gray-50 rounded border">${p.name}</li>
            </c:forEach>
        </ul>
    </div>

</div>

</body>
</html>


<%--<html>--%>
<%--  <head>--%>
<%--    <title>Title</title>--%>

<%--  </head>--%>
<%--  <body>--%>
<%--  <h1><c:out value="${category.name}" /></h1>--%>

<%--  <form action="/categories/${category.id}/addProduct" method="post">--%>
<%--      <select name="productId">--%>
<%--          <c:forEach var="p" items="${allProducts}">--%>
<%--              <option value="${p.id}">${p.name}</option>--%>
<%--          </c:forEach>--%>
<%--      </select>--%>
<%--      <button>Add</button>--%>
<%--  </form>--%>

<%--  <h3>Products:</h3>--%>
<%--  <ul>--%>
<%--      <c:forEach var="p" items="${category.products}">--%>
<%--          <li>${p.name}</li>--%>
<%--      </c:forEach>--%>
<%--  </ul>--%>

<%--  </body>--%>
<%--</html>--%>
