package Institute;
import Faculty.Faculty;
import java.util.ArrayList;

public class Institute 
{
    private InstituteData instituteData;

    public Institute(InstituteData instituteData) 
    {
        this.instituteData = instituteData;
    }

    public void setInstituteData(InstituteData instituteData) 
    {
        this.instituteData = instituteData;
    }

    public InstituteData getInstituteData() 
    {
        return instituteData;
    }
    
    public void addFaculty(Faculty faculty)
    {
        ArrayList<Faculty> faculties = instituteData.getFaculties();
        faculties.add(faculty);
    }
    
    public Faculty getFaculty(String name)
    {
        for (Faculty faculty: instituteData.getFaculties())
        {
            if (faculty.getFacultyData().getName().equals(name)) return faculty;
        }
        return null;
    }
}
