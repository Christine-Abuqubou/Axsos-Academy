<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 19/11/2025
  Time: 1:15 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>



<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-10">

<h1 class="text-3xl font-bold mb-6 text-blue-700">Products & Categories</h1>

<div class="grid grid-cols-2 gap-10">

    <!-- PRODUCTS -->
    <div class="bg-white p-6 shadow rounded-lg">
        <h2 class="text-xl font-semibold mb-4">Products</h2>

        <a href="/products/new"
           class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 mb-4 inline-block">
            + Add Product
        </a>

        <ul class="space-y-2">
            <c:forEach var="p" items="${products}">
                <li class="p-3 bg-gray-50 rounded border hover:bg-gray-100">
                    <a href="/products/${p.id}" class="text-blue-700 font-medium">${p.name}</a>
                </li>
            </c:forEach>
        </ul>
    </div>

    <!-- CATEGORIES -->
    <div class="bg-white p-6 shadow rounded-lg">
        <h2 class="text-xl font-semibold mb-4">Categories</h2>

        <a href="/categories/new"
           class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 mb-4 inline-block">
            + Add Category
        </a>

        <ul class="space-y-2">
            <c:forEach var="c" items="${categories}">
                <li class="p-3 bg-gray-50 rounded border hover:bg-gray-100">
                    <a href="/categories/${c.id}" class="text-green-700 font-medium">${c.name}</a>
                </li>
            </c:forEach>
        </ul>
    </div>

</div>

</body>
</html>

<%--<%@ page contentType="text/html;charset=UTF-8" language="java" %>--%>
<%--<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>--%>

<%--<html>--%>
<%--<head>--%>
<%--    <title>Title</title>--%>
<%--    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>--%>

<%--</head>--%>
<%--<body class="h-screen w-full">--%>
<%--<h1 class="mt-20 text-center text-5xl">welcome to our website </h1>--%>
<%--<h1 class="mt-10 text-center text-4xl">Home Page</h1>--%>

<%--<a href="/new" class="underline text-blue-500 ml-20 mt-10 text-3xl hover:text-blue-800">newProduct</a>--%>
<%--<br>--%>
<%--<br>--%>
<%--<a href="/newCategory" class="underline text-blue-500 ml-20 mt-10 text-3xl hover:text-blue-800">newCategory</a>--%>
<%--<div class="border-2 rounded-50% border-black w-[90%] mt-5 mx-auto mb-5"> </div>--%>
<%--<div class="flex text-center text-2xl border-black border-2 w-[90%] mx-auto">--%>
<%--    <div class="w-[50%] border-black border-2 p-3">--%>
<%--        Products--%>
<%--    </div>--%>
<%--    <div class="w-[50%] border-black border-2 p-3">--%>
<%--        Categories--%>
<%--    </div>--%>
<%--</div>--%>
<%--<div class="flex text-3xl border-black border-2 w-[90%] mx-auto">--%>
<%--    <div class="w-[50%] border-black border-2 p-3 flex flex-col">--%>
<%--        <c:forEach var="product" items="${products}">--%>
<%--            <p class="mt-2"><a href="/product/${product.id}" class="underline text-blue-500">- ${product.name}</a></p>--%>
<%--        </c:forEach>--%>
<%--    </div>--%>
<%--    <div class="w-[50%] border-black border-2 p-3">--%>
<%--        <c:forEach var="category" items="${categories}">--%>
<%--            <p class="mt-2"><a href="/${category.id}" class="underline text-blue-500">- ${category.name}</a></p>--%>
<%--        </c:forEach>--%>
<%--    </div>--%>
<%--</div>--%>






<%--</body>--%>
<%--</html>--%>
