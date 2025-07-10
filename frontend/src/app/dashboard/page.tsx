'use client';

import { Card, CardBody, CardHeader, CardFooter, Divider, Button, Progress } from '@nextui-org/react';
import { MapPin, AlertCircle, MessageCircle, CheckCircle } from 'lucide-react';

export default function DashboardPage() {
  // Mock data - in a real app, this would come from your API
  const stats = {
    issuesReported: 12,
    issuesResolved: 8,
    pendingTasks: 3,
    communityMembers: 42,
  };

  const recentActivities = [
    { id: 1, title: 'New farming technique shared', type: 'info', time: '2 hours ago' },
    { id: 2, title: 'Issue #123 resolved', type: 'success', time: '1 day ago' },
    { id: 3, title: 'New government scheme announced', type: 'info', time: '2 days ago' },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold text-gray-900">Dashboard</h1>
        <p className="mt-1 text-sm text-gray-500">Welcome back! Here's what's happening with your farm.</p>
      </div>

      {/* Stats Grid */}
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Card className="p-4">
          <CardHeader className="flex items-center justify-between pb-2">
            <p className="text-sm font-medium text-gray-500">Issues Reported</p>
            <div className="rounded-lg bg-red-100 p-2">
              <AlertCircle className="h-5 w-5 text-red-600" />
            </div>
          </CardHeader>
          <CardBody className="py-2">
            <p className="text-2xl font-bold">{stats.issuesReported}</p>
            <p className="text-xs text-gray-500">+2 from last month</p>
          </CardBody>
        </Card>

        <Card className="p-4">
          <CardHeader className="flex items-center justify-between pb-2">
            <p className="text-sm font-medium text-gray-500">Issues Resolved</p>
            <div className="rounded-lg bg-green-100 p-2">
              <CheckCircle className="h-5 w-5 text-green-600" />
            </div>
          </CardHeader>
          <CardBody className="py-2">
            <p className="text-2xl font-bold">{stats.issuesResolved}</p>
            <p className="text-xs text-gray-500">+67% from last month</p>
          </CardBody>
        </Card>

        <Card className="p-4">
          <CardHeader className="flex items-center justify-between pb-2">
            <p className="text-sm font-medium text-gray-500">Community Members</p>
            <div className="rounded-lg bg-blue-100 p-2">
              <MessageCircle className="h-5 w-5 text-blue-600" />
            </div>
          </CardHeader>
          <CardBody className="py-2">
            <p className="text-2xl font-bold">{stats.communityMembers}</p>
            <p className="text-xs text-gray-500">+5 new this week</p>
          </CardBody>
        </Card>

        <Card className="p-4">
          <CardHeader className="flex items-center justify-between pb-2">
            <p className="text-sm font-medium text-gray-500">Active Regions</p>
            <div className="rounded-lg bg-purple-100 p-2">
              <MapPin className="h-5 w-5 text-purple-600" />
            </div>
          </CardHeader>
          <CardBody className="py-2">
            <p className="text-2xl font-bold">8</p>
            <p className="text-xs text-gray-500">+2 new regions</p>
          </CardBody>
        </Card>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {/* Recent Activities */}
        <Card className="p-4">
          <CardHeader>
            <h3 className="text-lg font-medium">Recent Activities</h3>
          </CardHeader>
          <Divider />
          <CardBody className="space-y-4">
            {recentActivities.map((activity) => (
              <div key={activity.id} className="flex items-start space-x-3">
                <div className="mt-1 flex-shrink-0">
                  <div className="h-2 w-2 rounded-full bg-blue-500"></div>
                </div>
                <div>
                  <p className="text-sm font-medium">{activity.title}</p>
                  <p className="text-xs text-gray-500">{activity.time}</p>
                </div>
              </div>
            ))}
          </CardBody>
          <CardFooter>
            <Button variant="light" className="text-sm font-medium text-blue-600">
              View all activities
            </Button>
          </CardFooter>
        </Card>

        {/* Progress */}
        <Card className="p-4">
          <CardHeader>
            <h3 className="text-lg font-medium">Your Progress</h3>
          </CardHeader>
          <Divider />
          <CardBody className="space-y-6">
            <div>
              <div className="mb-1 flex justify-between">
                <span className="text-sm font-medium">Profile Completion</span>
                <span className="text-sm text-gray-500">80%</span>
              </div>
              <Progress aria-label="Profile completion" value={80} className="h-2" />
            </div>
            <div>
              <div className="mb-1 flex justify-between">
                <span className="text-sm font-medium">Training Modules</span>
                <span className="text-sm text-gray-500">3/5 completed</span>
              </div>
              <Progress aria-label="Training progress" value={60} className="h-2" color="secondary" />
            </div>
            <div>
              <div className="mb-1 flex justify-between">
                <span className="text-sm font-medium">Community Engagement</span>
                <span className="text-sm text-gray-500">45%</span>
              </div>
              <Progress aria-label="Community engagement" value={45} className="h-2" color="success" />
            </div>
          </CardBody>
          <CardFooter>
            <Button variant="light" className="text-sm font-medium text-blue-600">
              View full report
            </Button>
          </CardFooter>
        </Card>
      </div>
    </div>
  );
}
