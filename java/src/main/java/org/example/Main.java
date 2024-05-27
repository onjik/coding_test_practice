package org.example;// 단순 정렬하라는 문제인듯

import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        System.out.println(list.getClass());
        System.out.println(list.getClass() == list2.getClass());

        GenericClass<String> genericClass = new GenericClass<>(String.class);
        System.out.println(genericClass.getMyType());

    }
    public static class GenericClass<T> {

        private final Class<T> type;

        public GenericClass() {
            this.type = type;
        }

        public Class<T> getMyType() {
            return this.type;
        }

        public boolean isNull(){
            return this.type == null;
        }

    }
}