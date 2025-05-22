package edu.wgu.d387_sample_code.services;

import java.util.Locale;
import java.util.ResourceBundle;

public class MultilingualGreeter implements Runnable {
    private final Locale locale;
    private String message;

    public MultilingualGreeter(Locale locale) {
        this.locale = locale;
    }

    @Override
    public void run() {
        ResourceBundle bundle = ResourceBundle.getBundle("translation", locale);
        message = bundle.getString("welcome.message");
    }

    public String getMessage() {
        return message;
    }
}