class Node<T extends Comparable<T>> {
    private Node<T> right;
    private Node<T> left;
    private Color clr;
    private T data;
    public Node () {
        this.setClr(Color.RED);
        this.setLeft(null);
        this.setRight(null);
        this.setData(null);
    }

    public Node (T data) {
        this();
        this.setData(data);
    }

    public Node (T data, Color clr) {
        this(data);
        this.setClr(clr);
    }

    public Node<T> getRight() {
        return right;
    }

    public void setRight(Node<T> right) {
        this.right = right;
    }

    public Node<T> getLeft() {
        return left;
    }

    public void setLeft(Node<T> left) {
        this.left = left;
    }

    public Color getClr() {
        return clr;
    }

    public void setClr(Color clr) {
        this.clr = clr;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    @Override
    public String toString() {
        return this.data.toString();
    }
}