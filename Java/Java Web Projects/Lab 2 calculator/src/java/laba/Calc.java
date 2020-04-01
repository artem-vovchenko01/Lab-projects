package laba;
import java.util.HashMap;

class Calc
{
    private double a = 0;
    private double b = 0;
    private double c = 0;
    private double d = 0;
    private double result = 0;

    public Calc(HashMap<String, Double> numbers)
    {
        this.a = numbers.get("a");
        this.b = numbers.get("b");
        this.c = numbers.get("c");
        this.d = numbers.get("d");
    }
    
    public double calculate() throws IllegalArgumentException 
    {
        if (c <= 0) 
        {
            throw new IllegalArgumentException("IllegalArgumentException: параметр c повинен бути >= 0");
        }
         if (b <= 0) 
        {
            throw new IllegalArgumentException("IllegalArgumentException: параметр b повинен бути >= 0");
        }
        this.result = Math.sqrt(Math.abs(Math.sin(this.a) - 4 * Math.log(this.b) / (Math.pow(this.c, this.d))));
        return result;
    }
}
