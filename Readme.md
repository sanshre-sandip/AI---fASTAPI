# 🚀 FastAPI = Starlette + Pydantic (Visual Explanation)

## 🧠 Core Idea

FastAPI is built by combining:

- ⚙️ Starlette → Web framework (request handling)
- 📦 Pydantic → Data validation (type safety)

---

## 🔷 Overall Architecture (Visual Flow)

```mermaid
flowchart TD

A[Client Request 🌐] --> B[Starlette ⚙️]
B --> C[FastAPI Layer 🚀]

C --> D[Pydantic Validation 📦]
D --> E{Data Valid?}

E -- Yes --> F[Your API Function 🧑‍💻]
E -- No --> G[Error Response ❌]

F --> H[Starlette Response System 📤]
H --> I[Client Response ✅]
