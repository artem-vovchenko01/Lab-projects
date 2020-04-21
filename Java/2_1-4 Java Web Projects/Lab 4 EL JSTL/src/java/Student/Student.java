package Student;

public class Student
{
    private StudentData studentData;

    public Student(StudentData studentData) {
        this.studentData = studentData;
    }

    public StudentData getStudentData() {
        return studentData;
    }
}
