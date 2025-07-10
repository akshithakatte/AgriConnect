from pydantic import BaseModel, EmailStr, Field, validator
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

# Enums
class UserRole(str, Enum):
    FARMER = "farmer"
    VLE = "vle"
    NGO_ADMIN = "ngo_admin"
    EXPERT = "expert"

class IssueStatus(str, Enum):
    REPORTED = "reported"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"

class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

# Base schemas
class BaseSchema(BaseModel):
    class Config:
        from_attributes = True
        use_enum_values = True

# User schemas
class UserBase(BaseSchema):
    phone_number: str
    name: Optional[str] = None
    role: UserRole = UserRole.FARMER
    language: str = "en"

class UserCreate(UserBase):
    pass

class UserUpdate(BaseSchema):
    name: Optional[str] = None
    language: Optional[str] = None

class UserResponse(UserBase):
    id: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

# Farmer profile schemas
class FarmerProfileBase(BaseSchema):
    address: Optional[str] = None
    village: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None
    pincode: Optional[str] = None
    land_area: Optional[float] = None
    crops: List[str] = []

class FarmerProfileCreate(FarmerProfileBase):
    pass

class FarmerProfileUpdate(FarmerProfileBase):
    pass

class FarmerProfileResponse(FarmerProfileBase):
    user_id: str

# Issue schemas
class IssueBase(BaseSchema):
    title: str
    description: Optional[str] = None
    category: Optional[str] = None
    location: Optional[Dict[str, Any]] = None  # GeoJSON format
    priority: IssuePriority = IssuePriority.MEDIUM

class IssueCreate(IssueBase):
    pass

class IssueUpdate(BaseSchema):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[IssueStatus] = None
    priority: Optional[IssuePriority] = None
    assigned_to: Optional[str] = None
    category: Optional[str] = None
    location: Optional[Dict[str, Any]] = None

class IssueResponse(IssueBase):
    id: str
    status: IssueStatus
    reported_by: str
    assigned_to: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

# Issue update schemas
class IssueUpdateBase(BaseSchema):
    status: IssueStatus
    notes: Optional[str] = None

class IssueUpdateCreate(IssueUpdateBase):
    pass

class IssueUpdateResponse(IssueUpdateBase):
    id: str
    issue_id: str
    created_by: str
    created_at: datetime

# Government scheme schemas
class GovernmentSchemeBase(BaseSchema):
    title: str
    description: Optional[str] = None
    eligibility_criteria: Optional[Dict[str, Any]] = None
    benefits: Optional[Dict[str, Any]] = None
    documents_required: Optional[List[str]] = None
    application_process: Optional[str] = None
    website_url: Optional[str] = None

class GovernmentSchemeCreate(GovernmentSchemeBase):
    pass

class GovernmentSchemeUpdate(GovernmentSchemeBase):
    title: Optional[str] = None

class GovernmentSchemeResponse(GovernmentSchemeBase):
    id: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

# Training module schemas
class TrainingModuleBase(BaseSchema):
    title: str
    description: Optional[str] = None
    content: Optional[Dict[str, Any]] = None
    duration_minutes: Optional[int] = None
    language: str = "en"

class TrainingModuleCreate(TrainingModuleBase):
    pass

class TrainingModuleUpdate(TrainingModuleBase):
    title: Optional[str] = None
    language: Optional[str] = None

class TrainingModuleResponse(TrainingModuleBase):
    id: str
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

# Success story schemas
class SuccessStoryBase(BaseSchema):
    title: str
    description: Optional[str] = None
    location: Optional[Dict[str, Any]] = None
    before_images: Optional[List[str]] = None
    after_images: Optional[List[str]] = None
    is_featured: bool = False

class SuccessStoryCreate(SuccessStoryBase):
    pass

class SuccessStoryUpdate(SuccessStoryBase):
    title: Optional[str] = None
    is_featured: Optional[bool] = None

class SuccessStoryResponse(SuccessStoryBase):
    id: str
    farmer_id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

# Authentication schemas
class OTPRequest(BaseModel):
    phone_number: str = Field(..., min_length=10, max_length=15)

class OTPVerification(OTPRequest):
    otp: str = Field(..., min_length=4, max_length=6)

class OTPResponse(BaseModel):
    message: str
    otp: Optional[str] = None  # Only for development

class Token(BaseModel):
    access_token: str
    token_type: str
    user_id: str
    role: str

class TokenData(BaseModel):
    user_id: Optional[str] = None
    role: Optional[str] = None

# Generic response models
class MessageResponse(BaseModel):
    message: str

class PaginatedResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: List[Any]
