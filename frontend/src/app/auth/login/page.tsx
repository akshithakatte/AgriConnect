'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Button, Input, Card, CardHeader, CardBody, CardFooter } from '@nextui-org/react';

export default function LoginPage() {
  const [phoneNumber, setPhoneNumber] = useState('');
  const [otp, setOtp] = useState('');
  const [showOtp, setShowOtp] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();

  const handleSendOtp = async () => {
    if (!phoneNumber) return;
    
    setIsLoading(true);
    try {
      // TODO: Call backend API to send OTP
      const response = await fetch('/api/auth/send-otp', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ phone_number: phoneNumber }),
      });
      
      if (response.ok) {
        setShowOtp(true);
      }
    } catch (error) {
      console.error('Error sending OTP:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleVerifyOtp = async () => {
    if (!otp) return;
    
    setIsLoading(true);
    try {
      // TODO: Call backend API to verify OTP
      const response = await fetch('/api/auth/verify-otp', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 
          phone_number: phoneNumber,
          otp: otp 
        }),
      });
      
      if (response.ok) {
        // Redirect to dashboard on successful login
        router.push('/dashboard');
      }
    } catch (error) {
      console.error('Error verifying OTP:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-50 to-blue-50">
      <Card className="w-full max-w-md p-6">
        <CardHeader className="flex flex-col items-center">
          <h1 className="text-2xl font-bold text-green-700">Welcome to AgriConnect</h1>
          <p className="text-gray-600 mt-2">Sign in to access your account</p>
        </CardHeader>
        
        <CardBody className="space-y-4">
          {!showOtp ? (
            <>
              <Input
                label="Phone Number"
                placeholder="+91 XXXXXXXXXX"
                value={phoneNumber}
                onChange={(e) => setPhoneNumber(e.target.value)}
                type="tel"
                isRequired
              />
              <Button
                color="primary"
                className="w-full"
                onClick={handleSendOtp}
                isLoading={isLoading}
              >
                Send OTP
              </Button>
            </>
          ) : (
            <>
              <p className="text-sm text-gray-600">
                We've sent an OTP to {phoneNumber}
              </p>
              <Input
                label="Enter OTP"
                placeholder="123456"
                value={otp}
                onChange={(e) => setOtp(e.target.value)}
                type="number"
                isRequired
              />
              <Button
                color="primary"
                className="w-full"
                onClick={handleVerifyOtp}
                isLoading={isLoading}
              >
                Verify OTP
              </Button>
              <Button
                variant="light"
                size="sm"
                onPress={() => {
                  setShowOtp(false);
                  setOtp('');
                }}
              >
                Change Phone Number
              </Button>
            </>
          )}
        </CardBody>
        
        <CardFooter className="flex justify-center mt-4">
          <p className="text-sm text-gray-600">
            By continuing, you agree to our Terms of Service and Privacy Policy
          </p>
        </CardFooter>
      </Card>
    </div>
  );
}
