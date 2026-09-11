# ⚡ FastAPI Practice

<div align="center">

### 🚀 Building Modern, Validated & Production-Ready Python APIs

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-API%20Development-009688?style=flat-square&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?style=flat-square)
![REST API](https://img.shields.io/badge/REST-API-FF6B35?style=flat-square)

</div>

---

## 📌 About

A hands-on **FastAPI practice repository** focused on learning the fundamentals of modern Python backend development.

The project covers **API development, CRUD operations, Pydantic validation, schemas, nested models, serialization, and structured request/response handling** — building a strong foundation for future **ML, GenAI, RAG, and Agentic AI backends**.

---

## 🧩 What I Practiced

### ⚡ FastAPI Fundamentals

- Creating FastAPI applications
- Defining API routes and endpoints
- Handling HTTP requests and responses
- Path parameters
- Query parameters
- Request bodies
- Response models
- HTTP methods
- API status codes
- Automatic API documentation

### 🔄 CRUD Operations

Implemented the fundamentals of **CRUD-based API design**:

| Operation | HTTP Method | Purpose |
|---|---|---|
| 🟢 Create | `POST` | Create new data |
| 🔵 Read | `GET` | Retrieve data |
| 🟡 Update | `PUT / PATCH` | Modify existing data |
| 🔴 Delete | `DELETE` | Remove data |

This helped build an understanding of how real-world REST APIs manage resources.

### 🛡️ Pydantic & Data Validation

- Pydantic models
- Field validation
- Custom field validators
- Model validation
- Type validation
- Required & optional fields
- Default values
- Nested models
- Validating incoming API data

### 📦 Serialization & Data Handling

- Serialization
- Deserialization
- JSON handling
- Converting models to structured data
- Request/response data transformation
- Schema-based responses

### 🧱 API Schemas & Models

Practice with separating data structures for different API purposes:

```text
Client Request
      ↓
Pydantic Schema
      ↓
Validation
      ↓
API Logic
      ↓
Response Schema
      ↓
JSON Response
