package com.examples.devops.java;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

public class MainTests {

    @Test
    public void testMain() {
        // Forces to fail the test case
//        Assertions.assertEquals(1,2);
    }

    @Test
    public void testAddInt() {
        Main m = new Main();
        assertEquals(m.add(1, 1), 2);
    }

    @Disabled
    public void testAddIntFail() {
        Main m = new Main();
        assertEquals(m.add(5, 4), 3);
    }
}
