-- Task 4B: Separate subtype tables.
-- Shared attributes are stored in machine.
-- Each subtype has its own table.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS cnc_mill;
DROP TABLE IF EXISTS injection_molder;
DROP TABLE IF EXISTS machine;

CREATE TABLE machine (
    machine_id INTEGER PRIMARY KEY,
    serial_no TEXT NOT NULL UNIQUE,
    site TEXT NOT NULL,
    installed DATE NOT NULL
);

CREATE TABLE cnc_mill (
    machine_id INTEGER PRIMARY KEY,
    spindle_speed_rpm INTEGER NOT NULL
        CHECK (spindle_speed_rpm > 0),
    tool_capacity INTEGER NOT NULL
        CHECK (tool_capacity > 0),
    FOREIGN KEY (machine_id)
        REFERENCES machine(machine_id)
        ON DELETE CASCADE
);

CREATE TABLE injection_molder (
    machine_id INTEGER PRIMARY KEY,
    clamping_force_kn INTEGER NOT NULL
        CHECK (clamping_force_kn > 0),
    injection_volume_cm3 INTEGER NOT NULL
        CHECK (injection_volume_cm3 > 0),
    FOREIGN KEY (machine_id)
        REFERENCES machine(machine_id)
        ON DELETE CASCADE
);

-- Prevent a machine from belonging to both subtypes.
CREATE TRIGGER cnc_mill_disjoint_insert
BEFORE INSERT ON cnc_mill
WHEN EXISTS (
    SELECT 1 FROM injection_molder
    WHERE machine_id = NEW.machine_id
)
BEGIN
    SELECT RAISE(ABORT, 'Machine cannot be both subtypes');
END;

CREATE TRIGGER injection_molder_disjoint_insert
BEFORE INSERT ON injection_molder
WHEN EXISTS (
    SELECT 1 FROM cnc_mill
    WHERE machine_id = NEW.machine_id
)
BEGIN
    SELECT RAISE(ABORT, 'Machine cannot be both subtypes');
END;

-- Insert two parent machines.
INSERT INTO machine
    (machine_id, serial_no, site, installed)
VALUES
    (1, 'SN-CNC-001', 'Plant A', '2024-01-15'),
    (2, 'SN-IMM-001', 'Plant B', '2023-06-10');

-- Assign each machine to exactly one subtype.
INSERT INTO cnc_mill
    (machine_id, spindle_speed_rpm, tool_capacity)
VALUES
    (1, 12000, 24);

INSERT INTO injection_molder
    (machine_id, clamping_force_kn, injection_volume_cm3)
VALUES
    (2, 800, 250);

-- Display both subtypes in one result.
SELECT m.machine_id, m.serial_no, 'CNC_MILL' AS machine_type,
       c.spindle_speed_rpm, c.tool_capacity,
       NULL AS clamping_force_kn, NULL AS injection_volume_cm3
FROM machine AS m
JOIN cnc_mill AS c ON c.machine_id = m.machine_id

UNION ALL

SELECT m.machine_id, m.serial_no, 'INJECTION_MOLDER',
       NULL, NULL,
       i.clamping_force_kn, i.injection_volume_cm3
FROM machine AS m
JOIN injection_molder AS i ON i.machine_id = m.machine_id

ORDER BY 1;