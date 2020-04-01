import java.util.ArrayList;

public class HashTable <K, V> {
    private int size;
    private int pairNumber;
    private int capacity;
    private double loadFactor;
    private final int INIT_CAPACITY = 10;
    private final double MAX_LOAD_FACTOR = 0.7;
    private ArrayList<HashNode<K, V>> buckets;

    public HashTable() {
        buckets = new ArrayList<>();
        for (int i=0; i<INIT_CAPACITY; i++) {
            buckets.add(null);
        }
        capacity = INIT_CAPACITY;
    }

    public V get(K key) {
        HashNode<K, V> node =  buckets.get( hash(key) );
        while (node != null) {
            if (node.getKey() == key) {
                return node.getValue();
            }
            node = node.getNext();
        }
        return null;
    }

    public void add(K key, V value) {
        HashNode<K, V> node = new HashNode<>(key, value);
            int hash = hash(key);
            if (buckets.get(hash) == null) {
                buckets.set(hash, node);
                size++;
                pairNumber++;
                loadFactor = (double)size / capacity;
            } else {
                addToList(node, buckets.get(hash));
            }
        if (loadFactor > MAX_LOAD_FACTOR) {
            increaseTable();
        }
    }

    public boolean remove (K key) {
        int hash = hash(key);
        HashNode<K, V> node = buckets.get(hash);
        if (node == null) {
            return false;
        }
        if (node.getKey().equals(key)) {
            buckets.set(hash, node.getNext());
            if (buckets.get(hash) == null) {
                size--;
            }
            pairNumber--;
            return true;
        }
        HashNode<K, V> prev = node;
       while (node.getNext() != null) {
           node = node.getNext();
           if (node.getKey().equals(key)) {
               prev.setNext(node.getNext());
               pairNumber--;
               return true;
           }
           prev = prev.getNext();
       }
       return false;
    }

    public boolean isEmpty () {return size == 0;}

    public int size () {
        return pairNumber;
    }

    public String deepTraverse () {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < buckets.size(); i++) {
            str.append(i).append(" ");
            HashNode<K, V> node = buckets.get(i);
            if (node == null) {
                str.append("__empty__");
            } else {
                while (node != null) {
                    str.append(node.getValue().toString()).append(" ");
                    if (node.getNext() != null) {
                        node = node.getNext();
                    } else {
                        break;
                    }
                }
            }
            str.append("\n");
        }
        return str.toString();
    }

    public ArrayList<HashNode<K, V>> getEntries () {
        ArrayList<HashNode<K, V>> result = new ArrayList<>();
        for (HashNode<K, V> node : buckets) {
            while (node != null) {
                result.add(node);
                node = node.getNext();
            }
        }
        return result;
    }

    public ArrayList<K> getKeys () {
        ArrayList<K> result = new ArrayList<>();
        for (HashNode<K, V> node : buckets) {
            while (node != null) {
                result.add(node.getKey());
                node = node.getNext();
            }
        }
        return result;
    }

    public ArrayList<V> getUniqueValues () {
        ArrayList<V> result = new ArrayList<>();
        for (HashNode<K, V> node : buckets) {
            while (node != null) {
                if (! result.contains(node.getValue())) {
                    result.add(node.getValue());
                }
                node = node.getNext();
            }
        }
        return result;
    }

    private void increaseTable() {
        capacity *= 2;
        ArrayList<HashNode<K, V>> temp = buckets;
        buckets = new ArrayList<>();
        for (int i=0; i<capacity; i++) {
            buckets.add(null);
        }
        size = 0;
        pairNumber = 0;
        for (HashNode<K, V> node : temp) {
            while (node != null) {
                add(node.getKey(), node.getValue());
                node = node.getNext();
            }
        }
        loadFactor = (double)size / capacity;
    }

    private void addToList (HashNode<K, V> node, HashNode<K, V> head) {
        while (true) {
            if (head.getKey().equals(node.getKey())) {
                head.setValue(node.getValue());
                return;
            }
            if (head.getNext() != null) {
                head = head.getNext();
            } else {
                break;
            }
        }
        head.setNext(node);
        pairNumber++;
    }

    private int hash (K key) {
        return Math.abs(key.hashCode() % capacity);
    }

    @Override
    public String toString() {
        if (size == 0) {
            return "{}";
        }
        StringBuilder result = new StringBuilder("{");
        ArrayList<HashNode<K, V>> entries = getEntries();
        for (HashNode<K, V> entry : entries) {
            result.append(entry.toString()).append(", ");
        }
        return result.append("\b\b}").toString();
    }
}
