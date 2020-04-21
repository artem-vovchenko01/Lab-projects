package labka;

import java.util.HashMap;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class CookiesProcesor
{
    
    HttpServletRequest request;
    HttpServletResponse response;

    public CookiesProcesor(HttpServletRequest request, HttpServletResponse response) {
        this.request = request;
        this.response = response;
    }
        
        public void setCookies ()
    {

        rangeThrow("A");
        rangeThrow("B");
        rangeThrow("C");
        rangeThrow("D");
    }
    
    public void  rangeThrow(String name) {
        Cookie Begin = new Cookie("begin" + name, request.getParameter("begin" + name));
        Cookie End = new Cookie("end" + name, request.getParameter("end" + name));
        Cookie Step = new Cookie("step" + name, request.getParameter("step" + name));
      
       response.addCookie(Begin);
       response.addCookie(End);
       response.addCookie(Step);
    }

    
    public HashMap<String,Range> getCookies() 
    {
        
        HashMap<String,Range> ranges = new HashMap();
        
            Range rangeForA = rangeMaker("A");
            Range rangeForB = rangeMaker("B");
            Range rangeForC = rangeMaker("C");
            Range rangeForD = rangeMaker("D");

            ranges.put("A", rangeForA);
            ranges.put("B", rangeForB);
            ranges.put("C", rangeForC);
            ranges.put("D", rangeForD);
        
        return ranges;

    }

    public Range rangeMaker(String name)
    {
        
        String beginString = findCookies("begin" + name).getValue();
        String endString = findCookies("end" + name).getValue();
        String stepString = findCookies("step" + name).getValue();
        
        double begin = Double.parseDouble(beginString);
        double end = Double.parseDouble(endString);
        double step = Double.parseDouble(stepString);
        
        RangeData resultData = new RangeData(begin,end,step);
        Range result = new Range(resultData);
        
        return result;
    }

    
    public HashMap<String,String> getStringCookies()
    {
        
        HashMap<String,String> result = new HashMap();
        result.put("endA", this.findCookies("endA").getValue());
        result.put("endB", this.findCookies("endB").getValue());
        result.put("endC", this.findCookies("endC").getValue());
        result.put("endD", this.findCookies("endD").getValue());

        result.put("beginA", this.findCookies("beginA").getValue());
        result.put("beginB", this.findCookies("beginB").getValue());
        result.put("beginC", this.findCookies("beginC").getValue());
        result.put("beginD", this.findCookies("beginD").getValue());

        result.put("stepA", this.findCookies("stepA").getValue());
        result.put("stepB", this.findCookies("stepB").getValue());
        result.put("stepC", this.findCookies("stepC").getValue());
        result.put("stepD", this.findCookies("stepD").getValue());
        return result;
    }

    public Cookie findCookies(String name) 
    {
        Cookie[] CK = request.getCookies();
        for (Cookie c: CK) 
        {
            if (c.getName().equals(name))  return c;
        }
        return null;
    }


    public boolean hasCookiesForRange(String name) {
       if (findCookies("begin" + name) == null || findCookies("begin" + name).getValue() == null) return false;
       if (findCookies("end" + name) == null || findCookies("end" + name).getValue() == null) return false;
       if (findCookies("step" + name) == null || findCookies("step" + name).getValue() == null) return false;
       else return true;
    }

    public boolean hasCookies() {
        return hasCookiesForRange("A")&&hasCookiesForRange("B")&&hasCookiesForRange("C")&&hasCookiesForRange("D");
                
    }
}
