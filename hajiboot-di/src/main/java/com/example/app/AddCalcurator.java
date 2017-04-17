package com.example.app;

import org.springframework.stereotype.Component;

/**
 * Created by daniel on 2016-03-24.
 */
@Component
public class AddCalcurator implements Calculator {

    @Override
    public int calc(int a, int b) {
        return a + b;
    }

}
