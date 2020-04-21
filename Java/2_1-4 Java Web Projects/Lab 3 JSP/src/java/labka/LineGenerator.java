package labka;

import java.util.ArrayList;
import java.util.Iterator;

public class LineGenerator 
{
    private LineGeneratorData lineGeneratorData;
    private ArrayList<CalculatorData> calculatorDataList;
    private Iterator<CalculatorData> calculatorDataIterator;

    public LineGeneratorData getLineGeneratorData() {
        return lineGeneratorData;
    }

    public LineGenerator(LineGeneratorData lineGeneratorData) 
    {
        calculatorDataList = new ArrayList();
        this.lineGeneratorData = lineGeneratorData;
        generateCalculatorDataList();
        calculatorDataIterator = calculatorDataList.iterator();
    }
    
    public boolean hasNext()
    {
        return calculatorDataIterator.hasNext();
    }
    
    public TableLineData getNext() {
        return new TableLineData( calculatorDataIterator.next() );
    }
    
    private void generateCalculatorDataList () {
        double a;
        double b;
        double c;
        double d;
        CalculatorData data;
        while (lineGeneratorData.getRangeForA().hasNext()) 
        {
            a = lineGeneratorData.getRangeForA().getNext();
            while (lineGeneratorData.getRangeForB().hasNext()) 
            {
                b = lineGeneratorData.getRangeForB().getNext();
                while (lineGeneratorData.getRangeForC().hasNext()) 
                {
                    c = lineGeneratorData.getRangeForC().getNext();
                    while (lineGeneratorData.getRangeForD().hasNext()) 
                    {
                        d = lineGeneratorData.getRangeForD().getNext();
                        data = new CalculatorData(a, b, c, d);
                        calculatorDataList.add(data);
                    }
                    lineGeneratorData.getRangeForD().reloadRange();
                }
                lineGeneratorData.getRangeForC().reloadRange();
            }
            lineGeneratorData.getRangeForB().reloadRange();
        }
    }
}
 