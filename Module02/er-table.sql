-- Task B: Machine and Sensor (1:N)

-- Create Machine table
CREATE TABLE Machine (
    Machine_ID INT PRIMARY KEY,
    Machine_Name VARCHAR(50)
);

-- Create Sensor table
CREATE TABLE Sensor (
    Sensor_ID INT PRIMARY KEY,
    Sensor_Type VARCHAR(50),
    Machine_ID INT NOT NULL,
    FOREIGN KEY (Machine_ID) REFERENCES Machine(Machine_ID)
);

-- Insert one machine
INSERT INTO Machine (Machine_ID, Machine_Name)
VALUES (1, 'Machine A');

-- Insert two sensors
INSERT INTO Sensor (Sensor_ID, Sensor_Type, Machine_ID)
VALUES (101, 'Temperature', 1);

INSERT INTO Sensor (Sensor_ID, Sensor_Type, Machine_ID)
VALUES (102, 'Pressure', 1);

-- Count sensors per machine
SELECT
    m.Machine_ID,
    m.Machine_Name,
    COUNT(s.Sensor_ID) AS Total_Sensors
FROM Machine m
LEFT JOIN Sensor s
    ON m.Machine_ID = s.Machine_ID
GROUP BY m.Machine_ID, m.Machine_Name;