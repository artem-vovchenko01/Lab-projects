package Institute;
import Faculty.Faculty;
import java.util.ArrayList;

public class InstituteData 
{
    private String name;
    private ArrayList<Faculty> faculties;

    public InstituteData(String name) 
    {
        this.name = name;
        faculties = new ArrayList();
    }

    public void setName(String name) 
    {
        this.name = name;
    }

    public String getName() 
    {
        return name;
    }

    public ArrayList<Faculty> getFaculties() {
        return faculties;
    }
}
