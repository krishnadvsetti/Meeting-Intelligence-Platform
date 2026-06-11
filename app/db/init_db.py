from app.db.database import engine
from app.models.meeting import Base

Base.metadata.create_all(bind=engine)

print("Database tables created!")