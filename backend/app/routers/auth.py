from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
import random
import string

from .. import models, schemas
from ..database import get_db
from .utils import (
    get_password_hash,
    create_access_token,
    verify_otp,
    ACCESS_TOKEN_EXPIRE_MINUTES
)

router = APIRouter(prefix="/api/auth", tags=["Authentication"])

# In-memory storage for OTPs (in production, use Redis or a database)
otp_store = {}

def generate_otp(length=6):
    """Generate a random OTP of specified length."""
    return ''.join(random.choices(string.digits, k=length))

@router.post("/send-otp", response_model=schemas.OTPResponse)
async def send_otp(request: schemas.OTPRequest, db: Session = Depends(get_db)):
    """
    Send OTP to the provided phone number.
    In a production environment, this would integrate with an SMS gateway.
    """
    # Check if user exists, if not create a new user
    user = db.query(models.User).filter(models.User.phone_number == request.phone_number).first()
    
    if not user:
        # Create a new user with default role as FARMER
        user = models.User(
            phone_number=request.phone_number,
            role=models.UserRole.FARMER,
            is_active=True
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    
    # Generate and store OTP (in production, send via SMS)
    otp = generate_otp()
    otp_store[request.phone_number] = {
        "otp": otp,
        "user_id": user.id
    }
    
    print(f"OTP for {request.phone_number}: {otp}")  # For development only
    
    return {"message": "OTP sent successfully", "otp": otp}  # In production, don't return OTP

@router.post("/verify-otp", response_model=schemas.Token)
async def verify_otp_endpoint(request: schemas.OTPVerification, db: Session = Depends(get_db)):
    """Verify OTP and return access token if valid."""
    stored_otp_data = otp_store.get(request.phone_number)
    
    if not stored_otp_data or not verify_otp(stored_otp_data["otp"], request.otp):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid OTP",
        )
    
    # Get user from database
    user = db.query(models.User).filter(models.User.id == stored_otp_data["user_id"]).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    
    # Clean up OTP
    otp_store.pop(request.phone_number, None)
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": str(user.id),
        "role": user.role.value
    }

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """OAuth2 compatible token login, get an access token for future requests"""
    # This is a placeholder. In a real app, you would validate username/password
    # For now, we'll just return a token for any user that exists
    user = db.query(models.User).filter(models.User.phone_number == form_data.username).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # In a real app, you would verify the password here
    # if not verify_password(form_data.password, user.hashed_password):
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Incorrect username or password",
    #         headers={"WWW-Authenticate": "Bearer"},
    #     )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": str(user.id),
        "role": user.role.value
    }

@router.get("/me", response_model=schemas.UserResponse)
async def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    """Get current user information"""
    return current_user
