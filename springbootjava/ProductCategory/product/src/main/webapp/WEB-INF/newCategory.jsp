<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 19/11/2025
  Time: 3:07 pm
  To change this template use File | Settings | File Templates.
--%>

<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
         pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>
<head>
    <title>New Category</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 p-10">

<h1 class="text-3xl font-bold text-green-700 mb-6">Create New Category</h1>

<form:form action="/categories/new" method="post" modelAttribute="category"
           class="bg-white p-6 shadow rounded-lg max-w-lg">

    <label class="block mb-2 font-medium">Category Name</label>
    <form:input path="name" class="border p-2 w-full rounded mb-4"/>

    <button class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
        Save Category
    </button>
</form:form>

</body>
</html>


<%--<html>--%>
<%--<head>--%>
<%--    <title>Title</title>--%>
<%--    <script src="https://cdn.tailwindcss.com"></script>--%>
<%--</head>--%>
<%--<body class="h-screen w-full">--%>
<%--<h1    class="mt-20 text-center text-6xl">--%>
<%--    New Category--%>
<%--</h1>--%>
<%--<a href="/" class="underline text-blue-500 text-3xl ml-24 hover:text-blue-900">Home</a>--%>


<%--<div class="border-2 rounded-50% border-black w-[90%] mt-5 mx-auto mb-5"> </div>--%>

<%--<form:form method="post" action="/newCategory" modelAttribute="category">--%>

<%--    <div class="flex text-3xl border-black border-2 w-[90%] mx-auto">--%>
<%--        <div class="w-[50%] border-black p-3 flex flex-col border-2">--%>
<%--            Name--%>
<%--        </div>--%>
<%--        <div class="w-[50%] border-black p-3 flex flex-col border-2">--%>
<%--            <form:input path="name" class="w-[99%] pl-2 border-2 border-black"/>--%>
<%--        </div>--%>
<%--    </div>--%>



<%--    <div class="flex border-[3px] border-black text-3xl justify-center p-1 w-[90%] mx-auto h-[60px]">--%>
<%--        <button class="w-[98%] border-2 border-black">Submit</button>--%>
<%--    </div>--%>
<%--</form:form>--%>

<%--</body>--%>
<%--</html>--%>
