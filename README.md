# Library Management System

## How to run the project
1. Clone the repository
```
git clone https://github.com/AdityaGahukar/Library-Management-System.git
```
2. Open the terminal and navigate to the project directory
```
cd Library-Management-System
```
3. Go to `backend` directory and install dependencies
```
cd backend
npm install
```
4. Locate and rename the `.env.example` file in the `backend` to `.env` and add the following environment variables
```
PORT=define any suitable port
MONGODB_URI=your mongodb connection string
```
5. Run the following command to start the server
```
npm start
```
## How to run the Client
1. Go to the `frontend` directory and install the dependencies
```
cd frontend
npm install
```
2. rename the `.env.example` file in the `frontend` to `.env` and add the following environment variables:
```
REACT_APP_API_URI=http://localhost:<port>/api
```
(Note: the URI should end with `/api`. Else The below modification needs to be done on the `backend/server.js`)
```
app.use('/api/books', bookRoutes);  //replace these /api with your URI trailer

app.use('/api/borrowers', borrowerRoutes);  //replace these /api with your URI trailer

app.use('/api/authors', authorRoutes);  //replace these /api wwith your URI trailer

app.use('/api/counts', countRoutes);    //replace these /api wwith your URI trailer
```
3. Run the following command to start the client
```
npm start
```
4. Open the browser and navigate to `http://localhost:3000/` to view the client

# Note:
 - Test(useless).js is just a checking file to see if the server is running or not. It is not a part of the project
 - Run the server before running the client(else the client will not fetch data until the server is running)
 - The project is still under development and some features may not work as expecte 
 - the `npm start` command will start the server using nodemon. To change the behaviour, change the `start` script in `package.json` file in the `backend` directory

## Testing Requirement

Done using Selenium IDE and also using Python test scripts.

### Testing Details
- Selenium Test Scripts: Python scripts located in the `tests scripts` folder
- Selenium IDE Files: `.side` files located in the `Selenium IDE` folder
- Screenshots and Videos: Included in respective folders showcasing test results


# Contributed by:
 - Aditya Gahukar (202252302)
 - Amit Singh (202252305)
 - Shivansh Rawat (202252337)
 - Akarsh Yadav (202252303)
 - Ayush Yadav (202252308)
