package labka;

public class TableLineData 
{
    private String a;
    private String b;
    private String c;
    private String d;
    private String result;

    public TableLineData(CalculatorData data) 
    {
        a = Double.toString(data.getA());
        b = Double.toString(data.getB());
        c = Double.toString(data.getC());
        d = Double.toString(data.getD());
        Calculator calculator = new Calculator(data);
        Double dobleResult = calculator.calculate();
        this.result = Double.toString(dobleResult);
    }

    public String getA() 
    {
        return a;
    }

    public String getB() 
    {
        return b;
    }

    public String getC() 
    {
        return c;
    }

    public String getD() 
    {
        return d;
    }

    public String getResult() 
    {
        return result;
    }
   
}
