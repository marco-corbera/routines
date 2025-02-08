# Exercise Routine API

This project is a Django-based API for managing user exercise routines. Users can register, log in, create routines, add exercises to routines, and view statistics about their exercises over different periods.

---

## **Features**

1. **User Management**:
   - Register users.
   - Log in using JWT authentication.
   
2. **Routine Management**:
   - Create, Read, Update, Delete (CRUD) operations for routines.
   - Each routine includes exercises (e.g., "Bench Press", "Pull-Ups").

3. **Exercise Management**:
   - Add exercises to routines with sets and reps.

4. **Statistics**:
   - View how many exercises a user has performed in a day, week, month, or year.

5. **Admin Panel**:
   - Manage users, routines, and exercises using Django's admin site.

---

## **Installation with Docker**

### **1. Clone the repository**
```bash
git clone <repository-url>
cd routines
```

### **2. Build and run the Docker containers**
```bash
docker compose up --build
```
This will build the backend image and start the containers for the backend and PostgreSQL database.

### **3. Apply database migrations**
```bash
docker compose exec backend python manage.py migrate
```

### **4. Create a superuser**
```bash
docker compose exec backend python manage.py createsuperuser
```

### **5. Access the application**
- API: `http://127.0.0.1:8000`
- Admin Panel: `http://127.0.0.1:8000/admin`

---

## **API Endpoints**

### **Authentication**
- `POST /api/token/`: Obtain JWT access and refresh tokens.
- `POST /api/token/refresh/`: Refresh the access token.

### **Routines**
- `GET /api/routines/`: List all routines of the authenticated user.
- `POST /api/routines/`: Create a new routine.
- `PUT /api/routines/{id}/`: Update an existing routine.
- `DELETE /api/routines/{id}/`: Delete a routine.

### **Exercises**
- `GET /api/exercises/`: List all exercises for the authenticated user's routines.
- `POST /api/exercises/`: Add an exercise to a routine.
- `PUT /api/exercises/{id}/`: Update an exercise.
- `DELETE /api/exercises/{id}/`: Delete an exercise.

### **Statistics**
- `GET /api/routines/stats/?period=day|week|month|year`: View exercise statistics for the specified period.

---

## **Django Admin**
Access the admin panel at `/admin`. Use the superuser credentials to log in and manage users, routines, and exercises.

---

## **Technologies Used**

- **Backend**: Django, Django REST Framework
- **Authentication**: JWT (via `djangorestframework-simplejwt`)
- **Database**: PostgreSQL (via Docker container)
- **Admin Panel**: Django Admin
- **Containerization**: Docker, Docker Compose

---

## **Future Improvements**

1. Add support for social authentication (e.g., Google, Facebook).
2. Implement a frontend with React or Vue.js.
3. Expand statistics to include more granular details (e.g., calories burned, weight tracking).
4. Integrate with external fitness APIs for additional features.

---

## **License**
This project is licensed under the MIT License.

