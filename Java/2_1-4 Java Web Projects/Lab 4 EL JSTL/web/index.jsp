<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<%@page contentType="text/html;charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Главная страница</title>
        <link type="text/css" rel="stylesheet" href="/OP-labka4/styles.css"/>
    </head>
    <body>           
        <details>
            <summary>Институты</summary>
            <c:forEach items="${applicationScope.listOfInstitutes}" var="institute">
            <details>
                <summary>${institute.instituteData.name}</summary>
                <details>
                    <summary>Факультеты</summary>
                    <c:forEach items="${institute.instituteData.faculties}" var="faculty">
                    <details>
                        <summary>${faculty.facultyData.name}</summary>
                        <table>
                            <tr><td>Имя</td> <td>Фамилия</td> <td>Номер зачетной книжки</td> <td>Средний бал</td> </tr>
                            <c:forEach var="student" items="${faculty.facultyData.students}" >
                                <tr>
                                    <td>${student.studentData.name}</td>
                                    <td>${student.studentData.surname}</td>
                                    <td>${student.studentData.accountNumber}</td>
                                    <td>${student.studentData.meanScore}</td>
                                </tr>
                            </c:forEach>
                        </table>
                        <form action="Controller" method="post">
                            <br/>
                            <table>
                                <tr> <td>Имя:  </td> <td><input type="text" name="name"></td> </tr>
                                <tr> <td>Фамилия:  </td> <td><input type="text" name="surname"></td> </tr>
                                <tr> <td>Номер зачетной книжки:  </td> <td><input type="text" name="accountNumber"></td> </tr>
                                <tr> <td>Mean score: </td> <td><input type="text" name="meanScore"></td> </tr>
                            </table>
                            <input type="submit" value="Add student:${institute.instituteData.name}:${faculty.facultyData.name}" name="command"/>
                            
                        </form>
                    </details>
                    </c:forEach>
                </details>
                <form action="Controller" method="post">
                    <br/>Добавление нового факультета<br/>
                     Наименование: <input required name="facultyName" type="text"><br/>
                    <input type ="submit" value ="Create faculty:${institute.instituteData.name}" name="command"><br/>
                </form>
            </details>
            </c:forEach>
            <form action="Controller" method="post">
                <br/>Добавление нового института<br/>
                Наименование:   <input required name="instituteName" type="text"><br/>
                <input type ="submit" value ="Create institute:" name="command"><br/>
                
            </form>
        </details>
        <c:out value="${mesg}" default=""/>
    </body>
</html>
