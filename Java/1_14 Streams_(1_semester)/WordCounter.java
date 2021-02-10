import jdk.jfr.StackTrace;

import java.io.*;

public class WordCounter {
    static long numberOfWords (String filename) throws IOException {
        if (! new File(filename).exists()) {
            throw new FileNotFoundException("EXCEPTION! Can't find file specified. ");
        }
        String inputString = "";
        Reader reader = new FileReader(filename);
        BufferedReader br = new BufferedReader(reader);
        String line;
        while ( (line = br.readLine()) != null ) {
                inputString += line;
        }
        br.close();
        reader.close();

        String [] words = inputString.split("[\\W]");
        int count = 0;
        for (String str : words) {
            if (str.length() > 0){
                count++;
            }
        }

        return count;
    }
}
