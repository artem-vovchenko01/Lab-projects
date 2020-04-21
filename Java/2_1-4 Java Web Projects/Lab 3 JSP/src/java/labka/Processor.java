 package labka;

import java.util.HashMap;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Processor 
{
    
    private LineGenerator lineGenerator;
    private HashMap<String, Range> ranges;
    private HashMap<String, RangeData> rangesData;
    private HttpServletRequest request;
    private HttpServletResponse response;
    
    public Processor(HttpServletRequest request, HttpServletResponse response) {
        this.request = request;
        this.response = response;
        
        RequestProcessor requestProcessor = new RequestProcessor(request);
        this.ranges = requestProcessor.getRanges();
        this.rangesData = requestProcessor.getRangeData();
        
        Range rangeForA = ranges.get("A");
        Range rangeForB = ranges.get("B");
        Range rangeForC = ranges.get("C");
        Range rangeForD = ranges.get("D");
        
        LineGeneratorData data = new LineGeneratorData(rangeForA, rangeForB, rangeForC, rangeForD);
        lineGenerator = new LineGenerator(data);
    }
    
    public LineGenerator getGenerator() 
    {
        return lineGenerator;
    }

    public HashMap<String, RangeData> getRanges()
    {
        return rangesData;
    }
    

}
  
