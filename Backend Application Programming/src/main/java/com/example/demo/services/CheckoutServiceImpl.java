package com.example.demo.services;

import com.example.demo.dao.CartRepository;
import com.example.demo.dao.CustomerRepository;
import com.example.demo.entities.Cart;
import com.example.demo.entities.CartItem;
import com.example.demo.entities.Customer;
import com.example.demo.entities.StatusType;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Set;
import java.util.UUID;

@Service
public class CheckoutServiceImpl implements CheckoutService {

    private final CustomerRepository customerRepository;
    private final CartRepository cartRepository;

    public CheckoutServiceImpl(CustomerRepository customerRepository, CartRepository cartRepository) {
        this.customerRepository = customerRepository;
        this.cartRepository = cartRepository;
    }

    @Override
    @Transactional
    public PurchaseResponse placeOrder(Purchase purchase) {

        Cart cart = purchase.getCart();
        Customer customer = purchase.getCustomer();
        Set<CartItem> cartItems = purchase.getCartItems();

        String orderTrackingNumber;

        if (!cartItems.isEmpty()) {
            orderTrackingNumber = UUID.randomUUID().toString();

            // assign tracking and status
            cart.setOrderTrackingNumber(orderTrackingNumber);
            cart.setStatus(StatusType.ordered);

            // attach items to cart
            cartItems.forEach(cart::add); // this assumes cart.add(item) sets both sides of the relationship
            cart.setCartItems(cartItems); // 💥 This is what was missing!
            cart.setId(null); // 💥 force Hibernate to treat this as a new Cart

            cartRepository.save(cart);
        } else {
            orderTrackingNumber = "Cart is empty.";
        }

        return new PurchaseResponse(orderTrackingNumber);
    }
    private String generateOrderTrackingNumber()
    {
        return UUID.randomUUID().toString();
    }
    }
