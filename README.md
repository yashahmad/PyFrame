# PyFrame - Minimal Web Framework
---
*"REINVENTING THE WHEEL IS GREAT IF YOUR GOAL IS TO LEARN MORE ABOUT WHEELS."* -Jason Tauber
---

> ### Contents
1. Introduction & Getting Started
2. WSGI
3. HTTP request/response abstractions
4. Routing
5. Controllers, Views and Templates
6. Data storage
7. Closing thoughts

---
### Choices Web Framework Make
- "Do It Yourself" or "Best of Breed"?
- Pure WSGU or higher-level abstractions? What about WebSockets? HTTPS2?
- Framework or Library?
- Path-based or Object Oriented routing?
- MVC? MTV? WTF ? BBQ?
- Front-end or server-side templates?

---
### What is WSGI?
The Web Server Gateway Interface, defined by PEP 3333,.
WSGI defines a standard API for web servers(e.g. Gunicorn, uWSGI, Twisted, etc.) to connect and talk to web applications/frameworks(Django, Flask, etc.). WSGI is why you use any web server with any web application.