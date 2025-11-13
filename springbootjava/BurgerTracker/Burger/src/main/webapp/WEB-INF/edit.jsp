<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 13/11/2025
  Time: 1:24 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<html>
<head>
    <title>Edit Burger</title>
</head>
<body>
<h1>Edit Burger</h1>
<form:form action="/burgers/${burger.id}" method="post" modelAttribute="burger">
    <input type="hidden" name="_method" value="put" /> <!-- Simulate PUT request -->

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

    <input type="submit" value="Update Burger"/>
</form:form>

<p><a href="/">Back to Home</a></p>
</body>
</html>
