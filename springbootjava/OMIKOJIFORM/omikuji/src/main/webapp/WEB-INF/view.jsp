<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 10/11/2025
  Time: 3:41 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>


<html>
<head>
    <title>view</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">

<div class="bg-white p-8 rounded-xl shadow-lg text-center w-96">
    <h1 class="text-3xl font-bold text-blue-600 mb-4">Your Omikuji Fortune</h1>

    <p class="text-lg mb-2">In <span class="font-semibold">${sessionScope.city}</span>, you will have <span class="font-semibold">${sessionScope.number}</span> surprises!</p>
    <p class="text-lg mb-2"><span class="font-semibold">${sessionScope.person}</span> will play a big role in your life soon.</p>
    <p class="text-lg mb-2">Keep enjoying <span class="font-semibold">${sessionScope.hobby}</span>, it will bring you luck.</p>
    <p class="text-lg mb-2">Your home <span class="font-semibold">${sessionScope.living}</span> will feel especially comforting.</p>
    <p class="text-lg mb-4">And remember: <span class="font-semibold">${sessionScope.compliment}</span></p>

    <a href="/omikuji"
       class="inline-block bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition">
        Go Back
    </a>
</div>

</body>
</html>
