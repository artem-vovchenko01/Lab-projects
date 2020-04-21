import java.util.Comparator;
import java.util.TreeSet;

public class AnnonymousSorter {
    public TreeSet<Auto> getAsTreeSet(Auto[] arr) {
        TreeSet<Auto> set = new TreeSet<>(new Comparator<Auto>() {
            @Override
            public int compare(Auto o1, Auto o2) {
                return Integer.compare(o1.getSpeed(), o2.getSpeed());
            }
        });
        for (Auto a : arr) {
            set.add(a);
        }
        return set;
    }
}
