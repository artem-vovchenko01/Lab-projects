import java.util.ArrayList;
import java.util.HashMap;

public class TextAnalyzer {
    private final String ENG_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-#$%@*&^()+01234567890";
    private final String ARG_ERR = "There is a words that can't fit to English language rules";
    private String text;

    public TextAnalyzer (String text) {
        this.text = text;
    }

    public ArrayList<String> rarestWords ( ) {
        ArrayList<String> result = new ArrayList<>();
        HashMap<String, Integer> words = getWordMap();
        int min = minOccurrence(words);
        for (String word : words.keySet()) {
            if (words.get(word) == min) {
                result.add(word);
            }
        }
        return result;
    }

    private boolean checkEnglishWord (String word) {
        if (word.length() > 0) {
            for (char sym : word.toCharArray()) {
                if (!ENG_ALPHABET.contains(String.valueOf(sym))) {
                    throw new IllegalArgumentException(ARG_ERR);
                }
            }
        }  else {
            return false;
        }
        return true;
    }

    private HashMap<String, Integer> getWordMap () {
        HashMap<String, Integer> words = new HashMap<>();
        for (String word : text.split("[\\s,:.!?\"()]")) {
            if (checkEnglishWord(word)) {
                if (words.containsKey(word)) {
                    words.put(word, words.get(word) + 1);
                } else {
                    words.put(word, 0);
                }
            }
        }
        return words;
    }

    private int minOccurrence (HashMap<String, Integer> words) {
        int min = 0;
        for (int num : words.values()) {
            if (min == 0) {
                min = num;
            }
            if (num < min) {
                min = num;
            }
        }
        return min;
    }
}
