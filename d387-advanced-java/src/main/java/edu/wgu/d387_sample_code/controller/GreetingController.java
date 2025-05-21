package edu.wgu.d387_sample_code.controller;

import edu.wgu.d387_sample_code.services.MultilingualGreeter;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Locale;

@CrossOrigin(origins = "*")
@RestController
public class GreetingController {

    @GetMapping("/welcome")
    public ResponseEntity<String> showWelcomeMessage(@RequestParam(value = "lang", required = false) String language) {
        if (language == null || language.isEmpty()) {
            MultilingualGreeter english = new MultilingualGreeter(Locale.US);
            MultilingualGreeter french = new MultilingualGreeter(Locale.CANADA_FRENCH);

            Thread t1 = new Thread(english);
            Thread t2 = new Thread(french);

            t1.start();
            t2.start();

            try {
                t1.join();
                t2.join();
                return new ResponseEntity<>(english.getMessage() + "\n" + french.getMessage(), HttpStatus.OK);
            } catch (InterruptedException e) {
                return new ResponseEntity<>("Error processing request", HttpStatus.INTERNAL_SERVER_ERROR);
            }
        }

        try {
            Locale locale = Locale.forLanguageTag(language);
            MultilingualGreeter greeter = new MultilingualGreeter(locale);
            Thread t = new Thread(greeter);
            t.start();
            t.join();
            return new ResponseEntity<>(greeter.getMessage(), HttpStatus.OK);
        } catch (InterruptedException e) {
            return new ResponseEntity<>("Error processing request", HttpStatus.INTERNAL_SERVER_ERROR);
        }
    }
}