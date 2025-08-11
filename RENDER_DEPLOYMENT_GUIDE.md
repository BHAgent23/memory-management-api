# Memory Management API - Render Deployment Guide

## 🚀 Quick Deployment Steps

### 1. Prepare Your Repository
Make sure your `memory_management` folder is in a Git repository that Render can access.

### 2. Create New Web Service on Render
1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your repository
4. Configure the service:

### 3. Service Configuration
```
Name: memory-management-api
Environment: Python 3
Region: Oregon (or your preferred region)
Branch: main (or your deployment branch)
Root Directory: Backend/memory_management
Build Command: pip install -r requirements.txt
Start Command: python start.py
```

### 4. Environment Variables
Set these environment variables in Render:

**Required:**
- `MONGODB_URL` - Your MongoDB connection string
- `MEMORY_API_KEYS` - Comma-separated API keys for authentication

**Optional (with defaults):**
- `MEMORY_DB_NAME` - Database name (default: "gurukul")
- `MEMORY_RETENTION_DAYS` - Memory retention period (default: "365")
- `MEMORY_API_WORKERS` - Number of workers (default: "1")

### 5. MongoDB Setup
You'll need a MongoDB database. Options:
- **MongoDB Atlas** (recommended): Free tier available
- **Render PostgreSQL**: If you want to modify the code to use PostgreSQL
- **External MongoDB**: Any MongoDB instance accessible via URL

### 6. Health Check
Once deployed, verify the service at:
```
https://your-service-name.onrender.com/memory/health
```

### 7. API Documentation
Access the interactive API docs at:
```
https://your-service-name.onrender.com/memory/docs
```

## 🔧 Troubleshooting

### Common Issues:
1. **Database Connection**: Ensure MONGODB_URL is correct and accessible
2. **Port Issues**: Render automatically sets the PORT environment variable
3. **Import Errors**: The start.py script handles Python path issues

### Logs:
Check Render logs for detailed error information if deployment fails.

## 📋 Next Steps
After successful deployment:
1. Test the health endpoint
2. Test API endpoints using the docs interface
3. Update other services to use the new Memory Management API URL
4. Configure authentication keys for production use

## 🔗 Service URLs
- Health Check: `/memory/health`
- API Docs: `/memory/docs`
- ReDoc: `/memory/redoc`

## 🛡️ Security Notes
- Set strong API keys in production
- Consider IP whitelisting if needed
- Monitor usage and set up alerts
