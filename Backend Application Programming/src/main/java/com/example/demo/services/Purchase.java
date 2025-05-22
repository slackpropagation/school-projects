// Purchase.java
package com.example.demo.services;

import com.example.demo.entities.Cart;
import com.example.demo.entities.CartItem;
import com.example.demo.entities.Customer;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.PropertyNamingStrategies;
import com.fasterxml.jackson.databind.annotation.JsonNaming;
import lombok.Getter;
import lombok.Setter;

import java.util.Set;

@Getter @Setter
public class Purchase {
    private Customer customer;
    private Cart cart;
    @JsonProperty("cartItems")
    private Set<CartItem> cartItems;
}