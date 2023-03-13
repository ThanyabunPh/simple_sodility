// SPDX-License-Idemtifier: MIT

pragma solidity ^0.8.0;

contract storageUserData{

    struct Employee {
        string firstName;
        string lastName;
        int256 salary;
    }

    Employee public employee;

    function setEmployee(string memory _firstName, string memory _lastName, int256 _salary) public {
        employee = Employee(_firstName, _lastName, _salary);
    }

    function retrieveAll() public view returns (Employee memory) {
        return employee;
    }

    function retrieveFname() public view returns (string memory) {
        return employee.firstName;
    }

    function retrieveLname() public view returns (string memory) {
        return employee.lastName;
    }

    function retrieveSalary() public view returns (uint256) {
        return uint256(employee.salary);
    }

}