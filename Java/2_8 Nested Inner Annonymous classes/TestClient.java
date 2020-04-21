import java.util.Random;
import java.util.TreeSet;

public class TestClient {
    public static void main(String[] args) {
        Auto[] autoArray = getRandomizedAutoArray(10);
        StaticSorter staticSorter = new StaticSorter();
        AnnonymousSorter anonSorter = new AnnonymousSorter();
        Auto[] sortedByCountry = staticSorter.getSortedCopy(autoArray);
        TreeSet<Auto> sortedBySpeed = anonSorter.getAsTreeSet(autoArray);
        System.out.println("Unsorted ");
        for (Auto a : autoArray) {
            System.out.println(a);
        }
        System.out.println("Sorted by country");
        for (Auto a : sortedByCountry) {
            System.out.println(a);
        }
        System.out.println("Sorted by speed");
        for (Auto a : sortedBySpeed) {
            System.out.println(a);
        }
    }

    static Auto[] getRandomizedAutoArray(int size) {
        Random r = new Random();
        Auto[] array  = new Auto[size];
        for (int i = 0; i < size; i++) {
            array[i] = new Auto(TestClient.randString(10), r.nextInt(100) + 1);
        }
        return array;
    }

    static String randString(int len) {
        StringBuilder str = new StringBuilder();
        Random r = new Random();
        int forBigLetter = r.nextInt(25) + 65;
        String bigLetter = String.valueOf((char) forBigLetter);
        str.append(bigLetter);
        for (int i = 0; i < len - 1; i++) {
            int forSmallLetter = r.nextInt(25) + 97;
            String smallLetter = String.valueOf((char) forSmallLetter);
            str.append(smallLetter);
        }
        return str.toString();
    }
}
