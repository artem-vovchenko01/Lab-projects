package Faculty;

import Student.Student;
import java.util.ArrayList;

public class FacultyData 
{
    private String name;
    private ArrayList<Student> students;

    public FacultyData(String name) {
        this.name = name;
        students = new ArrayList();
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<Student> getStudents() {
        return students;
    }
    
}
