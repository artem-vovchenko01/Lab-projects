import java.util.List;

public interface DBInterface {
    static void registerShop(Shop shop) {}
    static void registerProduct(Product product) {}
    static List<Product> getProducts() {
        return null;
    }
    static List<Shop> getShops() {
        return null;
    }
    }

