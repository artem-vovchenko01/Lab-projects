package labka;

public class Range 
{
    private RangeData rangeData;
    private String massege = "no problem";
    
    public Range(RangeData range)
    {
        rangeData = range;
        RangeValidate.checkRangeData(this);
    }

    public void setMassege(String massege) {
        this.massege = massege;
    }

    public String getMassege() {
        return massege;
    }
    
    public boolean areOk()
    {
        if (massege.equals("no problem")) return true;
        else return false;
    }
    
    
    public boolean hasNext()
    {
        if (rangeData.getCurrent() <= rangeData.getEnd() && rangeData.getStep()>0)
        {
            return true;
        }
        else return rangeData.getCurrent()>= rangeData.getEnd() && rangeData.getStep()<0;
    }
    
    public double getNext()
    {   
        double result = rangeData.getCurrent();
        rangeData.setCurrent(rangeData.getCurrent() + rangeData.getStep());
        return result;
    }
    
    public void reloadRange()
    {
        rangeData.setCurrent(rangeData.getBegin());
    }
    
    public RangeData getRangeData () {
        return rangeData;
    }
}
