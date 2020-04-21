package labka;

import static java.lang.Double.NaN;

public class Calculator
{
    private CalculatorData data;
    
    public Calculator(CalculatorData data)
    {
        this.data = data;
    }
    
    public double calculate()
    {
        CalculatorValidate checker = new CalculatorValidate();
        if (checker.checkCalculatorData(data))
        {
            return Math.sqrt(Math.abs(Math.sin(data.getA()) - 4 * Math.log(data.getB()) / (Math.pow(data.getC(), data.getD()))));
        }
        else
        {
            return NaN;
        }
    }
    
}
