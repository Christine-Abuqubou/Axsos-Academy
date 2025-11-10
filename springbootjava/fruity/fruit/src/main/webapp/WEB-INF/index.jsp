<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 10/11/2025
  Time: 2:38 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>

<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>


<html>
<head>
    <title>Fruit Store</title>
    <link rel="stylesheet" href="/css/styles.css">
</head>
<body>
<div class="container">
    <h1>🍍 Welcome to the Fruit Store 🍓</h1>

    <table>
        <thead>
        <tr>
            <th>Fruit Name</th>
            <th>Price ($)</th>
        </tr>
        </thead>
        <tbody>
        <c:forEach var="fruit" items="${fruits}">
            <tr>
                <!-- Ninja Bonus: Make fruits starting with 'G' orange -->
                <td class="${fn:startsWith(fruit.name, 'G') ? 'orange-text' : ''}">
                        ${fruit.name}
                </td>
                <td>${fruit.price}</td>
            </tr>
        </c:forEach>
        </tbody>
    </table>
</div>
</body>
</html>
