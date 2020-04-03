import java.util.ArrayList;
import java.util.Arrays;
import java.util.TreeSet;

public class QuickUF implements UF {
    protected int[] arr;
    private int size;
    public QuickUF (int size) {
        this.size = size;
        arr = new int[size];
        for (int i=0; i < size; i++) {
            arr[i] = i;
        }
    }

    @Override
    public boolean isConnected(int i, int j) {
        return root(i) == root(j);
    }

    @Override
    public void union(int i, int j) {
        i = root(i);
        j = root(j);
        if (i == j) {return;}
        arr[j] = i;
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

    protected int root (int i) {
        while (i != arr[i]) {
            i = arr[i];
        }
        return i;
    }

    @Override
    public String toString() {
        ArrayList<ArrayList<Integer>> components = new ArrayList<>();
        TreeSet<Integer> roots = new TreeSet<>();
        for (int i=0; i < size; i++) {
            int root = root(i);
            roots.add(root);
        }

        for (int root : roots) {
            ArrayList<Integer> component = new ArrayList<>();
            for (int i=0; i < size; i++) {
                int temp = root(i);
                if (temp == root) {
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

