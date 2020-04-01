/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package org.example;

public class HTMLTemplateMaker {
      static public String getTemplate (String name, String link, String bio, String profilePic) {
            String template =  "<!DOCTYPE html>" +
           "<html>" +
           "<head>" +
            "<link rel=\"stylesheet\" type=\"text/css\" href=\"styles.css\">" +
          "<title>" + name + "</title>" +
            "</head>" +
          "<body>" +
            "<img class='profilePic' src='" + profilePic +"'/>" +
           "<p>" + bio + "</p>" +
          "</body>" +
         "</html>" +
            "<div align='center'><a href='" + link + "'>" +
           "<img src='images/tg_1.png' alt='contact via telegram' width='200' " +
            "</a></div>" ;
            
            return template;
       }
}
