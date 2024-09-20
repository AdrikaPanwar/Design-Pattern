# Design Patterns in Python 🐍

Welcome to the repository where I demonstrate various design patterns in Python, focusing on **Factory**, **Prototype**, and **Adapter** design patterns. These patterns are essential for creating maintainable, scalable, and efficient software solutions.

## 1. Adapter Design Pattern 🔌

**Definition**:  
The Adapter Pattern is a structural pattern that allows objects with incompatible interfaces to work together. In Python, this can be done by defining an adapter class that translates calls from one interface to another.

### Problem Statement:
- We have an old class `OldSystem` with a method `specific_request()`.
- We have a new interface `NewSystem` that requires a method `request()`.
  
**Goal**:  
Allow objects of `OldSystem` to be used in place of `NewSystem` without modifying `OldSystem`.

🔗 **[View Adapter Design Pattern Code](https://github.com/AdrikaPanwar/Design-Pattern/blob/main/Adapter%20Design%20Pattern.py)**

---

## 2. Prototype Design Pattern 🧬

**Definition**:  
The Prototype Pattern is a creational pattern that allows an object to create a copy of itself without needing to know the details of how the copy is created. This is useful when creating objects is expensive or complex, and you want to clone objects instead of creating new ones from scratch.

### Problem Statement:
- We have different types of shapes, like circles and squares.
- Instead of creating new objects each time, we want to clone existing objects and modify them as needed.

**Goal**:  
Avoid the complexity and overhead of manually creating new objects from scratch and efficiently create new instances by copying existing ones.

🔗 **[View Prototype Design Pattern Code](https://github.com/AdrikaPanwar/Design-Pattern/blob/main/Prototype%20Design%20Pattern.py)**

---

## 3. Factory Design Pattern 🏭

**Definition**:  
The Factory Pattern is a creational pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. This pattern promotes loose coupling by separating the process of object creation from the business logic.

### Problem Statement:
- We have different types of animals: `Dog` and `Cat`.
- Instead of directly instantiating these classes, we use a factory method to create them.

**Goal**:  
Make the code more flexible and extensible when we want to add new types of animals without changing the client code.

🔗 **[View Factory Design Pattern Code](https://github.com/AdrikaPanwar/Design-Pattern/blob/main/Factory%20Design%20Pattern.py)**

---

## Why These Patterns? 🤔

I created these examples to help understand the practical use of common design patterns in Python. These patterns:
- Make code more **maintainable**.
- Allow for **flexibility** and **extensibility**.
- Promote **reusability** of code.
  
By implementing design patterns like **Adapter**, **Prototype**, and **Factory**, you can improve the architecture of your applications, making them easier to manage and scale as requirements grow.

---

🌟 **Feel free to explore the code and learn how these design patterns can be applied to real-world problems!** 🌟   


