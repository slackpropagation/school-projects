#include <iostream>
#include <string>

#include "degree.h"
#include "roster.h"
#include "student.h"

using namespace std;


// Constructor
Student::Student(string ID, string first, string last, string email, int ageNum, int daysNum[], DegreeProgram degreeName) {
    
    this->studentID = ID;
    this->firstName = first;
    this->lastName = last;
    this->emailAddress = email;
    this->age = ageNum;

    for (int i = 0; i < 3; i++) {
        this->days[i] = daysNum[i];
    }

    this->degree = degreeName;
}

// Getters
string Student::getID() const {
    return this->studentID;
}

string Student::getFirst() const {
    return this->firstName;
}

string Student::getLast() const {
    return this->lastName;
}

string Student::getEmail() const {
    return this->emailAddress;
}

int Student::getAge() const {
    return this->age;
}

int* Student::getDays() {
    return this->days;
}

DegreeProgram Student::getDegree() {
    return this->degree;
}


// Setters
void Student::setID(string studID) {
    this->studentID = studID;
}

void Student::setFirst(string studFirst) {
    this->firstName = studFirst;
}

void Student::setLast(string studLast) {
    this->lastName = studLast;
}

void Student::setEmail(string studEmail) {
    this->emailAddress = studEmail;
}

void Student::setAge(int studAge) {
    this->age = studAge;
}

void Student::setDays(int courseDays[]) {
    for (int i = 0; i < 3; i++) {
        this->days[i] = courseDays[i];
    }
}

void Student::setDegree(DegreeProgram studDegree) {
    this->degree = studDegree;
}

void Student::print() {
    cout << studentID << "\t";
    cout << "First Name: " << firstName << "\t";
    cout << "Last Name: " << lastName << "\t";
    cout << "Age: " << age << "\t";
    cout << "daysInCourse: {";
    cout << days[0] << ", " << days[1] << ", " << days[2] << "} ";

    string deg = "Security";
    if (degree == NETWORK) {
        deg = "Network";
    }
    else if (degree == SOFTWARE) {
        deg = "Software";
    }
    
    cout << "Degree Program: " << deg << endl;
}