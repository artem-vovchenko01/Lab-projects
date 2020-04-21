import java.util.ArrayList;
import java.util.Arrays;
import java.util.TreeMap;
import java.util.TreeSet;

public class SlowUF implements UF {
    private int[] arr;
    private int size;

    public SlowUF(int size) {
        this.size = size;
        arr = new int[size];
        for (int i=0; i < size; i++) {
            arr[i] = i;
        }
    }

    @Override
    public void union (int i, int j) {
        int iIdx = arr[i];
        int jIdx = arr[j];

        for (int k=0; k < size; k++) {
            if (arr[k] == iIdx || arr[k] == jIdx) {
                arr[k] = iIdx;
            }
        }
    }

    @Override
    public boolean isConnected (int i, int j) {
        return arr[i] == arr[j];
    }

    @Override
    public String getRawRepr() {
        int[] indices = new int[size];
        for (int i=0; i < size; i++) {
            indices[i] = i;
        }
        String str = Arrays.toString(indices);
        return str + "\n" + Arrays.toString(arr);
    }

    @Override
    public String toString() {
        ArrayList<ArrayList<Integer>> components = new ArrayList<>();
        TreeSet<Integer> ts = new TreeSet<>();
        for (int i=0; i < size; i++) {
            ts.add(arr[i]);
        }

        for (int idx : ts) {
            ArrayList<Integer> component = new ArrayList<>();
            for (int i=0; i < size; i++) {
                if (arr[i] == idx) {
                    component.add(i);
                }
            }
            components.add(component);
        }
        StringBuilder result = new StringBuilder();
        if (components.size() > 0) {
            result.append("{");
        }
        for (ArrayList<Integer> component : components) {
            if (component.size() > 0) {
                result.append("{");
                for (int el : component) {
                    result.append(el).append(", ");
                }
                result.append("\b\b}, ");
            }
        }
        if (result.length() > 0) {
            result.append("\b\b}");
        } else {
            return "{}";
        }
        return result.toString();
    }
}
