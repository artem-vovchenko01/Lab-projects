import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Searcher implements Search {
    public List<Shop> isCheapestExists() {
        List<Shop> cheapest = new ArrayList();
        Iterator<Shop> shop_iter = Database.getShops().iterator();

        outerloop:
        while (shop_iter.hasNext()) {
            Shop shop = shop_iter.next();
            Iterator<Product> product_iter = shop.getProducts().iterator();

            if (!product_iter.hasNext()) {
                continue outerloop;
            }

            while (product_iter.hasNext()) {
                Product product = product_iter.next();
                if (shop.getPrice(product) >= product.getRecommendedPrice()) {
                    continue outerloop;
                }
            }











            cheapest.add(shop);
        }

        return cheapest;
    }
}
