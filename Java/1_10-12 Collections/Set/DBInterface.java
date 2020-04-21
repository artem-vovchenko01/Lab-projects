import java.util.List;
import java.util.Set;

public interface DBInterface {
    static void registerShop(Shop shop) {}
    static void registerProduct(Product product) {}
    static Set<Product> getProducts() {
        return null;
    }
    static Set<Shop> getShops() {
        return null;
    }
    }

