<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Daikichi Fortune</title>
</head>
<body>

<c:if test="${not empty message}">
    <h1>${message}</h1>
</c:if>

<c:if test="${not empty number}">
    <h1>Your Lucky Number: ${number}</h1>

    <c:if test="${number % 2 == 0}">
        <h2>You will take a grand journey in the near future but be wary of tempting offers.</h2>
    </c:if>

    <c:if test="${number % 2 != 0}">
        <h2>You have enjoyed the fruits of your labor, but now is a great time to spend time with family and friends.</h2>
    </c:if>
</c:if>

</body>
</html>
