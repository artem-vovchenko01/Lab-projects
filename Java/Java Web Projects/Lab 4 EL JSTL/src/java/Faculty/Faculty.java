package Faculty;

import Student.Student;

public class Faculty 
{
    private FacultyData facultyData;

    public Faculty(FacultyData facultyData) {
        this.facultyData = facultyData;
    }

    public FacultyData getFacultyData() {
        return facultyData;
    }
    
    public void addStudent(Student student)
    {
        facultyData.getStudents().add(student);
    }
}
