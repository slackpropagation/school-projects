package com.example.demo.controllers;

import com.example.demo.domain.OutsourcedPart;
import com.example.demo.service.OutsourcedPartService;
import com.example.demo.service.OutsourcedPartServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

import javax.validation.Valid;

@Controller
public class AddOutsourcedPartController {

    @Autowired
    private ApplicationContext context;

    @GetMapping("/showFormAddOutPart")
    public String showFormAddOutsourcedPart(Model theModel) {
        OutsourcedPart part = new OutsourcedPart();
        theModel.addAttribute("outsourcedpart", part);
        return "OutsourcedPartForm";
    }

    @PostMapping("/showFormAddOutPart")
    public String submitForm(@Valid @ModelAttribute("outsourcedpart") OutsourcedPart part,
                             BindingResult bindingResult,
                             Model theModel) {

        theModel.addAttribute("outsourcedpart", part);

        // Custom inventory validation
        if (!part.isInventoryValid()) {
            bindingResult.rejectValue("inv", "error.outsourcedpart", "Inventory must be between minimum and maximum values.");
        }

        if (bindingResult.hasErrors()) {
            return "OutsourcedPartForm";
        }

        OutsourcedPartService repo = context.getBean(OutsourcedPartServiceImpl.class);
        OutsourcedPart existingPart = repo.findById((int) part.getId());
        if (existingPart != null) {
            part.setProducts(existingPart.getProducts());
        }

        repo.save(part);
        return "confirmationaddpart";
    }
}