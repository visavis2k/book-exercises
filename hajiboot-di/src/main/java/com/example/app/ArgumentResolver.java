package com.example.app;

import java.io.InputStream;

/**
 * Created by daniel on 2016-03-24.
 */
public interface ArgumentResolver {
    Argument resolve(InputStream stream);
}
