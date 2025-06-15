#include <iostream>
#include <vector>
#include <string>

using namespace std;

// Student structure
struct Student {
    int rollNo;
    string name;
    // Add other fields as needed
};

vector<Student> students;

void addStudent() {
    Student newStudent;
    cout << "Enter Roll Number: ";
    cin >> newStudent.rollNo;
    cout << "Enter Name: ";
    cin.ignore(); // Clear the input buffer
    getline(cin, newStudent.name);
    
    students.push_back(newStudent);
    cout << "✓ Student added successfully.\n";
}

void viewAllStudents() {
    if (students.empty()) {
        cout << "No students found.\n";
        return;
    }
    
    cout << "\n--- All Students ---\n";
    for (const auto& student : students) {
        cout << "Roll No: " << student.rollNo << ", Name: " << student.name << "\n";
    }
}

void searchStudent() {
    if (students.empty()) {
        cout << "No students found.\n";
        return;
    }
    
    int roll;
    cout << "Enter Roll Number to search: ";
    cin >> roll;
    
    for (const auto& student : students) {
        if (student.rollNo == roll) {
            cout << "✓ Student found - Roll No: " << student.rollNo << ", Name: " << student.name << "\n";
            return;
        }
    }
    cout << "✗ Student not found.\n";
}

void deleteStudent() {
    if (students.empty()) {
        cout << "No students found.\n";
        return;
    }
    
    int roll;
    cout << "Enter Roll Number to delete: ";
    cin >> roll;
    
    for (auto it = students.begin(); it != students.end(); ++it) {
        if (it->rollNo == roll) {
            students.erase(it);
            cout << "✓ Student deleted successfully.\n";
            return;
        }
    }
    cout << "✗ Student not found.\n";
}

int main() {
    int choice;
    
    while (true) {
        cout << "\n1. Add Student\n2. View All Students\n3. Search Student\n4. Delete Student\n5. Exit\nEnter your choice: ";
        cin >> choice;
        
        switch (choice) {
            case 1: 
                addStudent(); 
                break;
            case 2: 
                viewAllStudents(); 
                break;
            case 3: 
                searchStudent(); 
                break;
            case 4: 
                deleteStudent(); 
                break;
            case 5: 
                cout << "Exiting...\n";
                return 0;
            default: 
                cout << "Invalid choice. Please try again.\n";
        }
    }
    
    return 0;
}
