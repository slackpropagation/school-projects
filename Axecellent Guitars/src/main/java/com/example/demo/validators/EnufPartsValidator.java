package com.example.demo.validators;

import com.example.demo.domain.Part;
import com.example.demo.domain.Product;
import com.example.demo.service.ProductService;
import com.example.demo.service.ProductServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;

import javax.validation.ConstraintValidator;
import javax.validation.ConstraintValidatorContext;

public class EnufPartsValidator implements ConstraintValidator<ValidEnufParts, Product> {

    @Autowired
    private ApplicationContext context;
    public static ApplicationContext myContext;

    @Override
    public void initialize(ValidEnufParts constraintAnnotation) {
        ConstraintValidator.super.initialize(constraintAnnotation);
    }

    @Override
    public boolean isValid(Product product, ConstraintValidatorContext constraintValidatorContext) {
        if (context == null) return true;
        myContext = context;

        ProductService repo = myContext.getBean(ProductServiceImpl.class);

        if (product.getId() != 0) {
            Product existingProduct = repo.findById((int) product.getId());

            int inventoryDifference = product.getInv() - existingProduct.getInv();

            for (Part part : existingProduct.getParts()) {
                int availableInventory = part.getInv();

                // Check if the new inventory level would cause the part inventory to go below minInventory
                if ((availableInventory - inventoryDifference) < part.getMinInventory()) {
                    return false;
                }
            }
        }

        return true;
    }
}