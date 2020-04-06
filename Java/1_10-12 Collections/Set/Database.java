import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Database implements DBInterface {
    private static Set<Product> product_db = new TreeSet(new CompareProduct());
    private static Set<Shop> shop_db = new TreeSet();
    public static void registerShop(Shop shop) {
        shop_db.add(shop);
    }
    public static void registerProduct(Product product) {
        product_db.add(product);
    }
    public static Set<Product> getProducts() {
        return product_db;
    }
    public static Set<Shop> getShops() {
        return shop_db;
    }
}
