package labka;

public class CalculatorValidate 
{
    public boolean checkCalculatorData(CalculatorData data)
    {
        if (data.getD() % 1 != 0 && data.getC() < 0)
        {
            return false;
        }
        else if (data.getB() <= 0)
        {
            return false;
        }
        else if (data.getC() == 0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
}
