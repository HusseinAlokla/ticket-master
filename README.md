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
