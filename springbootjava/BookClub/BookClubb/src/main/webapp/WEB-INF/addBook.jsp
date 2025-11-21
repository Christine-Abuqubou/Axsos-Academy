<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 21/11/2025
  Time: 2:43 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>

<!DOCTYPE html>
<html>
<head>
    <title>Add Book</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100">

<c:if test="${empty sessionScope.userId}">
    <c:redirect url="/" />
</c:if>

<div class="max-w-xl mx-auto mt-10 bg-white p-6 rounded shadow">

    <h1 class="text-2xl font-bold mb-4">Add a Book</h1>

    <form:form modelAttribute="book" action="/books/new" method="post" class="space-y-3">

        <div>
            <form:label path="title">Title</form:label>
            <form:input path="title" class="border w-full p-2"/>
            <p class="text-red-500 text-sm"><form:errors path="title"/></p>
        </div>

        <div>
            <form:label path="description">Description</form:label>
            <form:textarea path="description" class="border w-full p-2"/>
            <p class="text-red-500 text-sm"><form:errors path="description"/></p>
        </div>

        <button class="bg-blue-600 text-white px-4 py-2 rounded">Add Book</button>

    </form:form>

</div>

</body>
</html>
