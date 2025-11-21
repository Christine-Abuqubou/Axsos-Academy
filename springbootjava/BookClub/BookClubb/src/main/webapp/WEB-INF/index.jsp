<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 21/11/2025
  Time: 2:42 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
    <title>Login & Register</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100">

<div class="max-w-4xl mx-auto mt-10 grid grid-cols-1 md:grid-cols-2 gap-8">

    <!-- REGISTRATION -->
    <div class="bg-white p-6 rounded shadow">
        <h2 class="text-2xl mb-4 font-bold">Register</h2>

        <form:form action="/register" method="post" modelAttribute="newUser" class="space-y-3">

            <div>
                <form:label path="username">Username</form:label>
                <form:input path="username" class="border w-full p-2"/>
                <p class="text-red-500 text-sm"><form:errors path="username"/></p>
            </div>

            <div>
                <form:label path="email">Email</form:label>
                <form:input path="email" class="border w-full p-2"/>
                <p class="text-red-500 text-sm"><form:errors path="email"/></p>
            </div>

            <div>
                <form:label path="password">Password</form:label>
                <form:password path="password" class="border w-full p-2"/>
                <p class="text-red-500 text-sm"><form:errors path="password"/></p>
            </div>

            <div>
                <form:label path="confirmPassword">Confirm Password</form:label>
                <form:password path="confirmPassword" class="border w-full p-2"/>
                <p class="text-red-500 text-sm"><form:errors path="confirmPassword"/></p>
            </div>

            <button class="bg-blue-600 text-white px-4 py-2 rounded w-full">Register</button>
        </form:form>
    </div>

    <!-- LOGIN -->
    <div class="bg-white p-6 rounded shadow">
        <h2 class="text-2xl mb-4 font-bold">Login</h2>

        <form:form action="/login" method="post" modelAttribute="newLogin" class="space-y-3">

            <div>
                <form:label path="email">Email</form:label>
                <form:input path="email" class="border w-full p-2"/>
                <p class="text-red-500 text-sm"><form:errors path="email"/></p>
            </div>

            <div>
                <form:label path="password">Password</form:label>
                <form:password path="password" class="border w-full p-2"/>
                <p class="text-red-500 text-sm"><form:errors path="password"/></p>
            </div>

            <button class="bg-green-600 text-white px-4 py-2 rounded w-full">Login</button>
        </form:form>
    </div>

</div>

</body>
</html>
