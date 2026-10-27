-- Task 4A: Single-table inheritance with a discriminator.
-- Each machine must be either a CNC mill or an injection molder.

DROP TABLE IF EXISTS machine;

CREATE TABLE machine (
    machine_id INTEGER PRIMARY KEY,
    serial_no TEXT NOT NULL UNIQUE,
    site TEXT NOT NULL,
    installed DATE NOT NULL,

    machine_type TEXT NOT NULL
        CHECK (machine_type IN ('CNC_MILL', 'INJECTION_MOLDER')),

    -- CNC mill attributes
    spindle_speed_rpm INTEGER,
    tool_capacity INTEGER,

    -- Injection molder attributes
    clamping_force_kn INTEGER,
    injection_volume_cm3 INTEGER,

    -- Enforce disjointness and the correct subtype attributes.
    CHECK (
        (
            machine_type = 'CNC_MILL'
            AND spindle_speed_rpm > 0
            AND tool_capacity > 0
            AND clamping_force_kn IS NULL
            AND injection_volume_cm3 IS NULL
        )
        OR
        (
            machine_type = 'INJECTION_MOLDER'
            AND clamping_force_kn > 0
            AND injection_volume_cm3 > 0
            AND spindle_speed_rpm IS NULL
            AND tool_capacity IS NULL
        )
    )
);

-- Insert one valid example of each subtype.
INSERT INTO machine (
    machine_id, serial_no, site, installed, machine_type,
    spindle_speed_rpm, tool_capacity,
    clamping_force_kn, injection_volume_cm3
)
VALUES
    (1, 'SN-CNC-001', 'Plant A', '2024-01-15', 'CNC_MILL',
     12000, 24, NULL, NULL),
    (2, 'SN-IMM-001', 'Plant B', '2023-06-10', 'INJECTION_MOLDER',
     NULL, NULL, 800, 250);

-- Display the results.
SELECT machine_id, serial_no, machine_type,
       spindle_speed_rpm, tool_capacity,
       clamping_force_kn, injection_volume_cm3
FROM machine
ORDER BY machine_id;