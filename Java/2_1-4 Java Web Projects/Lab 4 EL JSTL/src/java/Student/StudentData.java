package Student;

public class StudentData
{
    private double meanScore;
    private int accountNumber;
    private String name;
    private String surname;

    public StudentData (String name, String surname, int accountNumber, double meanScore) 
    {
        this.name = name;
        this.surname = surname;
        this.accountNumber = accountNumber;
        this.meanScore = meanScore;
    }

    public double getMeanScore() 
    {
        return meanScore;
    }

    public int getAccountNumber()
    {
        return accountNumber;
    }

    public String getName() 
    {
        return name;
    }

    public String getSurname () 
    {
        return surname;
    }

    @Override
    public String toString() 
    {
        return getName();
    }

}

