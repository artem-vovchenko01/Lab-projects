import java.util.Set;

public interface ProductInterface {
    void addShop(Shop shop);
    String getTitle();
    int findMinPrice();
    Set<Shop> findBestShops();
}

