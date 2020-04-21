package org.example;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Artem extends HttpServlet {
   @Override
    protected void doGet (HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        try (PrintWriter out = response.getWriter()) {
        
            String name = "Artem";
            String link = "https://t.me/artem_vovchenko";
            String bio = "Артем, студент КПІ. Народився в малому містечку Помічна, що на "
                    + "Кіровоградщині. Вивчаю програмування та інші інформаційні технології.<brGood luck усім відвідувачам нашого сайту :) ";
            String profilePic = "images/artem.jpg";
            out.println(HTMLTemplateMaker.getTemplate(name, link, bio, profilePic));
       
        }
    }

}
