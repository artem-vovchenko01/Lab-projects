import java.io.*;
import java.util.Arrays;

public class Lab14 {
    public static void main (String[] args) {
        String path = "TestFile";
        try {
            WordCounter.numberOfWords("someFileNotExists");
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        try {
            Merger.unsplit("sourceCodeNotExists", "destination");
        } catch (IOException | IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
        try {
            System.out.println("Кількість слів у файлі " + new File(path).getAbsolutePath());
            System.out.println(WordCounter.numberOfWords(path));
            Merger.unsplit("source", "destination");
            System.out.println("Файли успішно скопійовані! ");
        } catch (IOException | IllegalArgumentException e) {
            e.printStackTrace();
        }

    }
}
