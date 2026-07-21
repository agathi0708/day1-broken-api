# Bug Fix Notes

## Bug 1: Authentication Fallback Vulnerability

### Problem
The authentication code returned the admin user whenever an exception occurred.

### Why it was a problem
This created a serious security vulnerability because invalid authentication attempts could gain administrator access.

### Fix
- Removed the fallback that returned the admin user.
- Added validation for:
  - Missing Authorization header
  - Invalid Bearer token format
  - Invalid token
  - User not found
- Returned HTTP 401 Unauthorized for invalid authentication.

---

## Bug 2: Mutable Default Argument

### Problem
The function used a mutable list as a default argument.

### Why it was a problem
Python reuses mutable default arguments between function calls, causing data from previous requests to leak into new requests.

### Fix
Changed the default argument from `[]` to `None` and created a new list inside the function.

---

## Bug 3: Blocking Call in Async Endpoint

### Problem
The endpoint used `time.sleep(2)` inside an asynchronous function.

### Why it was a problem
It blocked the event loop and prevented the server from handling other requests efficiently.

### Fix
Replaced it with `await asyncio.sleep(2)` to avoid blocking the event loop.