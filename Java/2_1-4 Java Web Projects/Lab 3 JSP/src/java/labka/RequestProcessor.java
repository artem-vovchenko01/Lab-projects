package labka;

import java.util.HashMap;
import javax.servlet.http.HttpServletRequest;

public class RequestProcessor
{
    private final HttpServletRequest request;
            
    public RequestProcessor(HttpServletRequest request) 
    {
        this.request = request;
    }
    
    public HashMap<String, RangeData> getRangeData()
    {
        HashMap<String, Range>  ranges = getRanges();
        HashMap<String, RangeData> result = new HashMap();
        result.put("A", ranges.get("A").getRangeData());
        result.put("B", ranges.get("B").getRangeData());
        result.put("C", ranges.get("C").getRangeData());
        result.put("D", ranges.get("D").getRangeData());
        return result;
    }
    
    public HashMap<String,Range> getRanges() 
    {
        HashMap<String,Range> ranges = new HashMap();
        if (hasParameters())
        {
            Range rangeForA = rangeMaker("A");
            Range rangeForB = rangeMaker("B");
            Range rangeForC = rangeMaker("C");
            Range rangeForD = rangeMaker("D");

            ranges.put("A", rangeForA);
            ranges.put("B", rangeForB);
            ranges.put("C", rangeForC);
            ranges.put("D", rangeForD);
        }
        else
        {
            RangeData rangeDataForA = new RangeData();
            RangeData rangeDataForB = new RangeData();
            RangeData rangeDataForC = new RangeData();
            RangeData rangeDataForD = new RangeData();
           
            Range rangeForA = new Range(rangeDataForA);
            Range rangeForB = new Range(rangeDataForB);
            Range rangeForC = new Range(rangeDataForC);
            Range rangeForD = new Range(rangeDataForD);
            
            ranges.put("A", rangeForA);
            ranges.put("B", rangeForB);
            ranges.put("C", rangeForC);
            ranges.put("D", rangeForD);
        }
        return ranges;

    }
    
    public boolean hasParametesForRange(String name)
    {
        if (request.getParameter("begin" + name ) == null) return false;
        else if (request.getParameter("end" + name ) == null) return false;
        else if( request.getParameter("step" + name ) == null) return false;
        else return true;
    }  
    
    public boolean hasParameters()
    {
        if (!hasParametesForRange("A")) return false;
        else if (!hasParametesForRange("B")) return false;
        else if (!hasParametesForRange("C")) return false;
        else return hasParametesForRange("D");
    }
          
    public Range rangeMaker(String name)
    {
        String beginString = request.getParameter("begin" + name);
        String endString = request.getParameter("end" + name);
        String stepString = request.getParameter("step" + name);
        
        double begin = Double.parseDouble(beginString);
        double end = Double.parseDouble(endString);
        double step = Double.parseDouble(stepString);
        
        RangeData resultData = new RangeData(begin,end,step);
        Range result = new Range(resultData);
        
        return result;
    }
}
