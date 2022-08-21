CREATE TABLE EMPLOYEE(
EmployeeID INTEGER PRIMARY KEY ,
FirstName VARCHAR() NOT NULL,
MiddleName VARCHAR(),
LastName VARCHAR() NOT NULL,
JoinDate DATETIME ,
MonthlySalary BIGINT,
DeptID INTEGER NOT NULL,
FOREIGN KEY (DeptID) REFERENCES DEPARTMENT(DeptID)
  

);





CREATE TABLE DEPARTMENT(

DeptID INTEGER PRIMARY KEY,
  DeptName VARCHAR() NOT NULL,
  DeptCode VARCHAR(),
  ParentDeptID INTEGER NOT NULL,
  ManagerID INTEGER,
  Description VARCHAR(),
  Active Boolean NOT NULL
  


);




SELECT  EMPLOYEE.DeptID, SUM(EMPLOYEE.MonthlySalary *(EMPLOYEE.JoinDate-CURDATE()) AS Total_Earnings 
FROM EMPLOYEE 
LEFT JOIN DEPARTMENT
ON
EMPLOYEE.DeptID=DEPARTMENT.DeptID
GROUP BY EMPLOYEE.DeptID;
                             
                             
                             
SELECT  *, 
FROM EMPLOYEE 
LEFT JOIN DEPARTMENT
ON
EMPLOYEE.DeptID=DEPARTMENT.DeptID
DEPARTMENT.DeptName='Department Sales'
WHERE EXTRACT(MONTH from (EMPLOYEE.JoinDate-CURDATE()))>6;
                             
                             
                             
                             
SELECT E.EmployeeID,E.FirstName,(SELECT FirstName FROM EMPLOYEE WHERE EMPLOYEE.EmployeeID=D.ManagerID  ) AS MANAGER_NAME 
FROM EMPLOYEE AS E
LEFT JOIN DEPARTMENT AS D
ON
E.DeptID=D.DeptID;                             
                             
                            
                             
                            
                             
 





