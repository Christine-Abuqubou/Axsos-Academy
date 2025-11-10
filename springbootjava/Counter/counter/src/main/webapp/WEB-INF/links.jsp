<%--
  Created by IntelliJ IDEA.
  User: chrisbsharah
  Date: 10/11/2025
  Time: 12:41 pm
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core"%>

<html>
<head>
    <title>welcome </title>
</head>
<body>
<p> You have Visited <a href="/your_server">http://your_server</a> 10 times </p>
<br>
<a href="/">Test another visit </a>

<p>You have visited the index page ${counter} times in this session.</p>
<a href="/">Increment Counter</a>

</body>
</html>
