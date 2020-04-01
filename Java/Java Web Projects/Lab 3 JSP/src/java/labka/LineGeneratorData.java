package labka;

public class LineGeneratorData 
{
    private final Range rangeForA;
    private final Range rangeForB;
    private final Range rangeForC;
    private final Range rangeForD;
    private Calculator calculator;
    private boolean areOk = false;
    private String massege = "";

    public LineGeneratorData(Range rangeForA, Range rangeForB, Range rangeForC, Range rangeForD) 
    {
        this.rangeForA = rangeForA;
        this.rangeForB = rangeForB;
        this.rangeForC = rangeForC;
        this.rangeForD = rangeForD;
        
        double currentA = rangeForA.getRangeData().getCurrent();
        double currentB = rangeForB.getRangeData().getCurrent();
        double currentC = rangeForC.getRangeData().getCurrent();
        double currentD = rangeForD.getRangeData().getCurrent();
        
        CalculatorData calculatorData = new CalculatorData(currentA,currentB,currentC,currentD);
        if (rangeForA.areOk()&rangeForB.areOk()&rangeForC.areOk()&rangeForD.areOk()) areOk = true;
        else
        {
            
            areOk = false;
            massege += "A: " + rangeForA.getMassege() + "\n";
            massege += "B: " + rangeForB.getMassege() + "\n";;
            massege += "C: " + rangeForC.getMassege() + "\n";;
            massege += "D: " + rangeForD.getMassege() + "\n";;
        }
    }

    public String getMassege() {
        return massege;
    }

    public boolean isAreOk() {
        return areOk;
    }

    public Range getRangeForA() 
    {
        return rangeForA;
    }

    public Range getRangeForB() 
    {
        return rangeForB;
    }

    public Range getRangeForC() 
    {
        return rangeForC;
    }

    public Range getRangeForD() 
    {
        return rangeForD;
    }
    
    
}
