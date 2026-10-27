"""Code-first data contract for the repaired maintenance schema."""

from datetime import date

from pydantic import BaseModel, Field, field_validator
from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
    UniqueConstraint,
    CheckConstraint,
    create_engine,
)
from sqlalchemy.schema import CreateTable


# --- 1. Application-level validation using Pydantic ---

class Machine(BaseModel):
    machine_id: int = Field(ge=1)
    serial_no: str = Field(min_length=3)
    site: str = Field(min_length=1)
    installed: date

    @field_validator("serial_no")
    @classmethod
    def serial_has_prefix(cls, value: str) -> str:
        if not value.startswith("SN-"):
            raise ValueError("Serial numbers must start with 'SN-'")
        return value


class MaintenanceJob(BaseModel):
    job_id: int = Field(ge=1)
    machine_id: int = Field(ge=1)
    technician: str = Field(min_length=1)
    done_on: date
    part_nos: list[str] = Field(default_factory=list)


# --- 2. Database-level constraints using SQLAlchemy ---

metadata = MetaData()

machine_t = Table(
    "machine",
    metadata,
    Column("machine_id", Integer, primary_key=True),
    Column("serial_no", String, nullable=False),
    Column("site", String, nullable=False),
    Column("installed", Date, nullable=False),
    UniqueConstraint("serial_no", name="uq_machine_serial"),
)

part_t = Table(
    "part",
    metadata,
    Column("part_no", String, primary_key=True),
    Column("description", String, nullable=False),
    Column("unit_price", Numeric(9, 2), nullable=False),
    CheckConstraint("unit_price >= 0", name="ck_part_price_nonnegative"),
)

maint_job_t = Table(
    "maint_job",
    metadata,
    Column("job_id", Integer, primary_key=True),
    Column(
        "machine_id",
        Integer,
        ForeignKey("machine.machine_id"),
        nullable=False,
    ),
    Column("technician", String, nullable=False),
    Column("done_on", Date, nullable=False),
)

# Junction table resolves the many-to-many relationship between
# maintenance jobs and parts.
job_part_t = Table(
    "job_part",
    metadata,
    Column(
        "job_id",
        Integer,
        ForeignKey("maint_job.job_id"),
        primary_key=True,
    ),
    Column(
        "part_no",
        String,
        ForeignKey("part.part_no"),
        primary_key=True,
    ),
    Column("quantity", Integer, nullable=False, default=1),
    CheckConstraint("quantity > 0", name="ck_job_part_quantity_positive"),
)


# --- 3. Generate and display the database DDL ---

if __name__ == "__main__":
    engine = create_engine("sqlite://")
    metadata.create_all(engine)

    for table in (machine_t, part_t, maint_job_t, job_part_t):
        print(str(CreateTable(table).compile(engine)).strip() + ";\n")

    engine.dispose()