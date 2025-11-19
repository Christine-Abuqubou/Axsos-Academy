<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 15/11/2025
  Time: 4:02 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Auth Portal</title>


    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 min-h-screen flex items-center justify-center">

<div class="w-full max-w-5xl bg-white shadow-lg rounded-xl p-10 flex gap-10">

    <!-- ========================= -->
    <!--        REGISTER FORM      -->
    <!-- ========================= -->
    <div class="w-1/2">
        <h2 class="text-2xl font-bold mb-6 text-indigo-600">Create an Account</h2>

        <form:form action="/register" method="post" modelAttribute="newUser" class="space-y-5">

            <!-- First Name -->
            <div>
                <label class="block mb-1 font-medium text-gray-700">First Name</label>
                <form:input path="firstName" cssClass="w-full border rounded-lg p-2 focus:ring focus:ring-indigo-300" />
                <form:errors path="firstName" cssClass="text-red-500 text-sm" />
            </div>

            <!-- Last Name -->
            <div>
                <label class="block mb-1 font-medium text-gray-700">Last Name</label>
                <form:input path="lastName" cssClass="w-full border rounded-lg p-2 focus:ring focus:ring-indigo-300" />
                <form:errors path="lastName" cssClass="text-red-500 text-sm" />
            </div>

            <!-- Email -->
            <div>
                <label class="block mb-1 font-medium text-gray-700">Email</label>
                <form:input path="email" cssClass="w-full border rounded-lg p-2 focus:ring focus:ring-indigo-300" />
                <form:errors path="email" cssClass="text-red-500 text-sm" />
            </div>

            <!-- Password -->
            <div>
                <label class="block mb-1 font-medium text-gray-700">Password</label>
                <form:password path="password" cssClass="w-full border rounded-lg p-2 focus:ring focus:ring-indigo-300" />
                <form:errors path="password" cssClass="text-red-500 text-sm" />
            </div>

            <!-- Confirm -->
            <div>
                <label class="block mb-1 font-medium text-gray-700">Confirm Password</label>
                <form:password path="confirm" cssClass="w-full border rounded-lg p-2 focus:ring focus:ring-indigo-300" />
                <form:errors path="confirm" cssClass="text-red-500 text-sm" />
            </div>

            <button
                    type="submit"
                    class="w-full py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition">
                Register
            </button>

        </form:form>
    </div>


    <!-- ========================= -->
    <!--         LOGIN FORM        -->
    <!-- ========================= -->
    <div class="w-1/2 border-l pl-10">
        <h2 class="text-2xl font-bold mb-6 text-indigo-600">Login</h2>

        <form:form action="/login" method="post" modelAttribute="newLogin" class="space-y-5">

            <!-- Email -->
            <div>
                <label class="block mb-1 font-medium text-gray-700">Email</label>
                <form:input path="email" cssClass="w-full border rounded-lg p-2 focus:ring focus:ring-indigo-300" />
                <form:errors path="email" cssClass="text-red-500 text-sm" />
            </div>

            <!-- Password -->
            <div>
                <label class="block mb-1 font-medium text-gray-700">Password</label>
                <form:password path="password" cssClass="w-full border rounded-lg p-2 focus:ring focus:ring-indigo-300" />
                <form:errors path="password" cssClass="text-red-500 text-sm" />
            </div>

            <button
                    type="submit"
                    class="w-full py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition">
                Login
            </button>

        </form:form>
    </div>

</div>

</body>
</html>
