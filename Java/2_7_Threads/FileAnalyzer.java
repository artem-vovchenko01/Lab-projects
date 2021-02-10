import java.io.*;

public class FileAnalyzer {
    public FileAnalyzer () {}

    public static String readFile (String fileName) throws IOException {
        StringBuilder str = new StringBuilder();
        try (FileReader fr = new FileReader(fileName)) {
            char[] buf = new char[1024];
            int read;
            while ( (read = fr.read(buf)) != -1 ) {
                for (int i = 0; i < read; i++) {
                    str.append(buf[i]);
                }
            }
        }
        return str.toString();
    }
}
