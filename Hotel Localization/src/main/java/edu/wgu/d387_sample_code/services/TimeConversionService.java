package edu.wgu.d387_sample_code.services;

import org.springframework.stereotype.Service;

import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.LinkedHashMap;
import java.util.Map;

@Service
public class TimeConversionService {

    public Map<String, String> getPresentationTimes() {
        ZonedDateTime easternTime = ZonedDateTime.of(2024, 4, 15, 18, 0, 0, 0, ZoneId.of("America/New_York"));

        Map<String, String> times = new LinkedHashMap<>();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm");

        times.put("ET", easternTime.format(formatter));
        times.put("MT", easternTime.withZoneSameInstant(ZoneId.of("America/Denver")).format(formatter));
        times.put("UTC", easternTime.withZoneSameInstant(ZoneId.of("UTC")).format(formatter));

        return times;
    }
}