import com.sun.source.tree.Tree;

import java.util.*;

public class Searcher implements Search {
    public Set<Shop> isCheapestExists() {
        Set<Shop> cheapest = new TreeSet();
        Iterator<Shop> shop_iter = Database.getShops().iterator();


            outerloop:while (shop_iter.hasNext()) {
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