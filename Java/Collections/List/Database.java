import java.util.ArrayList;
import java.util.List;

public class Database implements DBInterface {
    private static List<Product> product_db = new ArrayList();
    private static List<Shop> shop_db = new ArrayList();
    public static void registerShop(Shop shop) {
        shop_db.add(shop);
    }
    public static void registerProduct(Product product) {
        product_db.add(product);
    }
    public static List<Product> getProducts() {
        return product_db;
    }
    public static List<Shop> getShops() {
        return shop_db;
    }
}
