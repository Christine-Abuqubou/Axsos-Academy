<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 19/11/2025
  Time: 2:30 pm
  To change this template use File | Settings | File Templates.
--%>
<%--<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>--%>
<%--<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>--%>
<%--<%@ page language="java" contentType="text/html; charset=UTF-8"--%>
<%--         pageEncoding="UTF-8"%>--%>

<%--<html>--%>
<%--<head>--%>
<%--    <title>Title</title>--%>
<%--    <script src="https://cdn.tailwindcss.com"></script>--%>
<%--</head>--%>
<%--<body class="h-screen w-full">--%>
<%--<h1    class="mt-20 text-center text-6xl">--%>
<%--    New Product--%>
<%--</h1>--%>
<%--<a href="/" class="underline text-blue-500 text-3xl ml-24 hover:text-blue-900">Home</a>--%>


<%--<div class="border-2 rounded-50% border-black w-[90%] mt-5 mx-auto mb-5"> </div>--%>

<%--<form:form method="post" action="/new" modelAttribute="product">--%>


<%--    <div class="flex text-3xl border-black border-2 w-[90%] mx-auto">--%>
<%--        <div class="w-[50%] border-black p-3 flex flex-col border-2">--%>
<%--            Name--%>
<%--        </div>--%>
<%--        <div class="w-[50%] border-black p-3 flex flex-col border-2">--%>
<%--            <form:input path="name" class="w-[99%]  border-2 border-black"/>--%>
<%--        </div>--%>
<%--    </div>--%>

<%--    <div class="flex text-3xl border-black border-2 w-[90%] mx-auto">--%>
<%--        <div class="w-[50%] border-black p-3 flex flex-col border-2">--%>
<%--            Description--%>
<%--        </div>--%>
<%--        <div class="w-[50%] border-black p-3 flex flex-col border-2">--%>
<%--            <form:input path="description" class="w-[99%]  border-2 border-black"/>--%>
<%--        </div>--%>
<%--    </div>--%>


<%--    <div class="flex text-3xl border-black border-2 w-[90%] mx-auto">--%>
<%--        <div class="w-[50%] border-black p-3 flex flex-col border-2">--%>
<%--            Price--%>
<%--        </div>--%>
<%--        <div class="w-[50%] border-black p-3 flex flex-col border-2">--%>
<%--            <form:input path="price" class="w-[99%] pl-2 border-2 border-black"/>--%>
<%--        </div>--%>
<%--    </div>--%>

<%--    <div class="flex border-[3px] border-black text-3xl justify-center p-1 w-[90%] mx-auto h-[60px]">--%>
<%--        <button class="w-[98%] border-2 border-black">Submit</button>--%>
<%--    </div>--%>
<%--</form:form>--%>

<%--</body>--%>
<%--</html>--%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>--%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>


<!DOCTYPE html>
<html>
<head>
    <title>New Product</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-10">

<h1 class="text-3xl font-bold text-blue-700 mb-6">Create New Product</h1>

<form:form action="/products/new" method="post" modelAttribute="product"
           class="bg-white p-6 shadow rounded-lg max-w-lg">

    <label class="block mb-2 font-medium">Product Name</label>
    <form:input path="name" class="border p-2 w-full rounded mb-4"/>

    <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
        Save Product
    </button>
</form:form>

</body>
</html>

