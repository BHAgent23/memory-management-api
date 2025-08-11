#!/usr/bin/env python3
"""
Test script to verify Memory Management API deployment on Render.
Run this after deployment to ensure everything is working correctly.
"""

import requests
import json
import sys
from datetime import datetime

def test_deployment(base_url, api_key=None):
    """Test the deployed Memory Management API."""
    
    print(f"🧪 Testing Memory Management API at: {base_url}")
    print("=" * 60)
    
    headers = {}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    
    # Test 1: Health Check
    print("1. Testing Health Check...")
    try:
        response = requests.get(f"{base_url}/memory/health", timeout=10)
        if response.status_code == 200:
            print("   ✅ Health check passed")
            print(f"   📊 Response: {response.json()}")
        else:
            print(f"   ❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Health check error: {e}")
        return False
    
    # Test 2: API Documentation
    print("\n2. Testing API Documentation...")
    try:
        response = requests.get(f"{base_url}/memory/docs", timeout=10)
        if response.status_code == 200:
            print("   ✅ API docs accessible")
        else:
            print(f"   ❌ API docs failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ API docs error: {e}")
    
    # Test 3: Create Memory (if API key provided)
    if api_key:
        print("\n3. Testing Memory Creation...")
        try:
            test_memory = {
                "user_id": "test_user_123",
                "persona_id": "test_persona_456",
                "content": "This is a test memory for deployment verification",
                "content_type": "text",
                "metadata": {
                    "tags": ["test", "deployment"],
                    "importance": 5,
                    "topic": "deployment_test"
                }
            }
            
            response = requests.post(
                f"{base_url}/memory",
                json=test_memory,
                headers=headers,
                timeout=10
            )
            
            if response.status_code == 201:
                print("   ✅ Memory creation successful")
                memory_data = response.json()
                memory_id = memory_data.get("memory_id")
                print(f"   📝 Created memory ID: {memory_id}")
                
                # Test 4: Retrieve Memory
                print("\n4. Testing Memory Retrieval...")
                response = requests.get(
                    f"{base_url}/memory/{memory_id}",
                    headers=headers,
                    timeout=10
                )
                
                if response.status_code == 200:
                    print("   ✅ Memory retrieval successful")
                    print(f"   📖 Retrieved content: {response.json().get('content', '')[:50]}...")
                else:
                    print(f"   ❌ Memory retrieval failed: {response.status_code}")
                
            else:
                print(f"   ❌ Memory creation failed: {response.status_code}")
                print(f"   📄 Response: {response.text}")
                
        except Exception as e:
            print(f"   ❌ Memory creation error: {e}")
    else:
        print("\n3. Skipping authenticated tests (no API key provided)")
    
    print("\n" + "=" * 60)
    print("🎉 Deployment test completed!")
    return True

if __name__ == "__main__":
    # Default to your Render URL (update this after deployment)
    default_url = "https://memory-management-api.onrender.com"
    
    if len(sys.argv) > 1:
        base_url = sys.argv[1]
    else:
        base_url = input(f"Enter your Render URL (default: {default_url}): ").strip()
        if not base_url:
            base_url = default_url
    
    # Optional API key for authenticated tests
    api_key = input("Enter API key for authenticated tests (optional): ").strip()
    if not api_key:
        api_key = None
    
    test_deployment(base_url, api_key)
