#pragma once

#ifndef STUDENT_H
#define STUDENT_H

#include <iostream>
#include <string>
#include "degree.h"
#include "roster.h"

using namespace std;

class Student {
public:
    // Constructor
    Student(string ID, string first, string last, string email, int ageNum, int daysNums[], DegreeProgram degreeName);

    // Getters
    string getID() const;
    string getFirst() const;
    string getLast() const;
    string getEmail() const;
    int getAge() const;
    int* getDays();
    DegreeProgram getDegree();

    // Setters
    void setID(string studID);
    void setFirst(string studFirst);
    void setLast(string studLast);
    void setEmail(string studEmail);
    void setAge(int studAge);
    void setDays(int courseDays[]);
    void setDegree(DegreeProgram studDegree);

    // Print function
    void print();

private:
    string studentID;
    string firstName;
    string lastName;
    string emailAddress;
    int age;
    int days[3];
    DegreeProgram degree;
};

#endif // STUDENT_H