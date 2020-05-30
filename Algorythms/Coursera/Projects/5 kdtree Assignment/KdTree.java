import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.SET;
import edu.princeton.cs.algs4.StdDraw;

import java.awt.Color;

public class KdTree {
    private Node root;
    private int size;
    private static class Node {
        Node(Point2D p, RectHV r) {
            this.p = p;
            rect = r;
        }
        private Point2D p;      // the point
        private RectHV rect;    // the axis-aligned rectangle corresponding to this node
        private Node lb;        // the left/bottom subtree
        private Node rt;        // the right/top subtree
    }

    private SET<Point2D> set;
    public KdTree() {
        root = null;
    }

    public boolean isEmpty() {
        return root == null;
    }

    public int size() {
        return size;
    }

    public void insert(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        if (root == null) root = new Node(p, new RectHV(0, 0, 1, 1));
        Node cur = root;
        boolean xSplit = true;
        int cmp;
        boolean greater = false;
        while (true) {
            if (xSplit) cmp = Double.compare(p.x(), cur.p.x());
            else cmp = Double.compare(p.y(), cur.p.y());
            if (cur.p.x() == p.x() && cur.p.y() == p.y()) return;
            if (cmp < 0) {
                greater = false;
                if (cur.lb == null) break;
                else cur = cur.lb;
            } else {
                greater = true;
                if (cur.rt == null) break;
                else cur = cur.rt;
            }
            xSplit = !xSplit;
        }
        RectHV rect = null;
        if (greater && xSplit) rect = new RectHV(cur.p.x(), cur.rect.ymin(), cur.rect.xmax(), cur.rect.ymax());
        if (!greater && xSplit) rect = new RectHV(cur.rect.xmin(), cur.rect.ymin(), cur.p.x(), cur.rect.ymax());
        if (greater && !xSplit) rect = new RectHV(cur.rect.xmin(), cur.p.y(), cur.rect.xmax(), cur.rect.ymax());
        if (!greater && !xSplit) rect = new RectHV(cur.rect.xmin(), cur.rect.ymin(), cur.rect.xmax(), cur.p.y());

        Node newNode = new Node(p, rect);

        if (greater) cur.rt = newNode;
        else cur.lb = newNode;
        size++;
    }

    public boolean contains(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        boolean xSplit = true;
        if (root == null) return false;
        Node cur = root;
        int cmp;
        while (cur != null) {
            if (cur.p.x() == p.x() && cur.p.y() == p.y()) return true;
            if (xSplit) cmp = Double.compare(p.x(), cur.p.x());
            else cmp = Double.compare(p.y(), cur.p.y());
            if (cmp < 0) cur = cur.lb;
            else cur = cur.rt;
            xSplit = !xSplit;
        }
        return false;
    }

    public void draw() {
        if (root == null) return;
        boolean xSplit = true;
        Queue<Node> level = new Queue<>();
        Queue<Node> nextLevel = new Queue<>();
        level.enqueue(root);
        while (level.size() > 0) {
            for (Node n : level) {
                if (n.rt != null) nextLevel.enqueue(n.rt);
                if (n.lb != null) nextLevel.enqueue(n.lb);
                StdDraw.setPenColor(Color.BLACK);
                StdDraw.setPenRadius(0.01);
                n.p.draw();
                StdDraw.setPenRadius();
                if (xSplit) {
                    StdDraw.setPenColor(Color.RED);
                    StdDraw.line(n.p.x(), n.rect.ymin(), n.p.x(), n.rect.ymax());
                } else {
                    StdDraw.setPenColor(Color.BLUE);
                    StdDraw.line(n.rect.xmin(), n.p.y(), n.rect.xmax(), n.p.y());
                }
            }
            xSplit = !xSplit;
            level = nextLevel;
            nextLevel = new Queue<>();
        }
    }

    public Iterable<Point2D> range(RectHV rect) {
        if (rect == null) throw new IllegalArgumentException();
        Node cur = root;
        Queue<Point2D> q = new Queue<>();
        Queue<Node> level = new Queue<>();
        Queue<Node> nextLevel = new Queue<>();
        level.enqueue(root);
        while (level.size() > 0) {
            for (Node n : level) {
                if (rect.contains(n.p)) {
                    q.enqueue(n.p);
                }
                if (n.rt != null && n.rt.rect.intersects(rect)) nextLevel.enqueue(n.rt);
                if (n.lb != null && n.lb.rect.intersects(rect)) nextLevel.enqueue(n.lb);
            }
            level = nextLevel;
            nextLevel = new Queue<>();
        }
        return q;
    }

    public Point2D nearest(Point2D p) {
        if (p == null) throw new IllegalArgumentException();
        if (root == null) return null;
        Node cur = root;
        Queue<Node> level = new Queue<>();
        Queue<Node> nextLevel = new Queue<>();
        level.enqueue(root);
        Point2D min = root.p;
        while (level.size() > 0) {
            for (Node n : level) {
                double thisDist = n.p.distanceTo(p);
                if (min.distanceTo(p) > thisDist) min = n.p;
                if (n.rt != null && n.rt.rect.distanceTo(p) < min.distanceTo(p)) nextLevel.enqueue(n.rt);
                if (n.lb != null && n.lb.rect.distanceTo(p) < min.distanceTo(p)) nextLevel.enqueue(n.lb);
            }
            level = nextLevel;
            nextLevel = new Queue<>();
        }
        return min;
    }

    public static void main(String[] args) {

    }
}
