import java.util.Arrays;

public class WeightedUF extends QuickUF {
    protected int[] sizes;

    public WeightedUF (int size) {
        super(size);
        sizes = new int[size];
        for (int i=0; i < size; i++) {
            sizes[i] = 1;
        }
    }

    @Override
    public void union(int i, int j) {
        i = super.root(i);
        j = super.root(j);
        if (i == j) {return;}
        if (sizes[i] > sizes[j]) {
            arr[j] = i;
            sizes[i] = sizes[i] + sizes[j];
        } else {
            arr[i] = j;
            sizes[j] = sizes[j] + sizes[i];
        }
    }

    @Override
    public String getRawRepr() {
        return Arrays.toString(sizes) + "\n" + super.getRawRepr();
    }
}
