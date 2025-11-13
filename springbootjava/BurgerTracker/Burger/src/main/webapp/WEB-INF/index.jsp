<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 12/11/2025
  Time: 11:35 am
  To change this template use File | Settings | File Templates.
--%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<html>
<head>
    <title>Burger Tracker</title>
</head>
<body>
<h1>Burger Tracker</h1>

<h2>Add a Burger</h2>
<form:form action="/burgers" method="post" modelAttribute="burger">
    <p>
        <form:label path="name">Burger Name:</form:label>
        <form:input path="name"/>
        <form:errors path="name"/>
    </p>
    <p>
        <form:label path="restaurant">Restaurant:</form:label>
        <form:input path="restaurant"/>
        <form:errors path="restaurant"/>
    </p>
    <p>
        <form:label path="rating">Rating (1-5):</form:label>
        <form:input path="rating" type="number"/>
        <form:errors path="rating"/>
    </p>
    <p>
        <form:label path="notes">Notes:</form:label>
        <form:textarea path="notes"/>
        <form:errors path="notes"/>
    </p>
    <input type="submit" value="Add Burger"/>
</form:form>

<h2>All Burgers</h2>
<table border="1">
    <tr>
        <th>Name</th>
        <th>Restaurant</th>
        <th>Rating</th>
        <th>Notes</th>
    </tr>
    <c:forEach var="b" items="${burgers}">
        <tr>
            <td><c:out value="${b.name}"/></td>
            <td><c:out value="${b.restaurant}"/></td>
            <td><c:out value="${b.rating}"/></td>
            <td><c:out value="${b.notes}"/></td>
        </tr>
    </c:forEach>
</table>
</body>
</html>

