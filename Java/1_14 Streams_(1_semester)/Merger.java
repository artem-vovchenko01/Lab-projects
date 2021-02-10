import java.io.*;

public class Merger {
    static void unsplit (String sourcePrefix, String destination) throws IOException {
        File target = new File(destination);
        if(! target.createNewFile()) {
            target.delete();
            target.createNewFile();
        }
        String currentPath = System.getProperty("user.dir");
        File currentDir = new File(currentPath);
        String [] contents = currentDir.list();
        int countMatches = 0;
        for (String file : contents) {
            if (file.matches( sourcePrefix + ".\\d\\d\\d")) {
                appendToFile(currentPath + "/" + file, destination);
                countMatches += 1;
            }
        }
        if (countMatches == 0) {
            throw new IllegalArgumentException("EXCEPTION! Can't find files with that prefix. ");
        }
    }

    static void appendToFile (String source, String destination) throws IOException {
        InputStream inp = new FileInputStream(source);
        OutputStream out = new FileOutputStream(destination, true);
        BufferedInputStream bufInp = new BufferedInputStream(inp);
        BufferedOutputStream bufOut = new BufferedOutputStream(out);
        byte [] buf = new byte[512];
        int readed;

        while ( (readed = bufInp.read(buf)) != -1 ) {
            bufOut.write(buf, 0, readed);
            bufOut.flush();
        }
        bufInp.close(); inp.close();
        bufOut.close(); out.close();
    }

}
