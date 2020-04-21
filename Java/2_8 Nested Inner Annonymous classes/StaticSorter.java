import java.util.Arrays;
import java.util.Comparator;

public class StaticSorter {
    static class CountryComparator implements Comparator<Auto> {
        @Override
        public int compare(Auto o1, Auto o2) {
            return o1.getCountry().compareTo(o2.getCountry());
        }
    }
    public Auto[] getSortedCopy(Auto[] arr) {
        Auto[] copy = Arrays.copyOf(arr, arr.length);
        Arrays.sort(copy, new CountryComparator());
        return copy;
    }
}
