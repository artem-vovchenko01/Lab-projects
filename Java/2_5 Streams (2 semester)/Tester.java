import java.io.*;
import java.util.*;
public class Tester {
    public static void main(String[] args) throws IOException {
        FileAnalyzer fa = new FileAnalyzer("text.txt");
        String text = null;
        try {
            text = fa.readFile();
            TextAnalyzer analyzer = new TextAnalyzer(text);
            ArrayList<String> rarest = analyzer.rarestWords();
            for (String word : rarest) {
                System.out.println(word);
            }
        } catch (IOException ex) {
            System.out.println(ex);
        }
    }
}
