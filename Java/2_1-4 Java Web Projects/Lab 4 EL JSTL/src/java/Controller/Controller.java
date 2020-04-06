package Controller;

import Faculty.Faculty;
import Faculty.FacultyData;
import Institute.Institute;
import Institute.InstituteData;
import Student.Student;
import Student.StudentData;
import java.io.IOException;
import java.util.ArrayList;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Controller extends HttpServlet {

    RequestProcessor requestProcessor;  
   
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException 
    {
        requestProcessor = new RequestProcessor(request, response);
        String[] query = requestProcessor.getCommand().split(":");
        String command = query[0];
        switch (command)
        {
            case "Create institute":
                createInstitute(request);
                break;
            case "Create faculty":
                createFaculty(request, query);
                break;
            case "Add student":
                addStudent(request, query);
                break;
        }
        request.getRequestDispatcher("index.jsp").forward(request, response);
    }

    private void createInstitute (HttpServletRequest request) {
                ArrayList<Institute> institutes = requestProcessor.getListOfInstitutes();
                Institute newInstitute = new Institute(requestProcessor.getDataForInstitute());
                institutes.add(newInstitute);
                this.getServletContext().setAttribute("listOfInstitutes", institutes);
    }
    
    private void createFaculty (HttpServletRequest request, String[] query) {
                 Institute institute = requestProcessor.getCurrentInstitute(query);
                 FacultyData data = requestProcessor.getDataForFaculty();
                 Faculty faculty = new Faculty(data);
                 institute.addFaculty(faculty);
    }
    
    private void addStudent (HttpServletRequest request, String[] query) {
                Faculty faculty = requestProcessor.getCurrentFaculty(query);
                StudentData studentData = requestProcessor.getDataForStudent();
                if (studentData == null) {
                   request.setAttribute("mesg",requestProcessor.getMessage());
                } else {
                Student newStudent = new Student(studentData);
                faculty.addStudent(newStudent);
                }
    }
}
