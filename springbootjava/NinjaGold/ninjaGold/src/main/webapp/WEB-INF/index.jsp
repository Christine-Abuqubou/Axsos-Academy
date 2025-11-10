<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 10/11/2025
  Time: 6:33 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<html>
<head>
    <title>NinjaGold</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 flex flex-col items-center py-10">

<div class="bg-white p-6 rounded-lg shadow-md w-full max-w-4xl">
    <h1 class="text-2xl font-bold text-center text-yellow-600 mb-6">Ninja Gold Game</h1>

    <p class="text-center text-lg mb-6">
        Your Gold: <span class="font-bold text-green-600">${sessionScope.gold}</span>
    </p>

    <!-- Horizontal container for four divs -->
    <div class="flex justify-between gap-4 mb-6">
        <!-- Farm -->
        <div class="bg-green-100 p-4 rounded flex flex-col justify-between items-center w-1/4 h-32">
            <span class="text-lg font-semibold mb-2">Farm</span>
            <form action="process" method="post" class="mt-auto w-full">
                <input type="hidden" name="place" value="farm">
                <button class="w-full bg-green-500 text-white py-2 rounded hover:bg-green-600">Earn Farm (+10–20)</button>
            </form>
        </div>

        <!-- Cave -->
        <div class="bg-gray-100 p-4 rounded flex flex-col justify-between items-center w-1/4 h-32">
            <span class="text-lg font-semibold mb-2">Cave</span>
            <form action="process" method="post" class="mt-auto w-full">
                <input type="hidden" name="place" value="cave">
                <button class="w-full bg-gray-600 text-white py-2 rounded hover:bg-gray-700">Earn Cave (+5–10)</button>
            </form>
        </div>

        <!-- House -->
        <div class="bg-yellow-100 p-4 rounded flex flex-col justify-between items-center w-1/4 h-32">
            <span class="text-lg font-semibold mb-2">House</span>
            <form action="process" method="post" class="mt-auto w-full">
                <input type="hidden" name="place" value="house">
                <button class="w-full bg-yellow-500 text-white py-2 rounded hover:bg-yellow-600">Earn House (+2–5)</button>
            </form>
        </div>

        <!-- Quest -->
        <div class="bg-red-100 p-4 rounded flex flex-col justify-between items-center w-1/4 h-32">
            <span class="text-lg font-semibold mb-2">Quest</span>
            <form action="process" method="post" class="mt-auto w-full">
                <input type="hidden" name="place" value="quest">
                <button class="w-full bg-red-500 text-white py-2 rounded hover:bg-red-600">Earn Quest (±0–50)</button>
            </form>
        </div>
    </div>

    <h2 class="text-lg font-semibold mb-2">Activity Log:</h2>
    <div class="bg-gray-50 border border-gray-300 rounded p-2 h-48 overflow-y-auto text-sm whitespace-pre-line">
        ${sessionScope.log}
    </div>
</div>

</body>
</html>
