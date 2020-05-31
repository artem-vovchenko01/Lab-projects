public class WeightedFlattenUF extends WeightedUF {
    public WeightedFlattenUF (int size) {
        super(size);
    }

    @Override
    protected int root(int i) {
        while (i != arr[i]) {
            arr[i] = arr[arr[i]]; // flatten the tree on each pass
            i = arr[i];
        }
        return i;
    }

    public int findMaxInComponent (int i) {
        i = root(i);
        int max = i;
        for (int j=0; j < arr.length; j++) {
            if (root(j) == i) {
                if (j > max) {
                    max = j;
                }
            }
        }
        return max;
    }
}
