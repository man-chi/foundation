package com.example;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class AppTest {

    @Test
    public void testIsPrime() {
        boolean prime = App.isPrime(5);
        assertTrue(prime);
    }

    @Test
    public void testIsOdd_positiveOddNumber() {
        assertTrue(App.isOdd(5));
    }

    @Test
    public void testIsOdd_negativeNumber() {
        assertFalse(App.isOdd(-7));
    }

    @Test
    public void testIsOdd_evenNumber() {
        assertFalse(App.isOdd(4));
    }

    @Test
    public void testIsOdd_zero() {
        assertFalse(App.isOdd(0));
    }
}
