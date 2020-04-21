import java.util.ArrayList;

public class RedBlackTree<T extends Comparable<T>> {
    private enum Position {
        LL, LR, RR, RL
    }

    private Node<T> root;
    private int size;

    public RedBlackTree () {
        this.root = null;
        this.size = 0;
    }

    public boolean search (T obj) {
        Node<T> node = root;
        if (obj == null || node == null) {
            return false;
        }
        while (true) {
            if (obj.compareTo(node.getData()) == 0) {
                return true;
            }
            if (obj.compareTo(node.getData()) > 0) {
                if (node.getRight() != null) {
                    node = node.getRight();
                } else {
                    return false;
                }
            }

            if (obj.compareTo(node.getData()) < 0) {
                if (node.getLeft() != null) {
                    node = node.getLeft();
                } else {
                    return false;
                }
            }
        }
    }

    public Node<T> searchRef (T obj) {
        Node<T> node = root;
        if (obj == null || node == null) {
            return null;
        }
        while (true) {
            if (obj.compareTo(node.getData()) == 0) {
                return node;
            }

            if (obj.compareTo(node.getData()) > 0) {
                if (node.getRight() != null) {
                    node = node.getRight();
                } else {
                    return null;
                }
            }

            if (obj.compareTo(node.getData()) < 0) {
                if (node.getLeft() != null) {
                    node = node.getLeft();
                } else {
                    return null;
                }
            }
        }
    }


    public void add (T obj) {
        Node<T> node = place(obj);
        // if duplicate
        if (node == null) {
            return;
        } else {
            size += 1;
        }
        addHelper(node);
    }

    public void addAll (T[] objects) {
        for (T obj : objects) {
            add(obj);
        }
    }

    private void addHelper (Node<T> node) {
        // if was initialized as root
        if (node == root) {
            node.setClr(Color.BLACK);
            return;
        }
        // if parent is black - all ok
        Node<T> p = getParent(node);
        if (p.getClr() == Color.BLACK) {
            return;
        }
        // if uncle is RED
        Node<T> gp = getParent(p);
        Node<T> uncle = getUncle(gp, p, node);
        if (uncle != null) {
            if (uncle.getClr() == Color.RED) {
                recolor(gp, p, uncle);
                addHelper(gp);
                return;
            }
        }
        Position pos = definePosition(gp, p, node);
        switch (pos) {
            case LL:
                LLCase(gp, p, uncle, node);
                break;
            case LR:
                LRCase(gp, p, uncle, node);
                break;
            case RR:
                RRCase(gp, p, uncle, node);
                break;
            case RL:
                RLCase(gp, p, uncle, node);
                break;
        }
    }

    private void LLCase (Node<T> gp, Node<T> p, Node<T> uncle, Node<T> cur) {
        // gp Right Rotate
        Node<T> pRight = p.getRight();
        gp.setLeft(null);
        p.setRight(gp);
        gp.setLeft(pRight);
        p.setClr(Color.BLACK);
        gp.setClr(Color.RED);
        if (gp == root) {
            root = p;
        } else {
            Node<T> ggp = getParent(gp);
            if (ggp.getRight() == gp) {
                ggp.setRight(p);
            } else {
                ggp.setLeft(p);
            }
        }
    }

    private void LRCase (Node<T> gp, Node<T> p, Node<T> uncle, Node<T> cur) {
        // p Left Rotate
        gp.setLeft(cur);
        Node<T> curLeft = cur.getLeft();
        cur.setLeft(p);
        p.setRight(curLeft);
        // LLCase
        LLCase(gp, cur, uncle, p);
    }

    private void RRCase (Node<T> gp, Node<T> p, Node<T> uncle, Node<T> cur) {
        // gp Left Rotate
        Node<T> pLeft = p.getLeft();
        gp.setRight(null);
        p.setLeft(gp);
        gp.setRight(pLeft);
        p.setClr(Color.BLACK);
        gp.setClr(Color.RED);
        if (gp == root) {
            root = p;
        } else {
            Node<T> ggp = getParent(gp);
            if (ggp.getRight() == gp) {
                ggp.setRight(p);
            } else {
                ggp.setLeft(p);
            }
        }
    }

    private void RLCase (Node<T> gp, Node<T> p, Node<T> uncle, Node<T> cur) {
        // p Right Rotate
        gp.setRight(cur);
        Node<T> curRight = cur.getRight();
        cur.setRight(p);
        p.setLeft(curRight);
        // RRCase
        RRCase(gp, cur, uncle, p);
    }

