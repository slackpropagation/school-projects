package edu.wgu.d387_sample_code.controller;

import edu.wgu.d387_sample_code.services.TimeConversionService;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@CrossOrigin(origins = "*")
@RestController
public class TimeController {

    private final TimeConversionService service;

    public TimeController(TimeConversionService service) {
        this.service = service;
    }

    @GetMapping("/presentation")
    public Map<String, String> getTimes() {
        return service.getPresentationTimes();
    }
}