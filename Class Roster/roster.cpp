#include <iostream>
#include <string>

#include "degree.h"
#include "roster.h"
#include "student.h"

using namespace std;

// Constructors
Roster::Roster() {
    maxArraySize = 0;
    lastIndex = -1;
    classRosterArray = nullptr;
}

Roster::Roster(int maxArraySize) {
    this->maxArraySize = maxArraySize;
    lastIndex = -1;
    classRosterArray = new Student*[maxArraySize];
}

// Destructor
Roster::~Roster() {
    for (int i = 0; i < numStudents; ++i) {
        delete classRosterArray[i];
        classRosterArray[i] = nullptr;
    }
}

// Add student to classRosterArray
void Roster::add(string studentID, string firstName, string lastName, string emailAddress,
                 int age, int dayOne, int dayTwo, int dayThree, DegreeProgram degreeProgram) {
    
    int daysNum[3] = { dayOne, dayTwo, dayThree };

    classRosterArray[++lastIndex] = new Student(
        studentID, firstName, lastName, emailAddress, age, daysNum, degreeProgram
    );
}

// Remove student by ID
void Roster::remove(string studentID) {
    bool found = false;

    for (int i = 0; i <= lastIndex; ++i) {
        if (classRosterArray[i]->getID() == studentID) {
            found = true;

            // Swap with last and remove
            delete classRosterArray[i];
            classRosterArray[i] = classRosterArray[lastIndex];
            classRosterArray[lastIndex] = nullptr;
            --lastIndex;

            cout << "Student ID: " << studentID << " removed." << endl;
            break;
        }
    }

    if (!found) {
        cout << "Student ID: " << studentID << " not found." << endl;
    }
}

// Print all students
void Roster::printAll() {
    for (int i = 0; i <= lastIndex; ++i) {
        classRosterArray[i]->print();
    }
}

// Print average days in course for a given student
void Roster::printAverageDaysInCourse(string studentID) {
    for (int i = 0; i <= lastIndex; ++i) {
        if (classRosterArray[i]->getID() == studentID) {
            int* days = classRosterArray[i]->getDays();
            int avg = (days[0] + days[1] + days[2]) / 3;
            cout << studentID << ": " << avg << endl;
            return;
        }
    }
}

// Show invalid email addresses
void Roster::printInvalidEmails() {
    for (int i = 0; i <= lastIndex; ++i) {
        string email = classRosterArray[i]->getEmail();

        if (email.find(" ") != string::npos ||
            email.find('@') == string::npos ||
            email.find('.') == string::npos) {
            
            cout << email << " is not valid" << endl;
        }
    }
}

// Print all students with a specific degree
void Roster::printByDegreeProgram(DegreeProgram degreeProgram) {
    int count = 1;

    for (int i = 0; i <= lastIndex; ++i) {
        if (classRosterArray[i]->getDegree() == degreeProgram) {
            cout << count++ << " ";
            classRosterArray[i]->print();
        }
    }
}

// Parse student data
void Roster::parseData(const string studentData) {
    size_t start = 0;
    size_t end;

    end = studentData.find(",", start);
    string stuID = studentData.substr(start, end - start);

    start = end + 1;
    end = studentData.find(",", start);
    string stuFirst = studentData.substr(start, end - start);

    start = end + 1;
    end = studentData.find(",", start);
    string stuLast = studentData.substr(start, end - start);

    start = end + 1;
    end = studentData.find(",", start);
    string stuEmail = studentData.substr(start, end - start);

    start = end + 1;
    end = studentData.find(",", start);
    int stuAge = stoi(studentData.substr(start, end - start));

    start = end + 1;
    end = studentData.find(",", start);
    int dayOne = stoi(studentData.substr(start, end - start));

    start = end + 1;
    end = studentData.find(",", start);
    int dayTwo = stoi(studentData.substr(start, end - start));

    start = end + 1;
    end = studentData.find(",", start);
    int dayThree = stoi(studentData.substr(start, end - start));

    start = end + 1;
    string degreeStr = studentData.substr(start);

    DegreeProgram degreeType = SECURITY;
    if (degreeStr.find("SOFTWARE") != string::npos) {
        degreeType = SOFTWARE;
    } else if (degreeStr.find("NETWORK") != string::npos) {
        degreeType = NETWORK;
    }

    add(stuID, stuFirst, stuLast, stuEmail, stuAge, dayOne, dayTwo, dayThree, degreeType);
}