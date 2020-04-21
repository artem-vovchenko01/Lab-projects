package laba;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import javax.servlet.http.HttpServletResponse;

public class PageMaker {
    private HttpServletResponse resp;

    public PageMaker(HttpServletResponse response) {
        resp = response;
    }
    
    protected void makeErrorPage(String text) throws IOException 
    {
        try (PrintWriter out = resp.getWriter()) 
        {
            out.println("<html>");
            out.println("<head>");
            out.println("<title>TODO supply a title</title>");
            out.println("<meta charset=\"UTF-8\">");
            out.println("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">");
            out.println("</head>");
            out.println("<body>");
            out.println("<div>" + text + "</div>");
            out.println("</body>");
            out.println("</html>");
        }
    }

    protected void makePageWithNumber (HashMap<String, Double> numbers, double result)
            throws IOException 
    {
        try (PrintWriter out = resp.getWriter()) 
        {
            out.println("<html>");
            out.println("<head>");
            out.println("<title>TODO supply a title</title>");
            out.println("<meta charset=\"UTF-8\">");
            out.println("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">");
            out.println("</head>");
            out.println("<body>");
            out.println("<img src=\"formula.png\" height=\"100\">");
            out.println("<form action=\"task\" method=\"get\" name=\"frm\">");
            out.println("a:");
            out.println("<input required name=\"a\" type=\"text\" value=\"" + numbers.get("a") + "\"/><br>");
            out.println("b:");
            out.println("<input  required name=\"b\" type=\"text\" value=\"" + numbers.get("b") + "\"/><br> ");
            out.println("c:");
            out.println("<input required name=\"c\" type=\"text\" value=\"" + numbers.get("c") + "\"/><br>");
            out.println("d:");
            out.println("<input required name=\"d\" type=\"text\" value=\"" + numbers.get("d") + "\"/><br>");
            out.println("<input type=\"submit\" value=\"=\" >");
            out.println("</form>");
            out.println(result);
            out.println("</body>");
            out.println("</html>");
        }
    }
    
    public void makePageWithoutNumber() throws IOException
    {
        try (PrintWriter out = resp.getWriter()) 
        {
            out.println("<html>");
            out.println("<head>");
            out.println("<title>TODO supply a title</title>");
            out.println("<meta charset=\"UTF-8\">");
            out.println("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">");
            out.println("</head>");
            out.println("<body>");
            out.println("<img src=\"formula.png\" height=\"100\">");
            out.println("<form action=\"task\" method=\"get\" name=\"frm\">");
            out.println("a:");
            out.println("<input required name=\"a\" type=\"text\"/><br>");
            out.println("b:");
            out.println("<input required name=\"b\" type=\"text\"/><br> ");
            out.println("c:");
            out.println("<input required name=\"c\" type=\"text\"/><br>");
            out.println("d:");
            out.println("<input required name=\"d\" type=\"text\"/><br>");
            out.println("<input type=\"submit\" value=\"=\">");
            out.println("</form>");
            out.println("</body>");
            out.println("</html>");
        }
    }
}