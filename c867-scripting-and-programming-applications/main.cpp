#include <iostream>
#include <string>

#include "degree.h"
#include "roster.h"
#include "student.h"

using namespace std;

int main() {
    // Display course and student info
    cout << "Course Title: C687 - Scripting and Programming" << endl;
    cout << "Programming Language used: C++" << endl;
    cout << "WGU Student ID: 000000000" << endl;
    cout << "Name: John Doe" << endl;

    // Raw student data
    const string studentData[] = {
        "A1,John,Smith,John1989@gm ail.com,20,30,35,40,SECURITY",
        "A2,Suzan,Erickson,Erickson_1990@gmailcom,19,50,30,40,NETWORK",
        "A3,Jack,Napoli,The_lawyer99yahoo.com,19,20,40,33,SOFTWARE",
        "A4,Erin,Black,Erin.black@comcast.net,22,50,58,40,SECURITY",
        "A5,John,Doe,john.doe@cartcurt.com,23,20,25,30,SOFTWARE"
    };

    int numberOfStudents = 5;

    // Create a Roster object with 5 slots
    Roster* classRoster = new Roster(numberOfStudents);

    // Parse each string and add students to the roster
    for (int i = 0; i < numberOfStudents; ++i) {
        classRoster->parseData(studentData[i]);
    }

    cout << endl;

    // Display all student information
    cout << "Displaying all students:" << endl;
    classRoster->printAll();
    cout << endl;

    // Display invalid email addresses
    cout << "Displaying invalid email addresses:" << endl;
    classRoster->printInvalidEmails();
    cout << endl;

    // Display average days per course for each student
    cout << "Displaying average days spent per class:" << endl;
    for (int i = 0; i < numberOfStudents; ++i) {
        classRoster->printAverageDaysInCourse(classRoster->classRosterArray[i]->getID());
    }
    cout << endl;

    // Filter students by SOFTWARE degree program
    cout << "Displaying students by SOFTWARE program:" << endl;
    classRoster->printByDegreeProgram(SOFTWARE);
    cout << endl;

    // Remove student with ID "A3"
    cout << "Removing student A3:" << endl;
    classRoster->remove("A3");
    cout << endl;

    // Show all students after removal
    cout << "Displaying all students:" << endl;
    classRoster->printAll();
    cout << endl;

    // Try removing A3 again to show error message
    cout << "Removing student A3 again:" << endl;
    classRoster->remove("A3");

    return 0;
}
