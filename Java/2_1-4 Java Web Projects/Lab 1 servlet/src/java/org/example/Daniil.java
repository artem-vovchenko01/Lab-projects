package org.example;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Daniil extends HttpServlet {
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
            
            String name = "Daniil";
            String link = "https://t.me/Kronuc";
            String bio = "Даниїл - студент, але ви це можете змінити. Люблю їсти і максимально полекшувати собі роботу. ";
            String profilePic = "images/kronuc.jpg";
            out.println(HTMLTemplateMaker.getTemplate(name, link, bio, profilePic));
       
        }
    }
    
}
