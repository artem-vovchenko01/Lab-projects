<%@page import="labka.CookiesProcesor"%>
<%@page import="labka.Processor"%>
<%@page import="labka.TableLineData"%>
<%@page import="java.util.HashMap"%>
<%@page import="labka.Range"%>
<%@page import="labka.RangeData"%>
<%@page import="labka.RequestProcessor"%>
<%@page import="labka.LineGeneratorData"%>
<%@page import="labka.LineGenerator"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%--<%@page errorPage="error.jsp"%>--%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Main page</title>
    </head>
           <%
            Processor processor = new Processor(request, response);
            HashMap<String,RangeData> rangeData = processor.getRanges();
            %>
        <form action="main.jsp">
            Value 1: from: <input type="text" name="beginA" value="<%= rangeData.get("A").getBegin()%>">
            to: <input type="text" name="endA" value="<%= rangeData.get("A").getEnd() %>">
            step: <input type="text" name="stepA" value="<%= rangeData.get("A").getStep() %>">
            <br/>
            Value 2: from: <input type="text" name="beginB" value="<%= rangeData.get("B").getBegin() %>">
            to: <input type="text" name="endB" value="<%= rangeData.get("B").getEnd() %>">
            step: <input type="text" name="stepB" value="<%= rangeData.get("B").getStep() %>">
            <br/>
            Value 3: from: <input type="text" name="beginC" value="<%= rangeData.get("C").getBegin() %>">
            to: <input type="text" name="endC" value="<%= rangeData.get("C").getEnd() %>">
            step: <input type="text" name="stepC" value="<%= rangeData.get("C").getStep() %>">
            <br/>
            Value 4: from: <input type="text" name="beginD" value="<%= rangeData.get("D").getBegin() %>">
            to: <input type="text" name="endD" value="<%= rangeData.get("D").getEnd() %>">
            step: <input type="text" name="stepD"value="<%= rangeData.get("D").getStep() %>">
            <br/>
            <input type ="submit" value ="Calculate">
        </form>
        
        <table>
            <%
                LineGenerator lineGenerator = processor.getGenerator();
            if (lineGenerator.getLineGeneratorData().isAreOk())
            {
                
            
               %>
            <tr>
                <td>Value1</td><td>Value2</td><td>Value3</td><td>Value4</td><td>Result</td>
            </tr>
            
           <%
                 while (lineGenerator.hasNext()) 
                 {        
                     TableLineData tableLineData = lineGenerator.getNext();
            %>
                <tr>
                    <td><%=tableLineData.getA()%></td>
                    <td><%=tableLineData.getB()%></td>
                    <td><%=tableLineData.getC()%></td>
                    <td><%=tableLineData.getD()%></td>
                    <td><%=tableLineData.getResult()%></td>
                </tr>
           <%
                 }
            }
            else 
            {
           %>
            <tr><%=lineGenerator.getLineGeneratorData().getMassege()%></tr>
            <%          
            }
            %>
        </table>
        
    
</html>
