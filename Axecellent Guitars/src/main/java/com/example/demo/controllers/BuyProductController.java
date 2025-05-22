package com.example.demo.controllers;

import com.example.demo.domain.Product;
import com.example.demo.repositories.ProductRepository;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class BuyProductController {

    private final ProductRepository productRepository;

    public BuyProductController(ProductRepository productRepository) {
        this.productRepository = productRepository;
    }

    @GetMapping("/buyProduct")
    public String buyProduct(@RequestParam("productId") int productID) {
        Product product = productRepository.findById(Long.valueOf(productID)).orElse(null);

        if (product != null && product.getInv() > 0) {
            product.setInv(product.getInv() - 1);
            productRepository.save(product);
            return "purchaseSuccessful";
        } else {
            return "outOfStock";
        }
    }
}