import java.util.Map;
import java.util.Set;

public interface ShopInterface {
    void addProduct(Product product, int price);
    int getPrice(Product product);
    void setDiscount(Product product, int percent);
    Set<Map.Entry<Product, Integer>> getDiscounts();
}
