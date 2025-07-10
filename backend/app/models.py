from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Boolean, JSON, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from enum import Enum as PyEnum
import uuid

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class UserRole(str, PyEnum):
    FARMER = "farmer"
    VLE = "vle"
    NGO_ADMIN = "ngo_admin"
    EXPERT = "expert"

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=generate_uuid)
    phone_number = Column(String(15), unique=True, nullable=False, index=True)
    name = Column(String(100), nullable=True)
    role = Column(Enum(UserRole), nullable=False)
    language = Column(String(10), default="en")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    farmer_profile = relationship("FarmerProfile", back_populates="user", uselist=False)
    issues = relationship("Issue", back_populates="reported_by_user")
    assigned_issues = relationship("Issue", back_populates="assigned_to_user")

class FarmerProfile(Base):
    __tablename__ = "farmer_profiles"

    id = Column(String, primary_key=True, default=generate_uuid)
    user_id = Column(String, ForeignKey("users.id"), unique=True, nullable=False)
    address = Column(String(255), nullable=True)
    village = Column(String(100), nullable=True)
    district = Column(String(100), nullable=True)
    state = Column(String(100), nullable=True)
    pincode = Column(String(10), nullable=True)
    land_area = Column(Float, nullable=True)  # in acres
    crops = Column(JSON, default=list)  # List of crops grown
    
    # Relationships
    user = relationship("User", back_populates="farmer_profile")

class IssueStatus(str, PyEnum):
    REPORTED = "reported"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class IssuePriority(str, PyEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Issue(Base):
    __tablename__ = "issues"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    status = Column(Enum(IssueStatus), default=IssueStatus.REPORTED)
    priority = Column(Enum(IssuePriority), default=IssuePriority.MEDIUM)
    category = Column(String(100), nullable=True)
    location = Column(JSON, nullable=True)  # GeoJSON format
    reported_by = Column(String, ForeignKey("users.id"), nullable=False)
    assigned_to = Column(String, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    reported_by_user = relationship("User", foreign_keys=[reported_by], back_populates="issues")
    assigned_to_user = relationship("User", foreign_keys=[assigned_to], back_populates="assigned_issues")
    updates = relationship("IssueUpdate", back_populates="issue")

class IssueUpdate(Base):
    __tablename__ = "issue_updates"

    id = Column(String, primary_key=True, default=generate_uuid)
    issue_id = Column(String, ForeignKey("issues.id"), nullable=False)
    status = Column(Enum(IssueStatus), nullable=False)
    notes = Column(String(1000), nullable=True)
    created_by = Column(String, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    issue = relationship("Issue", back_populates="updates")
    created_by_user = relationship("User")

class GovernmentScheme(Base):
    __tablename__ = "government_schemes"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String(255), nullable=False)
    description = Column(String(2000), nullable=True)
    eligibility_criteria = Column(JSON, nullable=True)
    benefits = Column(JSON, nullable=True)
    documents_required = Column(JSON, nullable=True)
    application_process = Column(String(1000), nullable=True)
    website_url = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class TrainingModule(Base):
    __tablename__ = "training_modules"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    content = Column(JSON, nullable=True)  # Can store rich text or structured content
    duration_minutes = Column(Integer, nullable=True)
    language = Column(String(10), default="en")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class SuccessStory(Base):
    __tablename__ = "success_stories"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String(255), nullable=False)
    description = Column(String(2000), nullable=True)
    farmer_id = Column(String, ForeignKey("users.id"), nullable=False)
    location = Column(JSON, nullable=True)  # GeoJSON format
    before_images = Column(JSON, nullable=True)  # List of image URLs
    after_images = Column(JSON, nullable=True)  # List of image URLs
    is_featured = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    farmer = relationship("User")