    private void recolor (Node<T> gp, Node<T> p, Node<T> uncle) {
        gp.setClr(Color.RED);
        p.setClr(Color.BLACK);
        uncle.setClr(Color.BLACK);
    }

    private Node<T> getUncle (Node<T> gp, Node<T> p, Node<T> cur) {
        return gp.getLeft() == p ? gp.getRight() : gp.getLeft();
    }

    private Position definePosition (Node<T> gp, Node<T> p, Node<T> cur) {
        if (gp == null || p == null) {
            return null;
        }
        if (gp.getLeft() == p && p.getLeft() == cur) {
            return Position.LL;
        } else if (gp.getLeft() == p && p.getRight() == cur) {
            return Position.LR;
        } else if (gp.getRight() == p && p.getRight() == cur) {
            return Position.RR;
        } else return Position.RL;
    }

    private int getBranchHeight (Node<T> node) {
        if (node == null) {
            return 0;
        }
        ArrayList<Node<T>> level = new ArrayList<>();
        level.add(node);
        ArrayList<Node<T>> nextLevel = new ArrayList<>();
        int levelIdx = 0;
        while (level.size() > 0) {
            levelIdx ++;
            for (Node<T> currNode : level) {
                if (currNode.getLeft() != null) {
                    nextLevel.add(currNode.getLeft());
                }
                if (currNode.getRight() != null) {
                    nextLevel.add(currNode.getRight());
                }
            }
            level = nextLevel;
            nextLevel = new ArrayList<>();
        }
        return levelIdx;
    }

    public boolean remove (T obj) {
        Node<T> node = searchRef(obj);
        if (node == null) {
            return false;
        }
        BSTRemove(node);

        return true;
    }

    private void BSTRemoveRoot (Node<T> node) {
            switch (getNumberOfChildren(node)) {
                case 0:
                    this.root = null;
                    break;
                case 1:
                    if (node.getLeft() != null) {
                        this.root = node.getLeft();
                    } else {
                        this.root = node.getRight();
                    }
                    this.root.setClr(Color.BLACK);
                    break;
                case 2:
                    Node<T> min = findMinNode(node.getRight());
                    node.setData(min.getData());
                    BSTRemove(min);
                    break;
            }
    }

    private void BSTRemove (Node<T> node) {
        if (node == this.root) {
          BSTRemoveRoot(node);
          return;
        }
        Node<T> p = getParent(node);
        switch (getNumberOfChildren(node)) {
            case 0:
                colorFixup(node, null);
                if (p.getLeft() == node) {
                    p.setLeft(null);
                } else {
                    p.setRight(null);
                }

                break;
            case 1:
                Node<T> child = node.getLeft() != null ? node.getLeft() : node.getRight();
                colorFixup(node, child);
                if (p.getLeft() == node) {
                    p.setLeft(child);
                } else {
                    p.setRight(child);
                }
                break;
            case 2:
                Node<T> min = findMinNode(node.getRight());
                node.setData(min.getData());
                BSTRemove(min);
                break;
        }
    }

    private void colorFixup (Node<T> v, Node<T> u) {
        Color clrV = v.getClr();
        Color clrU;
        if (u == null) {
            clrU = Color.BLACK;
        } else {
            clrU = u.getClr();
        }
        // if u or v is red
        if (clrU == Color.RED || clrV == Color.RED) {
            if (u != null) {
                u.setClr(Color.BLACK);
                return;
            }
        }

        if (clrV == Color.BLACK && clrU == Color.BLACK) {
            v.setClr(Color.DOUBLE_BLACK);
            while (v.getClr() == Color.DOUBLE_BLACK && v != root) {
                // if at least on of sibling's children is red
                Node<T> sib = getSibling(v);
                if (sib.getClr() == Color.BLACK) {
                    Node<T> red = null;
                    if (sib.getLeft() != null) {
                        if (sib.getLeft().getClr() == Color.RED) {
                            red = sib.getLeft();
                        }
                    } else if (sib.getRight() != null) {
                        if (sib.getRight().getClr() == Color.RED) {
                            red = sib.getRight();
                        }
                    }
                    if (red == null) {
                        // if sibling has no red child
                    } else {
                        Node<T> p = getParent(sib);
                        Position pos = definePosition(p, sib, red);
                        // rotate
                    }
                }
            }

        }

    }

    private Node<T> getSibling(Node<T> node) {
        Node<T> p = getParent(node);
        return p.getLeft() == node ? p.getRight() : p.getLeft();
    }

