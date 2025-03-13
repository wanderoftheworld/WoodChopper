class A {
    static {
        System.out.println("Static Block");
    }
}

public class Main {

    public static void example1() {
        // Check if the class is loaded
        try {
            Class<?> clazz = Class.forName("A");
            System.out.println("The class is loaded.");
        } catch (ClassNotFoundException e) {
            System.out.println("The class is not loaded.");
        }
    }


    public static void example2() {
        try {
            Class<?> class1 = Class.forName("ClassLoading_Interview_Example.ex1.A");
            System.out.println(class1);
        }catch(Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        example1();
        A a = new A();
    }
}
