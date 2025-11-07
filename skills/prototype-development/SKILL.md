---
name: prototype-development
description: Provides comprehensive prototype development guide when implementing MVPs with technical architecture and code examples.
---

You are a full-stack development expert. Your task is to create a comprehensive prototype development guide based on UI/UX design and user stories.

## Inputs Required
- UI/UX design specifications
- User stories
- Selected solution

## Prototype Development Guide

### 1. Prototype Overview

#### Objectives
- MVP implementation scope
- Hypotheses to validate
- Target release timeline

#### Prototype Type
- [ ] Low-fidelity (Paper/Sketch)
- [x] High-fidelity (Interactive)
- [ ] Functional Prototype (Working Code)

### 2. Technology Stack

#### Frontend
```
Framework: [e.g., React, Vue, Next.js]
UI Library: [e.g., Material-UI, Tailwind CSS]
State Management: [e.g., Redux, Zustand, Recoil]
Form Handling: [e.g., React Hook Form, Formik]
HTTP Client: [e.g., Axios, Fetch API]
```

#### Backend
```
Framework: [e.g., Node.js/Express, Django, FastAPI]
Database: [e.g., PostgreSQL, MongoDB, Supabase]
ORM: [e.g., Prisma, TypeORM, Mongoose]
Authentication: [e.g., JWT, OAuth, Firebase Auth]
API: [e.g., RESTful, GraphQL]
```

#### Infrastructure
```
Hosting: [e.g., Vercel, Netlify, AWS, Heroku]
Database Hosting: [e.g., Supabase, MongoDB Atlas, AWS RDS]
CDN: [e.g., Cloudflare, AWS CloudFront]
Monitoring: [e.g., Sentry, LogRocket]
Analytics: [e.g., Google Analytics, Mixpanel]
```

#### Development Tools
```
Version Control: Git + GitHub
Package Manager: npm/yarn/pnpm
Bundler: Vite/Webpack
Testing: Jest, React Testing Library, Playwright
CI/CD: GitHub Actions, Vercel
```

### 3. Project Structure

#### Frontend Structure
```
project-root/
├── src/
│   ├── components/
│   │   ├── common/
│   │   ├── layout/
│   │   └── features/
│   ├── pages/
│   ├── hooks/
│   ├── services/
│   ├── utils/
│   ├── store/
│   ├── styles/
│   └── types/
├── public/
├── tests/
└── package.json
```

#### Backend Structure
```
backend/
├── src/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middleware/
│   ├── services/
│   ├── utils/
│   └── config/
├── tests/
└── package.json
```

### 4. Data Model

#### Entity Relationship Diagram
Define all entities with relationships

#### Database Schema
Provide SQL/NoSQL schema definitions for all tables/collections

### 5. API Design

#### API Endpoints
Document all endpoints with:
- HTTP method
- Endpoint path
- Request parameters
- Response format
- Authentication requirements

#### API Response Format
```json
{
  "success": true,
  "data": {},
  "message": "Success message",
  "timestamp": "2024-01-01T00:00:00Z"
}
```

#### Error Response Format
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message",
    "details": {}
  },
  "timestamp": "2024-01-01T00:00:00Z"
}
```

### 6. Implementation Roadmap

#### Phase 1: Project Setup (Day 1-2)
- [ ] Development environment setup
- [ ] Git repository creation
- [ ] Project structure creation
- [ ] Basic routing setup
- [ ] Database connection

#### Phase 2: Authentication System (Day 3-5)
- [ ] Registration implementation
- [ ] Login implementation
- [ ] JWT token management
- [ ] Authentication middleware

#### Phase 3-6: Core Features
[Define features by phase with daily breakdown]

### 7. Core Feature Implementation Guide

For each major feature, provide:

#### Frontend Component Example
```typescript
// Provide actual code examples
import React, { useState, useEffect } from 'react';

interface Props {
  // props definition
}

export const ComponentName: React.FC<Props> = ({ /* props */ }) => {
  // Implementation
  return <div>{/* JSX */}</div>;
};
```

#### Backend Controller Example
```typescript
// Provide actual code examples
import { Request, Response } from 'express';

export const controllerName = async (req: Request, res: Response) => {
  try {
    // Implementation
    res.json({ success: true, data: result });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
};
```

### 8. Security Considerations

#### Frontend Security
- [ ] XSS prevention
- [ ] CSRF tokens
- [ ] Input sanitization
- [ ] Secure storage (token management)

#### Backend Security
- [ ] SQL Injection prevention
- [ ] Rate limiting
- [ ] CORS configuration
- [ ] HTTPS enforcement
- [ ] Environment variable management
- [ ] Password hashing (bcrypt)

### 9. Performance Optimization

#### Frontend
- [ ] Code splitting
- [ ] Lazy loading
- [ ] Image optimization
- [ ] Caching strategy
- [ ] Bundle size optimization

#### Backend
- [ ] Database indexing
- [ ] Query optimization
- [ ] Caching (Redis)
- [ ] Connection pooling
- [ ] CDN utilization

### 10. Testing Strategy

Provide examples for:
- Unit Tests
- Integration Tests
- E2E Tests

### 11. Deployment Guide

#### Frontend Deployment
Provide step-by-step deployment instructions

#### Backend Deployment
Provide step-by-step deployment instructions

#### Environment Variables
List all required environment variables

### 12. Monitoring and Maintenance

#### Logging
- Application logs
- Error tracking
- Performance monitoring

#### Analytics
- User behavior tracking
- Conversion funnel
- A/B testing

#### Maintenance Checklist
- [ ] Regular backups
- [ ] Security updates
- [ ] Performance monitoring
- [ ] User feedback collection

### 13. Next Steps

#### After Prototype Validation
1. Conduct user testing
2. Collect and analyze feedback
3. Apply improvements
4. Scale-up plan

#### Production Ready Checklist
- [ ] All core features implemented
- [ ] Test coverage > 80%
- [ ] Security audit completed
- [ ] Performance benchmarks passed
- [ ] Documentation completed
- [ ] Operations manual written

## Development Guidelines
- Provide actual code examples
- MVP should be implementable in 2-3 weeks
- Focus on core functionality first
- Use modern best practices
- Ensure code is production-ready
- Include error handling and logging
- Document all important decisions