    private Node<T> findMinNode (Node<T> root) {
        while (root.getLeft() != null) {
            root = root.getLeft();
        }
        return root;
    }

    private int getNumberOfChildren (Node<T> node) {
        if (node.getRight() == null && node.getLeft() == null) {
            return 0;
        } else if (node.getLeft() != null && node.getRight() != null) {
            return 2;
        } else return 1;
    }

    public boolean test (boolean showLevels) {
            Node<T> node = this.root;
            if (node == null) {
                return true;
            }
        ArrayList<Node<T>> level = new ArrayList<>();
        level.add(node);
        ArrayList<Node<T>> nextLevel = new ArrayList<>();
        Color nodeClr;
        int levelIdx = 0;
        while (level.size() > 0) {
            for (Node<T> currNode : level) {
                if (showLevels) {
                    for (int i = 0; i < levelIdx; i++) {
                        System.out.print("\t");
                    }
                    System.out.print(currNode.getData());
                    System.out.println(": " + currNode.getClr());
                }
                nodeClr = currNode.getClr();
                if (currNode.getLeft() != null) {
                    if (nodeClr == Color.RED && currNode.getLeft().getClr() == Color.RED) {
                        return false;
                    }
                    nextLevel.add(currNode.getLeft());
                }
                if (currNode.getRight() != null) {
                    if (nodeClr == Color.RED && currNode.getRight().getClr() == Color.RED) {
                        return false;
                    }
                    nextLevel.add(currNode.getRight());
                }
            }
            level = nextLevel;
            nextLevel = new ArrayList<>();
            levelIdx ++;
        }
            int maxPossibleSize;
            if (size == 0) {
                maxPossibleSize = 0;
            } else {
                maxPossibleSize = (int) (Math.pow(2, levelIdx) - 1);
            }

            int leftHeight = 0;
                    if (root.getLeft() != null) {
                        leftHeight = getBranchHeight(root.getLeft());
                    }
            int rightHeight = 0;
                    if (root.getRight() != null) {
                        rightHeight = getBranchHeight(root.getRight());
                    }

        int minTreeHeight = Math.min(rightHeight, leftHeight);

        System.out.println("Number of elements: " + size);
        System.out.println("Tree height (highest branch): " + levelIdx);
        System.out.println("Tree height (lowest branch): " + minTreeHeight);
        System.out.println("Maximum possible elements with this height (highest branch): " + maxPossibleSize);
            return true;
        }

    private Node<T> getParent(Node<T> node) {
        Node<T> tempNode = this.root;
        if (node == tempNode) {
            return null;
        }
        do {
            if (tempNode.getLeft() == node) {
                return tempNode;
            }
            if (tempNode.getRight() == node) {
                return tempNode;
            }
            // here >= is helpful when delete uses this function (case with 2 children)
            tempNode = node.getData().compareTo(tempNode.getData()) >= 0 ? tempNode.getRight() : tempNode.getLeft();
        } while (tempNode != null);
        return null;
    }

    private Node<T> place (T obj) {
        Node<T> newNode = new Node<>(obj);
        Node<T> node = root;
        if (node == null) {
            this.root = newNode;
            return newNode;
        }
        while (node != null) {
            if (obj.compareTo(node.getData()) == 0) {
                return null;
            }
            if (obj.compareTo(node.getData()) > 0) {
                if (node.getRight() == null) {
                    node.setRight(newNode);
                    return newNode;
                } else {
                    node = node.getRight();
                }
            }
            if (obj.compareTo(node.getData()) < 0) {
                if (node.getLeft() == null) {
                    node.setLeft(newNode);
                    return newNode;
                } else {
                    node = node.getLeft();
                }
            }
        }
        return null;
    }

    public String traverse () {
        StringBuilder result = new StringBuilder("{");
        Node<T> node = this.root;
        if (node == null) {
            return "{}";
        }
        ArrayList<Node<T>> level = new ArrayList<>();
        level.add(node);
        ArrayList<Node<T>> nextLevel = new ArrayList<>();
        while (level.size() > 0) {
            for (Node<T> currNode : level) {
                result.append(currNode.toString()).append(", ");
                if (currNode.getLeft() != null) {
                    nextLevel.add(currNode.getLeft());
                }
                if (currNode.getRight() != null) {
                    nextLevel.add(currNode.getRight());
                }
            }
            level = nextLevel;
            nextLevel = new ArrayList<>();
        }
        if (result.length() > 1) {
            result.append("\b\b}");
        } else {
            result.append("}");
        }
        return result.toString();
    }

    @Override
    public String toString () {
        return traverse();
    }
}