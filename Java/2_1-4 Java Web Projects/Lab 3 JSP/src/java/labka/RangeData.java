package labka;

public class RangeData
{
    private double begin = 1;
    private double end = 3;
    private double step = 1;
    private double current;

    public RangeData() {
    }
    
    public RangeData(double begin, double end, double step)
    {
        this.begin = begin;
        this.end = end;
        this.step = step;
        this.current = begin;
    }

    public double getBegin() 
    {
        return begin;
    }

    public double getEnd() 
    {
        return end;
    }

    public double getStep() 
    {
        return step;
    }

    public double getCurrent() 
    {
        return current;
    }

    public void setCurrent(double current) 
    {
        this.current = current;
    }
    
    
}
