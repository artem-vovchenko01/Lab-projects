import java.util.ArrayList;

public class BSTTable <K extends Comparable<K>, V> {
    private Node root;

    private class Node {
        Node(K key, V val, int count) {
            this.key = key;
            this.val = val;
            this.count = count;
        }
        Node left;
        Node right;
        K key;
        V val;
        int count;
    }

    public void put(K key, V val) {
       root = put(root, key, val);
    }

    private Node put(Node x, K key, V val) {
        if (x == null) return new Node(key, val, 1);
        int cmp = key.compareTo(x.key);
        if (cmp > 0) x.right = put(x.right, key, val);
        else if (cmp < 0) x.left = put(x.left, key, val);
        else x.val = val;
        x.count = 1 + size(x.left) + size(x.right);
        return x;
    }

    public V get(K key) {
        Node x = root;
        int cmp;
        while (x != null) {
            cmp = key.compareTo(x.key);
            if (cmp < 0) x = x.left;
            else if (cmp > 0) x = x.right;
            else return x.val;
        }
        return null;
    }

   public void deleteMin() {
        root = deleteMin(root);
   }

   private Node deleteMin(Node root) {
        if (root == null) return null;
        if (root.left == null) return root.right;
        root.left = deleteMin(root.left);
        root.count = 1 + size(root.left) + size(root.right);
        return root;
   }

   public void deleteMax() {
        root = deleteMax(root);
   }

   private Node deleteMax(Node root) {
        if (root == null) return null;
        if (root.right == null) return root.left;
        root.right = deleteMax(root.right);
        root.count = 1 + size(root.left) + size(root.right);
        return root;
   }

   public void delete(K key) {
        root = deleteRec(key, root);
   }

   private Node deleteRec(K key, Node root) {
        if (root == null) return null;
        int cmp = key.compareTo(root.key);
        if (cmp < 0) root.left = deleteRec(key, root.left);
        else if (cmp > 0) root.right = deleteRec(key, root.right);
        else {
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            K min = min(root.right);
            root.right = deleteMin(root.right);
            root.key = min;
        }
        root.count = 1 + size(root.left) + size(root.right);
        return root;
   }

   public K min() {
        return min(root);
   }

    private K min(Node root) {
        if (root == null) return null;
        if (root.left == null) return root.key;
        return min(root.left);
    }

    public K max() {
        return max(root);
    }

    private K max(Node root) {
        if (root == null) return null;
        if (root.right == null) return root.key;
        return max(root.right);
    }

    public K floor(K key) {
        Node floor = floor(root, key);
        if (floor == null) return null;
        else return floor.key;
    }

    private Node floor(Node root, K key) {
        if (root == null) return null;
        int cmp = key.compareTo(root.key);
        if (cmp == 0) return root;
        if (cmp < 0) return floor(root.left, key);
        Node bigger = floor(root.right, key);
        if (bigger != null) return bigger;
        else return root;
    }

    public K ceiling(K key) {
        Node ceil = ceiling(root, key);
        if (ceil == null) return null;
        else return ceil.key;
    }

    private Node ceiling(Node root, K key) {
       if (root == null) return null;
       int cmp = key.compareTo(root.key);
       if (cmp == 0) return root;
       if (cmp > 0) return ceiling(root.right, key);
       Node less = ceiling(root.left, key);
       if (less != null) return less;
       else return root;
    }

    public int rank(K key) {
        return rank(root, key);
    }

    private int rank(Node root, K key) {
        if (root == null) return 0;
        int cmp = key.compareTo(root.key);
        if (cmp > 0) return 1 + size(root.left) + rank(root.right, key);
        else if (cmp < 0) return rank(root.left, key);
        else return size(root.left);
    }

    public int size() {
        return size(root);
    }

    private int size(Node root) {
        if (root == null) return 0;
        return root.count;
    }

    public boolean isEmpty() {
        return size(root) == 0;
    }

    public Iterable<K> keys() {
        ArrayList<K> items = new ArrayList<>();
        addInorder(items, root);
        return items;
    }

    private void addInorder(ArrayList<K> items, Node root) {
        if (root == null) return;
        addInorder(items, root.left);
        items.add(root.key);
        addInorder(items, root.right);
    }

    @Override
    public String toString() {
        if (root == null) return "{}";
        StringBuilder str = new StringBuilder("{");
        inorder(str, root);
        return str.toString() + "\b\b}";
    }

    private void inorder(StringBuilder str, Node root) {
        if (root == null) return;
        inorder(str, root.left);
        str.append(root.key + " : " + root.val + ", ");
        inorder(str, root.right);
    }
}
