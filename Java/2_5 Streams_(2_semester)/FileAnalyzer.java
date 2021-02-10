import java.io.*;

public class FileAnalyzer {
    private String fileName;
    public FileAnalyzer (String fileName) {
        this.fileName = fileName;
    }

    public String readFile () throws IOException {
        StringBuilder text = new StringBuilder();
        try (FileReader fr = new FileReader(fileName)) {
            char[] buf = new char[1024];
            int readed;
            while ((readed = fr.read(buf)) != -1) {
                for (int i = 0; i < readed; i++) {
                    text.append(buf[i]);
                    System.out.println("hello world");
                    
                }
            }
        }
        return text.toString();
    }
}
