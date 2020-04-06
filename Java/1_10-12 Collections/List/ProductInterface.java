import java.util.List;

public interface ProductInterface {
    void addShop(Shop shop);
    String getTitle();
    int findMinPrice();
    List<Shop> findBestShops();
}

