package org.example;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Dmytro extends HttpServlet {

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
         
            String name = "Dmytro";
            String link = "https://t.me/dmitrii_tarasov_24";
            String bio = "Пан Дмитро, зі столиці. Займаюсь спортом, вчу потроху programmimg";
            String profilePic = "images/dmytro.jpg";
            out.println(HTMLTemplateMaker.getTemplate(name, link, bio, profilePic));
       
        }
    }
    
}
