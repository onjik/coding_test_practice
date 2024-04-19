package org.example.p10825_국영수;
import java.util.*;
import java.io.*;
public class Main {
    public static void main(String args[]) throws Exception{
        var br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Student[] students = new Student[n];
        StringTokenizer tk;
        for (int i = 0; i < n; i++){
            tk = new StringTokenizer(br.readLine(), " ");
            Student s = new Student(
                    tk.nextToken(),
                    Integer.parseInt(tk.nextToken()),
                    Integer.parseInt(tk.nextToken()),
                    Integer.parseInt(tk.nextToken())
            );
            students[i] = s;
        }

        Arrays.stream(students).sorted().map(s -> s.name).forEach(System.out::println);
    }

    public static class Student implements Comparable<Student> {
        int kor;
        int eng;
        int math;
        String name;

        public Student(String name, int kor, int eng, int math){
            this.kor = kor;
            this.eng = eng;
            this.math = math;
            this.name = name;
        }


        // 앞에 있는게 작은거다
        public int compareTo(Student student){
            if (student.kor != this.kor){
                return student.kor - this.kor;
            }
            if (student.eng != this.eng){
                return this.eng - student.eng;
            }
            if (student.math != this.math){
                return student.math - this.math;
            }
            return this.name.compareTo(student.name);
        }

    }
}
