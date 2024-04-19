package org.example;// 단순 정렬하라는 문제인듯
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

        Arrays.stream(students)
                .sorted(Comparator.comparing(Student::getKor).reversed() //이렇게 간단하게 뒤집을 수 있다.
                        .thenComparing(Student::getEng)
                        .thenComparing(Comparator.comparing(Student::getMath).reversed()) // 여기서 그냥 쌩으로 쓰면 위에꺼 까지 한번에 뒤집힌다.
                        .thenComparing(Student::getName))
                .forEach(s -> System.out.println(s.name));
    }

    public static class Student implements Comparable<Student> {
        int kor;
        int eng;
        int math;
        String name;

        public int getKor(){
            return kor;
        }
        public int getEng(){
            return eng;
        }
        public int getMath(){
            return math;
        }
        public String getName(){
            return name;
        }

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