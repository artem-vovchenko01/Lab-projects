import java.util.*;

public class Product implements ProductInterface {
    private String title;
    private int recommendedPrice;
    private Set<Shop> shops = new HashSet<Shop>();
    public Product(String title, int price) throws EmptyTitle, IncorrectPrice {
        if (title.length() == 0) {
            throw new EmptyTitle();
        }
        if (price <= 0) {
            throw new IncorrectPrice();
        }
        this.title = title;
        this.recommendedPrice = price;
        Database.registerProduct(this);
    }
    @Override
    public void addShop(Shop shop) {
        shops.add(shop);
    }

    @Override
    public int findMinPrice () {
        int min_price = 1_000_000;
        for (Shop shop : shops) {
            if (min_price > shop.getPrice(this)) {
                min_price = shop.getPrice(this);
            }
        }
        return min_price;
    }

    @Override
    public Set<Shop> findBestShops () {
        int price = findMinPrice();
        Set<Shop> best_shops = new HashSet<Shop>();
        Iterator shop_iter = shops.iterator();
        while (shop_iter.hasNext()) {
            Shop shop = (Shop) shop_iter.next();
            if (price == shop.getPrice(this)) {
                best_shops.add(shop);
            }
        }
        return best_shops;
    }

    @Override
    public String getTitle() {
        return title;
    }

    public int getRecommendedPrice() {
        return recommendedPrice;
    }

    @Override
    public String toString() {
        return title;
    }

}
