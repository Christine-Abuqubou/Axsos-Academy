<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 10/11/2025
  Time: 3:01 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>


<html>
<head>
    <title>Omikuji</title>
    <script src="https://cdn.tailwindcss.com"></script>

</head>
<body>

<h1 class="text-center text-3xl font-bold mt-8 text-indigo-600">
    Send an Omikuji!
</h1>

<form
        action="/omikuji/process"
        method="POST"
        class="max-w-lg mx-auto mt-10 p-8 bg-white shadow-lg rounded-lg border border-gray-300"
>
    <div class="space-y-6">
        <div>
            <label class="block text-gray-700 font-semibold mb-1">
                Enter the name of any city
            </label>
            <input
                    type="text"
                    name="city"
                    class="w-full border-2 border-gray-300 rounded-md p-2 focus:border-indigo-500 focus:ring-indigo-500 focus:outline-none"
                    placeholder="e.g. Tokyo"
            />
        </div>

        <div>
            <label class="block text-gray-700 font-semibold mb-1">
                Pick any number from 5 to 25
            </label>
            <input
                    type="number"
                    name="number"
                    min="5"
                    max="25"
                    class="w-full border-2 border-gray-300 rounded-md p-2 focus:border-indigo-500 focus:ring-indigo-500 focus:outline-none"
                    placeholder="e.g. 12"
            />
        </div>

        <div>
            <label class="block text-gray-700 font-semibold mb-1">
                Enter the name of any real person
            </label>
            <input
                    type="text"
                    name="person"
                    class="w-full border-2 border-gray-300 rounded-md p-2 focus:border-indigo-500 focus:ring-indigo-500 focus:outline-none"
                    placeholder="e.g. Taylor Swift"
            />
        </div>

        <div>
            <label class="block text-gray-700 font-semibold mb-1">
                Enter a professional hobby
            </label>
            <input
                    type="text"
                    name="hobby"
                    class="w-full border-2 border-gray-300 rounded-md p-2 focus:border-indigo-500 focus:ring-indigo-500 focus:outline-none"
                    placeholder="e.g. photography"
            />
        </div>

        <div>
            <label class="block text-gray-700 font-semibold mb-1">
                Enter any type of living thing
            </label>
            <input
                    type="text"
                    name="living"
                    class="w-full border-2 border-gray-300 rounded-md p-2 focus:border-indigo-500 focus:ring-indigo-500 focus:outline-none"
                    placeholder="e.g. dolphin"
            />
        </div>

        <div>
            <label class="block text-gray-700 font-semibold mb-1">
                Say something nice to someone
            </label>
            <input
                    type="text"
                    name="compliment"
                    class="w-full border-2 border-gray-300 rounded-md p-2 focus:border-indigo-500 focus:ring-indigo-500 focus:outline-none"
                    placeholder="e.g. You’re amazing!"
            />
        </div>

        <div class="text-center">
            <input
                    type="submit"
                    value="Submit"
                    class="px-6 py-2 bg-indigo-600 text-white font-semibold rounded-md hover:bg-indigo-700 transition-all duration-300 cursor-pointer"
            />
        </div>
    </div>
</form>


</body>


</html>
