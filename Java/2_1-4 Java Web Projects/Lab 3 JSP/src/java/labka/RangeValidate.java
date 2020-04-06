package labka;

public class RangeValidate 
{
    static public Boolean checkRangeData(Range range) 
    {
        if (range.getRangeData().getBegin() < range.getRangeData().getEnd() && range.getRangeData().getStep() < 0) 
        {
            String massege;
            massege = "step should be positive";
            range.setMassege(massege);
            return false;
        } 
        else if (range.getRangeData().getBegin() > range.getRangeData().getEnd() && range.getRangeData().getStep() > 0) 
        {
            String massege;
            massege = "step should be negetive";
            range.setMassege(massege);
            return false;
        } 
        else if (range.getRangeData().getStep() == 0) 
        {
            String massege;
            massege = "step can't be 0";
            range.setMassege(massege);
            return false;
        } 
        else 
        {
            return true;
        }
    }
}
