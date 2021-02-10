import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
public class ConcurrentTextAnalyzer {
    private static final int FILE_NUMBER = 32;
    private final Thread[] threadPool;
    private HashMap<String, Integer> wordMap;
    private final int threads;
    private final String ENG_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz01234567890";
    public ArrayList<String> rarestWords () {
        ArrayList<String> words = new ArrayList<>();
        int minOccur = minOccurrence(wordMap);
        synchronized (wordMap) {
            for (String key : wordMap.keySet()) {
                if (wordMap.get(key) == minOccur) {
                    words.add(key);
                }
            }
        }
        return words;
    }
    public ConcurrentTextAnalyzer (int threads) throws InterruptedException {
        wordMap = new HashMap<>();
        threadPool = new Thread[threads];
        this.threads = threads;
        fillMap();
    }
    private void fillMap () throws InterruptedException {
        int times = FILE_NUMBER / threads;
        int[] currentFile = new int[1];
        currentFile[0] = 1;
        for (int i = 0; i < threads; i++) {
            threadPool[i] = new Thread(
                    () -> {
                        for (int j = 0; j < times; j++) {
                            try {
                                putToMap(FileAnalyzer.readFile("src/files/" + currentFile[0] + ".txt"));
                            } catch (IOException e) {
                                e.printStackTrace();
                            }
                            currentFile[0] = currentFile[0] + 1;
                        }
                    }
            );
        }
            for (Thread thread : threadPool) {
                thread.start();
            }
            for (Thread thread : threadPool) {
                thread.join();
            }
    }
    private void putToMap (String text)  {
        for (String word : text.split("[\\s:~!·;?\"()]")) {
            if (checkEnglishWord(word)) {
                synchronized (wordMap) {
                    if (wordMap.containsKey(word)) {
                        wordMap.put(word, wordMap.get(word) + 1);
                    } else {
                        wordMap.put(word, 1);
                    }
                }
            }
        }
    }
    private boolean checkEnglishWord (String word) {
        if (word.length() > 0) {
            for (char symbol : word.toCharArray()) {
                if (! ENG_ALPHABET.contains(String.valueOf(symbol))) {
                    return false;
                }
            }
        } else {
            return false;
        }
        return true;
    }
    private int minOccurrence (HashMap<String, Integer> words) {
        int min = 0;
        for (int value : words.values()) {
            if (min == 0 || value < min) {
                min = value;
            }
        }
        return min;
    }
}