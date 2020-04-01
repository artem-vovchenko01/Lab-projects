package laba;
import java.io.IOException;
import java.util.HashMap;
import javax.servlet.ServletException;
import javax.servlet.http.*;

public class Task extends HttpServlet
{
    private HttpServletRequest req;
    private HttpServletResponse resp;
    private PageMaker pageMaker;
    
   
    protected void processRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException 
    {   
        req= request;
        resp = response;
        pageMaker = new PageMaker(response);
        resp.setContentType("text/html;charset=UTF-8");
        HashMap<String, Double> numbers = getNumbers();
        double result;
        if (numbers != null) 
        {
            try
            {
                Calc calculator = new Calc(numbers);
                result = calculator.calculate();
                addCookies();
                pageMaker.makePageWithNumber(numbers, result);
            }
            catch (IllegalArgumentException | ArithmeticException e)
            {
                pageMaker.makeErrorPage(e.getMessage());
            }
        }
        else
        {
            pageMaker.makePageWithoutNumber();
        }
    }
        
    public HashMap<String, String> getParameters()
    {
        HashMap<String, String> result = new HashMap();
        result.put("a", req.getParameter("a"));
        result.put("b", req.getParameter("b"));
        result.put("c", req.getParameter("c"));
        result.put("d", req.getParameter("d"));
        if (result.get("a") == null || result.get("b") == null || result.get("c") == null || result.get("d") == null)
        {
            result = getCoockies();
        }
        return result;
    }

    public HashMap<String, Double> getNumbers() throws IOException
    {
        HashMap<String, String> parameters = getParameters();
        HashMap<String, Double>result = new HashMap();
            try 
            {
                result.put("a", Double.parseDouble(parameters.get("a")));
                result.put("b", Double.parseDouble(parameters.get("b")));
                result.put("c", Double.parseDouble(parameters.get("c")));
                result.put("d", Double.parseDouble(parameters.get("d")));
            }
            catch (NumberFormatException e) 
            {
                pageMaker.makeErrorPage("NumberFormatException: некоректно введені дані");
            }
            catch (NullPointerException e) {
                 return null;
            }
        return result;
    }
 
    public void addCookies()
    {
        HashMap<String, String> parameters = getParameters();
        Cookie cookieForA = new Cookie("a", parameters.get("a"));
        Cookie cookieForB = new Cookie("b", parameters.get("b"));
        Cookie cookieForC = new Cookie("c", parameters.get("c"));
        Cookie cookieForD = new Cookie("d", parameters.get("d"));
        
        int timeOfLife = 2*60 * 60 * 24;
        
        cookieForA.setMaxAge(timeOfLife);
        cookieForB.setMaxAge(timeOfLife);
        cookieForC.setMaxAge(timeOfLife);
        cookieForD.setMaxAge(timeOfLife);
        
        resp.addCookie(cookieForA);
        resp.addCookie(cookieForB);
        resp.addCookie(cookieForC);
        resp.addCookie(cookieForD);
    }
    
    public HashMap<String, String> getCoockies()
    {
        HashMap<String, String> result= new HashMap();
        if (req.getCookies() != null)
        {
            for (Cookie cookie : req.getCookies()) 
            {
                switch (cookie.getName()) 
                {
                    case "a":
                        result.put("a", cookie.getValue());
                        break;
                    case "b":
                        result.put("b", cookie.getValue());
                        break;
                    case "c":
                        result.put("c", cookie.getValue());
                        break;
                    case "d":
                        result.put("d",cookie.getValue());
                }
            }
        }
        else
        {
            result = null;
        }
        return result;
    }
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException 
    {
        processRequest(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException 
    {
        processRequest(request, response);
    }

    @Override
    public String getServletInfo() 
    {
        return "this servlet calculate the formula written in the welcome file";
    }
}