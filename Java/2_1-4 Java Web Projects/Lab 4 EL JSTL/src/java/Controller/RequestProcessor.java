package Controller;
import Faculty.Faculty;
import Faculty.FacultyData;
import Institute.Institute;
import Institute.InstituteData;
import Student.StudentData;
import java.util.ArrayList;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class RequestProcessor 
{
    private HttpServletRequest request;
    private HttpServletResponse response;
    private String message;

    public RequestProcessor(HttpServletRequest request, HttpServletResponse response) {
        this.request = request;
        this.response = response;
    }
    
    public String getCommand()
    {
        String command = request.getParameter("command");
        return command;
    }
    
    public Institute getCurrentInstitute (String[] query) {
        InstituteData data = new InstituteData (query[1]);
        return getInstitute(data);
    }
    
    public Faculty getCurrentFaculty (String[] query) {
        Institute institute = getCurrentInstitute(query);
        return institute.getFaculty(query[2]);
    }
        
    public InstituteData getDataForInstitute()
    {
        String instituteName = request.getParameter("instituteName");
        InstituteData instituteData = new InstituteData(instituteName);
        return instituteData;
    }
    
        public StudentData getDataForStudent()
    {
        StudentData studentData = null;
        String name = request.getParameter("name");
        String surname = request.getParameter("surname");
        String meanScoreStr = request.getParameter("meanScore");
        String accountNumberStr = request.getParameter("accountNumber");
        if (isValidStudentData(meanScoreStr, accountNumberStr)) 
        {
        double meanScore = Double.parseDouble(meanScoreStr);
        int accountNumber = Integer.parseInt(accountNumberStr);
        studentData = new StudentData(name, surname, accountNumber, meanScore);
        } 
        return studentData;
    }
        
    private boolean isValidStudentData (String meanScoreStr, String accountNumberStr) {
        Message mesg = DataValidator.validateMeanScore(meanScoreStr);
        if (! (mesg == Message.OK_MESG)) 
        {
            message = mesg.err;
            return false;
        }
           mesg = DataValidator.validateAccountNumber(accountNumberStr);
           if (! (mesg == Message.OK_MESG)) 
           {
            message = mesg.err;
            return false;
            }
           return true;
    }
        
    public FacultyData getDataForFaculty()
    {
        String name = request.getParameter("facultyName");
        FacultyData data = new FacultyData(name);
        return data;
    }

    public ArrayList<Institute> getListOfInstitutes()
    {
        ArrayList<Institute> institutes;
        if (request.getServletContext().getAttribute("listOfInstitutes") == null)
        {
            institutes = new ArrayList();
        }
        else
        {
            institutes = (ArrayList<Institute>) request.getServletContext().getAttribute("listOfInstitutes");
        }
        return institutes;
    }
    
    public Institute getInstitute(InstituteData data) 
    {
        ArrayList<Institute> listOfInstitute = getListOfInstitutes();
        for (Institute institute : listOfInstitute)
        {
            if (institute.getInstituteData().getName().equals(data.getName())) {return institute;}
        }
        return null;
    }
   
        public String getMessage () 
    {
        return message;
    }
    
}
