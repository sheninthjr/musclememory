class Animal {
    String name;
    Animal(String _name) {
        this.name = _name;
    }
    void sound() {
        System.out.println("It is a " + name);
    }
}

class Dog extends Animal {
    Dog(String name) {
        super(name);    
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog("Dog");
        dog.sound();
    }
}