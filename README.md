# 🎟️ Ticket-Master

Ticket-Master is a FastAPI-powered backend application that integrates with the [Ticketmaster Discovery API](https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/) to fetch public events. It allows users to authenticate using Auth0 and save personal favorite events.

---

## 🚀 Features

- 🔐 Third-party authentication via **Auth0**
- 🎫 Fetch public events from the **Ticketmaster API**
- 💾 Save and retrieve personal favorite events
- ⚡️ Async backend using **FastAPI** and **SQLAlchemy**
- 🐬 MySQL database
- 🐳 Dockerized with Docker Compose

---

## 🛠️ Setup & Run (with Docker Compose)

### 1. Clone the repository

```bash
git clone https://github.com/HusseinAlokla/ticket-master.git
cd ticket-master
## 🔧 Environment Variables

Create a `.env` file in the root directory with the following:

```env
DATABASE_URL=mysql+aiomysql://user:password@db:3306/ticketdb
AUTH0_DOMAIN=your-auth0-domain
AUTH0_API_AUDIENCE=your-api-audience
AUTH0_ALGORITHMS=RS256
TICKETMASTER_API_KEY=your-ticketmaster-api-key


## 🐳 Start with Docker

Run the following command to start the app:

```bash
docker-compose up --build
```

API will be available at:  
📍 `http://localhost:8000/docs`

---

## 🔐 Auth0 Setup

1. Create an Auth0 Application (Regular Web App).
2. Configure the following settings:
   - Callback URL: `http://localhost:8000/callback`
   - Allowed Logout URLs: `http://localhost:8000/logout`
3. Add these values to your `.env`:
   - `AUTH0_DOMAIN`
   - `AUTH0_API_AUDIENCE`

---

## 📑 API Usage

### Public Endpoints

| Method | Endpoint             | Description         |
|--------|----------------------|---------------------|
| GET    | `/events`            | Get public events   |
| GET    | `/events/{event_id}` | Get event by ID     |

### Authenticated Endpoints

| Method | Endpoint                  | Description                   |
|--------|---------------------------|-------------------------------|
| POST   | `/user/events/{event_id}` | Save event to user favorites |
| GET    | `/user/events`            | Retrieve saved events         |

🔐 Use your Auth0 Bearer token in the request header:

```http
Authorization: Bearer <your_token_here>
```

---

## 🧪 Testing

To run the tests inside Docker:

```bash
docker-compose exec backend pytest
```

---

## 🧱 Architecture Overview

```
           +-------------+
           |   Auth0     |
           +------+------+
                  |
            +-----v-----+
            |  FastAPI  |
            +-----+-----+
                  |
     +------------+-------------+
     |                          |
+----v-----+              +-----v-----+
| Ticketmaster API         |   MySQL  |
+--------------------------+----------+
```

---

## 📦 Tech Stack

- FastAPI
- Auth0
- SQLAlchemy (Async)
- aiomysql
- MySQL
- Docker
- Pytest

---

## 💡 Design & Decisions

| Decision           | Rationale                                |
|--------------------|-------------------------------------------|
| Auth0              | Easy and secure user authentication       |
| SQLAlchemy Async   | Non-blocking DB access                    |
| MySQL + aiomysql   | Lightweight, popular async DB stack       |
| Docker Compose     | Easy containerized dev environment        |
| Ticketmaster API   | Rich real-world data source for demo use  |
